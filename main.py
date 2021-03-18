from flask import Flask, render_template,request,redirect, Response,url_for
from camera import VideoCamera
from Card_reading import reader_card
from recognition import verify_photo
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from pop_up_NO_USE import popupmsg
import os
import schedule
#icon = os.path.join('static', 'icon') #connect FOLDER Photo
Photo_card_read = os.path.join('static', 'Photo_card_read')
ver = []
app = Flask(__name__)
#app.config['UPLOAD_FOLDER'] = icon
app.config['UPLOAD_FOLDER'] = Photo_card_read
#app.use("/static", express.static('./static/')); js
@app.after_request
def after_request(response):
    if response == "run" :
        try:
             verify_photo()
        except Exception as e:
             print("hello")

        app.logger.info("after_request")
        return response
    else :
        return response


@app.route('/')
def index():
    after_request("run")
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/verify')
def verify():
     # print("1")
     # check = verify_photo()
     # print(check)
     return 'hello'


@app.route('/Role')
def Role():

    return render_template('role.html')

@app.route('/Admin')
def Admin():

    return render_template('login.html')


@app.route('/register')
def register():
    data_profile = reader_card()
    file_img = data_profile[31]
    print(file_img)
    #img_profile = os.path.join(app.config['UPLOAD_FOLDER'], file_img)#รูปจากบัตร
    img_profile = os.listdir('static/img/temp_img/')
    return render_template('register.html',img_profile = img_profile, data_profile = data_profile)

@app.route('/Cardreading')
def Cardreading():
    # popupmsg()
    return render_template('Cardreading.html')

@app.route('/Cardreading_OFFICE')
def Cardreading_OFFICE():
    # popupmsg()
    return render_template('Cardreading.html')


@app.route('/information')
def information():
    return render_template('fill_in.html')

@app.route('/fill_in',methods = ['POST'])
def fill_in():
    data = []
    if request.method == "POST":
        PHONE_NUMBER = request.form['PHONE_NUMBER']
        explain = request.form['explain']
        Office = request.form['Office']  #เก็บดาต้าจากตรงนี้
        data.append(PHONE_NUMBER)
        data.append(explain)
        data.append(Office)
        #input เข้าdatabase สร้าง2 ตัว
        if Office == "kmitl":
            print("Welcome kmitl")
            return redirect(url_for('success_KMITL')) #function
        if Office == "kmutnb":
            print("Welcome kmutnb")
            return redirect(url_for('success_KMUTMD')) #function
        if Office == "kmutt":
            print("Welcome kmutt")
            return redirect(url_for('success_KMUTT')) #function
        #return redirect(url_for('success_KMITL'))
@app.route('/success_KMITL')
def success_KMITL():
    data_profile = reader_card()
    # Data_Office = { 'KMITL': 'KMITL',
    #                 'KMITL_floor' :'1st floor',
    #                 'KMUTMD': 'KMUTMD',
    #                 'KMUTND_floor' :'2nd floor',
    #                 'KMUTT': 'KMUTT',
    #                 'KMUTT_floor' :'3rd floor'
    # }
    #delete temp_img SIAM-ID txt.file  บรรทัดสุดท้าย
    # return render_template('success.html',Data_Office = Data_Office, data_profile = data_profile)
    return render_template('success_KMITL.html', data_profile = data_profile)


@app.route('/success_KMUTMD')
def success_KMUTMD():
    data_profile = reader_card()
    return render_template('success_KMUTMD.html', data_profile = data_profile)



@app.route('/success_KMUTT')
def success_KMUTT():
    data_profile = reader_card()
    return render_template('success_KMUTT.html', data_profile = data_profile)







if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
