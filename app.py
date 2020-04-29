#Import Libraries
from flask import Flask
import pandas as pd

app = Flask(__name__)

#Import database
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Thecheezer1!",
    database="drinks_database"
)


