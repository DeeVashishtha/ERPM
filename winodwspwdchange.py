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
pwdchg = URL + 'Job/PasswordChange'
token = login()
user = input("Enter the username")
serverw = input("Enter server name: \n")
dataw = {
"AuthenticationToken":token,
"PasswordChangeSettings":{
"AccountComment":"",
"AccountType":0,
"AddMissing":False,
"AddType":0,
"CancelIfCheckedOut":False,
"ChangeLoginAccount":True,
"ChangeRootAccount":False,
"ChangeTwice":False,
"ClearAutoLogon":False,
"ConfigFile":"",
"ConnectionType":1,
"CurrentPassword":"",
"DisableAccountLockout":False,
"DomainName":"",
"EmailOnChange":"",
"ExplicitPassword":"",
"FirstCharacterSetBits":15,
"FullAccountName":user,
"HostCodePage":1,
"KeepAccountLockedOutUntilComplete":False,
"KeyLabel":"",
"LastCharacterSetBits":15,
"LoginName":"",
"LoginPassword":"",
"MiddleCharactersSetBits":15,
"MinLettersLcase":1,
"MinLettersUcase":1,
"MinNumbers":1,
"MinSymbols":1,
"NewAccountName":"*",
"PasswordChangeType":0,
"PasswordCharacterSetBits":15,
"PasswordCompatibilityLevel":2,
"PasswordConstraints":{
	"DefaultPasswordFilterCompliance":0,
	"ExplicitPassword":"",
	"FailGenerationOnMissingPassfiltDLL":False,
	"FirstCharacterSetBits":15,
	"LastCharacterSetBits":15,
	"MiddleCharactersSetBits":15,
	"MinLettersLcase":1,
	"MinLettersUcase":1,
	"MinNumbers":1,
	"MinSymbols":1,
	"PasswordChangeType":0,
	"PasswordCharacterSetBits":15,
	"PasswordCompatibilityLevel":2,
	"PasswordLength":16,
	"PasswordSecurityOptions":0,
	"PasswordSegments":1,
	"PathToPassfiltDLL":"",
	"SymbolsExcludeProblematicWithAPIs":True,
	"SymbolsExcluded":"",
	"SymbolsSetOverride":""
	},
"PasswordLength":16,
"PasswordPropagationSettings":{
	"ConstrainToManagedSystems":False,
	"ConstrainToMembersOfGroup":False,
	"ConstrainToSystemsWithNonzeroInUse":False,
	"ExcludeDomainControllers":False,
	"ExcludeSystemWithAccount":False,
	"GroupName":"",
	"PropagateToSystemWithAccountOnly":False,
	"PropagateToTrustingDomains":False
	},
"PasswordPropagationTargets":{
"ListTargets":[]
},
"PasswordSecurityOptions":0,
"PasswordSegments":1,
"PreventUsernameInPassword":False,
"ReEnableAccountAfterSetTimeHours":False,
"ReEnableAccountIfOperationFails":False,
"RenameAccount":False,
"SendEmailOnChange":False,
"SerializedUtilityIDs":"",
"StoredAccountName":"",
"StoredNamespace":"",
"StoredSystemName":"",
"SymbolsSetOverride":"",
"TerminalType":0,
"Unique":True,
"UnlockAccount":False,
"UpdateAutoLogon":False,
"UpdatedAccountIsRootAccount":False,
"UseSavedPasswords":False,
"UseStoredLoginPassword":False
},
"ScheduleInfo": {
    "DayOfMonth": 7,
    "Hours": 14,
    "Minutes": 20,
    #"MonthOfYear": 2,
    "RetryEnabled": False,
    "ScheduleType": 8
    },
"SystemList": serverw

}
m = requests.post(pwdchg, data=json.dumps(dataw), headers=headers, verify=False)
print(m.content)
print("JOB Status Code",m.status_code)
logout()
