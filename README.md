# MaaLogSending


## 1 介绍 ##
这是一个当明日方舟MAA软件完成任务后，可以将日志信息以邮件发送的脚本
只适用于windows,无法用于mac.

## 2 使用方式 ##
1、下载发行版中的MaaLogSendingv1.0.zip
[链接]

2、解压，将里面的main.exe和config.txt拷贝到MAA.exe所在目录下。
[图片]

3、将config.txt中的配置信息改为自己邮箱的配置信息。
（1）SMTP服务器地址（每个公司不一样，自行百度）
smtp_server=smtp.example.com
（2）SMTP服务器端口号（每个公司不一样，自行百度）
port=465
（3）邮件发送者邮箱
sender=sender@example.com
（4）邮箱授权码 （在邮箱设置中生成，QQ邮箱可参考：https://zhuanlan.zhihu.com/p/643897161?utm_id=0）
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

4、在MAA的设置->连接设置->结束后脚本一栏填上main.exe的路径。
[图片]

5、测试，MAA一键长草界面中只勾选开始唤醒，并等待任务完成。如果一切顺利，收件人邮箱就会收到任务成功完成的邮件。
（1）任务执行成功截图
[图片]


（2）任务执行出错截图
[图片]