"""
Created on Tue Jun  8 10:07:27 2021

@author: AD
Creating my first MySQL database
"""

import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="", database="")
cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS bank")
cursor.execute("USE bank")
cursor.execute(
    "CREATE TABLE IF NOT EXISTS reg_bank(id int(10)PRIMARY KEY AUTO_INCREMENT NOT NULL , Acc_num BIGINT NOT NULL, "
    "name VARCHAR(100), "
    "email VARCHAR(100), dob VARCHAR(20),phone BIGINT(11), address VARCHAR(100), gender VARCHAR(6), marry_stat VARCHAR(7), acc_type VARCHAR(7))")
conn.commit()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS payment(id INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, account_number VARCHAR(100) NOT NULL, amount decimal(10,2), trans_details VARCHAR(100) )")
conn.commit()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS reg_app(id int(10) NOT NULL PRIMARY KEY, account_number "
    "BIGINT(10), "
    "username VARCHAR(100), pin INT(100))")
conn.commit()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS amount(id int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT, account_number BIGINT(10), "
    "balance INT(100))")
conn.commit()
conn.close()