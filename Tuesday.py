import wikipedia  #Adds wikipedia
import wolframalpha  #Adds wolfram alpha


while True:
    uinput = raw_input("Question: ")  #Adds user input
    
    try:
    #WOLFRAM ALPHA
        app_id = "G58JY9-WQ963T9EQV"  #to get the info
        client = wolframalpha.Client(app_id)  #connecting to info
        result = client.query(input)  #collecting result
        answer = next(result.results).text  #processing answer
        print answer  #answering with answer
        
    except: 
        #WIKIPEDIA
        #wikipedia.set_lang("en")  #Language!
        uinput = uinput.split(' ')
        uinput = " ".join(input[2:])
        print wikipedia.summary(uinput)
