from flask import Flask, render_template, request, Response
import game_deployment as gd
from chat import *
from fer.fer import top_emotion
import cv2
from fer_capstone import fun, cap
import random
import subprocess
import os
import joblib

app = Flask(__name__)

# HOME
@app.route('/')
def home():
    return render_template("index.html")



# DOUDOU'S CHATBOT
@app.route("/chatbot")
def chatbot():
    return render_template("chatbotApp.html")
    # return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(get_response(userText))



# GAME OF 21
@app.route('/gameof21', methods = ['GET', 'POST'])
def gameof21():
    return render_template("gameof21index.html")

@app.route('/gameof21about', methods = ['GET', 'POST'])
def gameof21about():
    return render_template("gameof21about.html")

@app.route('/orderPage', methods=['POST'])
def result():
    a = str(request.form['a'])
    result = gd.start1(a)

    b = str(request.form['b'])
    result2 = gd.start2(a, b)

    # return render_template("index.html", final = result)
    return render_template("gameof21index.html", final = result, final2 = result2)



# SENTIMENT RECOGNITION
camera = cv2.VideoCapture(0)
'''
for ip camera use - rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp' 
for local webcam use cv2.VideoCapture(0)
'''
result, top_emotion = fun()
cap.release()

def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/sentimentRecognition')
def sentimentRecognition():
    return render_template('sentimentRecognitionindex.html', resultA = result)

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')



# SONG RECOMMENDATION
@app.route('/songrecommendation')
def songrecommendation():
    
    # print(top_emotion)
    if top_emotion[0] is None:
        mp = 'C:/Program Files (x86)/Windows Media Player/wmplayer.exe'
        randomfile = random.choice(os.listdir("K:/DESKTOP_FILES/Capstone/fer/music/neutral/"))
        file = ("K:/DESKTOP_FILES/Capstone/fer/music/neutral/")
    
    else:
        mp = 'C:/Program Files (x86)/Windows Media Player/wmplayer.exe'
        randomfile = random.choice(os.listdir("K:/DESKTOP_FILES/Capstone/fer/music/" + top_emotion[0] + "/"))
        file = ("K:/DESKTOP_FILES/Capstone/fer/music/" + top_emotion[0] + "/" + randomfile)
    subprocess.call([mp, file])

    # return render_template('songrecommendationindex.html', resultA = result)
    return render_template("index.html")



# PSYCHOMETRIC TEST
model = joblib.load("psycometric.sav")

@app.route('/psychometrictest')
def psychometrictest():
    return render_template("psychoindex.html")

@app.route('/predict', methods=['POST'])
def test_result():
    a = float(request.form['a'])
    b = float(request.form['b'])
    c = float(request.form['c'])
    d = float(request.form['d'])
    e = float(request.form['e'])
    f = float(request.form['f'])
    g = float(request.form['g'])
    h = float(request.form['h'])
    i = float(request.form['i'])
    j = float(request.form['j'])
    k = float(request.form['k'])
    l = float(request.form['l'])
    m = float(request.form['m'])
    n = float(request.form['n'])
    o = float(request.form['o'])
    p = float(request.form['p'])
    q = float(request.form['q'])
    r = float(request.form['r'])
    s = float(request.form['s'])
    t = float(request.form['t'])
    u = float(request.form['u'])
    v = float(request.form['v'])
    w = float(request.form['w'])
    x = float(request.form['x'])
    y = float(request.form['y'])
    z = float(request.form['z'])
    A = float(request.form['A'])
    B = float(request.form['B'])
    C = float(request.form['C'])
    D = float(request.form['D'])
    E = float(request.form['E'])
    F = float(request.form['F'])
    G = float(request.form['G'])
    H = float(request.form['H'])
    I = float(request.form['I'])
    J = float(request.form['J'])
    K = float(request.form['K'])
    L = float(request.form['L'])
    M = float(request.form['M'])
    N = float(request.form['N'])
    O = float(request.form['O'])
    P = float(request.form['P'])
    Q = float(request.form['Q'])
    R = float(request.form['R'])
    S = float(request.form['S'])
    T = float(request.form['T'])
    U = float(request.form['U'])
    V = float(request.form['V'])
    W = float(request.form['W'])
    X = float(request.form['X'])
    
    pred = model.predict([[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X]])
    
    
    return render_template("psychoindex.html", result = pred[0])

# #DOUDOU'S CHATBOT
# @app.route("/chatbot")
# def chatbot():
#     return render_template("chatbotApp.html")
#     # return render_template("index.html")

# @app.route("/get")
# def get_bot_response():
#     userText = request.args.get('msg')
#     return str(get_response(userText))



# FRAGNANCE BLOG
@app.route('/fragnance', methods = ['GET', 'POST'])
def fragnance():
    return render_template("fragnance.html")

if __name__ == '__main__':
    app.run()