import zipfile
from time import time

logo = '''

_________ _______  _______      _______ _________ _______         _______  _       
\__   __/(  ____ \(  ___  )    / ___   )\__   __/(  ____ )       (  ____ \| \    /\
   ) (   | (    \/| (   ) |    \/   )  |   ) (   | (    )|       | (    \/|  \  / /
   | |   | (_____ | (___) | _____  /   )   | |   | (____)| _____ | |      |  (_/ / 
   | |   (_____  )|  ___  |(_____)/   /    | |   |  _____)(_____)| |      |   _ (  
   | |         ) || (   ) |      /   /     | |   | (             | |      |  ( \ \ 
___) (___/\____) || )   ( |     /   (_/\___) (___| )             | (____/\|  /  \ \
\_______/\_______)|/     \|    (_______/\_______/|/              (_______/|_/    \/

                                                                                  
==========================
 Hi Termux Hacker :)     =
==========================
 zip file name : isa.zip =========
password.txt name :passwords.txt =
==================================
login username : isa.py =
login password : isa.py =  
=========================               
'''

print(logo)

username = "isa.py"
password = "isa.py"

givUsername =input("Enter username : ")

if givUsername == username:
    print("Thank You :) ")
    
    givPassword =input("Enter password : ")
    
    
    if




else:
    print("Not Available : ")

'''


Zip password cracker
By Dictionary password attack
Using Python


'''

def main():
    try:
        myZip = zipfile.ZipFile("isa.zip")
    except zipfile.BadZipfile:
        print "There was an error opening your zip file."
        return

    password = ''
    
    print "Password cracking started..."
    print " "
    print "Please wait...."
    timeStart = time()
    with open("passwords.txt", "r") as f:
        passes = f.readlines()
        for pass_count, x in enumerate(passes):
            password = x.strip()
            try:
                myZip.extractall(pwd = password)
                totalTime = time() - timeStart
                print "\nPassword cracking successful: %s\n" % password
                print "%i Password tried per second " % (pass_count/totalTime)
                print " "
                return
            except Exception as e:
                if str(e[0]) == 'Bad password for file':
                    pass # TODO: properly handle exceptions?
                elif 'Error -3 while decompressing' in str(e[0]):
                    pass # TODO: properly handle exceptions?
                else:
                    print e
        print "Please try another passwords list file"

if __name__ == '__main__':
	main()
