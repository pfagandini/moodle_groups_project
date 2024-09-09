import requests
from bs4 import BeautifulSoup

# Moodle login credentials
login_url = "https://your-moodle-site.com/login/index.php"
username = "your_username"
password = "your_password"

# Start a session
session = requests.Session()

# Get the login page to retrieve any form data like tokens
login_page = session.get(login_url)
soup = BeautifulSoup(login_page.content, 'html.parser')

# You may need to get hidden form values like a login token
logintoken = soup.find("input", {"name": "logintoken"})["value"]

# Prepare payload for login
payload = {
    "username": username,
    "password": password,
    "logintoken": logintoken
}

# Send POST request to log in
response = session.post(login_url, data=payload)

# Check if login was successful
if "Dashboard" in response.text:
    print("Login successful!")
else:
    print("Login failed!")
