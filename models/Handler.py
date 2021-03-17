import os
import time
from dotenv import load_dotenv
from watchdog.events import FileSystemEventHandler
from .Parser import SyslogConfigParser
from .Database import MongoDB
import hashlib
from .Filter import Denylist




class LogFileEventHandler(FileSystemEventHandler):
	def __init__(self, file_location):
		load_dotenv()
		host = os.environ.get('HOST')
		self.__file = file_location
		self.__parser = SyslogConfigParser()
		#Set Filter
		self.__filter = Denylist()
		self.__db = MongoDB(host=host, database_name="Configuration-Change-Notification")
		self.__old = 0
	def on_modified(self, event):
		if event.is_directory:
			return None

		elif event.event_type == 'created':
		# Take any action here when a file is first created.
			pass

		elif event.event_type == 'modified':
			statbuf = os.stat(self.__file)
			new = statbuf.st_mtime
		#Avoids duplicate notifications of file changes made by the Parser (Modifies file to remove items sent to the database in quick succession)
		if (new - self.__old) > 0.5:
			print("Received modified event - %s." % event.src_path)
			# Do any action here.
			self.__parser.parse_file(self.__file)

			# for entry in self.__parser.getLogData()[0]:
			# 	if entry["time_stamp"] and entry["config_change"]
			# 		exists = db.collection.countDocuments({"time_stamp": entry["time_stamp"], "config_change" :  entry["config_change", "source_ip" : entry["source_ip"] ]}, { limit: 1 })
			# 		print(exists)
			# 		if exists == 0:
			

			


			for key, entry in self.__parser.getLogData().items():

				self.__db.write(entry)




		self.__old = new




		

