from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

browser = webdriver.Chrome()
browser.get('https://zigzag.kr/categories/-1?title=%EC%95%84%EC%9A%B0%ED%84%B0&category_id=-1&middle_category_id=436&sub_category_id=438&sort=201')
time.sleep(1)

html = browser.page_source
soup = BeautifulSoup(html,'html.parser')

# 상품 리뷰
zigzag_goods = '//*[@id="__next"]/main/section[2]/div/a[1]'
browser.find_element_by_xpath(zigzag_goods).click()  # a[]안에 숫자가 상위 30개의 옷 순서대로 커짐 (https://tbbrother.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%85%80%EB%A6%AC%EB%8B%88%EC%97%84Selenium%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%B4%EC%84%9C-%EC%9B%B9-%ED%81%B4%EB%A6%AD%ED%95%98%EA%B8%B0)참고
time.sleep(1)
# 리뷰 창으로 이동
zigzag_review = browser.find_element_by_xpath('//*[@id="__next"]/div[1]/div[16]/div[1]/button[2]/span')  # https://velog.io/@rkfksh/Selenium-click%EB%90%98%EC%A7%80-%EC%95%8A%EB%8A%94-element%EB%A5%BC-javascript-%EB%AA%85%EB%A0%B9%EC%96%B4%EB%A1%9C-click%ED%95%98%EA%B8%B0 참고.
browser.execute_script("arguments[0].click();", zigzag_review)