from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import urllib.request

driver = webdriver.Chrome(executable_path="path/chromedriver")

searchWord = ['html', 'css', 'javascript', 'python', 'java', 'c++']

downloadCount = 50
currentSearchWord = 0
frontDownloadPath = "DownloadPath/"

for currentWord in searchWord:
    #크롬포트 설정
    option = Options()
    option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    #검색어 검색
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl")
    searchWindow = driver.find_element_by_name("q")
    searchWindow.clear()
    searchWindow.send_keys(currentWord)
    searchWindow.send_keys(Keys.RETURN)

    #검색 페이지 로딩
    SCROLL_PAUSE_TIME = 0.5

    lastHeight = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(SCROLL_PAUSE_TIME)

        newHeight = driver.execute_script("return document.body.scrollHeight")
        if newHeight == lastHeight:
            break
        lastHeight = newHeight

    #이미지 다운로드
    imgList = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
    currentNum = 0
    for currentImg in imgList:
        try:
            currentImg.click()
            time.sleep(1)
            imgUrl = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img").get_attribute("src")
            downloadPath = frontDownloadPath + str(searchWord[currentSearchWord]) + "/" + str(currentNum) + ".jpg"
            urllib.request.urlretrieve(imgUrl, downloadPath)
            currentNum = currentNum + 1
            if currentNum >= downloadCount:
                break
        except:
            pass
    currentSearchWord = currentSearchWord + 1

driver.close()