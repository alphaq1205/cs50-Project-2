import os
from flask import Flask, request
from flask_cors import CORS
from flask_socketio import SocketIO, emit

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config["SECRET_KEY"] = 'xxxxxxxxxxxxxxxxxxxxxx'
socketio = SocketIO(app,cors_allowed_origins="*")

channels = []
messageData = []

@app.route("/")
def index():
    return "Project 2: TODOfsadfadsfsdaf"


@app.route("/api/username", methods=["POST"])
def getuser():
    username = request.form.get('username')
    logData = {'username':username, 'status':'logged_in'}
    print(request.form.get("username"))
    return {'authData':logData}


@app.route('/api/channels',methods=['GET','POST'])
def channel():
    
    chnlName = request.form.get('chnl_name')
    creatorName = request.form.get('creator_name')
    if(chnlName != 'none'):            
        data={'chnlName':chnlName,'creatorName':creatorName}
        channels.append(data)
        print(channels)
        return {'data':channels}
       


@socketio.on("getChat")
def chData(data):
    chat_data = data['chatData']
    messageData.append(chat_data)
    
    emit("fetchChat", chat_data, broadcast=True)

""" @socketio.on("delMsgId")
def delData(data):
    msgIds = data
    print(msgIds)
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

    for deldata in messageData:
        print(deldata['msgId'])
        print('pppppppppppppppppppppppppppppppppppppppppppppp')
        
        
    
    emit("updateMsg", 'xxxxxxxxxxxxxxx', broadcast=True)

 """

@app.route('/api/message/<channel>',methods=['GET','POST'])
def message(channel):
    print(channel)
    msgfilter = []
    print('111111111111111111111111111111111111111')
    for mdata in messageData:
        print('"'+mdata['channel']+'"')
        print(channel)
        print('sssssssssssssssssssssssssssssss')
        if('"'+mdata['channel']+'"' ==  channel):
            msgfilter.append(mdata)
            print(msgfilter)
            print('---------------------------------------------')
    
    print(msgfilter)
    return {'messageData':msgfilter}


@app.route("/api/<username>", methods=['GET',"POST"])
def getuser(username):
    userData = {'username':username}
    status = 'on'
    for x in users:
        if(x['username'] == username):
            status = 'off'
    users.append(userData)
    return {'status':status}
