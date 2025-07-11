from selenium import webdriver
from userinfo import username, password
from selenium.webdriver.common.keys import Keys
import time
class Instagram:
    driver_path = "C:\\Users\\lenovo\\Desktop\\python_fundamental\\11Week_Instagram\\chromedriver"
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.browser = self.browser = webdriver.Chrome(Instagram.driver_path)
    
    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        usernameInput = self.browser.find_element_by_name("username")
        passwordInput = self.browser.find_element_by_name("password")

        usernameInput.send_keys(username)
        passwordInput.send_keys(password)

        passwordInput.send_keys(Keys.ENTER)

    def getFollowers(self):
        pass

    def followUser(self,username):
        pass

    def unfollowUser(self,username):
        pass

    def __del__(self):
        time.sleep(5)
        self.browser.close


app = Instagram(username,password)
app.signIn()
app.getFollowers()
app.followUser("abc")
app.unfollowUser("abc")













