import wolframalpha as wf
import wikipedia

#the class for PyDA Python Digital Assistant
class PyDA():

    def __init__(self,appId):
        #this is the constructor
        #creating an object of the Client class of WF
        self.client = wf.Client(appId)

    def start(self):
        #this handles all the inputs and processing 
        #here i take in the input query
        self.query = raw_input("Hi! I am PyDA ask me anything! :")
        
        self.res = self.client.query(self.query)

        #if wf fails check for wiki, but make sure to filter out spellchecks
        if (self.res.success=="false"):
            self.answer=wikipedia.summary(self.query,sentences=2).encode("utf-8")
        elif('spellcheck' not in dict(self.res.warnings).values()):
            self.answer = next(self.res.results).text
        else:
            #where nobody should ever go...
            self.answer = "Too difficult, Baba...(=<)"

    def show_res(self):
        #just displaying boi.
        print(self.answer)

#create an object of the class while sending unique app id 
riya = PyDA('UJGL6P-TQRJV3UYV5')

#looping questions until exit
while True:
    riya.start()
    # if query is exit , quit
    if riya.query=="exit":
        break
    #else show results
    riya.show_res()
    