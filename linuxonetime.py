import json
import requests
#from ncdautomationUS8341FinalCopy import *
import urllib3
import getpass
from automation import *
# imports end here
# To suppress SSL certificate warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# API end points

global token
token = login()
print(token)
def linuxonetime():
    URL = 'http://anqa01-liebweb1.vcloudqa-int.net/ERPMWebService/AuthService.svc/REST/'
    LxPwd1 = URL + 'StoredCredential'
    mgmt = input("Enter the Mgmt: \n")
    TgtAct = input("Enter the Target Account: \n")
    currentpwd = getpass.unix_getpass()
    #loginpwd = getpass.unix_getpass()
    server = input("Enter the server name: \n")
    DataA1 = {
    "AuthenticationToken":token,
    "AccountName":TgtAct,
    "AssetTag":"",
    "AssociatedGroup":mgmt,
    "Comment":"",
    "Namespace":server,
    "OverwriteSettings":0,
    "Password":currentpwd,
    "SystemName":server
                }
    m = requests.post(LxPwd1, data=json.dumps(DataA1), headers=headers, verify=False)
    print(m.content)
    print("JOB Status Code",m.status_code)

#logout()
