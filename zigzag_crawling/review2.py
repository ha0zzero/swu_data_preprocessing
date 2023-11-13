from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

# 브라우저 꺼짐 방지 옵션
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# browser = webdriver.Chrome(options=chrome_options)

browser = webdriver.Chrome()
browser.get("https://zigzag.kr/categories/-1?title=%EC%95%84%EC%9A%B0%ED%84%B0&category_id=-1&middle_category_id=436&sub_category_id=438&sort=201")
time.sleep(1)

html = browser.page_source
soup = BeautifulSoup(html, "html.parser")

# 상위 30개 url_list 만들기
url_list = []
url_area = soup.select('div.css-1h2671j.e1dr6ufx0 a')
url_all = soup.find_all('a')
# print(url_all)

for url in url_all:
    href = url.attrs['href']
    url_list.append(['https://zigzag.kr'+href])
    if(len(url_list)==30):break  # 상위 30개 url만 크롤링
# print(url_list)
print('url 수집 끝, 해당 url 데이터 크롤링')

# 상위 30개 url을 돌며 리뷰 크롤링
result = []
id = 1

for u in url_list:
    url = ' '.join(u)   # 리스트를 문자열로 변환
    browser.get(url)
    time.sleep(1)

    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")

    review_area = soup.select('div.css-70rfrb.e1hi9732')
    browser.implicitly_wait(10) # 페이지 로드 기다리기
    for top_review in review_area:
        print('ID: '+str(id)+' 리뷰 크롤링')
        # print(top_review)
        ID = id
        리뷰어 = top_review.select_one('.BODY_16.SEMIBOLD.css-1k3hx0v.e1fnwskn0').text
        리뷰날짜 = top_review.select_one('.BODY_13.MEDIUM.css-1he5u5.e1okf4zi0').text
        리뷰텍스트 = top_review.select_one('.BODY_14.REGULAR.css-1huf8iy.eox2jl02').text
        review_list = [ID, 리뷰어, 리뷰날짜, 리뷰텍스트]
        result.append(review_list)
        if (len(result) == id * 5): break  # 상위 5개 리뷰 크롤링
    print(review_list)
    id = id+1

df = pd.DataFrame(result, columns=['ID','리뷰어', '리뷰날짜', '리뷰텍스트'])
df = df.set_index(keys='ID')
df.to_csv('zigzag_review1.csv', encoding='utf-8-sig')

browser.close()