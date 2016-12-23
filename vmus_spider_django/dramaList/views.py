from django.shortcuts import render
from . import vmus_spider
from .models import Show
from django.utils import timezone
import pytz

# Create your views here.


def index(request):

    def parse_show(show):
        (show_soup, latest_episode_url) = vmus_spider.get_latest_episode_url(show.show_url)

        if latest_episode_url != show.latest_episode_url:
            show_dict = vmus_spider.get_latest_episode_info(show_soup, latest_episode_url)
            show.latest_episode_name = show_dict['latest_episode_name']
            show.latest_episode_url = show_dict['latest_episode_url']
            show.latest_post_time = show_dict['latest_post_time']
            show.show_image = show_dict['show_image']

        # refreshed_time = timezone.now()
        taiwan_tz = pytz.timezone('Asia/Taipei')
        refreshed_time_taiwan = refreshed_time.astimezone(taiwan_tz)

        # show.refreshed_time = refreshed_time
        show.refreshed_time = refreshed_time_taiwan
        show.save()

    showName = request.GET.get('showName')

    if showName:
        if showName == 'all':
            for show in Show.objects.all():
                parse_show(show)
        else:
            show = Show.objects.get(show_name=showName)
            parse_show(show)

    shows_info_arr = Show.objects.order_by('-latest_post_time')

    context = {
        'shows_info_arr': shows_info_arr,
               }
    return render(request, 'index.html', context)


def start_loading(request):
    showName = request.GET.get('showName')
    context = {
        'showName': showName,
               }
    return render(request, 'start_loading.html', context)
