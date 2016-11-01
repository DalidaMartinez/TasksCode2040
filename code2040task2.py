import requests
import sys

def main():
    token = 'c802285d1d9fcb3af4606c08279961ef'
    urlSend = "http://challenge.code2040.org/api/reverse"
    urlRetrieve = "http://challenge.code2040.org/api/reverse/validate"

    tokenData= {'token' : token}

    r = requests.post(urlSend, tokenData)

    reversedString   = stringReverse(r.text)

    data2 =  {'token' : tokenData, 'string': reversedString}

    printStatement = requests.post(urlRetrieve, data2)

    print printStatement

main()

def stringReverse(s):
    return s[::-1]
