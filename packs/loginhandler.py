"""
    Writen by locust, whose aliases are mostly unknown, in 16/05/23
"""

import pandas as pd
import numpy as np

class logger():
    pass
    def __init__(self, user): #user here should be user class
        """
            how logger should work:
                get user
                    find user inside filesystem
                    if not able:
                        raise failflag
                    else:
                        proceed
                        if user is MEISTER:
                            create global variable "USERISMEISTER = 1" -> this will be checked for existance instead of value. python keeps track of what variable names are used
                        else:
                            create global variable "COMMONER = 1"
        """
        self.user = user
        
