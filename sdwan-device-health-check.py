import requests
import csv
import urllib3

# Ignore SSL certificate warnings (Lab Environment)
urllib3.disable_warnings()

# vManage Server Details
VMANAGE = "https://vmanage.example.com"
USERNAME = "admin"
PASSWORD = "password"

# Login URL
LOGIN_URL = f"{VMANAGE}/j_security_check"

# Device Status API
DEVICE_API = f"{VMANAGE}/dataservice/device"

# Login Session
session = requests.Session()

login_data = {
    "j_username": USERNAME,
    "j_password": PASSWORD
}

response = session.post(
    LOGIN_URL,
    data=login_data,
    verify=False
)

if response.status_code != 200:
    print("Login Failed")
    exit()

print("Login Successful")

# Retrieve Device Information
response = session.get(
    DEVICE_API,
    verify=False
)

devices = response.json()["data"]

with open("sdwan_device_health_report.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Hostname",
        "System IP",
        "Site ID",
        "Device Type",
        "Reachability"
    ])

    for device in devices:

        writer.writerow([
            device.get("host-name"),
            device.get("system-ip"),
            device.get("site-id"),
            device.get("device-type"),
            device.get("reachability")
        ])

print("Device Health Report Generated Successfully")
