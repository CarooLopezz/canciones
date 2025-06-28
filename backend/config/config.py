#levantar la base de datos
from dotenv import load_dotenv
import os

load_dotenv("C:/Users/SONY/Documents/canciones/.env")

user = os.getenv("MYSQL_USER")
print(os.getenv("MYSQL_USER")) 
password = os.getenv("MYSQL_PASSWORD")
host = os.getenv("MYSQL_HOST")

port = os.getenv("MYSQL_PORT", "3306")
database = os.getenv("MYSQL_DATABASE")
print(os.getenv("MYSQL_DATABASE")) 


DATABASE_CONNECTION_URI = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
print(DATABASE_CONNECTION_URI)


