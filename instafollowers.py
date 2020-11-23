#This program increase followers :)

#importing modules
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pyautogui
from time import sleep
import random

#Instagram Credentials
username = "iam_stubborn_"
password = "smileytina"

#Iniltializing Webdriver
try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
except:
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

#function to follow followers of insta pages
def follow():
    a = 1
    try :
        while a == 1:
            driver.find_element_by_class_name('fr66n').click()
            driver.find_element_by_css_selector("a._65Bje.coreSpriteRightPaginationArrow").click()
            pyautogui.sleep(2)
    except Exception as e :
        print(e)
       # driver.quit()


# Function to login Instagram

def INSTA_LOGIN():
    # swapping values from variables
    user = username
    passwd =password

    # maximizing window

    driver.maximize_window()

    # opening instagram using selenium
    driver.get("https://www.instagram.com/")
    sleep(0.5)

    # Targetting elements and entering credentials

    username_box = driver.find_element_by_name("username")
    username_box.send_keys(user)
    sleep(1)

    password_box = driver.find_element_by_name("password")
    password_box.send_keys(passwd)

    # clicking on login button

    login_box = driver.find_element_by_css_selector("button.sqdOP.L3NKy.y3zKF")
    login_box.click()
    sleep(5)

    # clicking on save now and not now buttons

    save_button = driver.find_element_by_css_selector(
        "button.sqdOP.L3NKy.y3zKF")
    save_button.click()
    sleep(5)

    not_button = driver.find_element_by_css_selector("button.aOOlW.HoLwm")
    not_button.click()
    sleep(3)

    # Search Button 
    
    usr = driver.find_element_by_xpath("//input[@type='text']")
    
    # random hastags

    #x =['#programming','#programmer','#python' '#tech' '#coder' "#noobcoder","#html""#computerscience","#codinglife","#technology","#software","#softwaredeveloper","#webdevelopment","#programmerlife","#programminglife","#softwareengineer","#linux","#webdesign","#programmingmemes","#development","#hacking"]
    x = ['programmer.me']
    hash_tag = random.choice(x)
    usr.send_keys(hash_tag)
    sleep(1)
    #clicking on the hashtag

    search_out = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]')
    search_out.click()
    sleep(3)

    #clicking on followers tab
    follow_btn = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
    follow_btn.click()
    sleep(3)
    #opening followers profile 
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li[1]/div/div[2]').click()




































INSTA_LOGIN()    


    









