// Import required libraries for web scraping, browser automation, and data processing
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

// Main function to scrape NCAA basketball player statistics from ESPN
def get_espn_ncaa_stats():
    url = "https://www.espn.com/mens-college-basketball/stats/player"

    // Configure Chrome browser options for headless operation
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    // Initialize Chrome driver with configured options
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)

    // Wait for the stats table to load on the page
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".Table__TBODY tr"))
        )
        print("NCAA player stats table loaded.")
    except Exception as e:
        print(f"ERROR: Stats table not found. {e}")
        driver.quit()
        return

    // Click 'Show More' button repeatedly until all players are loaded
    while True:
        try:
            show_more_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div.tc.mv5.loadMore a.loadMore__link"))
            )
            driver.execute_script("arguments[0].click();", show_more_button)
            print("Clicked 'Show More' button.")
            time.sleep(2)  # Allow time for new players to load
        except:
            print("No more 'Show More' button found. All players loaded.")
            break  # Exit loop when no more button is found

    // Extract player data from the table rows
    players = []
    rows = driver.find_elements(By.CSS_SELECTOR, ".Table__TBODY tr")

    // Process each row to extract player information and statistics
    for row in rows:
        try:
            cols = row.find_elements(By.TAG_NAME, "td")

            // Extract player name, position, and team from the first column
            player_name = cols[1].find_element(By.TAG_NAME, "a").text.strip()
            position = cols[1].find_element(By.TAG_NAME, "span").text.strip() if len(cols[1].find_elements(By.TAG_NAME, "span")) > 0 else "N/A"
            team = cols[1].text.replace(player_name, "").replace(position, "").strip()

            // Extract all statistical data from remaining columns
            stats = [col.text.strip() for col in cols[2:]]

            players.append([player_name, position, team] + stats)
        
        except Exception as e:
            print(f"Skipping row due to error: {e}")
            continue

    // Close the browser after data collection
    driver.quit()

    // Create DataFrame with extracted data and save to CSV
    headers = ["Name", "Position", "Team", "GP", "MIN", "PTS", "FGM", "FGA", "FG%", "3PM", "3PA", "3P%", "FTM", "FTA", "FT%", "REB", "AST", "STL", "BLK", "TO"]
    df = pd.DataFrame(players, columns=headers)

    // Save the processed data to a CSV file
    df.to_csv("ncaa_player_stats_cleaned.csv", index=False)
    print("Data extraction complete! File saved as 'ncaa_player_stats_cleaned.csv'.")

// Execute the main scraping function
get_espn_ncaa_stats()





















