# Importing required modules
import requests
import getpass
import urllib3
import sys
import string
# Import ends here

# To suppress SSL certificate warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
headers = {'Content-Type': 'application/json', 'Cache-Control': 'no-cache'}
ErpmEnv = input("Please Enter Environment Name. Valid opttions are NCD,NCS. \n")
if ErpmEnv == 'NCD':
   URL = 'http://anqa01-liebweb1.vcloudqa-int.net/ERPMWebService/AuthService_JSON.svc/'
elif ErpmEnv == 'NCS':
   NCSDC = input("Please Enter DataCenter location. Valid options are AN,SC,UK")
   if NCSDC == 'AN':
      URL = 'https://anderpm.cloudops-int.net/ERPMWebService/AuthService_Json.svc'
   elif NCSDC == 'SC':
      URL = 'https://scerpm.cloudops-int.net/ERPMWebService/AuthService_Json.svc'
   elif NSCDC == 'UK':
      URL = 'https://ukerpm.cloudops-int.net/ERPMWebService/AuthService_Json.svc'
   else:
      print("%s is not a valid option, %str()")
else:
   print("%s is not a valid Environment, %str()")

# API end points
#URL = 'http://anqa01-liebweb1.vcloudqa-int.net/ERPMWebService/AuthService_JSON.svc/'
LoginURL = URL + 'DoLogin'
LogoutURL = URL + 'DoLogout'
MgmtinfoURL = URL + 'ManagementSetOps_GetManagementSetInfo'
MgmtCreateURL = URL + 'ManagementSetOps_CreateManagementSet'
MgmtListURL = URL + 'ManagementSetOps_GetManagementSetList'
MgmtLxServerURL = URL + 'ManagementSetOps_GetLinuxSystemListForManagementSet'
#

# Acquire ERPM authentication Token


def login():
    username = input("Enter the Username: \n")
    password = getpass.getpass()
    logininfo = {'Username': username, "Password": password, "Authenticator": "vcloudqa-int", "LoginType": 2 }
    login = requests.post(LoginURL, data=json.dumps(logininfo), headers=headers, verify=False)
    if login.status_code != 200:
        return None
    else:
        global token
        token = login.json()
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
