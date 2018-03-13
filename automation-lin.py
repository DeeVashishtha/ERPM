# Importing required modules
import json
import requests
import getpass
import urllib3
import sys
import string
import time
#from ncdautomationUS8341FinalCopy import *
#from linuxonetime import *
# Import ends here

# To suppress SSL certificate warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
headers = {'Content-Type': 'application/json', 'Cache-Control': 'no-cache'}
ErpmEnv = input("Please Enter Environment Name. Valid opttions are NCD,Other. \n")
if ErpmEnv.lower() == 'NCD'.lower():
   URL = 'https://anqa01-liebweb1.vcloudqa-int.net/ERPMWebService/AuthService.svc/REST/'
   Authenticator = "vcloudqa-int"
elif ErpmEnv.lower() == 'other'.lower():
   Authenticator = "cloudops-int"
   NCSDC = input("Please Enter DataCenter location. Valid options are AN,SC,UK :\n")
   if NCSDC.lower() == 'AN'.lower():
      URL = 'https://anderpm.cloudops-int.net/ERPMWebService/AuthService.svc/REST/'
   elif NCSDC.lower() == 'SC'.lower():
      URL = 'https://scerpm.cloudops-int.net/ERPMWebService/AuthService.svc/REST/'
   elif NCSDC.lower() == 'UK'.lower():
      URL = 'https://ukerpm.cloudops-int.net/ERPMWebService/AuthService.svc/REST/'
   else:
      print("%s is not a valid option" %str(NCSDC))
      exit(0)
else:
   print("%s is not a valid Environment" %str(ErpmEnv))
   exit(0)
# API end points
#URL = 'http://anqa01-liebweb1.vcloudqa-int.net/ERPMWebService/AuthService_JSON.svc/'
LoginURL = URL + 'Login'
LogoutURL = URL + 'Logout'
MgmtinfoURL = URL + 'ManagementSet?Name='
MgmtCreateURL = URL + 'ManagementSetOps_CreateManagementSet'
MgmtListURL = URL + 'ManagementSets'
MgmtLxServerURL = URL + 'ManagementSet/System/Linux?Name='
lxurl = URL + 'ManagementSet/System/Linux'
winurl = URL + 'ManagementSet/System/Windows'
LxonetimePwd1 = URL + 'StoredCredential'
LxmonthlyPwd1 = URL + 'Job/PasswordChange'
#

# Acquire ERPM authentication Token


def login():
    username = input("Enter the Username: \n")
    password = getpass.getpass()
    MFA = input("Enter the MFA Token :\n")
    logininfo = {'Username': username, "Password": password, "Authenticator": Authenticator, "LoginType": 2, "MFATokenCode": MFA }
    login = requests.post(LoginURL, data=json.dumps(logininfo), headers=headers, verify=False)
    if login.status_code != 200:
        print("Login Failed")
        exit (0)
        return None
    else:
        global token
        token = login.json()
        return token
        print("\n ############################################ \n")
        print("Login Successful \n")


# Login Functions ends here

# Logout Function to destroy the authentication token


def logout():
    logoutdata = {"AuthenticationToken": token}
    logout = requests.post(LogoutURL, data=json.dumps(logoutdata), headers=headers, verify=False)
    if logout.status_code == 200:
        print("Log Out Successful")


# Logout function ends here

# Function for mangement set and server operation

def mgmtset():
    global mgmtname
    a = True
    m = {}
#    mgmtdata1 = {"AuthenticationToken": token}
    headers = {'Content-Type': 'application/json', 'Cache-Control': 'no-cache', "AuthenticationToken": token}
 #   m1 = requests.post(MgmtListURL, data=json.dumps(mgmtdata1), headers=headers, verify=False)
    m1 = requests.get(MgmtListURL, headers=headers, verify=False)
    m.update(m1.json())
    sublist = m["ListValues"]
    while a:
        mgmtname = input("Please provide Management Set Name: \n")
        for i in sublist:
            if i["Value"].lower() == mgmtname.lower():
                b = 0
                a = False
                break
            else:
                b = 1
        if b == 0:
            print("Validation completed, Management Set " + i["Value"] + " exists.\n")
        else:
            print("Management Set %s does not exit" % str(mgmtname))
            if ErpmEnv.lower() == 'other':
                print("Plesae confirm if you want to add new management set:\n")
                createnewmgmt = input(print("Press 'Y' to create new management set or Press 'N' to quit:\n"))
                if createnewmgmt.lower() == 'y':
                    newmgmtdata = {"AuthenticationToken":token, "ManagementSetName":mgmtname}
                    newmgmt = request.post(MgmtListURL, data=json.dumps(newmgmtdata),verify=False)
                    print(newmgmt.json())
                elif newmgmt.lower() == 'n':
                    a = False
                    logout()
                    sys.exit()
                else:
                    print("%s is not a valid option" %str(createnewmgmt))
            else:
                a = False
                logout()
                sys.exit()
# function to verify servers' existance in mangement set

def verifyserver():
    global server
    server = input("Enter the server name \n")
    MgmtServerInfo = {"AuthenticationToken":token}
    headers = {'Content-Type': 'application/json', "AuthenticationToken":token, 'Cache-Control': 'no-cache'}
