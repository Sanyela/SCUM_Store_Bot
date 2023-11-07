# SCUM_Store_Bot
一个用Python写的SCUM后端机器人，主要功能：自动发送礼包，传送交易区，增加余额，欢迎进服玩家  
运行起来还是以访问api形式执行发送礼包的方法，需要其他商城系统对接此api  
推荐系统：异次元发卡网
# 如何运行
使用Pycharm创建一个Flask项目，把本项目下的app.py覆盖创建好的app.py  
然后运行代码，没安装的模块使用pip进行安装  
运行成功后地址为：http://127.0.0.1:5000  
需要配合端口映射，把本地的Flask映射到外网再对接其它系统  
# 配置教程
需要修改代码的第43~44行，为你的FTP地址、端口、帐号、密码
# 函数解答
46行get_last_login_file方法是实现获取最后一个login文件的方法  
55行get_scum_pid方法是实现获取SCUM进程的PID方法  
61行paste方法是粘贴板的方法  
67行minimize_all_windows方法是实现快捷键Win + D来最小化所有窗口  
70行activate_scum_window方法激活SCUM窗口  
87行activate_and_lock_keyboard方法是实现锁定键盘  
96行unlock_keyboard方法是实现解锁键盘  
104行tp_service为Flask的url路径，里面的tp_service是实现传送玩家到交易区的方法  
136行new_tp为Flask的url路径，里面的new_tp是实现玩家传送玩家的方法  
136行new_people为Flask的url路径，里面的hello_world是实现发送新手礼包的方法  
136行add_blance为Flask的url路径，里面的add_blance是实现增加玩家余额的方法  
247行add blance(msg)方法是调用SCUM窗口发送玩家上下线的方法
266行run flask方法是运行Flask框架的方法
270行ftp_read_login方法是实现循环读取登录日志文件，来进行欢迎玩家上下线的方法  
最后的316行开始就是开启多线程，一个线程是开启Flask框架的线程，一个线程是开启欢迎玩家上下线的线程  

# 一点小小建议  
不会Python的最好不要研究代码，因为本来就是屎山，主要用到多线程，Flask，还有操作windows窗口的api  
此代码为不完全版，因为我也没开发完，有本事的自己重构或者加功能吧  
