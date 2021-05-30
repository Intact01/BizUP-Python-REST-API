import requests

BASE = "http://127.0.0.1:5000/"
response = requests.get(
    BASE, {"src": "https://storage.googleapis.com/bizupimg/profile_photo/goodwell_logo.png"})
print(response.json())
response = requests.get(
    BASE, {
        "src": "https://storage.googleapis.com/bizupimg/profile_photo/WhatsApp%20Image%202020-08-23%20at%203.11.46%20PM%20-%20Himanshu%20Kohli.jpeg"})
print(response.json())
response = requests.get(
    BASE, {"src": "https://storage.googleapis.com/bizupimg/profile_photo/918527129869%20instagram-logo-png-2451.png"})
print(response.json())
response = requests.get(
    BASE, {"src": "https://storage.googleapis.com/bizupimg/profile_photo/bhawya_logo.jpeg"})
print(response.json())
response = requests.get(
    BASE, {"src": "https://storage.googleapis.com/bizupimg/profile_photo/kppl_logo.png"})
print(response.json())
