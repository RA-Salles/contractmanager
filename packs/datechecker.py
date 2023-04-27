"""
    DateChecker: a simple python script to check for date validity and make sure the date exists.
    Made by Locust, with some other known aliases. 

    TODOLIST!:
        5. debugstuff!
            Must write some code in the __name__ = '__main__' block to test new functionalities!
    DONELIST:
        1. Basic structure
        2. String formatter
            program intakes dates in structure xx/xx/xx...x and should output this too. This is the standard. Don't fuck around.
        3. Number Isolator
            Useful for getting strings and extracting numbers. 
        4. getdate
            Retrieves a date from object date. kwargs include standard of date formatting and separator.
        5. General Checking!
            Checks for dumb mistakes and leap year stuff.
        6. Correct method!
            finds 'fuckups' and fixes them.
"""
from string import digits as DIGITS
DATEWRONG = False
MONTHLIMITS       = { "01": 31, "02": 28, "03": 31, "04": 30, "05": 31, "06": 30, "07": 31, "08": 31, "09": 30,
                       "1": 31,  "2": 28,  "3": 31,  "4": 30,  "5": 31,  "6": 30,  "7": 31,  "8": 31,  "9": 30,
                      "10": 31, "11": 30, "12": 31}
LEAPEDMONTHLIMITS = { "01": 31, "02": 29, "03": 31, "04": 30, "05": 31, "06": 30, "07": 31, "08": 31, "09": 30,
                       "1": 31,  "2": 29,  "3": 31,  "4": 30,  "5": 31,  "6": 30,  "7": 31,  "8": 31,  "9": 30,
                      "10": 31, "11": 30, "12": 31}


