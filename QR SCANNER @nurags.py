#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import random
import smtplib
def auto_email():
 user = input("Enter Your Name : ")
 email = input("Enter Your Email : ")
 my_message = (f"Dear {user}, your message")
 s = smtplib.SMTP('smtp.gmail.com', 587)
 s.starttls()
 s.login("your email id", "your password")
 s.sendmail('&&&&&&&&&&&', email, my_message)
 print("Email Sent to user...")

