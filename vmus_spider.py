import requests
from bs4 import BeautifulSoup
import datetime
from pytz import timezone


def BsRequest(url):
    res = requests.get(url)
    source_code = res.content
    soup = BeautifulSoup(source_code, 'html.parser')
    return soup


def collect_post(start_page, end_page):
    for m in range(start_page, end_page + 1):
        print ('page' + str(m))
        vmUrl = 'http://vmus.co/page/'
        soup = BsRequest(vmUrl + str(m) + '/')
        for i in soup.findAll('h2', {'class': 'post-title'}):
            if '連載中' in i.text:
                if '神煩' in i.text or '宅男' in i.text or '金裝' in i.text \
                        or '天蠍' in i.text or '報到' in i.text or '諜網' in i.text:
                    show_name = i.text.split('線上看')[0].split('[連載中]')[1]
                    show_url = i.a['href']

                    showSoup = BsRequest(show_url)
                    post_time_text = showSoup.find(
                        'time', {'class': 'entry-date'})
                    post_time_text = post_time_text.text

                    print('--------------------------------------------------')
                    show_name = i.text.split('線上看')[0].split('[連載中]')[1]
                    print(show_name)
                    print(show_url)
                    print (post_time_text)
                    print('--------------------------------------------------')
                else:
                    show_name = i.text.split('線上看')[0].split('[連載中]')[1]
                    print('crawling other show ' + show_name)


def collect_latest_post_url(daydelta):
    vm_url = 'http://vmus.co/'
    start_page = 1
    if start_page >= 1:
        number_of_page = start_page
    else:
        number_of_page = 1

    while True:
        try:
            num = str(number_of_page)
            current_page_url = vm_url + 'page/' + num
            soup = BsRequest(current_page_url)

            for i in soup.findAll('h2', {'class': 'post-title'}):
                if '連載中' in i.text:
                    if '神煩' in i.text or '宅男' in i.text or '金裝' in i.text \
                            or '天蠍' in i.text or '報到' in i.text \
                            or '諜網' in i.text:
                        show_url = i.a['href']

                        showSoup = BsRequest(show_url)
                        post_time_text = showSoup.find(
                            'time', {'class': 'entry-date'})
                        post_time_text = post_time_text['datetime']
                        post_time_naive = datetime.datetime.strptime(
                            post_time_text, '%Y-%m-%dT%H:%M:%S+00:00')
                        UTC_tz = timezone('UTC')
                        post_time_in_UTC = UTC_tz.localize(post_time_naive)
                        post_time = post_time_in_UTC
                        time_diff = datetime.datetime.utcnow().date() - \
                            post_time.date()
                        if time_diff.days > daydelta:
                            stop_crawling = 'ok'
                            print('-------------------------------')
                            show_name = i.text.split(
                                '線上看')[0].split('[連載中]')[1]
                            print(show_name)
                            print(show_url)
                            print(post_time)
                            print('-------------------------------')
                            print('This is the last show')
                            print('-------------------------------')
                            break
                        else:
                            stop_crawling = 'no'
                            print('------------------------------------------')
                            show_name = i.text.split(
                                '線上看')[0].split('[連載中]')[1]
                            print(show_name)
                            print(show_url)
                            print(post_time)
                            print('------------------------------------------')
                    else:
                        stop_crawling = 'no'
                        show_name = i.text.split('線上看')[0].split('[連載中]')[1]
                        print('crawling other show ' + show_name)

            if stop_crawling == 'ok':
                print('The end page URL is ' + current_page_url)
                break
            else:
                number_of_page += 1
        except AttributeError as e:
            print (e)
            print('The end page URL is ' + vm_url +
                  'page/' + str(number_of_page - 1))
            break


def shows_latest_episode(url):
    episodes_soup = BsRequest(url)
    latest_episode_url = episodes_soup.find(
        'span', {'class': 'category_nav_prev'}).a['href']
    latest_episode_soup = BsRequest(latest_episode_url)
    episode_name = latest_episode_soup.find('h2', {'class': 'post-title'}).text
    episode_name = episode_name.split('線上看')[0]
    post_time_text = latest_episode_soup.find(
        'time', {'class': 'entry-date'}).text
    if latest_episode_url == seen_show_url.values():
        seen_status = 'seen'
    else:
        seen_status = 'not yet'
    print('--------------------------------------------------------')
    print(post_time_text + '-' + seen_status)
    print(episode_name)
    print(latest_episode_url)
    return(post_time_text, seen_status, latest_episode_url, episode_name)


