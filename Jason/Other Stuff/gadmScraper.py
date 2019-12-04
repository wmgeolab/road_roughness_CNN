from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import os
from bs4 import BeautifulSoup as bs
url = "https://gadm.org/download_country_v3.html"

chrome_options = Options()
# Headless browsing, no visual display
# chrome_options.add_argument("--headless")

driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"), chrome_options=chrome_options)

#Find dropdown
driver.get(url)

soup = bs(driver.page_source, "lxml")
options = soup.find_all("option")

#shp URL Format found manually
#Script frag from gadm
#document.getElementById("shp").innerHTML ="<a href=" + base + "shp/gadm36_" + a[0] + "_shp.zip>Shapefile</a>";
# a[0] = (value from dropdown).split("_")


for option in options:
    base = "https://biogeo.ucdavis.edu/data/gadm3.6/"
    print(option.text)
    try:
        #print(option.attrs['value'])
        value = option.attrs['value'].split("_")[0]
        if value != "":
            shpUrl = base + "shp/gadm36_" + value + "_shp.zip"
        print(shpUrl)
        driver.get(shpUrl)
        #print("Failed for " + option.text)
    except:
        print("Failed for " + option.text)
