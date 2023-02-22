import csv
import json
import requests
from apscheduler.schedulers.background import BackgroundScheduler
from time import sleep

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

scheduler = BackgroundScheduler()

custom_path = r"C:\Users\username\Desktop\ "


def request():
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    result = r.text

    csvheader = ['BTC-USD', 'BTC-EUR']

    with open('A1.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f, delimiter=' ')

        writer.writerow(csvheader)
        writer.writerow(result)
    
    print(result)


scheduler.add_job(request, 'interval', minutes=1)

scheduler.start()

while True:
    sleep(1)








