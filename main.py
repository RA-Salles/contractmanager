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
import os 
import pandas as pd
from packs.atmhandler import getdatabasepath
from packs.atmhandler import createfolder
#K_DATABASEDIR = os.path.join(os.getcwd, 'data') #this causes a fucking error!
K_USERS = pd.DataFrame({
    'users' : ['root','testuser'],
    'home' : ['user00','xyz']
})
K_ROOTAUTH = pd.DataFrame(
    {
    'pass'  : ['masterpass'],
    'isroot': ['yes']
    }
    )
K_COMMONAUTH = pd.DataFrame(
    {
    'pass'  : ['pass'],
    'isroot': ['no']
    }
    )
K_ROOTACC = pd.DataFrame(
    {
        'cash' : [],
    }
)
K_ROOTHIST = pd.DataFrame(
    {
        'date'    : [], #should contain datetime print of when command was done
        'command' : [] #command should contain comand, targets and miscelaneous info.
    }
)
K_ROOTRQ = pd.DataFrame(
    {
        'user' : ['xyz'],
        'date' : ['19/09/2003'],
        'type' : ['crd 1000 3', ],
        'res'  : ['null'] #null or no or yes. Null ones get buttfucked into oblivion. yes and null are kept when requests clear command is given.
    }
)

K_PAYUP = pd.DataFrame(
    {
        'time'    : [],
        'destiny' : [],
        'cash'    : []
    }
)

def do_maker():
    K_USERS
    """
        do_maker is the function of your dreams! it prepares the database for functioning using pandas.
    """
    pass

def makeuser():
    """
        what it should do:
            create random string of 20 letters. This string will be the name of the folder.
            Get the name of the person.
            Write the name in the same space as the folder in the users.csv. 

    """
    pass



if __name__ == "__main__":
    path = getdatabasepath()
    path = os.path.join(path, 'user00')
    path = os.path.join(path, 'payup.csv')
    K_PAYUP.to_csv(path, index=False)

    
