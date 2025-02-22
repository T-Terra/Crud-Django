from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from .utils.Tests.lib import Utils
from dotenv import load_dotenv
import os

load_dotenv()

class SeleniumTestes(LiveServerTestCase):
    def testAddUser(self):
        # Condig Tests
        open_browser = True if os.getenv('OPEN_BROWSER') == 'true' else False

        if open_browser:
            browser = webdriver.Chrome()
        else:
            options = webdriver.ChromeOptions()
            options.add_argument('--headless=new')
            browser = webdriver.Chrome(options=options)

        browser.get(os.getenv('URL_DEV'))
        actions = ActionChains(browser)
        
        name = Utils.GetPerson('nome')

        age = Utils.GetPerson('idade')

        sleep(2)

        elemName = browser.find_element(By.NAME, 'nome')
        elemAge = browser.find_element(By.NAME, 'idade')

        Utils.SlowTypes(self, actions, name, elemName, 0.001)
        
        sleep(3)

        Utils.SlowTypes(self, actions, str(age), elemAge)

        button = browser.find_element(By.XPATH, "//button[contains(text(), 'Enviar')]")

        actions.click(button).perform()
        sleep(4)

        browser.close()

        sleep(1)
        