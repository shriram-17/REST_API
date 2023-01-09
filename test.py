
import requests

data=[
    {"likes":10111,"name":"Halo 3 is Awesome","views":10000},
    {"likes":11000,"name":"Why is Node is better than Flask","views":1000},
    {"likes":10000,"name":"Essay on War and Peace","views":10000}
]
BASE ="http://127.0.0.1:5000/"

for i in range(len(data)):
    response=requests.post(BASE+"video/" +str(i),data[i])
    print(response.json()) 


input()
response=requests.get(BASE+"video/all")
for i in range(response.json()):
    print(f"Record: {i}")