from django.urls import path

from webtoon import views

app_name = 'naver_webtoon'

urlpatterns = [
    path('', views.webtoon_home, name='home'),
    path('<str:key>/', views.webtoon_list, name='list'),
    path('<str:key>/<int:num>/', views.webtoon_detail, name='detail'),
    path('crawling/main', views.crawling__main, name='crawling'),
    path('crawling/episode', views.crawling__epi, name='crawling'),
    path('crawling/cut', views.crawling__cut, name='crawling'),
]
