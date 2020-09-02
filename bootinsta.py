from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)
        try:
            login_button = driver.find_element_by_xpath(
                "//a[@href='/accounts/login/?source=auth_switcher']"
            )
            login_button.click()
        except:
            print('já estamos na página de login')
            pass
        user_element = driver.find_element_by_xpath(
            "//input[@name='username']")
        user_element.clear()
        time.sleep(random.randint(4, 6))
        user_element.send_keys(self.username)
        time.sleep(random.randint(4, 6))
        password_element = driver.find_element_by_xpath(
            "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(random.randint(4, 6))
        password_element.send_keys(Keys.RETURN)
        time.sleep(random.randint(4, 6))
        self.curtir_fotos_com_a_hastag(
            "vitoria1306201"
        )  # Altere aqui para a hashtag que você deseja usar.

    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        """ Este código irá basicamente permitir que você simule a digitação como uma pessoa """
        print("going to start typing message into message share text area")
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1, 5) / 30)

    def curtir_fotos_com_a_hastag(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/" + hashtag + "/")
        time.sleep(5)
        for i in range(
            1, 3
        ):  # Altere o segundo valor aqui para que ele desça a quantidade de páginas que você quiser: quer que ele desça 5 páginas então você deve alterar de range(1,3) para range(1,5)
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)

        hrefs = driver.find_elements_by_tag_name("a")
        pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
        print(hashtag + " fotos: " + str(len(pic_hrefs)))

        #testes = [
        #    href
        #    for href in pic_hrefs
        #    if hashtag in href and href.index("https://www.instagram.com/p/") != 0
        #]
        for i in pic_hrefs:
            driver.find_element_by_class_name('eLAPa').click()
           ## nao ta cachando o elemento de curtir driver.find_element_by_xpath('//svg[@class="_8-yf5 "]')


vitorBot = InstagramBot(
    "vitor_santos.g", "shutdown-hnow")
vitorBot.login()