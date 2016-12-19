from django.shortcuts import render
from . import vmus_spider

# Create your views here.
def index(request):
    shows_info_arr = vmus_spider.get_shows_info_arr()
    context = {'shows_info_arr': shows_info_arr, }
    return render(request, 'index.html', context)
