import requests
from bs4  import BeautifulSoup

headers='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'

url='https://sms.bulk.ke/recipient'
 
r= requests.get(url,headers=headers)

print(r.status_code)