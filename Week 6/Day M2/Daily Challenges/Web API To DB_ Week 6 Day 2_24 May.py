import requests
import random
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

DB_NAME = 'web_api_to_db'
DB_USER = 'postgres'
DB_PASSWORD = 'admin123'
DB_HOST = 'localhost'
DB_PORT = '5432'

connection = psycopg2.connect(
    dbname='postgres',
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)  # Allows creating and dropping databases
cursor = connection.cursor()
cursor.execute(sql.SQL("DROP DATABASE IF EXISTS {}").format(sql.Identifier(DB_NAME)))
print(f"Database {DB_NAME} dropped successfully if it existed.")

cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(DB_NAME)))
print(f"Database {DB_NAME} created successfully.")
cursor.close()
connection.close()

response = requests.get('https://restcountries.com/v3.1/all')
if response.status_code == 200:
    countries = response.json()
    print(f"Fetched data for {len(countries)} countries.")
else:
    raise Exception("Failed to fetch data from the REST Countries API")

random_countries = random.sample(countries, 10)
print("Selected 10 random countries.")

connection = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)
cursor = connection.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS countries (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        capital VARCHAR(100),
        flag TEXT,
        subregion VARCHAR(100),
        population INTEGER
    )
''')
connection.commit()
print("Table 'countries' created successfully.")
for country in random_countries:
    name = country.get('name', {}).get('common')
    capital = country.get('capital', [None])[0] if 'capital' in country else None
    flag = country.get('flags', {}).get('png')
    subregion = country.get('subregion')
    population = country.get('population')
    cursor.execute('''
        INSERT INTO countries (name, capital, flag, subregion, population)
        VALUES (%s, %s, %s, %s, %s)
    ''', (name, capital, flag, subregion, population))
    print(f"Inserted country: {name}, capital: {capital}, flag: {flag}, subregion: {subregion}, population: {population}")
connection.commit()
cursor.execute('SELECT * FROM countries')
rows = cursor.fetchall()
print(f"\nData in the 'countries' table:")
for row in rows:
    print(row)

cursor.close()
connection.close()
