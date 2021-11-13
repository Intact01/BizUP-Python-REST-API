# Python REST API Task
Send Get request to API with src url of a logo image as attribute to get 2 color values: 
- Border color of image
- Primary logo color

## Installation and Run
Clone the repo on your device and install the dependencies:
```shell
$ git clone https://github.com/Intact01/BizUP-Python-REST-API.git
$ cd BizUP-Python-REST-API
$ pip install -r requirements.txt
```
NOTE: Make sure you have python3 and pip installed. If not then first install them from apt and then try installing dependencies.</br>

Now run the api server:
```shell
$ python3 main.py
```
## For Client
Send get request to server by sending image url as src attribute.
```shell
$ curl http://127.0.0.1:5000?src=<image_url>
```
Replace <image_url> by your logo image URL.

## Tests
### Testcase 1
[Input Logo 1](https://storage.googleapis.com/bizupimg/profile_photo/WhatsApp%20Image%202020-08-23%20at%203.11.46%20PM%20-%20Himanshu%20Kohli.jpeg)
```shell
$ curl http://127.0.0.1:5000?src=https://storage.googleapis.com/bizupimg/profile_photo/WhatsApp%20Image%202020-08-23%20at%203.11.46%20PM%20-%20Himanshu%20Kohli.jpeg
{
    "logo_border": "#98FC03",
    "dominant_color": "#040505"
}
```

### Testcase 2
[Input Logo 2](https://storage.googleapis.com/bizupimg/profile_photo/918527129869%20instagram-logo-png-2451.png)
```shell
$ curl http://127.0.0.1:5000?src=https://storage.googleapis.com/bizupimg/profile_photo/918527129869%20instagram-logo-png-2451.png
{
    "logo_border": "#000000",
    "dominant_color": "#000000"
}
```

### Testcase 3
[Input Logo 3](https://storage.googleapis.com/bizupimg/profile_photo/bhawya_logo.jpeg)
```shell
$ curl http://127.0.0.1:5000?src=https://storage.googleapis.com/bizupimg/profile_photo/bhawya_logo.jpeg
{
    "logo_border": "#9AC431",
    "dominant_color": "#C5031A"
}
```

### Testcase 4
[Input Logo 4](https://storage.googleapis.com/bizupimg/profile_photo/kppl_logo.png)
```shell
$ curl http://127.0.0.1:5000?src=https://storage.googleapis.com/bizupimg/profile_photo/kppl_logo.png
{
    "logo_border": "#05023E",
    "dominant_color": "#03023B"
}
```
