import schedule
import time
import os
from .Connection import PYATSConnection
from .Database import MongoDB
from dotenv import load_dotenv
from datetime import datetime
from .utils import gen_dict_extract

class Scheduler:
	def __init__(self, exact_daily_time=None, minutes=None, hour=None, seconds=None):
		self.exact_daily_time = exact_daily_time
		self.minutes = minutes
		self.hour = hour
		self.seconds = seconds

	def job(self):
		print("Don't forget to configure a job when extending off of this class!")
		pass

	def run(self):
		if self.seconds is not None:
			schedule.every(self.seconds).seconds.do(self.job)

		elif self.minutes is not None:
			schedule.every(self.minutes).seconds.do(self.job)

		elif self.hour is not None:
			schedule.every(self.hour).hour.do(self.job)

		elif self.exact_daily_time is not None:
			schedule.every().day.at(exact_daily_time).do(self.job)

		while True:
			schedule.run_pending()
			time.sleep(1)




		
class ConfigurationDenylistValidation(Scheduler):
	def __init__(self, exact_daily_time=None, minutes=None, hours=None, seconds=None):
		super().__init__()
		load_dotenv()
		host = os.environ.get('HOST')
		self.__device_testbed = PYATSConnection()
		self.__configuration_database = MongoDB(host=host, database_name="Configuration-Change-Notification")
		self.exact_daily_time = exact_daily_time
		self.minutes = minutes
		self.hour = hours
		self.seconds = seconds

	def job(self):
		flagged_entry_ids = list()
		query = {"denylist_flag" : True}
		data = self.__configuration_database.read(query)
		for entry in data:
			source_device_config = self.__device_testbed.get_device_running_config(entry['source_ip'])
			for deny_list_item in gen_dict_extract(source_device_config, entry['config_change']):
				self.__configuration_database.update_by_entry_id({'_id' : entry['_id']}, { "$set" : {"config_change_exists": True, "latest_config_review" : {"flagged_config_line" : deny_list_item, "time_last_reviewed": datetime.now().strftime("%b-%d-%Y T%H:%M:%S")}}})
				flagged_entry_ids.append(entry['_id'])

		for entry in data:
			if entry['_id'] not in flagged_entry_ids:
				self.__configuration_database.update_by_entry_id({'_id' : entry['_id']}, { "$set" : {"config_change_exists": False, "denylist_flag": False}})
				self.__configuration_database.update_by_entry_id({'_id' : entry['_id']}, { "$unset" : {"latest_config_review": ""}})








