from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)

# Replace with the actual path to your chromedriver
webdriver_service = Service('C:/projects/python/pythonProject/chromedriver-win64/chromedriver-win64/chromedriver.exe')

# Initialize WebDriver
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Open the URL
url = "https://www.google.com/maps/search/clinics+in+adyar/"
driver.get(url)

# Wait for the page to fully load
time.sleep(5)  # Adjust this as needed

# Find all the aTags (or relevant elements you want to click)
aTags = driver.find_elements(By.CLASS_NAME, "hfpxzc")

hospitalNames=[]

for aTag in aTags:
    hospitalNames.append(aTag.accessible_name)

# Initialize an empty list to hold the details
details = []
currentUrl = driver.current_url;
# Loop through each aTag
for i in range(len(aTags)):
    # Re-fetch the aTags to avoid stale element exception
    aTags = driver.find_elements(By.CLASS_NAME, "hfpxzc")

    # Click the current aTag
    aTags[i].click()

    # Wait for the page to load after the click
    time.sleep(2)

    # Extract the required information (adjust the class names as necessary)
    infos = driver.find_elements(By.CLASS_NAME, "CsEnBe")

    if len(infos) >= 2:  # Ensure there are at least two elements
        details.append({
            "address": infos[0].text.replace("\ue0c8\n",""),
            "phone": infos[1].text.replace("\ue0b0\n",""),
            "name":hospitalNames[i]

        })

    # Go back to the search results page
    #driver.back()
    driver.execute_script("window.history.go(-1)")

    # Wait for the search results page to load
    time.sleep(2)

# Print the collected details
for detail in details:
    print(detail)

# Close the browser
driver.quit()
