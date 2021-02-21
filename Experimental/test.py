"""# https://github.com/tasos-py/Search-Engines-Scraper.git
from search_engines import Google

query = "Round-robin scheduling allows interactive tasks quicker access to the processor is quite complex to implement gives each task the same chance at the processor allows processor-bound tasks more time in the processor"
engine = Google()
results = engine.search(query,pages=1)
links = results.links()

print(links)"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()

driver.execute_script('''window.open("http://bings.com","_blank");''')
for i in driver.window_handles:
    print(i)
print()

time.sleep(2)
driver.execute_script('''window.open("http://yahoo.com","_blank");''')
for i in driver.window_handles:
    print(i)
print()

time.sleep(2)
driver.execute_script('''window.open("http://google.com","_blank");''')
for i in driver.window_handles:
    print(i)
print()

time.sleep(2)

"""driver.switch_to.window(driver.window_handles[-1]) 
driver.close()
for i in driver.window_handles:
    print(i)"""


while(True):
    print(driver.window_handles[-1])
    tab = int(input("Enter tab number"))
    if tab ==-1:
        break
    driver.switch_to.window(driver.window_handles[tab])
driver.quit()