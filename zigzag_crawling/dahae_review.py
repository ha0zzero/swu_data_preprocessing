from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

browser = webdriver.Chrome('/Users/Esther/PycharmProjects/pre_project/week8/chromedriver')
browser.get('https://zigzag.kr/categories/-1?title=%EC%95%84%EC%9A%B0%ED%84%B0&category_id=-1&middle_category_id=436&sub_category_id=438&sort=201')
time.sleep(10)

html = browser.page_source
soup = BeautifulSoup(html,'html.parser')

zigzag_post_area = soup.select('section.css-baq3dp.eabfyam0')
# print(zigzag_post_area)

# result = []
# for z in range(30):
# for zigzag_post in zigzag_post_area:
#     title = zigzag_post.select_one('.CAPTION_12.REGULAR.css-4me7r9.e91dh064').text
#     print(title)
    # thumbnail = blog_post.select_one('.thumbnail_area > a > img').get('src')
    # result.append([title, thumbnail])
#
# df = pd.DataFrame(result,columns=['title', 'thumbnail'])
# df.to_csv('블로그포스팅.csv',encoding='utf-8-sig')

# 상품 리뷰
zigzag_goods = '//*[@id="__next"]/main/section[2]/div/a[1]/div/div[2]/div[2]'
browser.find_element_by_xpath(zigzag_goods).click()  # a[]안에 숫자가 상위 30개의 옷 순서대로 커짐 (https://tbbrother.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%85%80%EB%A6%AC%EB%8B%88%EC%97%84Selenium%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%B4%EC%84%9C-%EC%9B%B9-%ED%81%B4%EB%A6%AD%ED%95%98%EA%B8%B0)참고
time.sleep(10)
# for z in range(1, 31):  # 1부터 30까지 반복
#     zigzag_goods_xpath = f'//*[@id="__next"]/main/section[2]/div/a[{z}]/div/div[2]/div[2]'
#     element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "zigzag_goods_xpath")))
#     element.click()
#     browser.back()  # 메인 페이지로 돌아가기.

# 리뷰 창으로 이동
zigzag_page = '//*[@id="__next"]/div[1]/div[17]/div[1]/button[2]/span'
zigzag_review = browser.find_element_by_xpath(zigzag_page)  # https://velog.io/@rkfksh/Selenium-click%EB%90%98%EC%A7%80-%EC%95%8A%EB%8A%94-element%EB%A5%BC-javascript-%EB%AA%85%EB%A0%B9%EC%96%B4%EB%A1%9C-click%ED%95%98%EA%B8%B0 참고.
browser.execute_script("arguments[0].click();", zigzag_review)

# 리뷰
result = []
id = 1
html = browser.page_source
soup = BeautifulSoup(html, "html.parser")

zigzag_review_post_area = soup.select('.css-70rfrb.e1hi9732')
browser.implicitly_wait(10)
# print(zigzag_review_post_area)

# 리뷰 5개 뽑아내기
for zigzag_top_review in zigzag_review_post_area:
    ID = id
    리뷰어 = zigzag_top_review.select_one('.BODY_16.SEMIBOLD.css-1k3hx0v.e1fnwskn0')
    리뷰날짜 = zigzag_top_review.select_one('BODY_13.MEDIUM.css-1he5u5.e1okf4zi0')
    리뷰텍스트 = zigzag_top_review.select_one('BODY_14 REGULAR css-1huf8iy eox2jl02')
    review_list = [ID, 리뷰어, 리뷰날짜, 리뷰텍스트]
    result.append(review_list)
    if(len(result) == id*5): break  # 상위 5개 리뷰 크롤링
print(review_list)
id = id+1

browser.back()
time.sleep(5)