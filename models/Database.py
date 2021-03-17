from datetime import datetime
import pymongo

class Database:
	def __init__(self, host):
		self.__client = host


	def write(self, data):
		print("DATA NOT WRITTEN TO DATABASE - Override this function when extending base class!")


class MongoDB(Database):
	def __init__(self, host, database_name):
		collection_name = "Configuration Change Log"
		self.__client = pymongo.MongoClient(host, ssl=True, ssl_cert_reqs='CERT_NONE')
		if database_name in self.__client.list_database_names():
			self.__db = self.__client[database_name]
			print("Connected to %s database..."%database_name)
		else:
			self.__db = self.__client[database_name]
			print("Created database : %s..."%database_name)

		if collection_name in self.__db.list_collection_names():
			self.__collection = self.__db[collection_name]
			print("Connected to %s table..."%collection_name)
		else:
			self.__collection = self.__db[collection_name]
			print("Created table: %s..."%collection_name)




	def write(self, data: dict):
		if data:
		
			try:
				self.__collection.insert_one(data)
				print("New log entry detected! writing to database...")

			except pymongo.errors.DuplicateKeyError as e:
				pass


	def read(self, query: dict):
		return list(self.__collection.find(query))

	def update_by_entry_id(self, update_filter: dict, update: dict):
		if "_id" in update_filter.keys():
			print("Entry %s updated..."%update_filter['_id'])
			self.__collection.update_one(update_filter, update)
		else:
			print("Error, please use the following format for the update_filter: {'_id' : 'entry id' }")

		


