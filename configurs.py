#! /usr/bin/python3

print("### Hello this app is just for change your PS1 desired for ever ###")
print("#################### it's just for ubuntu base ####################")

import os
try:
    import getpass as gs
except ImportError:
    os.system("sudo apt-get install python3-pip")
    os.system("sudo pip3 install getpass4")

PS1 = str(input("Enter your ps1"))
USER = gs.getuser()
PWD = os.getcwd()
if USER != 'root':
    PWD = PWD.split('/')
    if PWD[1] == 'home':
        PWD_N = '/'+PWD[1]+'/'+USER+'/'
        os.chdir(PWD_N)
        DIRs = os.listdir()
        for target in DIRs:
            if target == '.bashrc':
                with open('.bashrc','a') as conf:
                    conf.write("PS1='{0}'\n".format(PS1))
    else:
        PWD = '/home'
else:
    print('super user please change and configur your configs manual.')
