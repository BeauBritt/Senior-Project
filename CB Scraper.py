import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "https://basketball.realgm.com/ncaa/stats/2025/Averages/Qualified/All/Season/All/points/desc/"


def get_ncaa_stats():
    all_rows = []
    headers = None
    page = 1  
    
    while True:
        url = f"{BASE_URL}{page}"
        headers_request = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        
        response = requests.get(url, headers=headers_request)
        
        if response.status_code != 200:
            print(f"Failed to fetch {url}, Status Code: {response.status_code}")
            break
        
        soup = BeautifulSoup(response.text, 'html.parser')
        stats_table = soup.find("table", class_="tablesaw")
        
        if not stats_table:
            print("No stats table found on the page. Stopping.")
            break
        
        if headers is None:
            headers = [th.get_text(strip=True) for th in stats_table.find("thead").find_all("th")]
        
        for row in stats_table.find("tbody").find_all("tr"):
            cells = row.find_all("td")
            if cells:
                all_rows.append([cell.get_text(strip=True) for cell in cells])
        
        print(f"Scraped page {page}")
        page += 1  
        time.sleep(2)  
    
    df = pd.DataFrame(all_rows, columns=headers)
    return df


df = get_ncaa_stats()

if df is not None:
    df.to_csv("ncaa_player_stats.csv", index=False)
    print("Data saved to 'ncaa_player_stats.csv'")
else:
    print("No player stats found.")



