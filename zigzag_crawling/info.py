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

info_area = soup.select('.css-34da54.e91dh069')
# print(info_area)

result = []
id = 1
for info_post in info_area:
    ID = id
    상품제목 = info_post.select_one('.CAPTION_12.REGULAR.css-4me7r9.e91dh064').text
    가격 = info_post.select_one('.BODY_15.SEMIBOLD.css-1a86z8c.eh5ooyt0').text
    try:
        할인율 = info_post.select_one('.BODY_15.SEMIBOLD.css-pd9h31.e91dh062').text
    except:
        할인율 = None
    리뷰평점 = info_post.select_one('.css-1a9std3.e13zfay41').text
    리뷰개수 = info_post.select_one('.css-1lykwaz.e13zfay40').text
    리뷰개수 = 리뷰개수.replace("(", "").replace(")", "")
    썸네일 = info_post.select_one('.e1xrpm0a2.css-i6kod5.e81k49g1 > div > div > img').get('src')
    result.append([ID, 상품제목, 가격, 할인율, 리뷰평점, 리뷰개수, 썸네일])
    id = id+1
    if (len(result) == 30): break

# print(result)

df = pd.DataFrame(result, columns=['ID', '상품제목', '가격', '할인율', '리뷰평점', '리뷰개수', '썸네일'])
df = df.set_index(keys='ID')
df.to_csv('zigzag_info.csv', encoding='utf-8-sig')

browser.close()