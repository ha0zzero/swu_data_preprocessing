from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://zigzag.kr/categories/-1?title=%EC%95%84%EC%9A%B0%ED%84%B0&category_id=-1&middle_category_id=436&sub_category_id=438&sort=201')
time.sleep(1)

html = browser.page_source
soup = BeautifulSoup(html,'html.parser')

review_list= []
result=[]

# 상품 리뷰
for id in range (1,31):
    zigzag_goods = '//*[@id="__next"]/main/section[2]/div/a['+str(id)+']'
    browser.find_element(By.XPATH, zigzag_goods).click()
    time.sleep(2)

    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')

    review_area = soup.select('div.css-z61zy2.e9uiogx0')

    browser.implicitly_wait(10) # 페이지 로드 기다리기
    for top_review in review_area:
        print('ID:'+str(id)+' 리뷰 크롤링')
        ID = id
        리뷰어 = top_review.select_one('.BODY_16.SEMIBOLD.css-1k3hx0v.e1fnwskn0').text
        리뷰날짜 = top_review.select_one('.BODY_17.REGULAR.BODY_13.MEDIUM.css-1w6topb.e1cn5bmz0').text
        리뷰텍스트 = top_review.select_one('.BODY_14.REGULAR.css-epr5m6.e1j2jqj72').text
        review_list = [ID, 리뷰어, 리뷰날짜, 리뷰텍스트]
        result.append(review_list)
        if (len(result) == id * 5): break  # 상위 5개 리뷰 크롤링
    print(review_list)

    browser.back()

df = pd.DataFrame(result, columns=['ID','리뷰어', '리뷰날짜', '리뷰텍스트'])
df = df.set_index(keys='ID')
df.to_csv('zigzag_review4.csv', encoding='utf-8-sig')

browser.close()