import requests

date = input("Date: ")
base = input("Base: ")
rate = input("Rate: ")

link = "https://api.exchangeratesapi.io/"
url = link + date + '?symbols=' + rate



result = requests.get(url=url,params={'base': base})
output = result.json()

print(output)
