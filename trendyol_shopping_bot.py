
from selenium import webdriver  # seleniumu import ettik
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select  # dropdown list için
import pandas as pd
from bs4 import BeautifulSoup
import requests

option1 = Options()
option1.add_argument("--disable-notifications")
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe", chrome_options=option1)
url = "https://www.trendyol.com"  # gideceğimiz urlyi yazdık
driver.get(url)  # url'ye gittik
driver.maximize_window()  # sayfayı tam ekran yaptık
time.sleep(1)
driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
time.sleep(1)

df = pd.read_excel('trendy.xlsx', index_col=None, header=None)
sl = df.to_numpy()


def trendyol():

    search_bar = driver.find_element_by_class_name("search-box")
    time.sleep(1)
    search_bar.clear()
    search_bar.send_keys(sl[number])
    search_bar.send_keys(Keys.ENTER)
    try:
        if driver.find_element_by_xpath("//*[@id='tydortyuzdortpage']/div/div/div[3]/div[1]/a/h1"):
            driver.get("https://www.trendyol.com/sepet")
        pass


    except:
        search_bar = driver.find_element_by_class_name("search-box")
        time.sleep(1)
        search_bar.send_keys(Keys.PAGE_DOWN)  # sayfayı aşağı kaydırdık (bildirim çıkabilir)
        time.sleep(1)
        try:
            if driver.find_element_by_class_name("overlay"):
               element1 = driver.find_element_by_class_name("overlay")
               driver.execute_script("arguments[0].click();", element1)

        except:

            pass  # boşluğa tıkladık
        driver.find_element_by_xpath("//*[contains(text(), 'Kargo Bedava')]").click()  # kargo bedava
        time.sleep(1)
        grbf = Select(driver.find_element_by_css_selector(
            "#search-app > div > div.srch-rslt-cntnt > div.srch-prdcts-cntnr > div.srch-rslt-title > div.sort-fltr-cntnr > select"))  # en çok değerlendirilen //*[@id='search-app']/div/div[1]/div[2]/div[1]/div[2]/select
        grbf.select_by_value('MOST_RATED')
        time.sleep(2)

        req = requests.get(driver.current_url)  # ürün urlsini al
        soup = BeautifulSoup(req.content, 'html.parser')
        x = soup.find(class_="p-card-chldrn-cntnr").find("a")['href']
        driver.get(url + x)  # ürün linkine gittik
        sepeteekle = driver.find_element_by_class_name("add-to-basket-button-text")  # sepete ekle
        sepeteekle.click()
        time.sleep(2)



for number in range(0, 7):

    trendyol()



