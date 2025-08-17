from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__)

@app.route('/createJira', methods=['Post'])
def createJira():
    url = "https://emailid.atlassian.net/rest/api/3/issue"

    auth = HTTPBasicAuth("", )

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {
        "description": {
        "content": [
            {
            "content": [
                {
                "text": "My First Jira ticket",
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },
        "issuetype": {
        "id": "10007"
        },
        "project": {
        "key": "SUH"
        },
        "summary": "First Ticket",
    },
    "update": {}
    } )

    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )


    return(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

app.run('0.0.0.0')