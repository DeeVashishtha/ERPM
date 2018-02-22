import json
import requests
from ncdautomationUS8341FinalCopy import *
import urllib3
import sys
import string
import getpass
# imports end here
# To suppress SSL certificate warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# API end points
URL = 'http://anqa01-liebweb1.vcloudqa-int.net/ERPMWebService/AuthService.svc/REST/'
winref = URL + 'Job/RefreshAndDiscoverWindows'
token = login()
serverw = input("Enter server name: \n")
dataw = {

	"AuthenticationToken":token,
	"JobInfoBase":{
		"RunJobOnNewSystems":True
	},
	"ScheduleInfo":{
		"ScheduleType":1
	},
    "SystemList": serverw
}
a = requests.post(winref, data=json.dumps(dataw), headers=headers, verify=False)
print(a.content)
print("JOB Status Code",a.status_code)
logout()
