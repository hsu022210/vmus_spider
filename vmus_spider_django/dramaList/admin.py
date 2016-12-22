from django.contrib import admin
from .models import Show

# Register your models here.


class ShowAdmin(admin.ModelAdmin):
    list_display = ('show_name', 'show_url', 'latest_episode_url',
                    'latest_episode_name', 'latest_post_time', 'show_image')

admin.site.register(Show, ShowAdmin)
