import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime

def TESTN():
    filer = ["Bob","Jobob"]
    filer = str(filer)
    filer = filer.replace("['","")
    filer = filer.replace("']","")
    filer = filer.replace("',","")
    filer = filer.replace("'","")
    xname = "tstin"
    file = open(xname + ".txt","w")
    file.write(filer)
    file.close()

    file = open(xname + ".txt","r")
    filer = file.read()
    print(filer)
    filer = filer.split()
    print(filer)
    filer.append("Bobabab")
    print(filer[0])
    print(filer[1])
    print(filer[2])



    #try:
    #    file = open(xname + ".txt", "r")
    #    for line in file.readlines():
    #        print(file.read())
    #    file.close()
    #    print("Load Comlpete")
    #except FileNotFoundError:
    #    print("Error, Load File Not Found")


#TESTN()
def testen():
    while 1:
            x = input("g")
            lstt = []

            for i in range(int(x)+1):
                lstt.append(i)
            print(lstt[0])
            lstt.remove(0)
            print(lstt[0])
            break


    print(lstt)



pythonDictionary = {'name':'Bob', 'age':44, 'isEmployed':True}
def save():
    pythonDictionary = {}
    ToJson = json.dumps(pythonDictionary)

    print(ToJson)

    xname = "2SDAYcanCollect"
    file = open(xname + ".txt","w")
    file.write(ToJson)
    file.close()

def openr():
    try:
        xname = "OWleagueMatch"
        file = open(xname + ".txt", "r")
        jsonData = file.read()
        file.close()
        print("Load Comlpete")
    except FileNotFoundError:
        print("Error, Load File Not Found")
    print(jsonData)
    ToPython = json.loads(jsonData)
    print(ToPython)
    print(ToPython)


    ToJson = json.dumps(ToPython)

    print(ToJson)

    xname = "OWleagueMatch"
    file = open(xname + ".txt","w")
    file.write(ToJson)
    file.close()



def leagueS():
    browser = webdriver.Chrome() # setting the browswer type
    try:
        xname = "OWleagueMatch"
        file = open(xname + ".txt", "r")
        jsonData = file.read()
        file.close()
        print("Load Comlpete")
    except FileNotFoundError:
        print("Error, Load File Not Found")
    print(jsonData)
    ToPython = json.loads(jsonData)
    print(ToPython)
    print("reached")
    browser.get("https://overwatchleague.com/en-us/match/" + ToPython)

    print("REACHED\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    element2 = browser.find_element_by_id("MatchOverview-awayScore")
    print("REACHED\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(element2.text)


    print(datetime.date.today())
    datetime1 = datetime.datetime.now()
    print(datetime1)
    time.sleep(5)
    diff = datetime1 - datetime.datetime.combine(datetime.date.today(), datetime.time())
    print(diff.seconds)
save()
