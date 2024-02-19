import requests
from requests.auth import HTTPBasicAuth

url = "https://ayush28chopde.atlassian.net/rest/api/3/issue/bulk"
api_token = "ATATT3xFfGF0wZzuNvtJLfRocR21j_nv3pONoKkihYlo0DWTMksXyen7-OeLmqK04v4_fqbnAdvW4O2d62EAVZXsLeAGlMnm2mJ0r6q5LVluv8g-mLtOX1c2IQlJ-xudaNYSeLYUz2p4MvjTiFyG8z4Xj6NnfDlGGaKn4SgjhnnJw20rAH6pxbw=1968ED35"

auth = HTTPBasicAuth("ayush28chopde@gmail.com", api_token)
project_key = "Ayush_Chopde"

# Get all issues in the project
get_issues_url = "https://ayush28chopde.atlassian.net/rest/api/3/search"
get_issues_params = {
    "jql": f"project={project_key}",
    "maxResults": 1000  # Set a sufficiently large number to fetch all issues
}

response_get = requests.get(get_issues_url, params=get_issues_params, auth=auth)

if response_get.status_code == 200:
    issues = response_get.json().get('issues', [])
    issue_keys = [issue['key'] for issue in issues]

    # Delete issues using the bulk delete endpoint
    bulk_delete_payload = {
        "issueKeys": issue_keys
    }

    response_delete = requests.post(url, json=bulk_delete_payload, headers={"Content-Type": "application/json"}, auth=auth)

    if response_delete.status_code == 200:
        print("All issues deleted successfully.")
    else:
        print(f"Error deleting issues. Status code: {response_delete.status_code}, Response: {response_delete.text}")
else:
    print(f"Error fetching issues. Status code: {response_get.status_code}, Response: {response_get.text}")
