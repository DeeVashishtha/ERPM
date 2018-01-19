import json
import requests
from ncdautomationUS8341FinalCopy import *
import urllib3
import sys
import string
# imports end here
# To suppress SSL certificate warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# API end points
URL = 'http://anqa01-liebweb1.vcloudqa-int.net/ERPMWebService/AuthService_JSON.svc/'
LxPwd1 = URL + 'JobOps_CreatePasswordChangeJob'
token = login()
username = input("Enter the Username: \n")
currentpwd = input("Enter the current password for %s: \n" %str(username))
server = input("Enter the server name: \n")
DataA1 = {
    "AuthenticationToken": token,
    "PasswordChangeSettings": {
        "AccountType": 4,
        "AddType": 0,
        "ChangeLoginAccount": False,
        "ChangeRootAccount": False,
        "ConfigFile": "C:\Program Files (x86)\Lieberman\Roulette\Response.xml",
        "ConnectionType": 1,
        "CurrentPassword": currentpwd,
        "FirstCharacterSetBits": 15,
        "MiddleCharactersSetBits": 15,
        "LastCharacterSetBits":15,
        "MinLettersLcase": 1,
        "MinLettersUcase": 1,
        "MinNumbers": 1,
        "MinSymbols": 1,
        "PasswordCharacterSetBits": 15,
        "FullAccountName": username,
        "LoginName": username,
        "LoginPassword": currentpwd,
        "PasswordChangeType": 0,
        "PasswordCompatibilityLevel": 2,
        "PasswordLength": 16,
        "Unique": True,
        "PasswordConstraints": {
            "FirstCharacterSetBits": 15,
            "MiddleCharactersSetBits": 15,
            "LastCharacterSetBits":15,
            "MinLettersLcase": 1,
            "MinLettersUcase": 1,
            "MinNumbers": 1,
            "MinSymbols": 1,
            "PasswordCharacterSetBits": 15,
            "SymbolsExcludeProblematicWithAPIs": True
        },
    },

#       "StoredAccountName": "dvashishtha",
#       "StoredNamespace": "dvashishtha",
#       "StoredSystemName": "String content",
#
#       "UpdatedAccountIsRootAccount": False,
        "UseStoredLoginPassword": False,


    "ScheduleInfo": {
        "DayOfMonth": 4,
        "Hours": 16,
        "Minutes": 43,
        "MonthOfYear": 10,
        "RetryEnabled": False,
        "ScheduleType": 8
    },
    "SystemList": server
}
######Password change for Root

DataA2 = {
    "AuthenticationToken": token,
    "PasswordChangeSettings": {
        "AccountType": 4,
        #"AddType": 0,
        "ChangeLoginAccount": False,
        "ChangeRootAccount": False,
        "ConfigFile": "C:\Program Files (x86)\Lieberman\Roulette\Response.xml",
        "ConnectionType": 1,
        "CurrentPassword": "GoodTime$",
        "FirstCharacterSetBits": 15,
        "MiddleCharactersSetBits": 15,
        "LastCharacterSetBits":15,
        "MinLettersLcase": 1,
        "MinLettersUcase": 1,
        "MinNumbers": 1,
        "MinSymbols": 1,
        "PasswordCharacterSetBits": 15,
        "FullAccountName": "root",
        "LoginName": "dvashishtha",
#        "LoginPassword": "y%NtCZkt25]@]7>K",
        "PasswordChangeType": 0,
        "PasswordCompatibilityLevel": 2,
        "PasswordLength": 16,
        "Unique": True,
        "PasswordConstraints": {
            "FirstCharacterSetBits": 15,
            "MiddleCharactersSetBits": 15,
            "LastCharacterSetBits":15,
            "MinLettersLcase": 1,
            "MinLettersUcase": 1,
            "MinNumbers": 1,
            "MinSymbols": 1,
            "PasswordCharacterSetBits": 15,
            "SymbolsExcludeProblematicWithAPIs": True
        },
    },

       "StoredAccountName": "dvashishtha",
       "StoredNamespace": "LINUX",
       "StoredSystemName": "salt-master-DV",
       "UseSavedPasswords": True,
       "UpdatedAccountIsRootAccount": True,
       "UseStoredLoginPassword": True,


    "ScheduleInfo": {
        "DayOfMonth": 4,
        "Hours": 16,
        "Minutes": 43,
        "MonthOfYear": 10,
        "RetryEnabled": False,
        "ScheduleType": 8
    },
    "SystemList": "salt-master-DV"
}
m = requests.post(LxPwd1, data=json.dumps(DataA1), headers=headers, verify=False)
print(m.content)
print("JOB Status Code",m.status_code)
logout()
