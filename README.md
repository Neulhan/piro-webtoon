# 🗺piro_crawling

```python
print('피로그래밍 12기 크롤링 강의 페이지입니다.')
```

## 사용환경
- jupyter notebook    (.ipynb)
- google colaboratory (.ipynb)


## request
파이썬 코드를 통해서 웹 페이지에 HTTP 요청을 보냄

### urllib
```python
import urllib

urllib_case = urllib.request.urlopen(url)
html_text = urllib_case.read().decode("utf-8")
```
[파이썬 binary 파일에 대해](https://wikidocs.net/15101)

### requests
```python
import requests

html_text = requests.get(url).text

# html_text 에는 str 형식의 html 문서가 담긴다
```

[urllib vs requests 정리된 블로그](https://brownbears.tistory.com/299)

## bs4.Beautifulsoup

[beautifulsoup란 무엇인지에 대해 잘 정리된 블로그](https://velog.io/@neulhan/%EC%B4%88%EB%B3%B4%EB%8F%84-%ED%95%A0-%EC%88%98-%EC%9E%88%EB%8A%94-python%EC%9C%BC%EB%A1%9C-%EB%84%A4%EC%9D%B4%EB%B2%84%EC%97%90%EC%84%9C-%EC%8B%A4%EC%8B%9C%EA%B0%84-%EA%B2%80%EC%83%89%EC%96%B4-%EC%A0%95%EB%B3%B4-%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0-2-BeautifulSoup-1uk4asqet0)
```python 
from bs4 import BeautifulSoup as bs

# beautiful soup 객체 생성
soup = bs(html_text, 'html.parser')

# html 안에서 선택자를 통해 특정 태그들 가져오기
selected_elements = soup.select('selector')

# 가져온 태그들 활용하기
# 1. .text로 내용 추출
# 2. .attrs
# 3. .get
```
## pandas 활용하기

