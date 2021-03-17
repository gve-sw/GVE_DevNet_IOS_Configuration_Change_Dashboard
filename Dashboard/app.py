""" Copyright (c) 2020 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
           https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied. 
"""

# Import Section
from flask import Flask, render_template, request
import datetime
import requests
import json
from dotenv import load_dotenv
import os


# load all environment variables
load_dotenv()

#Global variables
app = Flask(__name__)

#Methods
#Returns location and time of accessing device
def getSystemTimeAndLocation():
    #request user ip
    userIPRequest = requests.get('https://get.geojs.io/v1/ip.json')
    userIP = userIPRequest.json()['ip'] 

    #request geo information based on ip
    geoRequestURL = 'https://get.geojs.io/v1/ip/geo/' + userIP + '.json'
    geoRequest = requests.get(geoRequestURL)
    geoData = geoRequest.json()

    #create info string
    location = geoData['country']
    timezone = geoData['timezone']
    current_time=datetime.datetime.now().strftime("%d %b %Y, %I:%M %p")
    timeAndLocation = "System Information: {}, {} (Timezone: {})".format(location, current_time, timezone)
    
    return timeAndLocation


##Routes
#Instructions
@app.route('/')
def index():
    try:
        #Page without error message and defined header links 
        return render_template('charts.html') 
    except Exception as e: 
        print(e)  
        #OR the following to show error message 
        return render_template('instructions.html', error=False, errormessage="CUSTOMIZE: Add custom message here.", errorcode=e, timeAndLocation=getSystemTimeAndLocation())


#Settings
@app.route('/settings')
def settings():
    try:
        #Page without error message and defined header links 
        return render_template('settings.html', hiddenLinks=False, timeAndLocation=getSystemTimeAndLocation())
    except Exception as e: 
        print(e)  
        #OR the following to show error message 
        return render_template('settings.html', error=False, errormessage="CUSTOMIZE: Add custom message here.", errorcode=e, timeAndLocation=getSystemTimeAndLocation())


# https://www.chartjs.org/docs/latest/charts/bar.html
@app.route('/charts')
def charts():
    return render_template('charts.html') 

#Main Function
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

