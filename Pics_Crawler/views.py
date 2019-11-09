import datetime
from django.shortcuts import render, redirect, HttpResponse
from bs4 import *
import requests as rq
import os
import uuid
from os import path


def index(request):
    if request.method == 'POST':
        url = request.POST['url']
        r2 = rq.get(url)
        soup2 = BeautifulSoup(r2.text, "html.parser")

        links = []
        x = soup2.select('img[src^="https://images.pexels.com/photos"]')
        for img in x:
            links.append(img['src'])

        i = 1
        if path.exists('Prince'):
            for indexing, img_link in enumerate(links):
                if i <= 10:
                    img_data = rq.get(img_link)
                    with open(url[24:] + str(indexing + 1) + '.jpg', 'wb+') as f:
                        f.write(img_data.content)
                        i += 1
                else:
                    f.close()
                    break
            return redirect(index)
        else:
            for indexing, img_link in enumerate(links):
                if i <= 10:
                    img_data = rq.get(img_link)
                    with open('Prince' + str(indexing + 1) + '.jpg', 'wb+') as f:
                        f.write(img_data.content)
                        i += 1
                else:
                    f.close()
                    break
            return redirect(index)

    else:
        return render(request, 'Pics_Crawler/index.html', {})
