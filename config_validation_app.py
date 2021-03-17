from models.Scheduler import ConfigurationDenylistValidation


if __name__ == "__main__":
	scheduler = ConfigurationDenylistValidation(seconds=30)
	scheduler.run()