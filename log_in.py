from selenium import webdriver
from time import sleep

user = "instandbot"
pwd = "aiLKq0218,.q&"

def follow_hashtag(browser, hashtag):
    browser.get("https://www.instagram.com/explore/tags/"+hashtag+"/")
    posts = browser.find_elements_by_xpath("//ul[@class='Ln-UN' and position()<=12]")


#user= "alphabot44"
#pwd="Y$JJErhrG4u{H2,"

browser = webdriver.Firefox()

browser.get("https://www.instagramm.com/")


coockie_box = browser.find_element_by_xpath('//button[text()="Accept All"]')
coockie_box.click()

sleep(5)

user_box = browser.find_element_by_xpath("//input[@name='username' and @type='text']")
user_box.send_keys(user)

pwd_box = browser.find_element_by_xpath("//input[@name='password' and @type='password']")
pwd_box.send_keys(pwd)

login_button = browser.find_element_by_xpath("//button[@type= 'submit']")
login_button.click()

sleep(5)
save_login_button = browser.find_element_by_xpath('//button[text()="Not Now" and @type="button"]')
save_login_button.click()

no_notifikation = browser.find_element_by_xpath('//button[text()="Not Now"]')
no_notifikation.click()

browser.get("https://www.instagram.com/explore/tags/spirograph/")

links_tags = browser.find_elements_by_tag_name('a')

