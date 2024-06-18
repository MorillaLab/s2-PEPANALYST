from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException


import os

def create_and_save_file(folder_name, file_name, content):
    try:
        # Create the folder if it doesn't exist
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # Open the file in write mode inside the specified folder
        file_path = os.path.join(folder_name, file_name)
        with open(file_path, 'w') as file:
            # Write the content to the file
            file.write(content)
            file.flush()
            # Close the file to release system resources
            file.close()
        # print(f"File '{file_name}' created and saved successfully in folder '{folder_name}'!")
    except Exception as e:
        print(f"An error occurred: {e}")


# Create a WebDriver instance (assuming you have the appropriate driver installed, like ChromeDriver)
driver = webdriver.Chrome()
#es,scr,gasa
# urls = ["cape","cep","cif","CLAVATA3","eal","eca1","es","gasa","glv","ida","ltp","lure","pep","pip","psk","ralf","scr","stig","gri","tpd"]
urls = ["ltp","lure","pep","pip","psk","ralf","scr","stig","gri","tpd"]

# Configure Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode

# Create a WebDriver instance with Chrome options
driver = webdriver.Chrome(options=chrome_options)


for link in urls:
    # Open the webpage
    url = "https://www.arabidopsis.org/servlets/Search?type=general&search_action=detail&method=1&show_obsolete=F&name="+link+"&sub_type=gene&SEARCH_EXACT=4&SEARCH_CONTAINS=1"
    driver.get(url)

    # # Find the "get all sequences" button by its attributes
    # button = driver.find_element(By.CSS_SELECTOR, "input[type='button'][value='get all sequences']")
    # Find the "get all sequences" button by its attributes
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='button'][value='get all sequences']"))
    )
    # Click the button
    button.click()

    # Print the updated URL after clicking the button
    print(driver.current_url)

    # Find the button on the new page by its attributes
    # new_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Get Sequences']")
    # Find the new button on the redirected page (assuming it's available immediately)
    new_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='submit'][value='Get Sequences']"))
    )

    # Click the button on the new page
    new_button.click()
    try:
        # Find the <pre> tag containing the desired content
        pre_element = driver.find_element(By.CSS_SELECTOR, "pre[style='word-wrap: break-word; white-space: pre-wrap;']")
        # new_button = WebDriverWait(driver, 100).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, "pre[style='word-wrap: break-word; white-space: pre-wrap;']"))
        # )

        # Extract the text content of the <pre> tag
        content = pre_element.text

        # # Print the content
        # print("Content inside <pre> tag:")
        # print(content)
        create_and_save_file("Families",link+".fasta", content)
    except NoSuchElementException:
        print("Html code 'pre' is not present")

# Close the WebDriver instance
driver.quit()