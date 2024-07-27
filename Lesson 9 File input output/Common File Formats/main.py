# common file formats include csv, txt, json, html, office (excel, word, powerpoint)
# parquet, sqlite, pdf

import csv
import json
import openpyxl
import pandas as pd
import sqlite3
import PyPDF2
from bs4 import BeautifulSoup

# Read CSV (Comma-Separated Values)
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    print("CSV Data:")
    for row in reader:
        print(row)

# Read TXT (Plain Text)
with open('data.txt', 'r') as file:
    data = file.read()
    print("\nText Data:")
    print(data)

import json
# Read JSON (JavaScript Object Notation)
with open(r'C:\Users\stani\Downloads\electric_cars.json', 'r') as file:
    data = json.load(file)
    #print("\nJSON Data:")
    #print(data)

# Read HTML (Hypertext Markup Language)
with open(r'C:\Users\stani\Downloads\Home - Federal Reserve Bank of Boston.html', 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')
    print("\nHTML Data:")
    print(soup.get_text())
    from lxml import etree
    dom = etree.HTML(str(soup))
    dom.xpath('//*[@id="main-content"]/div[1]/div/div/div[2]/div/div[1]/div[2]/div/h2/a/text()')

# Read Excel (Office Documents)
import openpyxl
workbook = openpyxl.load_workbook(r'C:\Users\stani\Downloads\FoodImports.xlsx')
sheet = workbook.active
print("\nExcel Data:")
for row in sheet.iter_rows(values_only=True):
    print(row)

# Read Parquet
df = pd.read_parquet('data.parquet')
print("\nParquet Data:")
print(df)

# Read SQLite
conn = sqlite3.connect('data.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM table_name")
rows = cursor.fetchall()
print("\nSQLite Data:")
for row in rows:
    print(row)

# Read PDF
with open('data.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    print("\nPDF Data:")
    num_pages = reader.numPages
    for page_num in range(num_pages):
        page = reader.getPage(page_num)
        text = page.extractText()
        print(text)


