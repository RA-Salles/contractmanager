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
def changeproperty(path, property, newval): #won't work for multispace properties, such as hist stuff. Use accordingly
    df = pd.read_csv(path)
    df[property][0] = newval
    df.to_csv(path)

def getproperty(path, property): #also won't work for multiple space properties. Ultrafun
    df = pd.read_csv(path)
    val = df[property][0]
    return val

def histadd(user, command: str): #format command accordingly, else hist will get buttfucked. **Remember to implement a check to see if the user using the command has access to that specific home.**
    now     = datetime.today()
    now     =  now.isoformat()
    users   = getdatabasepath()
    users   = os.path.join(users, 'users.csv')
    dfusers = pd.read_csv(users)
    i: int  = -1
    for name in dfusers['users']:
        i += 1
        if name == user:
            break
    homename= dfusers['users'][i]
    home    = getdatabasepath()
    home    = os.path.join(home, homename)
    histpath= os.path.join(home, 'hist.csv')
    histdf  = pd.read_csv(histpath)
    comms   = [now, command]
    n = len(histdf.index)
    histdf.loc[n] = comms
    histdf.to_csv(histpath, index = False)

#MEISTERONLY
def addaccount(accpath: str, pswd: str): #IT WORKS!
    #set paths
    name         = accpath
    databasepath = getdatabasepath()
    userspd      = os.path.join(databasepath, 'users.csv')
    userspath    = userspd
    userspd      = pd.read_csv(userspd)
    baseuser     = os.path.join(databasepath, 'base')
    accpath      = os.path.join(databasepath, accpath)
    #create directory
    if not os.path.exists(accpath):
        fail = 0
        try:
            shutil.copytree(baseuser, accpath)
        except:
            fail = 1
        if fail == 0: #if creating directory works, 
            home     = name #this guy should be random TODO!
            newuser  = [name, name]
            n = len(userspd.index)
            userspd.loc[n] = newuser
            print(userspd)
            userspd.to_csv(userspath, index = False)
        else:
             print('fail in shutil on addaccount function')   
    else:
        print('user exists. halt')

def delaccount(name): #research how to dell an account TODO!
    pass

def checkuserhistory(name):
    databpath = getdatabasepath()
    userspath = os.path.join(databpath, 'users.csv')
    userspd = pd.read_csv(userspath)
    i = -1
    for user in userspd['users']:
        i += 1
        if user == name:
            break #meaning the position is stored inside i
    homename = userspd['home'][i]
    homepath = os.path.join(databpath, homename)
    hist = pd.read_csv(os.path.join(homepath, 'hist.csv'))
    print(hist)

def give(money, name): #this function NEEDS to check for the logged user name. meaning it MUST check for a global which MUST have the actual users homename or path, whatever. 
    dpath = getdatabasepath()
    userspath = os.path.join(dpath, 'users.csv')
    usersdf = pd.read_csv(userspath)
    i = -1
    for user in usersdf['name']:
        i += 1
        if user == name:
            break
    target = usersdf['home'][i]
    targethome = os.path.join(dpath, target)
    res = getproperty(targethome, 'cash') + money
    changeproperty(targethome, 'cash', res)

def take(money, name):
    dpath = getdatabasepath()
    userspath = os.path.join(dpath, 'users.csv')
    usersdf = pd.read_csv(userspath)
    i = -1
    for user in usersdf['name']:
        i += 1
        if user == name:
            break
    target = usersdf['home'][i]
    targethome = os.path.join(dpath, target)
    res = getproperty(targethome, 'cash') - money
    changeproperty(targethome, 'cash', res)

def usertransfer(origin, destiny, money):
    
    give(money, destiny)
    take(money, origin)


#COMMON -> moved to commands



if __name__ == '__main__': 
    '''
    a = pd.DataFrame(
        {
            'home'  : ['user1', 'user2', 'user3'],
            'funny' : ['a', 'b', 'c']
        }
                    )
    print(a)
    print(len(a.index))
    print(a.loc[0])
    a.loc[3] = ['user4', 'd']
    print(a)
    '''
    addaccount('evenmorefunny', 'evenmorefunny')