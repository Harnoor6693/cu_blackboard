"""# https://github.com/tasos-py/Search-Engines-Scraper.git
from search_engines import Google

query = "Round-robin scheduling allows interactive tasks quicker access to the processor is quite complex to implement gives each task the same chance at the processor allows processor-bound tasks more time in the processor"
engine = Google()
results = engine.search(query,pages=1)
links = results.links()

print(links)"""
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://uims.cuchd.in/uims/")
print(driver.get_cookies())