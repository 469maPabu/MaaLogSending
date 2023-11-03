# MaaLogSending


## 1 介绍 ##
这是一个当明日方舟MAA软件完成任务后，可以将日志信息以邮件发送的脚本.

只适用于windows,无法用于mac.

[MAA简体中文版](https://maa.plus/docs/)


## 2 使用方式 ##
### 1、下载  ### 

下载发行版中的MaaLogSendingv1.0.zip

- [MaaLogSendingv1.0.zip](https://gitee.com/Pabu469ma/maa-log-sending/releases/download/v1.0/MaaLogSendingv1.0.zip)


### 2、解压与拷贝  ### 
解压，将里面的main.exe和config.txt拷贝到MAA.exe所在目录下。

![zh1](https://gitee.com/Pabu469ma/maa-log-sending/raw/master/image/%E8%BF%9B%E5%85%A5MAA%E8%B7%AF%E5%BE%84.png)


### 3、修改config.txt ### 

将config.txt中的配置信息改为自己邮箱的配置信息。

（1）SMTP服务器地址

参考链接：[常见SMTP服务器地址](https://blog.csdn.net/qq_45392913/article/details/129601846)

smtp_server=smtp.example.com

（2）SMTP服务器端口号

参考链接：[常见收发邮件端口](https://blog.csdn.net/qq_45392913/article/details/129601846)

port=465

（3）邮件发送者邮箱

sender=sender@example.com

（4）邮箱授权码 

在邮箱设置中生成自己的授权码，参考链接：[QQ邮箱授权码生成](https://service.mail.qq.com/detail/0/75)

password=yourpassword

（5）邮件接收者邮箱（可以与发送者相同）

receiver=receiver@example.com


示例：
```
# SMTP服务器地址
smtp_server=smtp.qq.com
# SMTP服务器端口号
port=465
# 邮件发送者邮箱
sender=12345678@qq.com
# 邮箱授权码
password=abcdefghijklmn
# 邮件接收者邮箱
receiver=12345678@qq.com
```


### 4、设置MAA ### 

在MAA的设置 -> 连接设置 -> 结束后脚本一栏填上main.exe的路径。

![zh2](https://gitee.com/Pabu469ma/maa-log-sending/raw/master/image/%E8%AE%BE%E7%BD%AE%E8%84%9A%E6%9C%AC%E8%B7%AF%E5%BE%84.png)



### 5、测试  ### 
MAA一键长草界面中只勾选开始唤醒，并等待任务完成。如果一切顺利，收件人邮箱就会收到任务成功完成的邮件。

（1）任务执行成功截图

![zh3](https://gitee.com/Pabu469ma/maa-log-sending/raw/master/image/%E8%BF%90%E8%A1%8C%E6%88%90%E5%8A%9F%E6%88%AA%E5%9B%BE.png)


（2）任务执行出错截图

![zh4](https://gitee.com/Pabu469ma/maa-log-sending/raw/master/image/%E8%BF%90%E8%A1%8C%E5%87%BA%E9%94%99%E6%88%AA%E5%9B%BE.png)