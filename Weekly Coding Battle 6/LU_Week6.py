#Logic Behind program:
#In any OS there is "C:\Windows\System32\drivers\etc\hosts.txt" file available which contain hostnames of sites which we want to block.
#Simply we need add the site names in host.txt file using Python file handling.

print("---------------------------Alicia Sierra's Web Blocker---------------------------")

from datetime import datetime

Source="C:\Windows\System32\drivers\etc\hosts"
Goto="127.0.0.1"
Sites=["www.facebook.com","www.instagram.com","www.gmail.com"]
print("Enter Duration of Blocking")
print("From:")
year=int(input("Year :"))
month=int(input("Month:"))
day=int(input("Day  :"))
print("--------------------------------------------------------------------------------")
print("To:")
year2=int(input("Year :"))
month2=int(input("Month:"))
day2=int(input("Day  :"))

start=datetime(year,month,day)
end=datetime(year2,month2,day2)
today=datetime(datetime.now().year,datetime.now().month,datetime.now().day)

while True:
    if(start<=today<end):
        with open(Source,"r+") as fl:
            data=fl.read()
            for site in Sites:
                if site in data:
                    pass
                else:
                    fl.write(Goto+" "+site+"\n")
        print("--------------------------------------------------------------------------------")
        print("site is block")
        print("--------------------------------------------------------------------------------")
        break
    else:
        with open(Source,"r+") as fl:
            data=fl.readlines()
            fl.seek(0)
            for line in data:
                if not any(site in line for site in Sites):
                    fl.write(line)
            fl.truncate()
        print("--------------------------------------------------------------------------------")
        print("site is block")
        print("--------------------------------------------------------------------------------")
        break
