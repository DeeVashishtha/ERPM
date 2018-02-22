"""
print("############################################ \n  ")
print("Purpose of this script and disclaimer \n")
print("############################################ \n  ")
"""
# Importing required modules
import json
import requests
import getpass
import urllib3
import sys
import string
from automation import *
token = login()   #
# Import ends here

# To suppress SSL certificate warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
headers = {'Content-Type': 'application/json', 'Cache-Control': 'no-cache'}

# API end points
URL = 'http://anqa01-liebweb1.vcloudqa-int.net/ERPMWebService/AuthService.svc/REST/'
LoginURL = URL + 'Login'
LogoutURL = URL + 'Logout'
MgmtinfoURL = URL + 'ManagementSetOps_GetManagementSetInfo'
MgmtCreateURL = URL + 'ManagementSetOps_CreateManagementSet'
MgmtListURL = URL + 'ManagementSets'
MgmtLxServerURL = URL + 'ManagementSet/System/Linux?Name='
#
'''
# Acquire ERPM authentication Token


def login():
    username = input("Enter the Username: \n")
    password = getpass.getpass()
    logininfo = {'Username': username, "Password": password, "Authenticator": "vcloudqa-int", "LoginType": 2 }
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


# functions for Management set operation

'''
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
            a = False
            logout()
            sys.exit()

# function to verify servers' existance in mangement set

def verifyserver():
    global server
    server = input("Enter the server name \n")
    MgmtServerInfo = {"AuthenticationToken":token}
    headers = {'Content-Type': 'application/json', "AuthenticationToken":token, 'Cache-Control': 'no-cache'}
#    servervalidation = requests.post(MgmtLxServerURL, data=json.dumps(MgmtServerInfo), headers=headers, verify=False)
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
                lxurl = URL + 'ManagementSet/System/Linux'
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
                winurl = URL + 'ManagementSet/System/Windows'
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
        sys.exit()
'''
def main1():
    login()
    mgmtset()
    verifyserver()
    logout()

if __name__ == '__main__':
    main1()
'''
