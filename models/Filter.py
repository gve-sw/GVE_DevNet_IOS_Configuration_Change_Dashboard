class Filter:
	def __init__(self):
		self.filter = None
		self.flag_name = None
		self.filter_name = None

	def filter_data(self,data):
		

		flag, cmd = self.__filter_dict(data)
		
		data[self.flag_name] = flag
		data[self.filter_name + "_trigger"] = cmd

		return data

			

		return filtered_data


	def __filter_dict(self,command):
		for cmd in self.filter:
			if cmd.strip() in command["config_change"]:
				if "no" not in command["config_change"]:
					return True, cmd
			elif cmd.strip() == command["config_change"]:
				return True, cmd

		return False, "None"




class Denylist(Filter):
	def __init__(self):
		try:
			with open('./res/filters/Denylist.txt') as f:
				self.filter = f.read().splitlines() 
		except FileNotFoundError:
			print("Error! Could not find denylist.txt at ../res/filters/denylist.txt")

		self.filter_name = "denylist"
		self.flag_name = "denylist_flag"


class Allowlist(Filter):
	def __init__(self):
		try:
			with open('./res/filters/Allowlist.txt') as f:
				self.filter = f.read().splitlines()
		except FileNotFoundError:
			print("Error! Could not find allowlist.txt  at ../res/filters/allowlist.txt")
		self.filter_name = "allowlist"
		self.flag_name = "allowlist_flag"




