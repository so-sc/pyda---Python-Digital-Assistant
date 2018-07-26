import wolframalpha as wf
import wikipedia

#this handles all the inputs and processing 
#here i take in the input query
q = raw_input("Hi! I am PyDA ask me anything! :")

appId = 'UJGL6P-TQRJV3UYV5'
client = wf.Client(appId)

#getting the result after sending query thru client
res = client.query(q)

#if wf fails check for wiki, but make sure to filter out spellchecks
if (res.success=="false"):
    print(wikipedia.summary(q,sentences=2).encode("utf-8"))
else:
    answer = next(res.results).text
    print(answer)


