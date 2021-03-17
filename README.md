# GVE_DevNet_IOS_Configuration_Change_Dashboard
Tracks the configuration changes made to cisco IOS devices using the "Configuration Change Notification" logging available on certain IOS releases. 


## Contacts
* Charles Llewellyn

## Solution Components
* IOS
* Python
* Remote Syslog Server (This program has only been tested on a Linux OS).
* Minimum IOS release supported:
    * 12.3(4)T +
    * 12.2(25)S +
    * 12.2(27)SBC +
    * 12.2(33)SRA + 
    * 12.2(33)SB +
    * Cisco IOS XE Release 3.9S + 


## Installation/Configuration (Log Tracking)

1. Configure supported IOS device to allow [Configuration Change Notification and Logging](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/config-mgmt/configuration/15-sy/config-mgmt-15-sy-book/cm-config-logger.pdf).
1. Configure supported IOS device to send logs to a [Remote Log Server](https://www.cisco.com/c/en/us/td/docs/routers/access/wireless/software/guide/SysMsgLogging.html).
1. Clone this github repository onto the Remote Log Server.
1. Edit the .env file, specifically, edit the value of the 'HOST', 'LOG_FILEPATH', 'LOG_DIRECTORY_PATH' variable to point at your instance of MongoDB.
    1. Example: HOST = "mongodb+srv://<username>:<password>@server.example.com/"
    1. LOG_FILEPATH (Points to the log file that is being populated with the configuration change notification logs)
    1. LOG_DIRECTORY_PATH (Points to the directory that the Log file is located in)
1. Open denylist.txt found in res/filters
    1. Add any command that you would like to flag as an illegal configuration.
    1. These commands will be flagged in the database.
1. Run log_tracker_app.py
    1. configuration changes added to the log file will now populate the database.
    
    
### Here is a simple topology dipicting the device communications needed by this application.
![Syslog Configuration Tracking Topology](/IMAGES/cfg_change_topology.png)


### Configuration Validation (Optional) 
The configuration validation application that is also included in this repo is not required to run, but can offer some cool functionality.

You may want to use this application if you are looking to:
   * Monitor if denylisted configurations are currently in the running configuration of a device.
   
Requirements:
   * This application requires for configuration log data to already be stored in the database.
   * Open up the config_validation_app.py and set how often you would like the config validation to run:
         * Example: scheduler = ConfigurationDenylistValidation(hours=24)
         
   1. Open res/testbeds/testbed.yaml
      * Click [HERE](https://pubhub.devnetcloud.com/media/pyats/docs/topology/creation.html#testbed-file) for more information on PYATS testbed files.
      1. Enter SSH username and password of the devices you wish to validate. You can add more devices by following the same format. 
      1. Go to the first and second device in the testbed file and change its hostname to be the exact hostname of your target device
      1. Next change the IP address field to be the IP address you of the port you wish to SSH into.
      
         

1. Run the application 

### Visualize the data (optional)

If you would like the visualize the configuration change notification log data, you can run the Dashboard app found in Dashboard/app.py

1. Open up the dashboard directory
2. Pip install the requirements.txt file found in the Dashboard directory
3. Run app.py

If you want to see what the Dashboard looks like, scroll down to the screenshot section.

## Usage

To launch log_tracker_app.py and config_validation_app.py:

    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install -r requirements
    $ nohup python log_tracker_app.py
    $ nohup python config_validation_app.py (optional)
    
    
To launch the Dashboard:
   
    $ cd Dashboard
    $ pip install -r requirements
    $ nohup python app.py


# Screenshots

![/IMAGES/0image.png](/IMAGES/0image.png)
![Dashboard Top](/IMAGES/Dashboard_top.png)
![Dashboard Bottom](/IMAGES/Dashboard_bottom.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
