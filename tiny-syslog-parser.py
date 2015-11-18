from pyparsing import Word, alphas, Suppress, Combine, nums, string, Optional, Regex
from time import strftime
import re

class Parser(object):
  def __init__(self):
    ints = Word(nums)
    # timestamp
    month = Word(string.uppercase, string.lowercase, exact=3)
    day   = ints
    hour  = Combine(ints + ":" + ints + ":" + ints)
    timestamp = month + day + hour

    # hostname
    hostname = Word(alphas + nums + "_" + "-" + ".")

    # appname
    appname = Word(alphas + "/" + "-" + "_" + ".") + Optional(Suppress("[") + ints + Suppress("]")) + Suppress(":")

    # message
    message = Regex(".*")

    ## pattern build
    self.__pattern = timestamp + hostname + appname + message
    
  def payload_event(self, log_array):
    payload = {}
    payload["alert_type"] = "error"
    payload["event_type"] = "syslog.error"
    payload["aggregation_key"]  = log_array[3]
    payload["timestamp"] = strftime("%Y-%m-%d %H:%M:%S")
    payload["host"]  = log_array[3]
    payload["msg_title"] = log_array[4]
    if len(log_array) == 6:
        payload["msg_text"] = log_array[5]
    elif len(log_array) == 7:
        # payload["pid"] = log_array[5]
        payload["msg_text"] = log_array[6]
    
    return payload

  def syslog_parse(self, line):
    parsed = self.__pattern.parseString(line)
    event = self.payload_event(parsed) 
    pattern = r"INFO"
    if len(parsed) == 6:
        if (re.search(pattern, parsed[5])):
            event = self.payload_event(parsed) 
            return [event]
        else:
            return None
    elif len(parsed) == 7:
        if (re.search(pattern, parsed[6])):
            event = self.payload_event(parsed) 
            return [event]
        else:
            return None

def main():
  parser = Parser()
  
  with open('/var/log/syslog') as syslogFile:
    for line in syslogFile:
      fields = parser.syslog_parse(line)
      print "parsed:", fields
  
if __name__ == "__main__":
  main()
