from bs4 import BeautifulSoup
import requests
from rich.console import Console
from rich.table import Table
from rich.style import Style

def style_cell(value):
    if value.startswith('-'):
        return "red"
    elif value.startswith('+'):
        return "green"
    else:
        return ""

def get_top_languages(url):
    
    console = Console()
    RichTable = Table(title='Top 20 languages')
    
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    table = soup.find("table", {"id": "top20"})
    rows = table.find_all("tr")
    
    header = rows[0].find_all('th')
    
    RichTable.add_column(header[0].text, justify="center", style="cyan")
    RichTable.add_column(header[1].text, justify="center", style="magenta")
    RichTable.add_column(header[3].text, justify="center", style="green")
    RichTable.add_column(header[4].text, justify="right", style="blue")
    RichTable.add_column(header[5].text, justify="right", style="white")
    
    for row in rows[1:]:
        data = row.find_all("td")
        rank = data[0].text
        last_year_rank = data[1].text
        language = data[4].text
        ratings = data[5].text
        change = data[6].text
        
        RichRow = RichTable.add_row(rank, last_year_rank, language, ratings, change)
        
    console.print(RichTable)
    
get_top_languages('https://www.tiobe.com/tiobe-index/')
