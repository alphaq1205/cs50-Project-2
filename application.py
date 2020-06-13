import os
from flask import Flask, request, render_template
from flask_cors import CORS
from flask_socketio import SocketIO, emit

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config["SECRET_KEY"] = '1234'
socketio = SocketIO(app,cors_allowed_origins="*")

channels = []
users = []
messageData = []

@app.route("/")
def index():
    return render_template('frontPage.html')


@app.route("/registration")
def register():
    return render_template('registration.html')


@app.route("/homepage")
def home():
    return render_template('homepage.html')


@app.route('/api/channels',methods=['GET','POST'])
def channel():
    chnlName = request.form.get('chnl_name')
    creatorName = request.form.get('creator_name')
    if(chnlName != 'none'):            
        data={'chnlName':chnlName,'creatorName':creatorName}
        channels.append(data)
        return {'data':channels}
       

@socketio.on("getChat")
def chData(data):
    chat_data = data['chatData']
    messageData.append(chat_data)
    emit("fetchChat", chat_data, broadcast=True)


@app.route('/api/message/<channel>',methods=['GET','POST'])
def message(channel):
    print(channel)
    msgfilter = []
    for mdata in messageData:
        if('"'+mdata['channel']+'"' ==  channel):
            msgfilter.append(mdata)
    return {'messageData':msgfilter}
