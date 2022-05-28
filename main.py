from flask import Flask, request, jsonify
import os
import random

# 100-ok 101-server full 102-usr not found 103-rooms full

server = Flask(__name__)

usrtable = [[0, 0]] * 6

roomtable = [[0, 0]] * 3

def getUsr():
	global usrtable
	tmp = 101
	for i in range(6):
		if usrtable[i][0] == 0:
			tmp = i
			break
	return tmp


def findUsr(UID):
	global usrtable
	tmp = 102
	for i in range(6):
		if usrtable[i][0] == UID:
			tmp = i
			break
	return tmp


@server.route('/0x00/<uid>') # login
def login(uid):
	if not getUsr() == 101:
		usrtable[getUsr()][0] = uid
		return 100
	else:
		return 101

@server.route('/0x01/<uid>') # logout
def logout(uid):
	if not findUsr(uid) == 102:
		usrtable[findUsr(uid)][0] = 0
		usrtable[findUsr(uid)][1] = 0
		return 100
	else:
		return 102

@server.route('/0x02/<uid>') # request match
def getRoom(uid):
	global usrtable, roomtable
	tmp = 103
	for i in range(3):
		if roomtable[i][0] == 0 and roomtable[i][1] == 0:
			roomtable[i][0] = uid
			tmp = 100
			break
		if not roomtable[i][0] == 0 and roomtable[i][1] == 0:
			roomtable[i][1] = uid
			tmp = roomtable[i][0]
			break
	return tmp

@server.route('/0x03/<uid>') # get usr status
def getUsrStats(uid):
	global usrtable
	if not findUsr(uid) == 102:
		return usrtable[findUsr(uid)][1]
	else:
		return 102

if __name__ == '__main__':
    app.run(debug=True, port=os.environ.get('PORT', "8080"))
