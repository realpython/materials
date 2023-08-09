# How to Download Files From URLs With Python

This folder contains sample code for the [How to Download Files From URLs With Python](https://realpython.com/python-download-file-from-url/) tutorial on Real Python.

## Installation

Some of the code requires the following third-party libraries:

- [`aiohttp`](https://pypi.org/project/aiohttp/)
- [`requests`](https://pypi.org/project/requests/)

To install them into a [virtual environment](https://realpython.com/python-virtual-environments-a-primer/), type the following commands:

```shell
$ python3 -m venv venv/
$ source venv/bin/activate
(venv) $ python -m pip install -r requirements.txt
```

## Running

### 01_download_urllib

```shell
$ python 01_download_urllib.py
Date Wed, 28 Jun 2023 19:40:57 GMT
Content-Type application/zip
Content-Length 128310
Connection close
Set-Cookie api_https.cookieCORS=76a6c6567ab12cea5dac4942d8df71cc; Path=/; SameSite=None; Secure
Set-Cookie api_https.cookie=76a6c6567ab12cea5dac4942d8df71cc; Path=/
Cache-Control public, must-revalidate, max-age=1
Expires Wed, 28 Jun 2023 19:40:58 GMT
Last-Modified Wed, 28 Jun 2023 19:40:57 GMT
Content-Disposition attachment; filename=API_NY.GDP.MKTP.CD_DS2_en_csv_v2_5551501.zip
Request-Context appId=cid-v1:da002513-bd8b-4441-9f30-737944134422
Downloaded file gdp_by_country.zip
```

### 02_download_requests

```shell
(venv) $ python 02_download_requests.py
response.url = 'https://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.CD?downloadformat=csv'
response.ok = True
response.status_code = 200
Downloaded file gdp_by_country.zip
```

### 03_download_streaming

```shell
(venv) $ python 03_download_streaming.py
Downloading...
Downloaded file WDI_CSV.zip
```

### 04_download_threading

```shell
(venv) $ python 04_download_threading.py
Downloaded file API_SP.POP.TOTL_DS2_en_csv_v2_5551506.zip
Downloaded file API_EN.POP.DNST_DS2_en_csv_v2_5552158.zip
Downloaded file API_NY.GDP.MKTP.CD_DS2_en_csv_v2_5551501.zip
```

### 05_download_sequential

```shell
(venv) $ python 05_download_sequential.py
Downloaded file API_SP.POP.TOTL_DS2_en_csv_v2_5551506.zip
Downloaded file API_NY.GDP.MKTP.CD_DS2_en_csv_v2_5551501.zip
Downloaded file API_EN.POP.DNST_DS2_en_csv_v2_5552158.zip
```

### 06_download_async

```shell
(venv) $ python 06_download_async.py
Downloaded file API_SP.POP.TOTL_DS2_en_csv_v2_5551506.zip
Downloaded file API_EN.POP.DNST_DS2_en_csv_v2_5552158.zip
Downloaded file API_NY.GDP.MKTP.CD_DS2_en_csv_v2_5551501.zip
```
