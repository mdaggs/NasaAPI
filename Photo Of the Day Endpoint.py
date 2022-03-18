#--------------Photo Of the Day Endpoint--------------

import requests
import time
import json
from splinter import Browser
from datetime import datetime
from config import api_key, executable_path

def nasaphoto():

	#define variables
	endpoint = r"https://api.nasa.gov/planetary/apod?api_key={}".format(api_key) 

	#grab data
	data = requests.get(endpoint)
	#convert to JSON
	textdata = json.loads(data.text)
	#grab data out of JSON
	newurl = textdata["url"]
	explanation = textdata["explanation"]
	#photographer = textdata["copyright"]
	date = textdata["date"]
	title = textdata["title"]

	#Print title, data, photographer and explanation
	print(title)
	print("\n")
	print(date)
	print("\n")
	#print(photographer)
	print("\n")
	print(explanation)

	#download the photo of the day
	img_data = requests.get(newurl).content
	with open(date + ' ' + 'NasaPhotoOfTheDay.jpg', 'wb') as handler:
		handler.write(img_data)

	#visit url in chrome webdriver
	# Create a new instance of the browser, make sure we can see it (Headless = False)
	browser = Browser('chrome', **executable_path, headless=False)
	browser.visit(newurl)
	time.sleep(20)
	browser.quit()

	print("\nCode Has Finished Running")


nasaphoto()