'''

Copyright (c) 2020 Cisco and/or its affiliates.



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

'''
import time
import os
from watchdog.observers import Observer
from models.Handler import LogFileEventHandler
from dotenv import load_dotenv




if __name__ == "__main__":
	 load_dotenv()
	 LOG_FILEPATH = os.environ.get('LOG_FILEPATH')
	 LOG_DIRECTORY_PATH = os.environ.get('LOG_DIRECTORY_PATH')



	 event_handler = LogFileEventHandler(LOG_FILEPATH)
	 observer = Observer()
	 observer.schedule(event_handler, LOG_DIRECTORY_PATH, recursive=False)
	 observer.start()
	 try:
	     while True:
	         time.sleep(1)
	 finally:
	     observer.stop()
	     observer.join()


	
