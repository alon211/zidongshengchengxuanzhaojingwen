import os
import datetime
def log(path,data):
    with open(os.path.join(path,'log.txt'),'a') as file:
        file.write(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}:  {data}\n')
        file.close()
