import requests


output = requests.get("https://api.github.com/repos/argoproj/argo-cd/pulls")

details = output.json()

for i in range(len(details)):        
    print(details[i]["user"]["login"])