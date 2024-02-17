import random
import time
from random import randint

import openpyxl
import pickle
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
# from selenium import webdriver
#
# driver = webdriver.Chrome()

import undetected_chromedriver as uc
from time import sleep
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("user-data-dir=C:\\Users\\alienware\\AppData\\Local\\Google\\Chrome\\User Data")
chrome_options.add_argument("profile-directory=Profile 2")
driver = uc.Chrome(version_main = 120,options=chrome_options)
driver.maximize_window()
driver.get("https://google.com")