
import time
import datetime
from datetime import datetime as dt

hosts_temp=r"C:\Users\pc\Desktop\My web blocker\hosts"  
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
# the IP is where i am redirecting to  
redirect="127.0.0.1"
# this is the list of websites that i want to block
website_list= ["facebook.com","twitter.com" "www.Tvshowmobile.com"]

while True:
    # we want to check if the time now is greater than 8 o clock and less than 4pm....
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("You are at work already...")
        with open (hosts_path, 'r+') as file:
            content= file.read()  
            # this is if the website to be block is already in the hosts file
            for website in website_list:
                if website in content:
                    pass
            # if not, i will write the website to the hosts file
                else:
                    file.write(redirect+" "+ website+"\n")
    # the else statement is for when the we have pass the working hour:if the if statement is false
    else:
        with open(hosts_path, 'r+') as file:
            # the essence of the readlines is so that we can read the hosts file line by line
            # since we want to delete some lines from the hosts file
            content=file.readlines()
            # this is to set the pointer to the beginning of the hosts file and nit the deafault end
            file.seek(0)
            for line in content: 
                if not any(website in line for website in website_list):
                    file.write(line)
            # this will delete all contents that is below the original host file
            file.truncate()    
            
        print("Go and have fun...")
    time.sleep(20)                            
 