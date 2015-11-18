# from pyparsing import Word, alphas, Suppress, Combine, nums, string, Optional, Regex
from time import strftime
import re
import time

#def payload_event(log_array):
#  payload = {}
#  payload["alert_type"] = "error"
#  payload["event_type"] = "syslog.error"
#  payload["aggregation_key"]  = log_array[3]
#  payload["timestamp"] = strftime("%Y-%m-%d %H:%M:%S")
#  payload["host"]  = log_array[3]
#  payload["msg_title"] = log_array[4]
#  if len(log_array) == 6:
#      payload["msg_text"] = log_array[5]
#  elif len(log_array) == 7:
#      # payload["pid"] = log_array[5]
#      payload["msg_text"] = log_array[6]
#  
#  return payload

def syslog_parser(log, line):
# def syslog_parser():
  regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) (\d+) "(.*?)" "(.*?)"'
  # line = '172.16.0.3 - - [25/Sep/2002:14:04:19 +0200] "GET / HTTP/1.1" 401 - "" "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.1) Gecko/20020827"'
  # line = '127.0.0.1 - - [19/Nov/2015:01:01:25 +0900] "GET / HTTP/1.1" 200 11764 "-" "curl/7.35.0"'
  result = list(re.match(regex, line).groups())
  # print type(result)
  # f.write(str(result))
  # f.close()

  event = {}
  event["alert_type"] = "error"
  event["event_type"] = "apache.error"
  #event["aggregation_key"]  = log_array[3]
  event["timestamp"] = strftime("%Y-%m-%d %H:%M:%S")
  event["host"]  = result[3]
  event["msg_title"] = result[4]
  #if len(log_array) == 6:
  #    event["msg_text"] = result[5]
  #elif len(result) == 7:
  #    # payload["pid"] = log_array[5]
  #    event["msg_text"] = result[6]
  f = open('/tmp/text.txt', 'a') 
  f.write(str(event))
  f.close()
  return [event]

# syslog_parser()

  #ints = Word(nums)
  #month = Word(string.uppercase, string.lowercase, exact=3)
  #day   = ints
  #hour  = Combine(ints + ":" + ints + ":" + ints)
  #timestamp = month + day + hour
  #hostname = Word(alphas + nums + "_" + "-" + ".")
  #appname = Word(alphas + "/" + "-" + "_" + ".") + Optional(Suppress("[") + ints + Suppress("]")) + Suppress(":")
  #message = Regex(".*")

  #pattern = timestamp + hostname + appname + message
  #parsed = pattern.parseString(line)
  #event = payload_event(parsed) 

  #f = open('/tmp/text.txt', 'a') 
  #f.write(event)
  #f.close()


  #return [event]
  #pattern = re.compile("WARNING")
  #if len(parsed) == 6:
  #    if (re.search(pattern, parsed[5])):
  #        event = payload_event(parsed) 
  #        return [event]
  #    else:
  #        return None
  #elif len(parsed) == 7:
  #    if (re.search(pattern, parsed[6])):
  #        event = payload_event(parsed) 
  #        return [event]
  #    else:
  #        return None
