import os
from subprocess import call
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import io
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidSessionIdException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

missingDescriptionProjects = []
os.chdir('E:\hk12021\oop\code')
for dir in os.listdir():
    if dir[0] == 'J' and not os.path.exists(".\\" + dir + "\\" + dir + ".txt"):
        missingDescriptionProjects.append(dir)
for ele in missingDescriptionProjects:
    print(ele)       
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://code.ptit.edu.vn/login')
wait = WebDriverWait(browser, 5)

def getDescription(browser):
    des = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "submit__des")))
    contents = des.find_elements_by_xpath("./*")
    table = des.find_elements_by_tag_name('tr')
    contents = contents[:-3] if table else contents[:-2]
    res = '\n_______________________________________________________________________________\n'
    for content in contents:
        res += content.text + '\n'
    if table:
        if len(table[0].find_elements_by_tag_name('td')) < 2:
            for test in table:
                res += test.text + '\n'
        else:
            table = table[1:]
            out_tmp = ""
            for i, test in enumerate(table):
                res += f'\n|||||||||||||||||INPUT {i}||||||||||||||||||\n'
                res += test.find_element_by_xpath('./td[1]').text
                try:
                    out_text = test.find_element_by_xpath('./td[2]').text
                    res += out_tmp
                    out_tmp = ""
                    out_tmp += f'\n-----------------OUTPUT {i}-----------------\n'
                    out_tmp += out_text
                except NoSuchElementException:
                    pass
            if out_tmp != "":
                res += out_tmp
    res += '\n_______________________________________________________________________________\n'
    reqs = browser.find_elements_by_class_name('submit__req')
    for req in reqs:
        res += '\n' + req.text
    return res

# Login:
username = browser.find_element_by_id('login__user')
password = browser.find_element_by_id('login__pw')
username.send_keys('B19DCCN333')
password.send_keys('h001201023360')
password.send_keys(Keys.RETURN)

def getDes(i):
    for i in range(i, len(missingDescriptionProjects)):
        id = missingDescriptionProjects[i]
        base_dir = '.\\' + id
        print(id)
        url = "https://code.ptit.edu.vn/student/question/" + id
        # Get Content:
        try:
            browser.get(url)
            with io.open(base_dir + '\\' + id + '.txt', "w", encoding="utf-8") as f:
                f.write(getDescription(browser))
            f.close()
            print(id + ' done!')
        except (NoSuchElementException, InvalidSessionIdException):
            print('Server not have ' + id)
            i += 1
        except TimeoutException:
            print("Pausing...")
            time.sleep(1)
            getDes(i)

browser.close()
getDes(0)
print("DONE!")
call(r"taskkill /im chromedriver.exe /f")