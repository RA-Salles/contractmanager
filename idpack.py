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

"""
import numpy as np
TYPELIST = {"CNPJ", "CPF"}
TYPESIZELIST = {14, 11}
PARSEFAILCODE = {"notdone", "notnumber"}
FAILUREFLAG = False
DELETEFLAG = False

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
            cpf = rng.integers(10, size = 11)
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
            cnpj = rng.integers(10, size = 14)
            string = ""
            for char in cpf:
                string = string + str(char) #this guy makes every part of the list go into a nice dandy string. 
            print(cnpj) #debug stuff
            print(string)  #this too
            self.cnpj = string
            randos.append('cn') #flags that cnpj got created randomly
        #CHECKING BLOCK
            if 'cp' in randos:
                pass
            else:
                pass
            if 'cn' in randos:
                pass
            else:
                pass
            
    def reroller(self, **kwarg): # this guy shou
        pass
    def idtesting(someid: str) -> int: #THIS IS A STUB. FINISH ME! TODO!
        failcode = 0
        return failcode
class enterprise:
    def __init__(self):
        pass

class contract:
    def __init__(self):
        pass

def idtester(someid): #tests cpf and cnpj and whatever; 
    """
    funcname: idtester
    function: tests to see if it's an valid brazilian honest
        to god id. If not, gives user the middle fingah, ringa.
    process:
        1. Parse string;
        2. Verify id type;
            May be done through size or something like that.
            I do believe to be the most easy way.
        3. Crunch
            Get the verify code
        4. Compare
        5. Return
            CREATION OF STANDARD #1:
                return type of idtester is as follows:
                    1. failure:
                        returns 0
                    2. Success(!):
                        TYPENUMBER
                            TYPE - Corresponds to the type of id we're using. May be CP(F) or CN(PJ).
                            NUMBER - Corresponds to the cnpj or cpf of whatever it is we just checked.
                            OBS1: Will come out as string. Shouldn't be too hard.
                            OBS2: No spaces or whatever bullshit of that kind.
                            OBS3: With letters and numbers, we might be able to implement any kind of code
                                without too much hassle. Buckle up(?); yee haw?

    """
    checks = {'types' : TYPELIST, 'sizes': TYPESIZELIST }
    iscnpj = iscpf = False
    hasfailed = False
    #1. PARSE
    parsed = stringparser(someid)
    if parsed in PARSEFAILCODE:
        print("ERRORCODE: STRINGPARSER NOT WORKING. MAKE IT WORK")
        hasfailed = 1
        global idtesthasfailed
        idtesthasfailed = True

    #2. VERIFY TYPE
    elif hasfailed == False:
        size = len(parsed)


def stringparser(someid): #makes ids with any point or whatever lose that shit. MAKE IT HAVE NO POINTS OR WHATEVER OF THAT FUCKING PIECE OF CRAP! 
    """
    funcname: stringparser
    function: makes so that strings have no shit on them
        also checks if string is idlike to some extent.
    process:
        1. get string #this should already be done by this point, but whatever.
        2. get rid of space
        3. get rid of shit
        4. check for not number. If not number, put code notnumber. Must be number
    """
    done = "notdone"
    notnumber = 0
    if notnumber == 1:
        done = "notnumber"
    return done
