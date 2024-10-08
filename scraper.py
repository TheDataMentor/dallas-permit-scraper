import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Define the URL to scrape
url = "https://dallascityhall.com/departments/sustainabledevelopment/buildinginspection/Pages/permit_reports2.aspx"

# Send a GET request to fetch the content of the page
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all month links (January to September)
month_links = []
for month in ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep"]:
    link = soup.find('a', href=f"/departments/sustainabledevelopment/buildinginspection/DCH%20documents/excel/Permits_{month}2024.xlsx")
    if link:
        month_links.append(link['href'])

# Base URL for downloading files
base_url = "https://dallascityhall.com"

# Create a directory to store downloaded files
os.makedirs('permits', exist_ok=True)

# Download each file and save it locally
for link in month_links:
    file_url = base_url + link
    file_name = os.path.join('permits', link.split('/')[-1])
    
    with requests.get(file_url) as r:
        with open(file_name, 'wb') as f:
            f.write(r.content)

print("Files downloaded successfully.")

# Initialize an empty list to hold DataFrames
dataframes = []

# Read each Excel file into a DataFrame and append it to the list
for month in ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep"]:
    file_path = f'permits/Permits_{month}2024.xlsx'
    df = pd.read_excel(file_path)
    dataframes.append(df)

# Concatenate all DataFrames into one
combined_df = pd.concat(dataframes, ignore_index=True)

# Display the combined DataFrame
print(combined_df.head())
