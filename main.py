from typing import List
from multiprocessing import Process, Queue
import time
from RandomWordGenerator import RandomWord

rnd=RandomWord(max_word_size=10)
name:str=rnd.generate()
def calc(q):
    while(True):
        time.sleep(1)
        if(not q.empty()):
            a:List=q.get()
            s:int=a[0]**a[1]
            sum:int=0
            for i in range(s+1):
                sum+=i
            with open('./text/'+name,'a') as conn:
                conn.write(str(a[0])+" "+str(a[1])+" "+str(s)+" "+str(sum)+"\n")

if(__name__=='__main__'):
    q = Queue()
    p=Process(target=calc, args=[q])
    p.start()
    while(True):
        print("Введите число и степень через пробел")
        try:
            text=input().split()
            if(text[0]=="end"):
                break
            else:
                a = [int(x) for x in text]
                if(len(a)==2):
                    q.put(a)
                else:
                    print("Ошибка ввода")
        except(TypeError):
            print("Ошибка ввода")
    p.join()