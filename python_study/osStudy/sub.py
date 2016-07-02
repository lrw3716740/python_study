#coding:utf-8

import os,time

def printNumber(number,t):
    for i in range(0,number):
        
        print "打印%s,还有%s次没有打印"%(i,number-i-1)
        time.sleep(t)
        
        
if __name__=="__main__":
    
    printNumber(20,1) 