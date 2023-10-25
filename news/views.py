from django.shortcuts import render
from rest_framework import generics
from news.models import News
from news.serializers import NewsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


# class NewsApiView(generics.ListAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer

QUANTITY_NEWS_ON_ONE_PAGE = 3

class NewsApiView(APIView):
    def get(self, request):

        news_list = News.objects.all().values()

        news_quantity = len(news_list)

        remainder = news_quantity % QUANTITY_NEWS_ON_ONE_PAGE
        if remainder > 0:
            pages_county = news_quantity // QUANTITY_NEWS_ON_ONE_PAGE + 1
        
        else:
            pages_county = news_quantity // QUANTITY_NEWS_ON_ONE_PAGE

        pages = []

        for page in range(pages_county):
            pages.append(page + 1)

        news_on_page = 0
        index_page = 0

        data = []
        for n in list(news_list):

            if news_on_page > 2:
                news_on_page = 0
                index_page += 1
            
            date_published = n["datePublished"].strftime("%d.%m.%Y")
            print(date_published)
            data.append({
                "id": n["id"],
                "photo_preview_news": 'http://127.0.0.1:8000/media/' + n["photo_preview_news"],
                "title": n["title"],
                "shortDescription": n["shortDescription"],
                "datePublished": date_published,
                "textNews": n["textNews"],
                "page": pages[index_page]
            })

            news_on_page += 1


        return Response({
            "news": data,
            "pages_county": pages_county
        })
    

class NewsDetail(APIView):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        news_list = News.objects.all().values()
        news_list = list(news_list)

        news_detail = {}
        for n in news_list:
            if n["id"] == pk:
                n["photo_preview_news"] = 'http://127.0.0.1:8000/media/' + n["photo_preview_news"]
                n["datePublished"] = n["datePublished"].strftime("%d.%m.%Y")
                news_detail = n
                break

        return Response({
            "news_detail": news_detail
        })

