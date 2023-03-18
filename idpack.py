"""
    Writen by Locust, with some other aliases in about q1-2023, made to work along with datechecker, though they're modular. 
    That's why you don't see me importing shit from it here. Anyway, 
    DONELIST!  :
        NOTHING :>
    TODOLIST1! :
        1. People class
            This should be the basic class. Therefore, other classes should inherit idtesting and other useful stuff. Contracts, though,
            is special. I do think i should move him to main so i can put some date class inside this bitch, but we'll see...

            1.1 Basic structure
                Should at least write some stubs
                Want to add support to both cpf and cnpj since at least in brazil,
                peopla can have both, while enterprises can only have cpnj. 
                wawnt to write some testing functions too.
                When something goes wrong, user should have means to cancel
                or fix or let the program fix it to whatever works(Maybe you
                just want some random id to do some testing or whatever, so 
                this conduct is fine and stuff).
            1.2 Test functions
                These guys gotta run some standard tests with the id and gather 
            1.3 Prompt and correct functions
                Meaning not only the program does not let user pass with some ass wipe id, it also 
                asks him if he wants to correct it already or at least sends him back to initialization
                so he can correct the fuckup he made alright. 
                Maybe it could be cool to also let him cancel operations of creating some variables and 
                classes to give more power to the user, but whatever, lets make it work first.
        2. Enterprise class
            Basically a people class, but it only takes CN as a id type, since its only and always
            a juridical entity, it got no physical form, so no cpf for it. Since contracts may be handled
            between two persons, two enterprises or person-enterprise, it is kind of useful to have it.
            
            2.1 Basic Structure
                Literally the same as people. A contract should have a contractor, a contracted, a date of contract
                and terms of the agreement. A contract should only be registered if it was accepted. Things like that
                are kind of key to what these classes should have and do. 
                I do believe the basic structure to be done if its simply a people class without the ability to 
                hold a cpf and that should do it. Implementing other types of id should also be quite easy.

    NOTES IN DESIGNING THE CHECKS AND CREATING CLASSES
        Thing is some user will eventually fuck up and input very shitty id and expect me to deal with it.
        Shame on him, i won't. Really. I will make him input the id again or cancel the operation. I WILL
        DO THIS. So, i got to thinking about how to do it anyway. We should prompt the user for the class type
        to be created too. As a contract manager, most operations *should* be controlled by the user anyway,
        even if he gotta go ahead and import the stuff directly in python terminal.
    NOTES IN WHY THE FUCK THE ID'S ARE MOSTLY STORED AS STRINGS
        Basically, because i did just this in my last script, so it just came naturally to do it again.
        Not that it will help with some kind of compat., specially considering the other "script" was in C.
        C99, to be more exact, and that runned like fucking dogshit, i kid you not. Anyway, did once and will
        do it again or something like that. This one should run worse, though. Very very fucking badly, i'd wager.
"""
import numpy as np
TYPELIST = {"CNPJ", "CPF"}
TYPESIZELIST = {14, 11} #kind of legacy
PARSEFAILCODE = {"notdone", "notnumber"} #legacy
FAILUREFLAG = False #legacy
DELETEFLAG = False #legacy
CODERISMONKY = "MONKYMAKESBADCODE.FUCKYOU.FIXIT!" #this guy is useful to tell you "STOP MAKING BAD FUCKING CODE, BLOODEE MONKEE"

