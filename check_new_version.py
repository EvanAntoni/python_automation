import requests
from bs4 import BeautifulSoup
from notifications import show_notification


def get_latest_version():
    download_page = requests.get('https://ospanel.io/download/').text
    soup = BeautifulSoup(download_page, features="lxml")
    latest_version = soup.find(id="fver").find_all('option')[1].text.split(" - ")[0]

    return latest_version


show_notification('New version OSPanel is available', get_latest_version())
