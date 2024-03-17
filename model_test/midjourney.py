from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# Chrome 옵션 설정
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # 브라우저 창 숨기기
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--no-sandbox')


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#service = Service(executable_path=os.environ.get("CHROMEDRIVER_PATH"))
#options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
#driver = webdriver.Chrome(service=service, options=options)
driver.get('https://shopsquare.naver.com')
