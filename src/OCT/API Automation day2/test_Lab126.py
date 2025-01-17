# PASSWORD - I store the password in Framework?-- No

# Env File .(dot.env)
# How do u store ur password or credentials in a Framework?
# pip install python-dotenv

from dotenv import load_dotenv
import os

def test_update_req():
    load_dotenv()
    username=os.getenv("USERNAME")
    password=os.getenv("PASSWORD")
    print(username)
    print(password)



