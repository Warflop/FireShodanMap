import pyrebase
import paho.mqtt.client as mqtt
import requests
import shodan
import time
import os

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

			data = {"id": count,  "ip": searching, "lat" : lat, "lng" : lng, "Country" : country_name}
			print "[+] IP: " + str(searching) + ", Latitude: " + str(lat) + ", Longitude: " + str(lng) + ", Country: " + str(country_name)
			db.child("shodanmap").push(data)
			count = count + 1


        except shodan.APIError, e:
                pass

if __name__ == "__main__":

	#Ask for the TERM_TO_SEARCH
	SHODAN_API_KEY = "API_SHODAN_KEY"
	TERM_TO_SEARCH = raw_input("Please enter Search String: ")

	config = {

        	"apiKey": "KEY_FIREBASE_HERE",
        	"authDomain": "shodanmap.firebaseapp.com",
        	"databaseURL": "https://shodanmap.firebaseio.com",
        	"storageBucket": "shodanmap.appspot.com",
        	"serviceAccount": "FILE_WITH_KEY.json"

	}

        firebase = pyrebase.initialize_app(config)
        db = firebase.database()
	#Delete DB bevore Filling
	deletedb = raw_input("Delte DB ? y/n: ")
	if deletedb == 'y':
	   db.child("shodanmap").remove()
	   searching()
        else:
           searching()
	searching()