class date:

    def __init__(self, day: str, month: str, year: str, **kwargs) -> None: #handle data types as strings so as to not get hid of the zeroes!
        """
        if by whatever fucking reason you wish to handle a very very wrong date with date object, 
        initialize date with name = date(day, month, year, disablecheck = 1)
        This should enable the object to handle alien dates. !!!!BEWARE OF UNSTABLE FUNCTIONING!!!!
        """
        #INITIALIZATION BLOCK
        self.day   = day 
        self.month = month 
        self.year  = year 
        self.ldate = [day, month, year] #this guy is useful if ye wannnnnnna do some iterables. Use updateldate to keep him in check
        self.datewrong = 0 #Not easily accessible. Mostly used for checking
        self.isleapyear = 0 #Same here.
        self.derror = [0] * 3
        listofbeforechristcodes = ['before', 'bc', 'before christ']
        listofafterchristcodes = ['dc', 'ad', 'after', 'after christ']
        if 'christ' not in kwargs or kwargs['christ'] in listofafterchristcodes:
            self.christ = 'ad'
        elif kwargs['christ'] in listofbeforechristcodes:
            self.christ = 'bc'
        else:
            print('christ code not recognized. Reversing to anno domini (ad) default')
            self.christ = 'ad'
        #CHECKBLOCK
        if 'disablecheck' not in kwargs or kwargs['disablecheck'] == 0:
            self.allcheck()
        elif kwargs['disablecheck'] == 1:
            pass

    def allcheck(self):
        self.zeroer() #As zeroer runs before any monthlimits are checked, dictionary constants are probably bigger than they should...
        self.leapcheck()
        self.gcheck()
        #if self.datewrong == 1:
        #    self.correct()

    def update(self, somedates: list):
        self.day = somedates[0]
        self.month = somedates[1]
        self.year = somedates[2]
        self.ldate = [self.day, self.month, self.year]

    def zeroer(self):
        """
        Zeroer: the bastion of the xx/xx/xxxx standard!
        Function: puts zeroes when there's dates like 1/2/32
            turning this shitty ass format into a great and 
            big dick 01/02/0032. I do not fucking care, it look
            much better than whatever else. 
        Functioning:
            1. Detect fucked up len.
            2. Mark every fucked up len.
            3. run zero**** function for every fuck up user made.
            4. Done!
        """
        #comments are debugging messages. Uncomment for debugging fuckery
        def zeroday(dateobj: date):
            #print("executed zeroer's zeroday")
            dateobj.day = '0' + dateobj.day # 2 -> 02

        def zeromonth(dateobj: date):
            #print("executed zeroer's zeromonth")
            dateobj.month = '0' + dateobj.month # 3 -> 03

        def zeroyear(dateobj: date):
            #print("executed zeroer's zeromonth")
            while len(dateobj.year) < 4: # 32 -> 032 -> 0032 
                dateobj.year = '0' + dateobj.year 

        switch = {'1': zeroday,
                  '2': zeromonth,
                  '3': zeroyear}
        mustzero = list()
        mustzero.clear()
        #print("executing zeroer's lenchecks ")
        if len(self.day) < 2:
        #    print(self.day)
        #    print(len(self.day))
        #    print("single digit day. Correcting!")
            mustzero.append('1')
        if len(self.month) < 2:
        #    print("single digit month. Correcting!")
            mustzero.append('2')
        #print("printing contents of mustzero")
        #print(mustzero)
        if len(self.year) < 4:
            mustzero.append('3')
        counter = 0
        for zeroing in mustzero:
            counter += 1
            switch[zeroing](self)
        #print("times zeroing happen'd: " + str(counter))

    def leapcheck(self) -> None: #DONE
        leap = 0
        year = int(self.year)
        if year % 400 == 0:
            self.isleapyear = 1
        elif year % 4 == 0 and year % 100 != 0:
            self.isleapyear = 1

    def gcheck(self): #detects general errors.
        """
            gcheck: the user shennanigan detector
            Will perform a series of checks and then send the check result to correct so they can be corrected.
            One thing to be aware of is the day overflow (day > 31) check.
                As it is dependant of the month, the month must be first checked.
                If it gets a bloody error before it can even check for a day, it stops in its tracks.
                Then, the program should send the message to correct. 
                Correct calls gcheck again anyway, so the idea is simple: it repeats until it
                cracks all errors and stuff.
        """
        #error codes are detailed in correct method
        self.datewrong = 0
        self.derror = [0] * 3
        gonewrong = 0
        day, month, year = int(self.day), int(self.month), int(self.year) #these are numbers! Date object stores dates as strings for ease of output!
        #MONTHCHECKING
        try:
            MONTHLIMITS[self.month] #this checks for month overflow/underflow. Basically, if this guy goes, then month is under the limits.
        except: #else, this dude is of limits.
            if month > 12: self.derror[1] = 1
            elif month <= 0: self.derror[1] = 2
            self.datewrong = 1
        #DAY OVERFLOW CHECKING
        if self.datewrong != 1: # if datewrong was already activated, then the block down here shouldn't run at all, else many errors!
            if self.isleapyear == 0 and day > MONTHLIMITS[self.month]: 
                self.derror[0] = 1
                self.datewrong = 1
            elif self.isleapyear == 1 and day > LEAPEDMONTHLIMITS[self.month]: #handles february 29th!
                self.derror[0] = 1
                self.datewrong = 1

        #DAY-YEAR UNDERFLOW CHECK
        if day <= 0:
            self.derror[0] = 2
            self.datewrong = 1
        if year <= 0:
            self.derror[2] = 2
            self.datewrong = 1
        #Correction phase
        if self.datewrong == 1:
            self.correct()

    def correct(self): #TODO!
        """
            Year errors are very rare, but may happen. I actually doubt anyone using the 
            proper date extractor method can extract a negative date, but anyway:

            ERROR CODES:
                0: no error
                1: upper limit reached
                    correction: sends back within limit.
                2: lower bound broke
                    correction: fucked up bit goes to 1
                n: negative 
                    Deprecated. Solutions is the same as underflow, anyway :/
                obs: 
                    These error codes basically dictate the correction functioning :>
            This guy in general prevents unstable functioning. It is better to have your date corrected
            and have to type again than to get unstable functioning in your database and endup
            fucking up a lot of important contract data. If you want some major shit going on, 
            simply go ahead and use the disablechecks
        """

        if self.datewrong == 1:
            print("date is wrong! correcting...")
            def fday(dateobj: date, fuckup: int): #TODO
                print("running for day")
                if fuckup == 1:
                    dickson = 1 #THIS SHIT IS NO CODE, ITS A PLACEHOLDER!!! TODO!
                    try:
                        if dateobj.isleapyear == 0:
                            dateobj.day = str(MONTHLIMITS[dateobj.month])
                        else:
                            dateobj.day = str(LEAPEDMONTHLIMITS[dateobj.month])
                    except:
                        print("month is fucked up also. We'll get 'em next run") #Meaning the while loop will have to run some more to correct.
                elif fuckup == 2:
                    dateobj.day = '01'
            def fmonth(dateobj: date, fuckup): #TODO
                print("running for month")
                if fuckup == 1:
                    dateobj.month = '12'
                elif fuckup == 2:
                    dateobj.month = '01'
            def fyear(dateobj: date, fuckup): #TODO
                if fuckup != 0:
                    print("how the fuck did you even manage to\
                        fuckup a year????")
                    if fuckup == 1:
                        pass
                    elif fuckup == 2:
                        if int(self.year) < 0: #handles negatives. this should be a code n, but we can handle without it just fine.
                            self.year = str(int(self.year) * -1)
                        elif int(self.year) == 0: #zero is special case
                            self.year = '01'

            switch = { 1 : fday , 2 : fmonth , 3 : fyear }
            loopcounter = 0
            while self.datewrong == 1:
                fuckups = self.derror
                intercounter = 0
                for fuckup in fuckups:
                    intercounter += 1
                    switch[intercounter](self, fuckup)
                self.gcheck() #this guy makes datewrong = 0 in its beggining. It runs check again to make sure no fuckup is made.
                loopcounter += 1
                if loopcounter > 100: #if the process runned for long and shit ain't happening, then, print a debug alarm and break
                    print("MAJOR FUCKUP DETECTED IN CORRECT METHOD. DATEWRONG NEVER 0. FIXME!")
                    break
        elif self.datewrong == 0:
            print("Date not wrong. Not correcting.")

    def getdate(self, **kwargs) -> str:
        """
            accepted kwargs:
                strd: defines standard of date outputting
                    us: MM/DD/YYYYY
                    bizarre1: YYYY...Y/MM/DD
                    DEFAULT: DD/MM/YYYY
                sep: defines separator 
                    Can be anything printable. Beware what you put is what you get.
                    Using other numbers as separators, for example, may cause you 
                    great dismay when you try to separate the formatted date into 
                    a date object again.

        """
        if 'sep' not in kwargs:
            sep = '/' #STANDARD OUTPUT TYPE XX/XX/XXXX
        else:
            sep = kwargs['sep']
        def usformat():
            string1 = self.month + sep + self.day + sep + self.year #US Standard
            return string1
        def bizarre1format():
            string1 = self.year + sep + self.month + sep + self.day #Bizarre Testing Standard
            return string1
        strdswitch = { "us"       : usformat,
                       "bizarre1" : bizarre1format}
        if 'strd' not in kwargs:
            string = self.day + sep + self.month + sep + self.year #Brazilian Standard
        else:
            string = strdswitch[kwargs['strd']]
        return string
    
    def stringdategetter(somestring: str) -> list :
        """
        cool little function to parse a xx/xx/xx...xx string into a dandy little [day, month, year] list.
        Makes life somewhat easier.
        """
        counter: int = 0
        bars = list()
        day = str()
        month = str()
        year = str()
        for char in somestring:
            counter += 1
            if char == '/':
                bars.append(counter-1)
        day = somestring[0:bars[0]] #'xx'/xx/xxxxx...xxx
        month = somestring[bars[0]+1:bars[1]] #xx/'xx'/xxxx...xx
        year = somestring[bars[1]+1:len(somestring)] #xx/xx/'xxx...xxx'
        datelist = [day, month, year]
        return datelist
    def numberisolator(somestring: str) -> list : #returns a list of numbers found in a string.
        """
        funcname: numberisolator
        function: isolates any numbers found in string
        functioning:
            1. accumulates chars until it finds a non-digit (not in DIGITS)
            2. when it finds a not number, deposits string of digits (a number) in the list of numbersfound. 
                2.1. while at this, clears the digit accumulator 
            3. repeats process until all chars from string have been checked.
            4. when done, cleans numbersfound of any disgraceful empty string entries.
        obs:
            this guy probably can be repurposed to isolate any group of things. Remember though
            that the EOS code gotta be different from what you're trying to find! Like, use numbers or
            symbols if you're trying to isolate words. Things like this. 
        """ 
        somestring = somestring + 'EOS' #End Of String 
        numbersfound = list()
        numbers = ""
        counter = 0
        for char in somestring:
            counter += 1 
            if char not in DIGITS: 
                if len(numbers) > 0:
                    numbersfound.append(numbers) #add to list of numbers found
                    numbers = "" #clean up
            else:
                numbers = numbers + char #accumulation phase
        return numbersfound


