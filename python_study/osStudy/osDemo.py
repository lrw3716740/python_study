#coding:utf-8
import os
import subprocess,time
#os.system("python sub.py")
#sub=os.popen("python sub.py") #不好控制何时让它结束




sub=subprocess.Popen("python sub.py")
#sub.wait()
time.sleep(10)
print "mainMethod go on !"
sub.terminate()