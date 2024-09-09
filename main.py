import requests
from bs4 import BeautifulSoup

import os
from dotenv import load_dotenv

def main():

    load_dotenv()

    # Moodle login credentials
    login_url = os.getenv("MOODLE")
    username = os.getenv("USER")
    password = os.getenv("PASSWORD")

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

    groups_url = "https://moodle1.ipl.pt/course/groups.php?id=course_id"
    groups_page = session.get(groups_url)
    groups_soup = BeautifulSoup(groups_page.content, 'html.parser')

    # Now parse the HTML to find the form or elements where groups are managed

    add_group_url = "https://moodle1.ipl.pt/course/groups.php?id=course_id&action=add_member"
    payload = {
        'group_id': '12345',
        'user_id': '67890'
    }
    response = session.post(add_group_url, data=payload)


def extract_data():
    pass