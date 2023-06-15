"""
    Writen by locust, whose aliases are mostly unknown, in 16/05/23
"""

import pandas as pd
import numpy as np
from atmhandler import getdatabasepath as gdb
import os

class logger():
    global logname 
    global logpath
    K_LOGGEDNAME = '' #No user should be alowed to have length 0 names. Allow this to pass and I will find you AND kill. kill you :>
    K_HOMEPATH = ''
    K_ISLOGGED   = False
    K_ISROOT     = False

    def login(self):
        #get info 
        self.user = input("insert user: ")
        self.pswd = input("insert password: ")
        #user login
        dpath = gdb()
        userspath = os.path.join(dpath, 'users.csv')
        usersdf = pd.read_csv(userspath)
        i : int = -1
        found = 0
        for name in usersdf['users']:
            i += 1
            if name == self.user:
                found = 1 #else, means we never got this and whatever name it is it isn't on the fucking list
                break
        if found == 1:    
            home = usersdf['home'][i]
            self.userpath = os.path.join(dpath, home)
            authpath = os.path.join(self.userpath, 'auth.csv')
            authpd = pd.read_csv(authpath)
            if authpd['pass'][0] == self.pswd:
                self.K_ISLOGGED = True
                self.K_LOGGEDNAME = self.user
                self.K_HOMEPATH = home
                if authpd['isroot'][0] == 'yes':
                    self.K_ISROOT= True
            else:
                print('login incorrect')
        else:
            print('login incorrect')
            self.cleanup()
            self.login()
    
    def logout(self):
        self.cleanup()


    def cleanup(self):
        self.K_LOGGEDNAME = '' 
        self.K_HOMEPATH   = ''
        self.K_ISLOGGED   = False
        self.K_ISROOT     = False
    
    def getstatus(self):
        print('stats:')
        print('user: '     , self.K_LOGGEDNAME)
        print('home: '       , self.K_HOMEPATH)
        print('is logged: ' , self.K_ISLOGGED)
        print('isroot: '    , self.K_ISROOT)

if __name__ == '__main__':
    loghandler = logger()
    loghandler.login()
    loghandler.getstatus()
    loghandler.logout()
    loghandler.getstatus()
