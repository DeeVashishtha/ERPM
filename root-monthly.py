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
LxPwd1 = URL + 'Job/PasswordChange'
token = login()
LoginAct = input("Enter the Login Account: \n")
TgtAct = input("Enter the Target Account: \n")
#currentpwd = getpass.getpass()
server = input("Enter the server name: \n")
DataA1 = {
	"AuthenticationToken":token,
    "PasswordChangeSettings":{
    "AccountComment":"",
	"AccountType":4,
	"AddMissing":False,
	"AddType":0,
	"CancelIfCheckedOut":False,
	"ChangeLoginAccount":False,
	"ChangeRootAccount":False,
	"ChangeTwice":False,
	"ClearAutoLogon":False,
	"ConfigFile":"C:\Program Files (x86)\Lieberman\Roulette\AnswerFiles\Response.xml",
	"ConnectionType":1,
	"CurrentPassword":"",
	"DisableAccountLockout":False,
	"DomainName":"",
	"EmailOnChange":"",
	"ExplicitPassword":"",
	"FirstCharacterSetBits":15,
	"FullAccountName":"root",
	"HostCodePage":1,
	"KeepAccountLockedOutUntilComplete":False,
	"KeyLabel":"",
	"LastCharacterSetBits":15,
	"LoginName":"sysadmin",
	"LoginPassword":"",
	"MiddleCharactersSetBits":15,
	"MinLettersLcase":0,
	"MinLettersUcase":0,
	"MinNumbers":0,
	"MinSymbols":0,
	"NewAccountName":"",
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
		"MinLettersLcase":0,
		"MinLettersUcase":0,
		"MinNumbers":0,
		"MinSymbols":0,
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
		"GroupName":"Navisite NCD QA",
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
	"StoredAccountName":"sysadmin",
	"StoredNamespace":"[Linux]",
	"StoredSystemName":"Centos-6-dv",
	"SymbolsSetOverride":"",
	"TerminalType":0,
	"Unique":True,
	"UnlockAccount":False,
	"UpdateAutoLogon":False,
	"UpdatedAccountIsRootAccount":True,
	"UseSavedPasswords":False,
	"UseStoredLoginPassword":True,
    },
    "ScheduleInfo": {
        "DayOfMonth": 6,
        "Hours": 15,
        "Minutes": 53,
        #"MonthOfYear": 2,
        "RetryEnabled": False,
        "ScheduleType": 5
    },
    "SystemList": server
}
######Password change for Root

m = requests.post(LxPwd1, data=json.dumps(DataA1), headers=headers, verify=False)
print(m.content)
print("JOB Status Code",m.status_code)
logout()
