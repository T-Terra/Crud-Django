from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from .utils.Tests.lib import Utils
from dotenv import load_dotenv
import os

load_dotenv(override=True)

class SeleniumTestes(LiveServerTestCase):
    def testAddUser(self):
        # Condig Tests
        open_browser = True if os.getenv('OPEN_BROWSER').strip().lower() == 'true' else False

        if open_browser:
            options = webdriver.ChromeOptions()
            options.add_argument('--start-maximized')
            options.add_argument('--incognito')
            browser = webdriver.Chrome(options=options)
        else:
            options = webdriver.ChromeOptions()
            options.add_argument('--start-maximized')
            options.add_argument('--headless=new')
            options.add_argument('--incognito')
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
    
    def testDeleteUser(self):
        # Condig Tests
        open_browser = True if os.getenv('OPEN_BROWSER').strip().lower() == 'true' else False

        if open_browser:
            options = webdriver.ChromeOptions()
            options.add_argument('--start-maximized')
            options.add_argument('--incognito')
            browser = webdriver.Chrome(options=options)
        else:
            options = webdriver.ChromeOptions()
            options.add_argument('--start-maximized')
            options.add_argument('--headless=new')
            options.add_argument('--incognito')
            browser = webdriver.Chrome(options=options)
        
        browser.get(os.getenv('URL_DEV'))
        actions = ActionChains(browser)

        sleep(3)


        buttonListUser = browser.find_element(By.XPATH, "//a[contains(text(), 'Lista de Usuários')]")

        actions.click(buttonListUser).perform()

        sleep(2)

        idUser = browser.find_element(By.XPATH, "(//tr[2]/th)[1]").text

        sleep(2)        

        buttonNavBar = browser.find_element(By.XPATH, "//a[contains(text(), 'Deletar Usuários')]")

        actions.click(buttonNavBar).perform()
        

        elemId = browser.find_element(By.NAME, 'id')

        Utils.SlowTypes(self, actions, idUser, elemId, 0.001)
        
        sleep(3)

        buttonSubmit = browser.find_element(By.XPATH, "//button[contains(text(), 'Apagar')]")

        actions.click(buttonSubmit).perform()

        browser.find_element(By.XPATH, "//div[contains(text(), 'Usuário deletado com sucesso!')]")

        sleep(3)

        browser.close()