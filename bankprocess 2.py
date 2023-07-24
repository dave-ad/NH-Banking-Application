__author__ = "AD"

import shelve

"""Server script to handle user authentication requests."""

import mysql.connector
import socket
import json
import threading
from tkinter import messagebox
from datetime import datetime


class processServer(threading.Thread):
    def __init__(self, client, addr):
        threading.Thread.__init__(self)
        self.client = client
        self.addr = addr
        self.conn = mysql.connector.connect(host="localhost", database="bankdb2", user="root", password="")
        self.cursor = self.conn.cursor()

    def run(self):
        myclient = threading.local()
        myclient.client = self.client
        myclient.addr = self.addr
        print("Accepted connection from ", myclient.addr)
        # myclient.client.send(str.encode("Welcome to my server!"))

        while True:
            data = client.recv(1024)
            message = json.loads(bytes.decode(data))
            print(message)
            if "register" in message:
                message.remove("register")
                self.cursor.execute(
                    "INSERT INTO reg_app (id, account_number, username, pin) VALUES('{}', "
                    "'{}', '{}', '{}')".format(
                        *message))
                self.cursor.execute("SELECT * FROM reg_app ORDER BY id DESC LIMIT 1")
                resp = self.cursor.fetchall()
                print("resp is")
                print(resp)
                print("Sending registration response...")
                self.client.send(str.encode(json.dumps(resp)))
                self.conn.commit()
            elif "account" in message:
                message.remove("account")
                print("Sending response...")
                self.cursor.execute(
                    "INSERT INTO reg_bank (Acc_num, name, email, dob, phone, address) VALUES('{}', '{}', '{}','{}','{}', '{}')".format(
                        *message))
                self.cursor.execute("SELECT Acc_num,name,email,dob,phone,address FROM reg_bank ORDER BY id DESC LIMIT 1")
                resp = self.cursor.fetchall()
                print(resp)
                print("Sending account reg details...")
                self.client.send(str.encode(json.dumps(resp)))
                self.conn.commit()
            elif "login" in message:
                message.remove("login")
                print("hey")
                self.cursor.execute(
                    "SELECT * FROM reg_app WHERE username = '{}' AND pin = '{}'".format(*message))
                resp = self.cursor.fetchall()
                print("Sending login response...")
                self.client.send(str.encode(json.dumps(resp)))
                self.conn.commit()

            elif "transaction" in message:
                del message['transaction']
                trans = shelve.open("trans_info", flag="n")
                username = message['username']

                self.cursor.execute("SELECT user_id FROM reg_app WHERE username = '{}'".format(username))
                user_id = self.cursor.fetchone()
                message['user_id'] = user_id[0]

                for item in message:
                    trans[item] = message[item]
                trans.close()
                print("Sending transaction response...")
                self.client.send(str.encode(json.dumps(message)))
                self.conn.commit()
            elif "deposit" in message:
                print("qqqq")
                message.remove("deposit")
                account_number = message['account_number']
                amount = message['amount']
                print("hello")
                self.cursor.execute( "SELECT balance FROM amount WHERE account_number = '{}'".format(account_number))
                resp = self.cursor.fetchone()
                print("hiiiii")
                resp[0] += amount
                self.cursor.execute("UPDATE amount SET balance WHERE account_number = '{}'".format(account_number))
                print("Sending deposit response...")
                self.client.send(str.encode(json.dumps(resp)))
                self.conn.commit()
            # elif "transfer" in message:
            #     message.remove("transfer")
            #     account_number = message['account_number']
            #     username = message['username']
            #     amount = message['amount']
            #     self.cursor.execute(
            #         "INSERT INTO payment (account_number, amount, trans_details) VALUES ('{}','{}','{}')".format(*message))
            #     self.cursor.execute("SELECT account_number FROM reg_app WHERE username = '{}'".format(username))
            #     result = self.cursor.fetchone()
            #     print("ooihfffhkjm")
            #     self.cursor.execute("SELECT balance FROM amount WHERE account_number = '{}'".format(result[0]))
            #     results = self.cursor.fetchone()
            #     print("ooihfffh")
            #     results[0] -= amount
            #     print("ooitrthh")
            #     self.cursor.execute(
            #         "INSERT INTO amount (balance) values ('{}')".format(results[0]))
            #     self.conn.commit()
            #     self.cursor.execute("SELECT * FROM reg_bank WHERE account_number = '{}'".format(account_number))
            #     result1 = self.cursor.fetchall()
            #     print("ooihh")
            #
            #     if account_number in result1:
            #         messagebox.showinfo("Success", "Transfer Successful.")
            #     else:
            #         messagebox.showerror("Error", "Account does not exist!")

            # elif "post" in message:
            #     newdicts = {}
            #     trans = shelve.open("trans_info")
            #     for item in trans:
            #         newdicts[item] = trans[item]
            #     trans.close()
            #     user_id = newdicts['user_id']
            #     username = newdicts['username']
            #     transaction_date = datetime.now()
            #     trans_date = transaction_date.strftime("%Y-%m-%d %H:%M:%S")
            #     del newdicts['user_id']
            #     del newdicts['username']
            #
            #     print(newdicts)
            #
            #     for row in newdicts:
            #         self.cursor.execute(
            #             "INSERT INTO reg_bank (id, employee, item, amount, date_purchased) VALUES ('{}', '{}', '{}', '{}', '{}')".format(
            #                 user_id, username, row, newdicts[row], trans_date))
            #     self.cursor.execute("SELECT * FROM transaction WHERE date_purchased = '{}'".format(trans_date))
            #     result = self.cursor.fetchall()
            #     print(result)
            #     if not result:
            #         msg = "failed"
            #     else:
            #         msg = "success"
            #     self.conn.commit()
            #     self.client.send(str.encode(msg))


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ""
port = 8000
server.bind((host, port))
server.listen(5)

while True:
    print("Listening for a client...")
    client, addr = server.accept()
    client1 = processServer(client, addr)
    client1.start()
