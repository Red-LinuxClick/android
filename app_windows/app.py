from splinter import Browser
from easygui import *
from sys import exit
from time import sleep
from re import sub
from os import path, makedirs

executable_path = {'executable_path': 'C:/path/to/chromedriver.exe'}

chrome = Browser('chrome', **executable_path)
chrome_options.add_argument("--app=https://redlinuxclick.ml/")