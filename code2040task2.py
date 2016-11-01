import requests


def main():
    urlSend = "http://challenge.code2040.org/api/reverse"
    urlRetrieve = "http://challenge.code2040.org/api/reverse/validate"

    tokenData= {'token' : 'c802285d1d9fcb3af4606c08279961ef'}

    r = requests.post(urlSend, tokenData)

    reversedString   =  r.text[::-1]

    data2 =  {'token':'c802285d1d9fcb3af4606c08279961ef', 'string': reversedString}

    printStatement = requests.post(urlRetrieve, data2)

    print printStatement.text

main()

