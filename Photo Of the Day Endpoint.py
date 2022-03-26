#--------------Photo Of the Day Endpoint--------------

import requests
import time
import json
from splinter import Browser
from datetime import datetime
from config import api_key, executable_path

def nasaphoto():

	#----- Define variables -----
	endpoint = r"https://api.nasa.gov/planetary/apod?api_key={}".format(api_key) 

	#----- Grab data -----
	data = requests.get(endpoint)

	#----- Convert to JSON -----
	textdata = json.loads(data.text)

	#----- Grab data out of JSON -----
	newurl = textdata["url"]
	explanation = textdata["explanation"]
	date = textdata["date"]
	title = textdata["title"]

	#----- Print title, data, photographer and explanation -----
	print(title)
	print("\n")

	print(date)
	print("\n")

	print("\n")
	print(explanation)

	#----- Download The Photo Of The Day -----
	img_data = requests.get(newurl).content

	#----- Specify Save Locaiton -----
	hierFolder = 'NASAPhotos/'

	#----- Save Photo -----
	with open(hierFolder + date + ' ' + 'NasaPhotoOfTheDay.jpg', 'wb') as handler:
		handler.write(img_data)
		print(handler)


nasaphoto()