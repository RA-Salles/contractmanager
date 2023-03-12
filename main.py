"""
    Writen by Locust, without any other known aliases, alongside idpack and datechecker.

    The basic functioning should be as it goes:
        1. Register some random types (people or enterprises);
        2. Register a contract between them;
            Contracts are classes while beign handled by the script, but contracts 
            should be stored in files. This little guy should be able to handle
            literally any kind of contract, but the Contract (as in Contract class)
            actually only contains what contractor contracted whoever, whoever the contractor
            contracted and the date the contract was created
        3. Incript and store the contract
            Might actually go ahead and create a script to facilitate the writing of contracts,
            since its usually a very samy mumbo jumbo, but, for now, the contract must be provided
            to the program in a .txt file. The program then must encrypt the contractor and contractee
            info in the beggining in a certain way so as to go ahead and retrieve this info in the future
        4. Do some cryptography to the contract
            Go ahead and fuck up things quite badly. Make it unreadable to the unprogrammed eye. I **should** 
            implement a password protection to these things, but i might actually make the contractor info the 
            pass. The pass could also be an encryption key of sorts and, if you input the wrong pass, the program
            decrypts it the wrong way and shows some random stuff to the user, meaning there's no such thing as
            "oh, this pass is wrong! Try try again". Nah, it will show you random stuff and that's how you 
            know you fucked up. This might be good to dissuade brute force attackers, too. Don't know shit about
            encryption, though, so it must take some time to learn it. Might lead to some funny stuff...
            if it works :>... 
            It would be godly if i could extract always a given paste of actual not garbage contracts 
            while exctracting a bin and a lot of fucked up messes as another thing like:
                anencryptedbin.bin ->
                    a paste with the contracts equivalent to the cpf you inputed:
                        contract 1
                        contract 2
                        contract 3
                    encryptedshit.bin
            meaning the encryptedbin would be a collection of everyone's contracts, but only a single paste
            may be produced from a password at a time. This. This would be godly, would solve and work alrighty alright.
            A man can dream, i guess. 
        5. Check the info you made
            A planned function, a contract is as good as nothing if it can't be checked, so go ahead 
            and let the user look for contracts using cpf as a searcher. 
"""
import numpy as np
import datechecker as dating
TYPELIST = {"CNPJ", "CPF"}
TYPESIZELIST = {14, 11}
PARSEFAILCODE = {"notdone", "notnumber"}
FAILUREFLAG = False

class people:
    def __init__(self):
        pass

class enterprise:
    def __init__(self):
        pass

class contract:
    def __init__(self):
        pass

def test1(): #function base, just for remembering alright sake
    print("did no shit, boss. I promise.")
    done = "some shit"
    return done

def test2():
    print("don't trust him, boss! he did some shit!")
    return 0

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
                            TYPE - Corresponds to the type of id we're using. May be CP or CN.
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

test1()
test2()
