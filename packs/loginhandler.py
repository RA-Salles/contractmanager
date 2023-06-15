"""
    Writen by locust, whose aliases are mostly unknown, in 16/05/23
"""

import pandas as pd
import numpy as np
import atmhandler 
K_LOGGEDNAME = '' #No user should be alowed to have length 0 names. Allow this to pass and I will find you AND kill. kill you :>
K_ISLOGGED   = None
K_ISROOT     = None
class logger():
    global logname 
    global logpath

    def log(self):
        #get info 
        self.user = input("insert user:")
        self.pswd = input("insert password:")
        #user login
        dpath = getdatabasepath()
        
        
