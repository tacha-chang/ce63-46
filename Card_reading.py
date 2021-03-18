import os
import shutil
def set_stage():
    path = 'C:/Users/Tacha/VideoStreamingFlask/static/img/SIAM-ID/Data.txt'
    last_time = os.path.getctime(path)
    with open("base.txt", "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
        last_line = lines[-1] #บรรทัดสุดท้าย
        print(last_line)
        print(last_time)
        if float(last_line) < float(last_time):
            print(last_time)
            f = open('base.txt','a')
            f.write("\n" +str(last_time))
            f.close()
            return 1
        elif float(last_line) == float(last_time):
            print("ok")
            return 0
#set_stage()
#print(set_stage())
####### อ่านค่าตอนเสียบบัตร
def reader_card():
    path = 'C:/Users/Tacha/VideoStreamingFlask/static/img/SIAM-ID/Data.txt'
    path_dest = 'C:/Users/Tacha/VideoStreamingFlask/static/img/temp_img'
    with open(path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
        last_line = lines[-1] #อ่่านบรรทัดสุดท้าย
    x  = last_line.split(",")
    shutil.copy(x[31],path_dest)
    return x
x = reader_card() #
# print(x[1])
# print(x[2])
print("call function Card reading")