#GIANT TESTING BLOCK. RUN BY INITILIAZING SCRIPT AS MAIN SCRIPT!
if __name__ == "__main__":
    print("script initialized as main. INITIATING TESTING ROUTINES.")
#TESTBLOCK1#################################################################################################################
    print("BEGGINING TEST 1: STRINGDATEGETTER")
    dates = date.stringdategetter("01/02/2003")
    print(dates)
    testdate = date(dates[0], dates[1], dates[2]) #this oughta work! ps: it fucking does!!!!!
#TESTBLOCK2#################################################################################################################
    print("BEGGINING TEST 2.1: NUMBERISOLATOR 1")
    bigstringofisolatornumbers = "aaaaaaaaahahahahahoooohooooo12314241412iiiiiiiii123412412412 1241241     123145666 aaaaaaaa1321414214 "
        #expected results: ['12314241412', '1234124123412', '1241241', '123145666', '1321414214']
    isolatednumbers = date.numberisolator(bigstringofisolatornumbers)
    print(isolatednumbers)
    print("BEGGINING TEST 2.2: NUMBERISOLATOR 2")
    bigstringofisolatornumbers = "19/09/2003"
        #expected results: ['19', '09', '2003']
    isolatednumbers = date.numberisolator(bigstringofisolatornumbers)
    print(isolatednumbers)
    print("BEGGINING TEST 2.3: NUMBERISOLATOR 3")
    bigstringofisolatornumbers = "19-09!2003"
        #expected results: ['19', '09', '2003']
    isolatednumbers = date.numberisolator(bigstringofisolatornumbers)
    print(isolatednumbers)
