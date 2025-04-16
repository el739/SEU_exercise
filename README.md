# SEU_exercise

## 简介

一款解决东南大学体育锻炼打卡问题的工具。无需通过官方小程序，直接将运动数据上传至服务器，避免网络问题和加载卡顿。

## 功能特点

- 绕过官方小程序直接上传运动数据
- 支持自定义运动时间、距离和照片
- 稳定可靠，不受校园网络环境影响

## 安装指南

### 方法1：直接下载

从[发布页](https://github.com/el739/SEU_exercise/releases)下载最新版本的程序。

### 方法2：源码运行

需要Python环境：

```bash
git clone https://github.com/el739/SEU_exercise.git
cd SEU_exercise
pip3 install -r requirements.txt
python3 run.py
```

![主界面](files/main_program.png)

## 使用教程

### 准备工作

*注意！通过校园网使用官方小程序和本软件会产生网络证书问题，因此以下操作最好均在手机个人热点+使用流量的情况下进行。*

1. 下载并安装[Cheat Engine](https://www.cheatengine.org/)
2. 打开电脑端微信
3. 运行"东南大学体育管理"小程序并登录
4. 进入"锻炼"界面，如图：
   ![小程序主界面](files/miniapp_main_menu.png)

### 配置Cheat Engine

1. 启动Cheat Engine并跳过教程
2. 点击左上角进程选择图标，选择微信小程序进程
3. 将搜索类型改为"String"（字符串）
   ![用Cheat Engine打开小程序](files/choose_process.png)
   ![将搜索类型改为字符串](files/search_string.png)

### 获取必要凭证的两种方法

#### 方法一：直接获取token和id

##### 1. 获取token

1. 在搜索框中输入`Bearer `（注意末尾有空格）
2. 点击"First scan"
3. 在搜索结果中选择最后一个条目
4. 按Ctrl+B打开内存查看器
5. 找到并选择`Bearer `后面的一长串无规则字符（通常包含字母、数字和符号）
6. 复制该字符串到程序的token输入框
   ![搜索token_1](files/search_token_1.png)
   ![搜索token_2](files/search_token_2.png)
   ![搜索token_3](files/search_token_3.png)
   ![编辑token](files/edit_token.png)

*注：如果未能找到一串无规则字符串，请使用相同的方法查看第二个、第三个地址，直到找到token。如果所有地址均没有，则尝试打开小程序的其他页面，重复以上步骤。
token值通常只在小程序启动后1分钟内可见。如果未找到，请重启小程序重试。*

##### 2. 获取id

1. 在搜索框中输入`\"id\":\"`
2. 点击"First scan"
3. 选择搜索结果并按Ctrl+B
4. 找到约18位的数字（通常以3开头）
5. 复制该值到程序的id输入框
   ![搜索id_1](files/search_id_1.png)
   ![搜索id_2](files/search_id_2.png)
   ![编辑id](files/edit_id.png)

*同上，若没有找到正确的id值，则尝试重启小程序并重试。`id`一定是一串约18位的数字，实际查看时有诸多混淆项，请注意辨别。*

#### 方法二：获取小程序的openid并重新登陆

1. 在搜索框输入`{"data":"`
2. 点击"First scan"
3. 依次按Ctrl+B查看每个搜索结果的data对应值，直到找到一串约20个数字+字母（一般以`ok`开头）。
![搜索OpenId1](files/search_openid_1.png)
![搜索OpenId2](files/search_openid_2.png)
4. 复制该值，并保存备用。
5. 双击运行login.exe，依次填入身份证号、一卡通号、openid
6. 将程序输出的token、Student Id复制，并填写到本软件中的相应位置。
![获取凭证](files/credentials_got.png)

*此值的混淆项颇多，但是较为稳定地存在。
若程序没有输出这两项值，而是返回结果中包括“该用户已被其他微信账号绑定”字样，则代表OpenId有误，需返回第三步重新寻找。*

### 2. 配置运动信息

在主程序界面填写：

| 字段 | 说明 | 格式示例 |
|------|------|----------|
| Start Image | 开始运动照片 | 文件路径 |
| Finish Image | 结束运动照片 | 文件路径 |
| Date | 运动日期 | 2025-04-01 |
| Start Time | 开始时间 | 18:00:00 |
| Finish Time | 结束时间 | 18:08:00 |
| Distance | 运动距离(km) | 1.24 |

### 3. 运行程序

1. 点击"Save Changes"保存配置
2. 输入License Key（当前可用：`LOVESEU`）
3. 点击"Run"开始运行
4. 等待成功提示。当弹窗显示`Operation completed successfully!`或右侧日志区中输出`INFO - Record added successfully`时，即成功上传自己的运动记录。
![运行成功示例](files/save_succeeded.png)
此时可前往官方小程序查看上传结果。
![运行结果](files/result.png)

## 故障排查

程序运行日志实时显示在右侧文本框，可用于排查问题。项目初期错误处理尚不完善，希望大家能够提交issue帮助我们改进！

### 常见问题

![SSLerror](files/SSLerr.jpg)
一般是网络问题，此时电脑连接手机热点即可解决（注意，手机也需要使用流量，不使用校园网）。若连接热点后仍然无法解决，则应重新检查凭证是否正确。

## 免责声明

本程序旨在为用户提供方便的锻炼记录上传功能，以促进健康意识和锻炼习惯的养成。然而，使用本程序的用户须注意以下几点：

1. **记录真实性**：本程序不对用户上传的锻炼记录的真实性与准确性负责。所有用户应对其所提交的记录负责，确保所提供的信息真实、准确，严禁任何形式的伪造或篡改。
2. **数据使用**：本程序收集的锻炼记录仅用于学校内部活动及相关统计分析，不会用于其他任何商业用途。
3. **后果自负**：用户因使用本程序而导致的任何直接或间接的损失、争议、法律责任等后果，均由用户自行承担。我们不对因用户的不当使用所引发的任何法律问题或后果负责。
4. **使用条款**：通过使用本程序，用户即表示同意遵守上述条款，并理解相关责任。我们保留随时修改本免责声明的权利，修改后的免责声明将在本程序中发布。

感谢您对本程序的支持与使用！希望您能够诚实记录锻炼信息，共同营造积极健康的校园氛围。

## License

使用key：`LOVESEU`（限前1000次使用）
