from genie.testbed import load
from prettyprinter import pprint

class PYATSConnection:
	def __init__(self):
		self.__testbed = load("./res/testbeds/testbed.yaml")

	def __find_device_by_ip(self, ip):
		for device_name, device in self.__testbed.devices.items():
			if ip == str(device.connections['ssh']['ip']):
				return device

		return None

	def get_device_running_config(self, ip):
		device = self.__find_device_by_ip(ip)
		if device is not None:
			pprint(type(device))
			device.connect(init_config_commands=[])
			return device.learn('config')
		else:
			return None
