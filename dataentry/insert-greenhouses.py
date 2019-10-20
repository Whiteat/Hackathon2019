from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector, csv, os

def load_csv(cursor, command):

    file_path = os.getcwd()
    file_path = os.path.join(file_path, 'data', 'greenhouses.csv')
    print(os.getcwd())
    data = [];

    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        for row in csv_reader:
            line_data = []

            print(row)
            join_date = date(int(row[4]), int(row[5]), int(row[6]))
            data = (row[0], row[1], row[2], row[3], join_date);
            print(data)

            count_cmd = "SELECT * FROM app_greenhouse WHERE name = \"" + row[0] + "\""
            print(count_cmd)
            cursor.execute(count_cmd)
            cursor.fetchall();
            existing_count = cursor.rowcount
            print("Existing Count: " + str(existing_count))

            if existing_count == 0:
                print("Inserting: " + data)
                cursor.execute(command, data)

            line_count += 1
            #print(f'Processed {line_count} lines.');

cnx = mysql.connector.connect(user='alex', password='H@ckath0n', host="192.168.0.20", database='dbname')
cursor = cnx.cursor()
cnx.cursor(buffered=True)

#cursor.execute("TRUNCATE TABLE app_greenhouse");

add_greenhouse = ("INSERT INTO  app_greenhouse"
               "(name, type, address, phone, joinDate) "
               "VALUES (%s, %s, %s, %s, %s)")

load_csv(cursor, add_greenhouse);
# Make sure data is committed to the database
cnx.commit()

cursor.close()
cnx.close()
