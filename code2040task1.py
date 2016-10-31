from urllib2 import Request,urlopen,URLError
import json

data = {'http://challenge.code2040.org/api/register' : 'https://github.com/DalidaMartinez/task1.git'    }
request = Request("http://challenge.code2040.org/api/register")

try:
    response = urlopen(request, json.dump(data))
    answer = response.read()
    print (answer)

except URLError, e:
    print ("error code", e)