class people:
    def __init__(self, **keyw):
        """
        Keys should be:
            cpf
            cnpj
            seed
            norandom -> this guy is very very planned. He might not be available in general. I hope so. Too much hassle.
        and then, the structure 
        """
        #INITIALIZATION BLOCK
        seedi : int = 12345
        if 'seed' in keyw:
            try:
                seedi = int(keyw['seed'])
                self.seed = seedi
            except:
                print("initialization seed should be int compatible. Defaulting to basic seed")
                seedi : int = 12345
        else:
            seedi: int = 12345
        randos = []
        rng = np.random.default_rng( seed = seedi ) #this oughta work
        if 'cpf' in keyw:
            self.cpf = keyw[cpf]
        else: #actually, should generate a random cpf. this is a stub, then. TODO!
            cpf = rng.integers(10, size = 9)
            string = ""
            for char in cpf:
                string = string + str(char)
            print(cpf) #debug stuff
            print(string)  #this too
            self.cpf = string
            randos.append('cp') #flags that cpf got created randomly
        if 'cnpj' in keyw:
            self.cnpj = keyw[cnpj]
        else: #actually, should generate a random cpf. this is a stub, then. TODO!
            cnpj = rng.integers(10, size = 12)
            string = ""
            for char in cpf:
                string = string + str(char) #this guy makes every part of the list go into a nice dandy string. 
            print(cnpj) #debug stuff
            print(string)  #this too
            self.cnpj = string
            randos.append('cn') #flags that cnpj got created randomly
        #CHECKING BLOCK
        if 'cp' in randos: # if cp in randos, then it got to be completed. Can't send him to the checker willy nilly, since it got quite a lot of chance to fuckup. 1/99 or something like that.
            fail = self.idtesting(self.cpf, rando = 1)
        else:
            fail = self.idtesting(self.cpf)
        if 'cn' in randos:
            fail = self.idtesting(self.cnpj, rando = 1)
        else:
            fail = self.idtesting(self.cnpj)
        
            
    def reroller(self, **kwarg): #this guy should be able to reroll bad cpf or cnpj rolls.
        rng = np.random.default_rng(seed = self.seed)
        newcpf = rng.integers(10, size = 9)
        newcnpj = rng.integers(10, size = 12)
        if 'cnpj' in kwarg and kwarg['cnpj'] == 1:
            return newcnpj
        else: 
            return newcpf #pretty simple eh. It just shouldn't be called when you don't need it!
    
    def idtesting(someid: str, **kwarg) -> int: #THIS IS INCOMPLETE!!! TODO!
        """
            funcname: idtester
            function: tests to see if it's an valid brazilian honest
                to god id. If not, gives user the middle fingah, ringa.
            process:
                1. Checks via kwarg if rando
                2. Do check or generation
                    2-1. GENERATION PROCESS
                        2-1.1. run for first verifier. Append obtained to id
                        2-1.2. run for second. 
                        2-1.3. check for fuckup. if fuckup, 
                    2-2. CHECKING PROCESS

            if kwarg raises flag for rando, then it should add the verification numbers to 
            the checked number, since random generated id won't have proper verification.
            ah yeah, as long as keyarg rando is in kwarg, it doesn't even check its value.
            So if its not rando, do not put rando in the kwarg.   

            TODO NOTE! I CAN PROBABLY CUT THE SIZE OF THIS MONSTER IN HALF IF I DEFINE
            A FUNCTION TO DO THE HEAVY LIFTING AND SIMPLY USE IT TWICE!!!!!! TODO!!!!!!!!!!!

            its done, though. actually done, iguess. i need to finish the __init__ to actually
            go ahead and test it, but its done.

            failcodes:
                0 - passed alright.
                1 - error during verifier generation in checker
                2 - invalid id (verifier provided not equal to generated)
                3 - error during verifier generation in rando
        """
        failcode = 0
        size = len(someid) #randos come small size. Gotta have this bit up here.
        if 'rando' in kwarg: #this guy handles creating verifier digits. Good only for randos. You put a very naughty non-rando here and you're basically asking me to give you the funny error code.
            fuckup = 0
            if size == 9: #cpf
                marker = 11
                res = 0
                for char in someid:
                    marker -= 1
                    try:
                        res += marker * int(char) #if this guy does not work, there's a not "intable" inside id. Then we are very fucked. MEANS WE GOT A LETTER IN A RANDO! THIS IS A VERY VERY NAUGHTY FUCKUP!!!
                    except:
                        print("major fuckup. check code. this shit got me a NOTNUMBER inside the check. stop this pussy ass mf")
                        fuckup = 1
                        break    
                res = (res * 10)% 11
                if res == 10:
                    res = 0
                try:
                    someid = someid + char(res) #there, we got the first one. Onto the next.
                except:
                    print("got a major one down in a rando.")
                res = 0 #some cleanup. this and the guy below
                marker = 12
                for char in someid: #Go back, Jack, do it again! Wheels turning 'round and 'round...
                    marker -= 1
                    try:
                        res += marker * int(char)
                    except:
                        print("major fuckup. check code. this shit got me a NOTNUMBER inside the check. stop this pussy ass mf")
                        fuckup = 1
                        break
                res = (res * 10) % 11
                if res == 10:
                    res = 0
                try:
                    someid = someid + char(res)
                except:
                    print("major fuckup down in rando, second verifier.")
            elif size == 12: #cnpj TODO!!!! 
                #its basically the same as cpf, little to no shit is actually changed.
                marker = 6
                res = 0
                for char in someid:
                    marker -= 1
                    if marker == 1: #dumb stuff, but whatever.
                        marker = 9
                    try:
                        res += marker * int(char) 
                    except:
                        print("major fuckup. check code. this shit got me a NOTNUMBER inside the check. stop this pussy ass mf")
                        fuckup = 1
                        break    
                res = (res * 10)% 11
                if res == 10:
                    res = 0
                try:
                    someid = someid + char(res)
                except:
                    print("got a major one (and by one i mean fuckup) down in a rando.") #NOTE: remember to change these fuckups to some error code. then we write major random fuckup in the code name :>
                res = 0 
                marker = 7
                for char in someid:
                    marker -= 1
                    try:
                        res += marker * int(char)
                    except:
                        print("major fuckup. check code. this shit got me a NOTNUMBER inside the check. stop this pussy ass mf")
                        fuckup = 1
                        break
                res = (res * 10) % 11
                if res == 10:
                    res = 0
                someid = someid + char(res)
            else:
                print(CODERISMONKY) #skill issue detected. Send him the funny constant :>
                fuckup = 1
            #THE FUCKUP BLOCK: notice these checks independ of the result of the checks up there. We check if you fucked up even when you went fine.
            if fuckup == 0: #meaning no shit got detected during most of the rando stuff. Thennnnnn we run a final check.
                print("Generated verifier digits successfully. Procceeding to normal check.")
                failcode = people.idtesting(someid) #now its for real. If it passes the MAN test, then we speak human language in this viscinity!
            else:
                print("something wrong in your rando. Here, have some monky :>")
                someid = CODERISMONKY #Else, you monkey, ooga ooga. Generate some proper id before trying to play aorund this block.
                failcode = 3
        else: #this guy handles actual testing. It's the same as generating the stuff, somewhat. 
            """
                Basically what we do is generating the correct numbers and check 
                to see if its the same as the numbers provided. If true, then human
                language was spoken.
            """
            fuckup = 0
            checkcode = [someid[-2], someid[-1]]
            someid = someid[0 : size - 2] #this guy here grants me the power of ctrl-c ctrl-v :> We already got the excluded numbers in checkcode, so no harm done.
            if size == 9: 
                marker = 11
                res = 0
                for char in someid:
                    marker -= 1
                    try:
                        res += marker * int(char) 
                    except:
                        print("NOTNUMBER IN CPF")
                        fuckup = 1
                        break    
                res = (res * 10)% 11
                if res == 10:
                    res = 0
                try:
                    someid = someid + char(res) 
                except:
                    print("NOTCHARABLE IN RES")
                res = 0 #some cleanup. this and the guy below
                marker = 12
                for char in someid: #Go back, Jack, do it again! Wheels turning 'round and 'round...
                    marker -= 1
                    try:
                        res += marker * int(char)
                    except:
                        print("NOTNUMBER IN CHAR")
                        fuckup = 1
                        break
                res = (res * 10) % 11
                if res == 10:
                    res = 0
                try:
                    someid = someid + char(res)
                except:
                    print("NOTCHARABLE IN RES")
            elif size == 12:
                marker = 6
                res = 0
                for char in someid:
                    marker -= 1
                    if marker == 1:
                        marker = 9
                    try:
                        res += marker * int(char) 
                    except:
                        print("NOTNUMBER IN CHAR")
                        fuckup = 1
                        break    
                res = (res * 10)% 11
                if res == 10:
                    res = 0
                try:
                    someid = someid + char(res)
                except:
                    print("NOT CHARABLE IN RES")
                res = 0 
                marker = 7
                for char in someid:
                    marker -= 1
                    try:
                        res += marker * int(char)
                    except:
                        print("NOT NUMBER IN CHAR")
                        fuckup = 1
                        break
                res = (res * 10) % 11
                if res == 10:
                    res = 0
                someid = someid + char(res)

            else:
                print("SIZE INCORRECT!")
                fuckup = 1
            #THE FUCKUP BLOCK
            if fuckup == 0: # No fuckup during processing. Means we can do the final check.
                checkgot = [someid[-2], someid[-1]]
                for a, b in checkgot, checkcode:
                    if a != b:
                        failcode = 2
            else: #we got something during process (fuckup = 1)
                failcode = 1
        return failcode
class enterprise:
    def __init__(self):
        pass

class contract:
    def __init__(self):
        pass

if __name__ == '__main__':
    pass



