import pyrebase
import paho.mqtt.client as mqtt
import requests
import shodan
import time
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8') #fix for output errors


def get_lat_lon(ip):

	r = requests.get("https://freegeoip.net/json/" + ip)
        json_response = r.json()
        if json_response['latitude'] and json_response['longitude']:
            lat = json_response['latitude']
            lng = json_response['longitude']
	    country_name = json_response['country_name']

	return lat, lng, country_name



def searching():

	api = shodan.Shodan(SHODAN_API_KEY)

        try:
                results = api.search(TERM_TO_SEARCH)
		count = 0
                for result in results['matches']:
                        searching = result['ip_str']
			lat,lng, country_name = get_lat_lon(searching)
                        port = result['port']
			data = {"id": count,  "ip": searching, "lat" : lat, "lng" : lng, "Country" : country_name, "Port" : port}
			print "[+] IP: " + str(searching) + ", Port: " + str(port) + ", Latitude: " + str(lat) + ", Longitude: " + str(lng) + ", Country: " + str(country_name)
			db.child("shodanmap").push(data)
			count = count + 1


        except shodan.APIError, e:
                pass

if __name__ == "__main__":

	SHODAN_API_KEY = "SHODAN_KEY_HERE"
        print('the basic searches you can use: \n FUN: Webcam / Webcamxp / Cams / Netcam / Android cam / default password \n IND: SCADA / ICS / PLC / DCS / RTU \n CTY: Germany / etc. \n CSTM: Android cam -Authentification / SCADA -Authentification ')
	TERM_TO_SEARCH =  raw_input("Please enter Search String: ")

	config = {

        	"apiKey": "FIREBASE_KEY_HERE",
        	"authDomain": "FIREBASE_DATA_HERE",
        	"databaseURL": "FIREBASE_DATA_HERE",
        	"storageBucket": "FIREBASE_DATA_HERE",
        	"serviceAccount": "FIREBASE_SERVERKEY_JSON_HERE.json"

	}

        firebase = pyrebase.initialize_app(config)
        db = firebase.database()
        #Delete DB bevore Filling
	deletedb = raw_input("Delte DB ? y/n: ")
	if deletedb == 'y':
           db.child("shodanmap").remove()
           print('Starting Search..')
	   searching()
        else:
           print('Starting Search..')
           searching()
	searching()
