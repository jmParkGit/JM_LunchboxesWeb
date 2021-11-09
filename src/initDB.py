from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# client = MongoClient('mongodb://ID:PASSWORD@IP', 27017)
client = MongoClient('localhost', 27017)
db = client.dbJM

def getDataFromGS25():
    # mac Safari
    driver = webdriver.Safari()
    driver.get('http://gs25.gsretail.com/gscvs/ko/products/youus-freshfood')
    time.sleep(1)
    #도시락 버튼 클릭
    try:
        lunchboxBtn = driver.find_element(By.ID, 'productLunch')
        lunchboxBtn.click()
    except NoSuchElementException as e:
        print(e)

    time.sleep(3)
    lunchboxes=driver.find_elements(By.CSS_SELECTOR, '#contents > div.yCmsComponent.span-24.section1.cms_disp-img_slot > div > div > div > div > div > div.tblwrap.mt20 > div.tab_cont.on > ul > li')

    #GS25는 뒤 cost에서 one제외해야됨
    for lunchbox in lunchboxes:
        title = lunchbox.find_element(By.CLASS_NAME, 'tit').text
        cost = lunchbox.find_element(By.CLASS_NAME, 'cost').text
        img = lunchbox.find_element(By.CSS_SELECTOR, 'div > p.img > img').get_attribute('src')

        cost = cost.replace(',', '')
        cost = int(cost.replace('원', ''))

        if title is not None:
            doc = {
                'title': title,
                'img_url': img,
                'cost': cost,
                'convenience': 'GS25',
                'like': 0
            }

            db.lunchbox.insert_one(doc)
            print(title, str(cost), img)


    print('GS25 done')

def getDataFromCU():
    # mac Safari
    driver = webdriver.Safari()
    driver.get('http://cu.bgfretail.com/product/product.do?category=product&depth2=4&sf=N')
    time.sleep(1)
    #도시락 버튼 클릭
    try:
        lunchboxBtn = driver.find_element(By.CLASS_NAME, 'eventInfo_02')
        lunchboxBtn.click()
    except NoSuchElementException as e:
        print(e)

    time.sleep(3)

    #더보기 버튼 클릭
    try:
        plusBtn = driver.find_element(By.CSS_SELECTOR, '#dataTable > div.prodListBtn > div.prodListBtn-w > a')
        plusBtn.click()
    except NoSuchElementException as e:
        print(e)
    time.sleep(3)

    lunchboxes=driver.find_elements(By.CSS_SELECTOR, '#dataTable > div.prodListWrap > ul > li')

    for lunchbox in lunchboxes:
        title = lunchbox.find_element(By.CSS_SELECTOR, 'p.prodName > span').text
        cost = lunchbox.find_element(By.CSS_SELECTOR, 'p.prodPrice > span').text
        img = lunchbox.find_element(By.CSS_SELECTOR, 'div > a > img').get_attribute('src')

        cost = int(cost.replace(',', ''))
        #CU는 title이 도)로 시작하는것이 도시락임
        if title is not None:
            doc = {
                'title': title,
                'img_url': img,
                'cost': cost,
                'convenience': 'CU',
                'like': 0
            }

            db.lunchbox.insert_one(doc)
            print(title,str(cost),img)

    print('CU done')

def getDataFrom7Eleven():
    # mac Safari
    driver = webdriver.Safari()
    driver.get('https://www.7-eleven.co.kr/product/bestdosirakList.asp?pTab=mini')
    time.sleep(1)
    #더보기 버튼이 안보일때 까지 클릭
    try:
        i=0
        while(i<8):
            lunchboxBtn = driver.find_element(By.ID, 'moreImg')
            lunchboxBtn.click()
            time.sleep(2)
            i = i+1
    except NoSuchElementException as e:
        print(e)
        print('NoSuchElementException#1')

    time.sleep(3)

    lunchboxes=driver.find_elements(By.CSS_SELECTOR, '#listDiv > div.dosirak_list.dosirak_list_01.dosirak_list_01_02 > ul > li')
    for lunchbox in lunchboxes:
        try:
            title = lunchbox.find_element(By.CSS_SELECTOR, 'div > div > div.name').text
            cost = lunchbox.find_element(By.CSS_SELECTOR, 'div > div > div.price > span').text
            img = lunchbox.find_element(By.CSS_SELECTOR, 'div > img').get_attribute('src')

            cost=int(cost.replace(',', ''))

            if title is not None:
                doc = {
                    'title': title,
                    'img_url': img,
                    'cost': cost,
                    'convenience': 'Eleven',
                    'like': 0
                }

                db.lunchbox.insert_one(doc)

                print(title,str(cost),img)
        except NoSuchElementException as e:
            print(e)
            print('NoSuchElementException#2')

    print('7Eleven done')

def main():
    db.lunchbox.drop()
    getDataFromGS25()
    getDataFromCU()
    getDataFrom7Eleven()

if __name__ == "__main__":
    main()