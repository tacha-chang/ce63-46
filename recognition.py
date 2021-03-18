import face_recognition
import cv2
import time
import schedule
def verify_photo():
    # เปิดการใช้ webcam
    video_capture = cv2.VideoCapture(0)

    # โหลดภาพ Peen.jpg และให้ระบบจดจำใบหน้า
    person1_image = face_recognition.load_image_file("tacharat20.jpg")
    person1_face_encoding = face_recognition.face_encodings(person1_image)[0] #vector

    # สร้าง arrays ของคนที่จดจำและกำหนดชื่อ ตามลำดับ
    known_face_encodings = [
        person1_face_encoding,
    ]

    known_face_names = [
        "Tachrat"
    ]

    # ตัวแปรเริ่มต้น
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    stage = 0
    print(stage)
    while True:
        # ดึงเฟรมภาพมาจากวีดีโอ
        ret, frame = video_capture.read()

        # ย่อขนาดเฟรมเหลือ 1/4 ทำให้ face recognition ทำงานได้เร็วขึ้น
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # แปลงสีภาพจาก BGR (ถูกใช้ใน OpenCV) เป็นสีแบบ RGB (ถูกใช้ใน face_recognition)
        rgb_small_frame = small_frame[:, :, ::-1]

        # ประมวลผลเฟรมเว้นเฟรมเพื่อประหยัดเวลา
        if process_this_frame:
            # ค้นหาใบหน้าที่มีทั้งหมดในภาพ จากนั้นทำการ encodings ใบหน้าเพื่อจะนำไปใช้เปรียบเทียบต่อ
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # ทำการเปรียบเทียบใบหน้าที่อยู่ในวีดีโอกับใบหน้าที่รู้จักในระบบ
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                # ถ้า encoding แล้วใบหน้าตรงกันก็จะแสดงข้อมูล
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]
                    stage = 1
                face_names.append(name)
        named_tuple = time.localtime() # get struct_time
        time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
        print(stage)
        print(time_string)
        print(face_names)
        return [stage,face_names,time_string]
        process_this_frame = not process_this_frame

    video_capture.release()
    cv2.destroyAllWindows()
# print(d())
# schedule.every(1).seconds.do(d)
print("call function verify")
