from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException


import os

def create_and_save_file(folder_name, file_name, content):
    try:
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        file_path = os.path.join(folder_name, file_name)
        with open(file_path, 'w') as file:
            file.write(content)
            file.flush()
            file.close()
    except Exception as e:
        print(f"An error occurred: {e}")


driver = webdriver.Chrome()
#es,scr1,gasa
urls = ["cape","cep1","cif1","CLAVATA3","eal1","eca1","es","gasa","glv","ida","ltp","lure","pep","pip","psk","ralf","scr1","stig","gri","tpd"]
# urls = ["ltp","lure","pep","pip","psk","ralf","scr","stig","gri","tpd"]

# # Configure Chrome options for headless mode
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run in headless mode

# # Create a WebDriver instance with Chrome options
# driver = webdriver.Chrome(options=chrome_options)


for link in urls:
    # Open the webpage
    url = "https://www.arabidopsis.org/servlets/Search?type=general&search_action=detail&method=1&show_obsolete=F&name="+link+"&sub_type=gene&SEARCH_EXACT=4&SEARCH_CONTAINS=1"
    driver.get(url)


    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='button'][value='download all']"))
    )
    # Click the button
    button.click()


driver.quit()