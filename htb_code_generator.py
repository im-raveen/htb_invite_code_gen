import base64
import subprocess
import time
time.sleep(2)
print(''' 
         _   _ _____ ____       ___ _   ___     _____ _____ _____
        | | | |_   _| __ )     |_ _| \ | \ \   / /_ _|_   _| ____|
        | |_| | | | |  _ \ _____| ||  \| |\ \ / / | |  | | |  _|
        |  _  | | | | |_) |_____| || |\  | \ V /  | |  | | | |___
        |_| |_| |_| |____/     |___|_| \_|  \_/  |___| |_| |_____|


          ____ ___  ____  _____       ____ _____ _   _
         / ___/ _ \|  _ \| ____|     / ___| ____| \ | |
        | |  | | | | | | |  _| _____| |  _|  _| |  \| |
        | |__| |_| | |_| | |__|_____| |_| | |___| |\  |
         \____\___/|____/|_____|     \____|_____|_| \_|
      
                                                           MADE BY RAVEEN ''')



print("")
print("")
print("tool made for lazy-hacker, i recommend the correct way")

print("")
print("")



subprocess.call("curl -XPOST https://www.hackthebox.eu/api/invite/generate", shell=True) #The command to get the encypted invite-code
print('\n')
api = str(input("copy the code you get and paste it here:\n==> ")) #To store the encrypted in a value
print('\n') #This string will produce a new line
dec = str(base64.standard_b64decode(api)) #The Decrypted code after decoded
print("[+]==> " + dec.replace('b', '')) #replacing th extra charater with a space
print('\n')
print("GOT IT NOW COPY THE CODE YOU GOT WITHOUT " " and paste it in link given below ") #The correct invite code you get
print(" ")
print(" ")
print("https://www.hackthebox.eu/invite")
print('\n')

print("if u like our service please join our yt channel")
print("")
print("https://www.youtube.com/channel/UCXZv6LibWI5exXD6qxWuJyw")
