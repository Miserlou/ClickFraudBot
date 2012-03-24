#!/usr/bin/env python
from splinter.browser import Browser
from TorCtl import TorCtl
import time

#Settings
TORCTL_PASS="derp"
SEARCH_TERMS = ['derpasquirt', 'bronana']
CHAFF = ['cute cats', 'funny cat pictures', 'kitty cat', 'cute kitty', 'meow']

# Are we going through Tor?
def check_tor():
    conn = TorCtl.connect(passphrase=TORCTL_PASS)
    if conn:
        return True
    else:
        return False

# Tell Tor we want a new Exit Node
# Make sure Tor has a control channel open!
def get_new_address():
    conn = TorCtl.connect(passphrase=TORCTL_PASS)
    conn.sendAndRecv('signal newnym\r\n')
    conn.close()
    time.sleep(10)

def search_click():
    browser = Browser('firefox', profile='fraudbot')

    # Visit URL
    url = "http://www.google.com" 
    browser.visit(url) 
    browser.fill('q', "karmachamillionaire") 
    time.sleep(1)

    # Find and click the 'search' button 
    button = browser.find_by_name("btnG") 

    # Interact with elements 
    button.click() 
    time.sleep(2)

    if browser.is_text_present("did not match any documents"):
        print "nobody likes us =("
    else:
        print "we're popular =)"

    browser.quit()

def main():

    if not check_tor():
        quit()

    while True:
        get_new_address()
        browser = search_click()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        quit()
