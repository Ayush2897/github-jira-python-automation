# Projects- Github-jira-python-automation

Step 1: Set Up Jira
Install and Configure Jira:

Install and configure Jira as a Scrum project.
Create and log in to Jira as a Scrum user.
Generate API Token:

Go to Jira Settings -> Profile -> Manage your account settings -> Security -> API token.
Create a new API token and copy it.
Step 2: Communicate Between GitHub, Python, and Jira
Create Python Script to Create Jira Issue:

Refer to the code file "create_jira_ticket_through_api.py".
Edit the code with your Jira URL, API token, and email.
Run Python Script:

Execute the Python script to create a new Jira ticket.
Verify the ticket creation in the Jira console.
Step 3: Set Up Flask on EC2 Instance
Launch EC2 Instance:

Launch an EC2 instance (or use your own machine).
Install Python and pip on the EC2 instance.
Install Flask:

Install Flask using pip: pip install flask.
Create Flask App:

Refer to the code file "Final_code_github_to_jira_ticket_creation.py" to see how Flask is used to create a web service with an endpoint /createJira that listens for HTTP POST requests.
Step 4: Create GitHub Webhook
GitHub Repository Settings:

Go to your GitHub repository settings.
Navigate to Webhooks -> Add Webhook.
Configure Webhook:

Set the Payload URL to your EC2 instance DNS with the path /createJira.
Set Content type to application/json.
Add the webhook.
Step 5: Test the Automation
Commit to GitHub:

Commit some changes or create an issue in your GitHub repository.
Verify Jira Ticket:

Check Jira for the newly created ticket through the automation.
Summary
This setup allows you to automate the process of creating Jira tickets directly from GitHub commits. It involves creating a Python script to interact with the Jira API, setting up a Flask web service on an EC2 instance, and creating a GitHub webhook to trigger the automation. With this setup, every GitHub commit will result in the creation of a corresponding Jira ticket.
