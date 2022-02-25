import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

os.chdir('C:/Users/ADMIN/Desktop')
existProb = []
for prj in os.listdir('E:/hk12021/oop/code'):
    existProb.append(prj)
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://code.ptit.edu.vn/login')
wait = WebDriverWait(browser, 5)

def logIn(browser):
    username = browser.find_element_by_id('login__user')
    password = browser.find_element_by_id('login__pw')
    username.send_keys('B19DCCN333')
    password.send_keys('h001201023360')
    password.send_keys(Keys.RETURN)
    time.sleep(1)
    browser.get('https://code.ptit.edu.vn/student/question?course=141')

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


root = 'https://code.ptit.edu.vn/student/question'
page = 1
header = {}
accepted = []
status = 1
cur_prob_st = 0

def getProb():
    global header, accepted, page, hkey
    for page in '123':
        browser.get(root + f'?page={page}')
        # Find all missing problem and categorize:
        for row in wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "tr")))[1:]:
            info = row.find_elements_by_tag_name("td")
            id = info[2].text
            if id in existProb:
                continue
            header[id] = (info[3].text, info[4].text, info[5].text)
            if 'bg--10th' in row.get_attribute('class'):
                accepted.append(id)
    hkey = list(header.keys())
    print("-----------MISSING----------")
    for ele in header:
        print(ele)
    print("----------ACCEPTED----------")
    for ele in accepted:
        print(ele)
    print("____________DONE____________")

# Create descriptions:
def creDes():
    global status, cur_prob_st, root
    status = 1
    try:
        for cur_prob_st in range(cur_prob_st, len(header)):
            id = hkey[cur_prob_st]
            browser.get(root + '/' + id)
            path = 'Others/'
            if id in accepted:
                continue
            with open(path + id + '.txt', 'w', encoding='utf-8') as desf:
                desf.write(f"ID: {id}\nProblem's name: {header[id][0]}\nType: {header[id][1]}\nTopic: {header[id][2]}\n\n")
                desf.write(getDescription(browser))
            desf.close()
            print(f"Create {id}'s description successfully!")
        status = 2
        cur_prob_st = 0
    except (NoSuchElementException, TimeoutException):
        print("Pausing...")
        time.sleep(2)
        if status == 1:
            try: 
                browser.find_element_by_class_name('blank.b403')
                cur_prob_st += 1
            finally:
                creDes()
        else:
            creSols()

# Create solutions:
def creSols():
    global status, cur_prob_st
    status = 2
    try:
        for cur_prob_st in range(cur_prob_st, len(accepted)):
            id = accepted[cur_prob_st]
            browser.get(root + '/' + id)
            table = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'table-striped.status__table')))
            submits = table.find_elements_by_tag_name('tr')[1:]
            sub_id = []
            run_time = []
            memory = []
            # Get infomation of AC solutions:
            for submit in submits:
                if submit.find_element_by_xpath('td[4]/a/span').text != 'AC':
                    continue
                info = submit.find_elements_by_tag_name('td')
                sub_id.append(info[0].text)
                run_time.append(info[4].text)
                memory.append(info[5].text)
            # Create files:
            for i, sid in enumerate(sub_id[::-1]):
                browser.get(f'https://code.ptit.edu.vn/student/solution/{sid}/edit')
                with open('Others/Accepted/' + id + f'/submit_{i}.py', 'w', encoding='utf-8') as solf:
                    solf.write(f'\'\'\'\n\tRun time: {run_time[i]}\n\tMemory: {memory[i]}\n\'\'\'\n')
                    solf.write(wait.until(EC.presence_of_element_located((By.ID, 'source_code'))).get_attribute('value'))
                solf.close()            
                print(f"Create {id}'s submit_{i}.py successfully!")
    except (NoSuchElementException, TimeoutException):
        print("Pausing...")
        time.sleep(2)
        if status == 1:
            creDes()
        else:
            creSols()
    

logIn(browser)
getProb()
creDes()
browser.close()