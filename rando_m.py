import datetime
from time import sleep
l=[]
tym=[]

def generate():
    for i in range (10):
        time=datetime.datetime.now()
        t=time.microsecond
        l.append(t)
        sleep(0.038)
    for i in l:
        tym.append(int(i/10000))
    return str(tym[3])+str(tym[8])+str(tym[0])