def update_show_html():
    text_file = open("show.html", "w+")
    text_file.close()
    # for show in show_url.values():
    #    (post_time_text, seen_status, latest_episode_url, episode_name) = \
    #     shows_latest_episode(show)
    #     text_file = open("show.html", "a")
    #   text_file.write('<li>' + post_time_text + '-' +\
    #   seen_status + '<br>' + '<a href="' +\
    #    latest_episode_url + '">' + episode_name + '</a>' + '</li>' + '<br>')
    #     text_file.close()
    html_template = '<!DOCTYPE html><html lang="en"><head>' + \
        '<meta charset="utf-8">' + \
        '<meta name="viewport" content="width=device-width,' + \
        ' initial-scale=1, shrink-to-fit=no">' + \
        '<meta http-equiv="x-ua-compatible" content="ie=edge">' + \
        '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/' + \
        'bootstrap/4.0.0-alpha.2/css/bootstrap.min.css"' + \
        ' integrity="sha384-y3tfxAZXuh4HwSYylfB' + \
        '+J125MxIs6mR5FOHamPBG064zB+AFeWH94NdvaCBm8qnd"' + \
        ' crossorigin="anonymous"></head><body><div class="list-group">'

    for show in show_url.values():
        (post_time_text, seen_status, latest_episode_url,
         episode_name) = shows_latest_episode(show)
        show_list = '<a href="' + latest_episode_url + \
            '" class="list-group-item">' + \
            post_time_text + ' | ' + episode_name + '</a>'
        html_template += show_list

    html_template += '<!-- jQuery first, then Bootstrap JS. -->' + \
        '<script src="https://ajax.googleapis.com/' + \
        'ajax/libs/jquery/2.1.4/jquery.min.js"></script>' + \
        '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/' + \
        '4.0.0-alpha.2/js/bootstrap.min.js" integrity="sha384-vZ2WRJMws' + \
        'jRMW/8U7i6PWi6AlO1L79snBrmgiDpgIWJ82z8eA5lenwvxbMV1PAh7"' + \
        ' crossorigin="anonymous"></script></body></html>'
    text_file = open("show.html", "a")
    text_file.write(html_template)
    text_file.close()

show_url = {
    'scorpion': 'http://vmus.co/天蠍蠍子網絡-scorpion/',
    'suits': 'http://vmus.co/金裝律師訴訟雙雄-suits/',
    'brooklyn-nine-nine': 'http://vmus.co/神煩警察神煩警探-brooklyn-nine-nine/',
    'new-girl': 'http://vmus.co/俏妞報到杰茜駕到-new-girl/',
    'quantico': 'http://vmus.co/quantico/',
    'bigbang': 'http://vmus.co/宅男行不行生活大爆炸-the-big-bang-theory/',
    'fresh-off-the-boat': 'http://vmus.co/fresh-off-the-boat/',
    'billions': 'http://vmus.co/billions/',
    'rush-hour': 'http://vmus.co/rush-hour/',
    'dr-ken': 'http://vmus.co/dr-ken/',
}

seen_show_url = {
    'scorpion': 'http://vmus.co/天蠍蠍子蠍子網絡-scorpion-第二季-第十八集-s02e18-線上看-簡/',
    'suits': 'http://vmus.co/金裝律師訴訟雙雄-suits-第五季-第十六集-s05e16-線上看-簡中/',
    'brooklyn-nine-nine': 'http://vmus.co/神煩警察神煩警探-brooklyn-nine-nine-第三季-第十八集-s03e18-線上看/',
    'new-girl': 'http://vmus.co/俏妞報到杰茜駕到-new-girl-第五季-第十集-s05e10-線上看-簡中/',
    'quantico': 'http://vmus.co/諜影行動諜網新生無間道-quantico-第一季-第十二集-s01e12-線/',
    'bigbang': 'http://vmus.co/宅男行不行生活大爆炸-the-big-bang-theory-第九季-第十八集-s09e18-線/',
    'fresh-off-the-boat': 'http://vmus.co/初來乍到菜鳥新移民-fresh-off-the-boat-第二季-第十五集-s02e15-線上/',
    'white-collar': 'http://vmus.co/雅痞神探貓鼠遊戲妙警賊探-white-collar-第三季-第八集-s03e08-線/',
}

if __name__ == '__main__':
    # collect_latest_post_url(5)
    # collect_post(1, 6)
    update_show_html()
