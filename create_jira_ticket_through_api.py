import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://ayush28chopde.atlassian.net/rest/api/3/issue"
api_token = "<api_token>"

auth = HTTPBasicAuth("ayush28chopde@gmail.com", api_token)

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

payload = json.dumps({
    "fields": {
        "description": {
            "content": [
                {
                    "content": [
                        {
                            "text": "My first Jira ticket",
                            "type": "text"
                        }
                    ],
                    "type": "paragraph"
                }
            ],
            "type": "doc",
            "version": 1
        },
        "project": {
            "key": "AC"
        },
        "issuetype": {
            "id": "10012"
        },
        "summary": "First JIRA Ticket"
    }
})

response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

