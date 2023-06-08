"""
    Writen by locust, initially in 15/5/23, 21st century after christ.
    This guy should contain the actual manipulation functions using pandas.
    This assumes the user is logged. 
    This assumes there's a file system.
"""
import pandas as pd
import os
import shutil
from datetime import datetime

#FOLDERTHINGS
def getdatabasepath():
    path = os.getcwd()
    path = os.path.join(path, 'data')
    return path

def createfolder(name: str): #folders should be separated by '/' like data/user00/folder1  
    point = os.getcwd()
    path = name.split('/')
    for folder in path:
        point = os.path.join(point, folder)  
        print(point)
    if not os.path.exists(point):
        print("creating folder!")
        print(point)
        os.makedirs(point)
#PANDAS THINGS
def changeproperties(path, property, newval): #won't work for multispace properties, such as hist stuff. Use accordingly
    df = pd.read_csv(path)
    df[property][0] = newval
    df.to_csv(path)

def histadd(user, command: str): #format command accordingly, else hist will get buttfucked. **Remember to implement a check to see if the user using the command has access to that specific home.**
    now = datetime.today()
    now =  now.isoformat()
    users = getdatabasepath()
    users = os.path.join(users, 'users.csv')
    dfusers = pd.read_csv(users)
    i: int = -1
    for name in dfusers['users']:
        i += 1
        if name == user:
            break
    homename = dfusers['users'][i]
    home = getdatabasepath()
    home = os.path.join(home, homename)
    histpath = os.path.join(home, 'hist.csv')
    histdf = pd.read_csv(histpath)
    comms = pd.DataFrame([[now, command]], ['date', 'command'])
    newhist = pd.concat(histdf, comms)
    newhist.to_csv(histpath, index = False)

#MEISTERONLY
def addaccount(accpath: str, pswd: str): #this guy take no input. There should be a handler for a name and a pass, though.
    #CREATE BASE DIRECTORY
    name = accpath
    databasepath = getdatabasepath()
    userspd = os.path.join(databasepath, 'users.csv')
    userspd = pd.read_csv(userspd)
    baseuser = os.path.join(databasepath, 'base')
    accpath = os.path.join(databasepath, accpath)
    
    if not os.path.exists(accpath):
        fail = 0
        try:
            shutil.copytree(baseuser, accpath)
        except:
            fail = 1
        if fail == 0:
            home = 'sometesthome' #this guy should be random TODO!
            newuser = pd.DataFrame([[name, home]], index = ['users', 'home'])
        else:
             print('fail in shutil on addaccount function')   
    else:
        print('user exists. halt')

def delaccount(name):
    pass
def checkuserhistory(name):
    pass
def give(money, name):
    pass
def take(money, name):
    pass
def usertransfer(origin, destiny, money):
    pass

#COMMON
def checkhistory(): #
    pass

def pay(money, destiny):
    pass

def getmoney(money):
    pass

def putmoney(money):
    pass

def program(money, user, times, date):
    pass

def getcredit(money, times, date):
    pass





