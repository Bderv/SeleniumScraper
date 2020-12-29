from selenium import webdriver
import pandas as pd

driver = webdriver.Firefox()
driver.get("https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops")


assert "Web" in driver.title
prod_elements = driver.find_elements_by_class_name("title")
price_elements = driver.find_elements_by_class_name("price")
review_elements = driver.find_elements_by_css_selector('.ratings > p.pull-right')

infos = []
for product, price, review in zip(prod_elements, price_elements, review_elements):
    infos.append([product.get_attribute('title'), price.text, review.text])

df = pd.DataFrame(infos, columns = ["Product Name", "Price", "No of reviews"])
df.to_csv("infos.csv")

driver.close()