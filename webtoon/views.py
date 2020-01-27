from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .crawling import *
# Create your views here.


def webtoon_home(request):
    context = {'webtoons': Webtoon.objects.all()}
    return render(request, 'webtoon/home.html', context)


def webtoon_list(request, key):
    context = {'episodes': Episode.objects.filter(webtoon__title=key)}
    return render(request, 'webtoon/list.html', context)


def webtoon_detail(request, key, num):
    cut_list = Cut.objects.filter(ep_id=num, ep__webtoon__title=key)
    context = {'cuts': cut_list}
    return render(request, 'webtoon/detail.html', context)


def crawling__main(request):
    crawling_main()
    return HttpResponse(199)


def crawling__epi(request):
    # crawling_main()
    webtoon_all = Webtoon.objects.all()
    webtoon_len = len(webtoon_all)
    for num, webtoon in enumerate(webtoon_all):
        print(num, '/', webtoon_len, webtoon)
        crawling_list(webtoon)
    return HttpResponse(200)


def crawling__cut(request):
    for wt in Webtoon.objects.all():
        for ep in wt.episode_set.all():
            print(ep)
            crawling_cut(ep)
    return HttpResponse(201)
