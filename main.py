# Selenium Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
# Utils
from utils import Browser, Trello
# Others
from dotenv import load_dotenv
import os, time


# --- Code ---
load_dotenv()
browser = Browser.get_browser_name()

def browser_to_use(browser):
    if browser == "AppXycpy9mb5aa9x31qd69xmfqbdxkq7ra6z":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")

        driver = webdriver.Firefox(options=options)
        return driver
    elif browser == "ChromeHTM":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")

        driver = webdriver.Chrome(options=options)
        return driver
    
    options = webdriver.EdgeOptions()
    options.add_argument("headless")
    options.add_argument("disable-gpu")

    driver = webdriver.Edge(options=options)
    return driver
    
driver = browser_to_use(browser)

class App:
    def log_in(username, password):
        username_field = driver.find_element(By.XPATH, "//input[@id='Username']")
        username_field.send_keys(username)

        password_field = driver.find_element(By.XPATH, "//input[@id='Password']")
        password_field.send_keys(password)

        log_in_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
        log_in_btn.click()

        time.sleep(2)

    def slide():
        btn = driver.find_element(By.XPATH, "//button[@aria-label='prev']")
        btn.click()

        time.sleep(2)

    def get_events():
        events = driver.find_elements(By.CLASS_NAME, "fc-day-grid-event.fc-h-event.fc-event.fc-start.fc-end")
        titles = [title.text for title in events]
        data_ids = [data_id.get_attribute("data-id") for data_id in events if data_id.get_attribute("data-id") != None]
        number_of_events = len(titles)

        existent_cards = Trello.get_cards()

        for index in range(number_of_events):
            driver.get(f"https://alhassania.emadariss.net/Events/EventShow/{data_ids[index]}")

            name = titles[index]
            description = driver.find_element(By.XPATH, "//body/div[contains(@class,'modal-body')]/div[1]").text

            if "/Docs/Enseignant/" in description:
                split_desc = description.split("/Docs/Enseignant/")
                print(split_desc)
                split_desc.insert(1, "https://alhassania.emadariss.net/Docs/Enseignant/")
                print(split_desc)

                description = ''.join(split_desc)

            green = "656dba17c35d9b9c6d23b079"
            red = "656dba17c35d9b9c6d23b088"
            blue = "656dba17c35d9b9c6d23b07b"
            if "[Devoir]" in name:
                label_id = green
            elif "[Support de cours ]" in name:
                label_id = blue
            elif "[Contrôle]" in name:
                label_id = red
            
            if name not in existent_cards:
                Trello.send_card(name, description, label_id=label_id)
            else:
                pass

        time.sleep(2)

    def main():
        username = os.getenv("NAME")
        password = os.getenv("PASSWORD")

        driver.get(r"https://alhassania.emadariss.net/Login?ReturnUrl=%2fEvents")
        App.log_in(username, password)
        App.slide()
        App.get_events()

if __name__ == "__main__":
    App.main()
