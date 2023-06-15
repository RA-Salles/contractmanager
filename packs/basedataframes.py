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
