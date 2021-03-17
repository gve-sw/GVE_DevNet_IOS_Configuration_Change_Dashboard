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


	
