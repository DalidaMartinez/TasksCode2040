import requests
import json


def main():

    token = 'c802285d1d9fcb3af4606c08279961ef'
    gitURL = "https://github.com/DalidaMartinez/TasksCode2040"
    req = "http://challenge.code2040.org/api/register"

    dataInput = {'token' : token, 'github': gitURL  }

    answer = requests.post(req, dataInput)


    print answer

main()


