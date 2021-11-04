import requests
import json
print("Enter a number between 5 and 20")
num=input()
iterator=num
adviceList=[] #will append the advices returned from api
arr=[]
def randData(iterator):
    rows, cols = (int(iterator), 2)
    for i in range(rows):
        response_API = requests.get('https://api.adviceslip.com/advice')
        data = response_API.text
        parse_json=json.loads(data)
        id=parse_json['slip']['id']
        advice=parse_json['slip']['advice']
        col = []
        for j in range(1):
            col.append(id)
            col.append(advice)
        arr.append(col)
    arr.sort()
    for l in range(len(arr)):
        adviceList.append(arr[l][1])
    print(arr)
while(int(num)<5 or int(num)>20):
    print("Enter a number between 5 and 20")
    num=input()
if(int(num)>=5 and int(num)<=20):
    randData(num)