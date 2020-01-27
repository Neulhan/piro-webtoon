import requests
from bs4 import BeautifulSoup as bs
from .models import *


def crawling_main():
    print('crawling_main start')
    html = requests.get('https://comic.naver.com/webtoon/weekdayList.nhn')
    soup = bs(html.text, 'html.parser')
    webtoon_list = soup.select('.list_area .thumb a')
    print()
    for count, webtoon in enumerate(webtoon_list, 1):
        print(f"{count}/{len(webtoon_list)} {webtoon.get('title')} 크롤링 중")
        print(webtoon)
        Webtoon.objects.create(title=webtoon.get('title'),
                               title_id=f"https://comic.naver.com{webtoon.get('href')}",
                               thumb_src=webtoon.find('img').get('src'))



def crawling_list(webtoon):
    html = requests.get(webtoon.list_url)
    # html = requests.get(webtoon)
    soup = bs(html.text, 'html.parser')
    episode__list = soup.select('#content .viewList  tr td:first-child a')
    for episode in episode__list:
        try:
            Episode.objects.create(thumb_src=episode.find('img').get('src'),
                                   ep_url=f"https://comic.naver.com{episode.get('href')}",
                                   title=episode.find('img').get('alt'),
                                   webtoon=webtoon
                                   )
        except Exception as e:
            print(e)
        print()


def crawling_cut(epi):
    html = requests.get(epi.ep_url)
    soup = bs(html.text, 'html.parser')
    cut_list = soup.select('#comic_view_area .wt_viewer img')

    for count, cut in enumerate(cut_list, 1):
        Cut.objects.create(cut_src=cut.get('src'),
                           num=count,
                           ep=epi
                           )

