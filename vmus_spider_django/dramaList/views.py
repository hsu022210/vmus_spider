from django.shortcuts import render
from . import vmus_spider
from .models import Show
from datetime import datetime
from django.utils import timezone

# Create your views here.


def index(request):
    showName = request.GET.get('showName')
    if showName:
        if showName == 'all':
            for show in Show.objects.all():

                (show_soup, latest_episode_url) = vmus_spider.get_latest_episode_url(show.show_url)

                if latest_episode_url != show.latest_episode_url:
                    show_dict = vmus_spider.get_latest_episode_info(show_soup, latest_episode_url)
                    show.latest_episode_name = show_dict['latest_episode_name']
                    show.latest_episode_url = show_dict['latest_episode_url']
                    show.latest_post_time = show_dict['latest_post_time']
                    show.show_image = show_dict['show_image']
                    show.save()
        else:
            show = Show.objects.get(show_name=showName)
            (show_soup, latest_episode_url) = vmus_spider.get_latest_episode_url(show.show_url)

            if latest_episode_url != show.latest_episode_url:
                show_dict = vmus_spider.get_latest_episode_info(show_soup, latest_episode_url)
                show.latest_episode_name = show_dict['latest_episode_name']
                show.latest_episode_url = show_dict['latest_episode_url']
                show.latest_post_time = show_dict['latest_post_time']
                show.show_image = show_dict['show_image']
                show.save()

        # shows_info_arr = vmus_spider.get_shows_info_arr()

        shows_info_arr = Show.objects.order_by('-latest_post_time')
        current_time = datetime.now()
        # current_time = timezone.now()
        context = {'shows_info_arr': shows_info_arr,
                   'current_time': current_time,
                   }
        return render(request, 'index.html', context)
    else:
        shows_info_arr = Show.objects.order_by('-latest_post_time')
        current_time = datetime.now()
        context = {'shows_info_arr': shows_info_arr,
                   'current_time': current_time,
                   }
        return render(request, 'index.html', context)


def start_loading(request):
    showName = request.GET.get('showName')
    context = {'showName': showName,
               }
    return render(request, 'start_loading.html', context)
