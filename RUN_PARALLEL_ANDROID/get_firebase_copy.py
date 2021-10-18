#!/usr/bin/env python3
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

def listener1(event):
	dataP1 = event.data
	print (dataP1)
def listener2(event):
	dataP2 = event.data
	print (dataP2)
def listener3(event):
	dataP3 = event.data
	print (dataP3)

cred_obj = firebase_admin.credentials.Certificate('/home/pi/Downloads/microfluid/test_parellel/pi_stream_android/test-18cfb-firebase-adminsdk-717o7-9d907373d4.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL': 'https://test-18cfb-default-rtdb.firebaseio.com/'
	})

ref1 = db.reference("/Pump1").listen(listener1)

ref2 = db.reference("/Pump2").listen(listener2)

ref3 = db.reference("/Pump3").listen(listener3)
