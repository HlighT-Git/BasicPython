from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import io
import os
import time
from os import path

id = input()
id = id.upper()
url = "https://code.ptit.edu.vn/student/question/" + id

browser = Chrome(ChromeDriverManager().install())
browser.get(url)
wait = WebDriverWait(browser, 5)

# Login:
username = browser.find_element_by_id('login__user')
password = browser.find_element_by_id('login__pw')
username.send_keys('B19DCCN333')
password.send_keys('h001201023360')
password.send_keys(Keys.RETURN)

# Change Course:
time.sleep(1)
browser.get('https://code.ptit.edu.vn/student/question?course=141')
# Get Content:
browser.get(url)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "submit__nav")))
content = browser.find_element_by_class_name("submit__nav").text + '\n' + browser.find_element_by_class_name('submit__des').text
content = str(content)
browser.close()

# Generate:
base_dir = 'E:\hk12021\python\code\\' + id
if not os.path.exists(base_dir):
    os.mkdir(base_dir)
with io.open(base_dir + '\\' + id + '.txt', "w", encoding="utf-8") as f:
    f.write(content)
f.close()
if not path.exists(base_dir + '\\' + id + '.py'):
    f = open(base_dir + '\\' + id + '.py', "w")
    f.close()

# Start coding:
os.startfile(base_dir + '\\' + id + '.py')
time.sleep(1)
os.startfile(base_dir + '\\' + id + '.txt')