#    servervalidation = requests.post(MgmtLxServerURL, data=json.dumps(MgmtServerInfo), headers=headers, verify=Fals                                                                                                                          e)
    servervalidation = requests.get(MgmtLxServerURL+mgmtname, headers=headers, verify=False)
    i = servervalidation.json()
    for j in i:
        if j["SystemName"].lower() == server.lower():
            b = 0
        else:
            b = 1
    if b  == 0:
        print("Server already exists")
        logout ()
        sys.exit()
    else:
        print("Go Ahead and add the server")
        Server ()

# Function for Management Set ends here

def Server():
    if len(server) != 0:
        a = True
        while a:
            serveros = input("Enter the OS of the Server: \n")
            print("Going to add %s in Management Set" % str(server))
            mgmtdata3 = {"AuthenticationToken": token, "ManagementSetName": mgmtname}
            m = requests.post(MgmtinfoURL,data=json.dumps(mgmtdata3), headers=headers, verify=False)

            if serveros.lower() == "linux":
                lxdata = {"AuthenticationToken": token, "ManagementSetName": mgmtname, "SystemName": server}
                #lxurl = URL + 'ManagementSet/System/Linux'
                l = requests.post(lxurl, data=json.dumps(lxdata), headers=headers, verify=False)
                print(l.status_code)
                print(l.json())
                server2  = input("Do you want to add another server, Type Yes or No: \n")
                if server2.lower() == "yes":
                    verifyserver()
                    a = False
                elif server2.lower() == "no":
                    a = False
                else:
                    print("Valid options are Yes or No")
                    a = False
            elif serveros.lower() == "windows":
                #winurl = URL + 'ManagementSet/System/Windows'
                windata = {"AuthenticationToken": token, "ManagementSetName": mgmtname, "SystemName": server}
                w = requests.post(winurl, data=json.dumps(windata), headers=headers, verify=False)
                print(w.status_code)
                print(w.json())
                server2  = input("Do you want to add another server, Type Yes or No: \n")
                if server2.lower() == "yes":
                    verifyserver()
                    a = False
                elif server2.lower() == "no":
                    a = False
                else:
                    print("Valid options are Yes or No")
                    a = False
            else:
                print("Valid options for ServerOS are Windows and Linux")
    else:
        print("Invalid server name , Exiting")
        logout()
        exit(0)

def linuxonetime():
    #URL = 'http://anqa01-liebweb1.vcloudqa-int.net/ERPMWebService/AuthService.svc/REST/'
    #LxPwd1 = URL + 'StoredCredential'
    #mgmt = input("Enter the Mgmt: \n")
    TgtAct = input("Enter the Target Account: \n")
    currentpwd = getpass.unix_getpass()
    #loginpwd = getpass.unix_getpass()
    #server = input("Enter the server name: \n")
    DataA1 = {
    "AuthenticationToken":token,
    "AccountName":TgtAct,
    "AssetTag":"",
    "AssociatedGroup":mgmtname,
    "Comment":"",
    "Namespace":"[Linux]",
    "OverwriteSettings":0,
    "Password":currentpwd,
    "SystemName":server
                }
    m = requests.post(LxonetimePwd1, data=json.dumps(DataA1), headers=headers, verify=False)
    print(m.content)
    print("JOB Status Code",m.status_code)


def linuxmonthly():
    #URL = 'http://anqa01-liebweb1.vcloudqa-int.net/ERPMWebService/AuthService.svc/REST/'
    #LxPwd1 = URL + 'Job/PasswordChange'
    #token = login()
    LoginAct = input("Enter the Login Account for monthly job: \n")
    TgtAct = input("Enter the Target Account for monthly job: \n")
    #currentpwd = getpass.getpass()
    #server = input("Enter the server name: \n")
    mytime = (int(time.time())*1000+90000)
    dates = "/Date"+"("+ str(mytime) + ")/"
    DataA1 = {
        "AuthenticationToken":token,
        "JobInfoBase":{
            "NextRunTimeUTC": '''/Date(1518651327000)/''',
            "RunJobOnNewSystems":True
    },
        "PasswordChangeSettings":{
        "AccountComment":"",
        "AccountType":4,
        "AddMissing":False,
        "AddType":0,
        "CancelIfCheckedOut":False,
        "ChangeLoginAccount":True,
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
        "FullAccountName":LoginAct,
        "HostCodePage":1,
        "KeepAccountLockedOutUntilComplete":False,
        "KeyLabel":"",
        "LastCharacterSetBits":15,
        "LoginName":TgtAct,
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
        "StoredAccountName":TgtAct,
        "StoredNamespace":"[Linux]",
        "StoredSystemName":server,
        "SymbolsSetOverride":"",
        "TerminalType":0,
        "Unique":True,
        "UnlockAccount":False,
        "UpdateAutoLogon":False,
        "UpdatedAccountIsRootAccount":False,
        "UseSavedPasswords":False,
        "UseStoredLoginPassword":True,
    },
    "ScheduleInfo": {
        "DayOfMonth": 9,
        "Hours": 18,
        "Minutes": 25,
        #"MonthOfYear":"" ,
        "RetryEnabled": False,
        "ScheduleType": 5
    },
    "SystemList": server
    }
######Password change for Root
    DataA2 = {"NextRunTimeUTC": dates}
    DataA1.update({"JobInfoBase":{"NextRunTimeUTC": dates}})
    m = requests.post(LxmonthlyPwd1, data=json.dumps(DataA1), headers=headers, verify=False)
    print(m.content)
    print("JOB Status Code",m.status_code)
####
def main1():
    login()
    mgmtset()
    verifyserver()
    linuxonetime()
    linuxmonthly()
    logout()

if __name__ == '__main__':
    main1()
