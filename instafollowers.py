#This program increase followers :)

#importing modules
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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


# Like Posts and Get back to Followers Page
def like():
    try:
        photo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME , "_9AhH0"))
        )
        photo.click()
    except:
        driver.back()
    
    for i in range(10):
        print("Liking Posts...")
        try:
            like_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH , "/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span"))
            )
            like_button.click()

            next_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME , "coreSpriteRightPaginationArrow"))
            )
            next_button.click()
        except Exception as e:
            print(e)
            driver.back()

    try:
        close_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH , '/html/body/div[4]/div[3]/button/div/svg'))
        )
        close_btn.click()
    except Exception as e:
        print(e)


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


    #Follow all the users except who is already been followed    
    ul = driver.find_elements_by_class_name("PZuss")[0]
    users = ul.find_elements_by_tag_name("li")
    for user in users:
        user.find_elements_by_class_name("_6q-tv")[0].click()
        try:
            print("\nSearching Follow Button")
            follow_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME , '_5f5mN'))
            )
        except selenium.common.exceptions.StaleElementReferenceException:
            driver.back()
        
        else:
            print("\nFollow Button Found")
            if follow_button.text == "Follow":
                follow_button.click()
                like()
                driver.back()
                sleep(3)
            

if __name__ == "__main__":
    INSTA_LOGIN()
