from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
import random

import pyautogui
from pynput.keyboard import Controller

class instand():
    def __init__(self):
        self.keyboard = Controller()

        #self.user = "instandbot"
        #self.pwd = "aiLKq0218,.q&"

        self.user = "alphabot44"
        self.pwd = "Y$JJErhrG4u{H2,"

    def automate(self):
        #nötige Initialisierungen
        browser = webdriver.Firefox()

        browser.get("https://www.instagramm.com/")

        def check_viability_by_xpath(xpath, timeout=1):
            try:
                element = WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, xpath)))
                return True
            except TimeoutException:
                return False

        """
            Einloggen
            
            Selenium sucht nach den nötigen button um sich einzuloggen:
            -Zunächst werden Coockies abgelehnt
            -Sobald Password und Nutzername sichtbar sind werden dort die Daten eingetragen
            -Danach werden all Interaktionsfelder geschlossen
            
            
            Follow
            
            -Es werden nach definierten # gesucht
                -dort werden alle Posts erfasst 
                -Es werden zufällige Post herausgesucht 
                -diese Posts werden geliked und den Accounts gefolgt
            
            Posten
            
            -Zurück auf die Hauptseite
            -auf posten
            -der Post wird direkt über Pfad zum Post gesucht
            -Folgende Pop Ups werden geschlossen 
            -Informationen werden aus den entsprechenden .txt Dateien Eingelesen und in den Post eingefügt
            -auf Posten klicken  
        """

        coockie_box = browser.find_element_by_xpath('//button[text()="Accept All"]')
        coockie_box.click()

        user_box = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='username' and @type='text']")))
        user_box.send_keys(self.user)

        pwd_box = browser.find_element_by_xpath("//input[@name='password' and @type='password']")
        pwd_box.send_keys(self.pwd)

        sleep(3)
        login_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type= 'submit']")))
        login_button.click()

        save_login_button = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//button[text()="Not Now" and @type="button"]')))
        save_login_button.click()

        no_notifikation = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//button[text()="Not Now"]')))
        no_notifikation.click()

        explore_tags = ["https://www.instagram.com/explore/tags/spirograph/",
                        "https://www.instagram.com/explore/tags/asmr/",
                        "https://www.instagram.com/explore/tags/animation/",
                        "https://www.instagram.com/explore/tags/coding/"]
        for tag in explore_tags:
            browser.get(tag)

            link_tags = browser.find_elements_by_tag_name('a')
            links = []
            for element in link_tags:
                href = element.get_attribute('href')

                if href.__contains__('/p/'):
                    links.append(href)

            random_amount = random.randint(0, 5)
            amount_of_links = len(links)
            list_of_post_to_follow = []
            random_post_index = 0

            for i in range(0, random_amount):
                random_post_index = random.randint(0, amount_of_links - 1)
                list_of_post_to_follow.append(links[random_post_index])
                del links[random_post_index]
                amount_of_links -= 1

            for element in list_of_post_to_follow:
                browser.get(element)
                like_button = browser.find_element_by_xpath(
                    "//span[contains(@class,'fr66n')]//button[contains(@type,'button')]")
                like_button.click()

                if random.randint(0, 1000) % 2 == 0:
                    if check_viability_by_xpath(
                            "//div[@class='bY2yH']//button[@type='button'][normalize-space()='Follow']"):
                        follow_button = browser.find_element_by_xpath(
                            "//div[@class='bY2yH']//button[@type='button'][normalize-space()='Follow']")
                        follow_button.click()

        browser.get("https://www.instagram.com/")

        create_post = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='vZuFV']//button[@type='button']")))
        create_post.click()

        select_from_pc = browser.find_element_by_xpath("//button[normalize-space()='Select from computer']")
        select_from_pc.click()

        sleep(10)

        t = r"C:\Users\Korbinian\Desktop\Git_official\Insta_star\user\contend\post\post.mp4"
        self.keyboard.type(t)
        sleep(10)
        pyautogui.press('enter')
        pyautogui.press('enter')

        next_button =WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Next']")))
        next_button.click()
        next_button =WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Next']")))
        next_button.click()

        a = browser.find_element_by_xpath("//textarea[@placeholder='Write a caption...']")
        a.click()

        path_to_caption = r"C:\Users\Korbinian\Desktop\Git_official\Insta_star\user\contend\post_subtitle\subtitle.txt"
        path_to_hashtag = r"C:\Users\Korbinian\Desktop\Git_official\Insta_star\user\contend\hashtags\hashtags.txt"

        post_string = ""

        with open(path_to_caption) as f:
            lines = f.readlines()
            for line in lines:
                post_string += line

        hashtag_list = []

        with open(path_to_hashtag) as f:
            lines = f.readlines()
            for line in lines:
                hashtag_list.append(line)

        a.send_keys(post_string)
        a.send_keys("\n")

        for element in hashtag_list:
            a.send_keys(element)

        share = browser.find_element_by_xpath("//button[normalize-space()='Share']")
        share.click()

        sleep(5)
        if check_viability_by_xpath("//h2[normalize-space()='Your post has been shared.']", 50):
            browser.close()
