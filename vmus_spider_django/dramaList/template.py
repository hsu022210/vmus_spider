# import vmus_spider

def get_template():

    html_template = '<!DOCTYPE html><html lang="en"><head>' + \
        '<meta charset="utf-8">' + \
        '<meta name="viewport" content="width=device-width,' + \
        ' initial-scale=1, shrink-to-fit=no">' + \
        '<meta http-equiv="x-ua-compatible" content="ie=edge">' + \
        '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/' + \
        'bootstrap/3.3.7/css/bootstrap.min.css"' + \
        ' integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u"' + \
        ' crossorigin="anonymous"><title>Shows real time updated</title> '+ \
        '</head><body style="padding: 50px; background:#2b303a;"><div class="row">'
    # background:#26547c

    data = vmus_spider.get_data()

    each_show_thumbnail = '<div class="col-sm-6 col-md-4">' +\
        '<div class="thumbnail" style="min-height:300px;"><img src="{}">' + \
            '<div class="caption">' + \
                '<h3>{}</h3>' + \
                '<p>{}</p>' + \
                '<p><a href="{}" class="btn btn-default" role="button">series</a>' +\
                '<a href="{}" class="btn btn-danger pull-right" role="button">{}</a></p>' + \
            '</div>' + \
         '</div>' + \
         '</div>'

    for show in data:
        (post_time_text, latest_episode_url, episode_name, episode_image, episodes_url) = vmus_spider.shows_latest_episode(show['url'])
        show_list = each_show_thumbnail.format(episode_image, show['name'], episode_name, episodes_url, latest_episode_url, post_time_text)
        html_template += show_list

    html_template += '<div class="clearfix"></div>'+ \
        '</div>' + \
        '<!-- jQuery first, then Bootstrap JS. -->' + \
        '<script src="https://ajax.googleapis.com/' + \
        'ajax/libs/jquery/2.1.4/jquery.min.js"></script>' + \
        '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/' + \
        '4.0.0-alpha.2/js/bootstrap.min.js" integrity="sha384-vZ2WRJMws' + \
        'jRMW/8U7i6PWi6AlO1L79snBrmgiDpgIWJ82z8eA5lenwvxbMV1PAh7"' + \
        ' crossorigin="anonymous"></script></body></html>'

    return html_template
