# -*- coding: utf-8 -*-
"""
Created on Thu May 19 11:33:32 2022

@author: DennisLin
"""

import requests
from bs4 import BeautifulSoup
import csv
import os

def get_raw_data(target_website):
    csv_raw = []
    resp = requests.get(target_website)
    soup = BeautifulSoup(resp.text, "html5lib")
    level1 = soup.tbody.find_all("tr")

    for level2 in level1:
        level3 = level2.find_all("td")
        individual = [ 
            level3[0].text,
            level3[1].text,
            level3[2].text
            ]
        csv_raw.append(individual)   
    return csv_raw

if __name__=="__main__":
    target_website = "http://blog.castman.net/py-scraping-analysis-book/ch2/table/table.html"
    items = get_raw_data(target_website)
    with open("class_price.csv", 'w', newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(('Class', 'Recommendation', 'Price'))
        for item in items:
            writer.writerow((column for column in item))
            
    print("Reading file...")
    print()
    with open("class_price.csv", 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row['Class'], row['Recommendation'], row['Price'])