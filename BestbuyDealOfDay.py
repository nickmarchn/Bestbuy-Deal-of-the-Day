from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import re


# Replace 'path_to_chromedriver' with the actual path to your ChromeDriver executable.
driver = webdriver.Chrome()



# Navigate to Bestbuy's website
driver.get('https://www.bestbuy.com/')
driver.maximize_window()
time.sleep(5)


# Select "Deal of the Day" on web page
driver.find_element(By.LINK_TEXT, 'Deal of the Day').click()
time.sleep(5)






#Find the live ticker element
countdown_element = driver.find_element(By.CLASS_NAME,"countdown-timer-wrapper")

#Extract the text and remove unwanted characters 
countdown_text = countdown_element.text
pattern = r"Sale expires in \d+ hours and \d+ minutes"
match = re.search(pattern, countdown_text)
if match:
    sale_expires_text = match.group()
    print(sale_expires_text)   



#Go to discounted item
discounted_item = driver.find_element(By.ID,"wf-offer-1488e024-83a8-483e-a9c5-73509fa892a7-product-title")
discounted_item.click()
time.sleep(5)


#Find the Name of the item
item_description = driver.find_element(By.CLASS_NAME,"sku-title")

item_description_text = item_description.text
print("Product Name: " + item_description_text)   

# Select "Deal of the Day" on web page
driver.find_element(By.LINK_TEXT, 'Deal of the Day').click()
time.sleep(5)


# Find the current price
item_current_price = driver.find_element(By.CLASS_NAME,"pricing-price__savings-regular-price")

# Get the savings and original price
savings = float(item_current_price.text.splitlines()[0].replace("Save $", ""))
original_price = float(item_current_price.text.splitlines()[1].replace("Was $", ""))

# Get the discounted price
discounted_price = round(original_price - savings, 2)

print(f"Discounted Price: ${discounted_price}\n"
      f"Original Price: ${original_price}\n"
      f"Total Savings: ${savings}")







    

