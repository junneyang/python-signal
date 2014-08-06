python-signal
=============

python捕捉系统信号(sigint/sigterm/sigkill)，控制程序优雅退出.


* SIGINT    : 终止进程  中断进程  (control+c)    
* SIGTEM    : 终止进程     软件终止信号    
* SIGKILL   :  终止进程     杀死进程

进程结束信号 SIGTERM和SIGKILL的区别:
* SIGTERM比较友好，进程能捕捉这个信号，根据您的需要来关闭程序。在关闭程序之前，您可以结束打开的记录文件和完成正在做的任务。在某些情况下，假如进程正在进行作业而且不能中断，那么进程可以忽略这个SIGTERM信号。
* 对于SIGKILL信号，进程是不能忽略的。这是一个 “我不管您在做什么,立刻停止”的信号。假如您发送SIGKILL信号给进程，Linux就将进程停止在那里。
