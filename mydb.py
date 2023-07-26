# Install Mysql on your computer
# https://dev.mysql/downloads/installer/
# pip.install.mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

# dataBase = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = 'Password123',
#     auth_plugin='mysql_native_password'

# )

dataBase = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='Password123'
    )

# Prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE centag")

print("All Done !")


# ALTER USER 'root'@'localhost' IDENTIFIED BY 'Password123' PASSWORD EXPIRE NEVER;
# ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Password123';