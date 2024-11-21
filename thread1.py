import threading 
import os
import time
def fun1(x,y):
    print("started execution of fun1")
    print(threading.current_thread())
    c=x+y 
    for i in range(6):
        print(threading.active_count())
        time.sleep(1)
    #time.sleep(6) #IO BOUND JOB
    #sum(range(100000000))# CPU BOUND JOB
    print("fun1:",c)
    print("ended executionb of fun1")
    
def fun2(x,y):
    print("started execution of fun2")
    print(threading.current_thread())
    c=x-y 
    for i in range(6):
        print(threading.active_count())
        time.sleep(1)
    #time.sleep(6) #IO BOUND JOB
    #sum(range(100000000))# CPU BOUND JOB
    print("fun2:", c)
    print("ended executionb of fun2")
    


print(threading.current_thread())
print(os.getpid())
a=1000
b=2000
c=a+b 
print(c)
t1=time.time()
# fun1(10,20)
# fun2(10,20)
#print(time.time()-t1)
thr1 = threading.Thread(target=fun1, args=(10,20))
thr2 = threading.Thread(target=fun2, args=(10,20))
thr1.start()
thr2.start()
thrs = [thr1, thr2]
# for thr in thrs:
#     while thr.is_alive():
#         print(f"checking for {thr.name} status: {thr.is_alive()}")
#         time.sleep(1)
#print(time.time()-t1)
print("DONE")