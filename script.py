#  Importing essential libraries
from selenium import webdriver
import pandas as pd

#  telling the scraper where to start and what webdriver to use
driver = webdriver.Firefox()
driver.get("https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops")

# grabbing the specific elements by class name and css selector
assert "Web" in driver.title
prod_elements = driver.find_elements_by_class_name("title")
price_elements = driver.find_elements_by_class_name("price")
review_elements = driver.find_elements_by_css_selector('.ratings > p.pull-right')

# creating an array with the extracted elements
infos = []
for product, price, review in zip(prod_elements, price_elements, review_elements):
    infos.append([product.get_attribute('title'), price.text, review.text])

# turn that array into a csv with columns for each
df = pd.DataFrame(infos, columns = ["Product Name", "Price", "No of reviews"])
df.to_csv("infos.csv")

driver.close()