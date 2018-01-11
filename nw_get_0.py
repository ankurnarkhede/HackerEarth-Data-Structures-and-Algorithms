
import requests

# phone=input("Enter a phone number:")
n=int(input("How many times? :"))

for i in range(0,n,+1):
    r = requests.get ("http://www.curlybraces.in/HackYourExams/")
    print('done ',i,' times')



