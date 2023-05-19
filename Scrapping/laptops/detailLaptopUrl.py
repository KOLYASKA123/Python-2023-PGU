from bs4 import BeautifulSoup as BS
import requests
import csv

def detailLaptopUrl(base_url, links):
    
    with open('laptops.csv', 'w', newline='') as file:
        
        writer = csv.writer(file)
        writer.writerow(["Title", "Price", "Description"])
        
        for link in links:
            
            page = requests.get(f'{base_url}{link}')
            soup = BS(page.text, 'lxml')
            title = soup.select_one('.caption h4:nth-of-type(2)').text
            price = soup.select_one('.caption .price').text
            description = soup.select_one('.caption .description').text
            writer.writerow([title, price, description])