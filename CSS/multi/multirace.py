import threading

g_count=0

def thread_main():
    global g_count
    #임계영역(Critical section)
    #공유 자원에 접근해서 값을 수정하려는 코드
    


    lock.acquire()
    for _ in range(100000):
        g_count+=1
    lock.release()

threads=[]
#lock 객체 생성
lock=threading.Lock()

for _ in range(50):
    threads.append(threading.Thread(target=thread_main))

for th in threads:
    th.start()

for th in threads:
    th.join()

print('g_count : {}'.format(g_count))

