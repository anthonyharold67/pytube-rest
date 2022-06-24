from django.http import HttpResponse
from django.shortcuts import render
from pytube import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
import time
from hurry.filesize import size #dosya boyutunu görüntü değiştirmek için
# Create your views here.

@api_view(['GET'])
def youtube(request):
    if request.method == 'GET':
        url = request.GET.get('url')
        if url:
            yt=YouTube(url)
            video={
                "info":{
                    "title":yt.title,
                    "thumbnail":yt.thumbnail_url,
                    "description":yt.description,
                    "author":yt.author,
                    "published":yt.publish_date,
                    "views":yt.views,
                    "length":time.strftime('%H:%M:%S',time.gmtime(yt.length)),
                },
                "sources":[]
            }
            videos = yt.streams.filter(progressive=True)
            for v in videos:
                video["sources"].append({
                    "url":v.url,
                    "size":size(v.filesize),
                    "quality":v.resolution,
                })
        return Response(video)
