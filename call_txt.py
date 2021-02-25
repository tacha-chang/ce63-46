from parinya import LINE
import requests
import cv2
import pymongo
line = LINE('jXQm7pCNfjeLEzK9Dcn5V2VJMdvSGQaTfBkbg8O4d6h')
line2  = LINE('873qWHl2U3JWxLEb2wOLXsqCuWkKW6h5Azf02s4sjcj')
myclient = pymongo.MongoClient("mongodb://localhost:27017/local")
mydb = myclient["attendance"]
mycol = mydb["test_1"]

data = ["วันที่", "เวลา", "เลขประจำตัวประชาชน", ",คำนำหน้า", "ชื่อ", "ชื่อกลางและนามสกุล", "คำนำหน้า(E)", "ชื่อ(E)", "ชื่อกลางและนามสกุล(E)",
        "วันเกิด",  "เพศ,", "ศาสนา", "อายุขณะทำบัตร", "อายุปัจจุบัน",  "บ้านเลขที่",  "หมู่ที่", "ตรอก", "ซอย", "ถนน", "ตำบล",
        "อำเภอ", "จังหวัด", "วันออกบัตร", "วันบัตรหมดอายุ", "เลขประจำบัตร", "สถานที่ออกบัตร", "หมายเลขคำขอ", "กำหนดเอง 1",
        "กำหนดเอง 2", "กำหนดเอง 3", "กำหนดเอง 4", "ภาพถ่าย"]
data_json = {"วันที่": "15 พฤศจิกายน 2563",                         #0
             "เวลา": "19:17",                          #1
             "เลขประจำตัวประชาชน": "1 1018 01037 08 3",              #2
             ",คำนำหน้า": "นาย",                     #3
             "ชื่อ": "ธชรัฐ",                            #4
             "ชื่อกลางและนามสกุล": "ช้างมงคล",              #5
             "คำนำหน้า(E)": "Mr",                 #6
             "ชื่อ(E)": "Tacharat",                         #7
             "ชื่อกลางและนามสกุล(E)":"Changmongkol",            #8
             "วันเกิด": "12 กรกฎาคม 2542",                     #9
             "เพศ,": "ชาย",                    #10
             "ศาสนา": "พุทธ",                   #11
             "อายุขณะทำบัตร" : 20,               #12
             "อายุปัจจุบัน": 22 ,                     #13
             "บ้านเลขที่": "10/19",                  #14
             "หมู่ที่": "หมู่ที่ 10",                     #15
             "ตรอก": "",                    #16
             "ซอย": "",                     #17
             "ถนน": "",                     #18
             "ตำบล": "บางขุนเทียน",                    #19
             "อำเภอ": "จอมทอง",                   #20
             "จังหวัด": "กรุงเทพมหานคร",                     #21
             "วันออกบัตร": "11 ธันวาคม 2561",                  #22
             "วันบัตรหมดอายุ": "11 กรกฎาคม 2570",              #23
             "เลขประจำบัตร": "1035-05-12110839",                #24
             "สถานที่ออกบัตร": "ท้องถิ่นเขตจอมทอง กรุงเทพมหานคร",              #25
             "หมายเลขคำขอ": "1035-4-332550/12110839",             #26

             "ภาพถ่าย": "C:\Users\ADMIN\Documents\SIAM-ID\1101801037083.jp"}                 #31
i = 0
x = mycol.insert_one(data_json)
with open("Data.txt", "r",  encoding='utf-8') as file:
    for line in file:
        s = line.split(",")
#        print(s)    #ได้ทุุกบรรทัด
    print(s)  #ได้ข้อมูลใหม่สุด
count  = 0
for i in data_json:
    data_json[i]  = s[count]
    count+=1
print(data_json.items())
print(data_json["ชื่อ"])
print(data_json["อายุปัจจุบัน"])
print(data_json["ภาพถ่าย"])
frame  = cv2.imread(data_json["ภาพถ่าย"])  # ไม่ได้
cap = cv2.imread('1104500011096.jpg')  ##อ่านรูป

#for i in data:
#    print(data)
        # for i in range(len(line)): ## 1 แถว
        #     if line[i] == ',':   ## เอา,ออก
        #         continue
        #     s = s+line[i]
attendance = str(data_json["วันที่"])
name = str(data_json["ชื่อ"])
age = str(data_json["อายุปัจจุบัน"])
line2.sendtext('เข้ามา วันที่ : '+ attendance + name +' อายุ : ' + age)
line2.sendimage(cap)
line2.sendimage(frame)  ##ไม้่ไดเ

x = mycol.insert_one(s)
print(x.inserted_id)