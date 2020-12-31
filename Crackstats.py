from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time


def fetch5():
    print("Fetching status of top 5 games................")
    # noinspection PyBroadException
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "overlay-button"))
        )
        element.click()
    except:
        pass

    x = driver.find_element_by_class_name("game-gallery-hot")
    games = [i.text for i in x.find_elements_by_class_name('main-title')]
    status = []

    for i in x.find_elements_by_class_name("sub-title"):
        # noinspection PyBroadException
        try:
            status.append(
                i.find_element_by_class_name("inline-block").find_element_by_class_name("status-not-cracked").text)

        except:
            status.append(i.find_element_by_class_name("inline-block").find_element_by_class_name("status-cracked").text
                          )

    x = driver.find_element_by_class_name("game-gallery")

    for i in range(len(status)):
        print("\n" + games[i] + "--->  " + status[i], end='\n')


def search():
    driver.get("https://crackwatch.com/search")
    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)

    # noinspection PyBroadException
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "overlay-button"))
        )
        element.click()
    except:
        pass

    g_name = input("Enter the name of the game (Note: please make sure the spelling is right to get correct result): ")\
        .lstrip().rstrip()
    print("Please wait while we fetch you the info...")
    x = driver.find_element_by_class_name("bar-search")
    x.clear()
    time.sleep(2)
    x.send_keys(g_name)
    time.sleep(2)
    x.send_keys(Keys.RETURN)

    games = [i.text for i in driver.find_elements_by_class_name('main-title')]
    status = [j.text for j in driver.find_elements_by_class_name('sub-title')]

    if len(games) == 1:
        print("No game found with the given name. Please check your spelling and try again")
        driver.get('https://crackwatch.com/')
        return

    for i, j in zip(games[:len(games) - 1], status[:len(status) - 1]):
        print("\n" + i + "---> " + j)

    driver.get('https://crackwatch.com/')


if __name__ == '__main__':
    print("WELCOME!".center(50, '-'))
    print("Standby...")

    path = r'Enter chrome driver's path'
    chrome_opt = Options()
    chrome_opt.add_argument("--headless")
    chrome_opt.add_argument("--window-size=1920,1080")
    chrome_opt.binary_location = r'Enter chrome browser's path'
    driver = webdriver.Chrome(path, options=chrome_opt)
    driver.get('https://crackwatch.com/')

    while True:
        print("\n")
        a = input("T. Get info of top 5 games\nS. Get info of a specific game\nE. End\nEnter your choice: ").lstrip()\
            .rstrip()
        print("\n")

        if a.upper() == 'T':
            print("Please wait while we fetch you the info...")
            fetch5()

        elif a.upper() == 'S':
            print("Standby...")
            search()

        elif a.upper() == 'E':
            driver.close()
            print('Thank You!')
            break

        else:
            print("Please give a valid input..")