#TESTBLOCK3#################################################################################################################
    print("BEGGINING TEST 3.1: GETDATE")
    print(testdate.getdate())
    print("BEGGINING TEST 3.2: GETDATE US")
    print(testdate.getdate(strd = "us"))
    print("BEGGINING TEST 3.3: GETDATE BIZARRE")
    print(testdate.getdate(strd = "bizarre1"))
    print("BEGGINING TEST 3.4: GETDATE LUDICROUS SEPARATORS")
    print(testdate.getdate(sep = 'bigdickson'))
    print(testdate.getdate(sep = '!!!'))
    print(testdate.getdate(sep = '#'))
    print(testdate.getdate(sep = 'nodickson'))
    print("BEGGINING TEST 3.5: GETDATE SEPARATOR + US FORMATTING")
    print(testdate.getdate(sep = 'nodickson', strd = 'us'))
    print(testdate.getdate(sep = '|', strd = 'us'))
    print(testdate.getdate(sep = 'SEPARATOR', strd = 'us'))
#TESTBLOCK4 - OBJECT Fuckeriess >:#################################################################################################################
    print("BEGINNING TEST 4.1 - DATE OBJECT DEBUGGING I")
    somedate = "02/03/2003"
    somedate = date.numberisolator(somedate)
    testdate = date(somedate[0], somedate[1], somedate[2])
    print(testdate.getdate())
    print("BEGGINING TEST 4.2 - DATE OBJECT DEBUGGING 2: zeroer")
    somedate = "2/3/3"
    somedate = date.numberisolator(somedate)
    testdate = date(somedate[0], somedate[1], somedate[2])
    somedate = "2/3/3"
    print("Date before zeroing: "+ somedate + "\n" +\
          "Date after zeroing: " + testdate.getdate())
    print("BEGGINING TEST 4.3 - DATE OBJECT DEBUGGING 3: leap year fuckery")#JUST PUTTING SOME CANNON FODDER HERE. TODO!! REMEMBER TO ACTUALLY CODE A TESTBLOCK YOU DUMB LAZY ASS BASTARUDO!
    somedate = "29/2/1999"
    somedate = date.numberisolator(somedate)
    testdate = date(somedate[0], somedate[1], somedate[2])
    somedate = "29/2/1999"
    print("original:" + somedate + "\n"\
          "corrected:" + testdate.getdate())
    print("control! testing for a valid date:")
    somedate = "29/2/2000"
    somedate = date.numberisolator(somedate)
    testdate = date(somedate[0], somedate[1], somedate[2])
    somedate = "29/2/2000"
    print(testdate.getdate())
    print("NEXT TEST!")
    somedate = "-82/321/-1999"
    somedate = date.numberisolator(somedate)
    testdate = date(somedate[0], somedate[1], somedate[2])
    somedate = "-82/321/-1999" #some real fdup date. Program handled it like a champ.
    print("original:" + somedate + "\n"\
          "corrected:" + testdate.getdate())