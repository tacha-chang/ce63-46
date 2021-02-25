from tkinter import *
import cv2
from PIL import  ImageTk, Image
import time
class App:
    def __init__(self,video_source=0):
        self.appName = "Attendent BY ID Card"
        self.window = Tk()
        self.window.title(self.appName)
        self.window.resizable(0,0)
#        self.window.wm_iconbitmap("bibi")
        self.window['bg'] = 'black'
        self.Video_source = video_source

        self.vid = MyVideoCapture(self.Video_source)
        self.label = Label(self.window,text =self.appName,font =15,
                           bg='blue',fg='white').pack(side =TOP,fill=BOTH)
        #Create a canvas that can fit the above video source size
        self.canvas = Canvas(self.window, width=self.vid.width,height =self.vid.height,bg='red')
        self.canvas.pack(side = LEFT)
        #Create  photo
        self.canvas1 = Canvas(self.window, width = 300, height = 300)
        self.canvas1.pack()
        #Button that snap
        self.btn_snapshot = Button(self.window,text="Snapshot",width=30,bg='goldenrod2',
                                   activebackground='red',command=self.snapshot)
        self.btn_snapshot.pack(anchor=CENTER,expand=True)
        self.update()
        self.window.mainloop()
    def snapshot(self):
        check, frame = self.vid.getFrame()
        if check:
            image = "IMG-" + time.strftime("%H-%M-%S-%d-%m") + ".jpg"
            cv2.imwrite(image, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        #==========show msg on window
            msg = Label(self.window,text='image saved'+image,bg='black',fg='green').place(x=430,y=510)
    def update(self):
        isTrue, frame= self.vid.getFrame()

        if isTrue:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0,0,image =self.photo,anchor =NW)
        self.window.after(15, self.update)



class MyVideoCapture:
    def __init__(self,video_source=0):
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open This camera",video_source)
        self.width =self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    def getFrame(self):
        if self.vid.isOpened():
            isTrue, frame = self.vid.read()
            if isTrue:
                return (isTrue, cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
            else:
                return (isTrue, None)
        else:
            return (isTrue, None)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
if __name__ =="__main__":
    App()



