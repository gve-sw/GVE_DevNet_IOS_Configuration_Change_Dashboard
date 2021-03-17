import gzip
import re
from prettyprinter import pprint
from .Filter import Denylist
import hashlib


class ParseModule:
    def __init__(self, options=[]):
        """Initialize a log parsing module"""
        self.name = ''
        self.desc = ''
        self.format_regex = None
        self.fields = []
        self.__data = {}
        self.__new_file_lines = []
        self.filter = None


    def parse_file(self, sourcepath):
        """Parse a file into a LogData object"""
        # Get regex objects:
        self.regex = re.compile(r'{}'.format(self.format_regex))
 
        # Get our lines:
        try:
        	fparts = sourcepath.split('.')
        except Exception as e:
        	print("Warning! No file extension!")
        if fparts[-1] == 'gz':
            with gzip.open(sourcepath, 'r') as logfile:
                loglines = reversed(logfile.readlines())
        else:
            with open(str(sourcepath), 'r') as logfile:
                loglines = reversed(logfile.readlines())

        # Parse our lines:
        for line in loglines:
            logline = line.rstrip()

            # Send the line to self.parse_line
            entry = self.__parse_line(logline)

        logfile.close()
        return self.__data



    def getLogData(self):
        return self.__data


    def __parse_line(self, line):
        """Parse a line into a dictionary"""
        match = re.findall(self.regex, line)
        if match:
            match = list(match[0])


            fields = self.fields
            entry = {self.fields[i]: match[i] for i in range(len(fields))}

            #Filter blacklist/whitelist entries 
            try:
                entry = self.filter.filter_data(entry)
            except AttributeError:
                #If no filter then pass
                pass

            uid = hashlib.sha256()
            uid_string = ""
            for key, value in entry.items():
                uid_string += str(key)
                uid_string += str(value)
                    
            uid.update(str.encode(uid_string))
            entry["_id"] = uid.hexdigest()

            if uid.hexdigest() not in self.__data.keys():
                self.__data[uid.hexdigest()] = entry







class SyslogConfigParser(ParseModule):
    def __init__(self):
        """Initialize the syslog parsing module"""
        super().__init__()
        self.name = 'syslog config'
        self.desc = 'syslog config parsing module'
        self.format_regex = \
                '(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s[\d]*:\s(\w{3,4}\s{1,2}\d{1,2}\s\d{4})\s(\d\d:?\d\d:?\d\d\.?\d*\sUTC)\:\s%PARSER-5-CFGLOG_LOGGEDCMD:\sUser:(\w*)\s*logged\scommand:(.*)'
        self.fields = ['source_ip', 'date_stamp', 'time_stamp', 'user', 'config_change']
        self.filter = Denylist()



    def getLogData(self):
    	return super().getLogData()



  
