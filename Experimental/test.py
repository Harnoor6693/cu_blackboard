from selenium import webdriver
driver = webdriver.Chrome()
driver.get("file:///E:/cu_blackboard/Experimental/Tue_2_project(C)%20-%20Bb%20Collaborate.html")
# Checking if Moderator removed you form class
try:
    driver.find_element_by_xpath("//h1[text()='A moderator removed you']")
    print("Moderator removed you form class.")
except Exception as e:
    print(e)
    print("ERROR")
    
