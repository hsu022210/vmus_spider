import requests
from bs4 import BeautifulSoup
import os
import json
# import template

raw_data = [
    {
        "name": "scorpion",
        "url": "http://vmus.co/天蠍蠍子網絡-scorpion/",
    }, {
        "name": "brooklyn-nine-nine",
        "url": "http://vmus.co/神煩警察神煩警探-brooklyn-nine-nine/",
    }, {
        "name": "suits",
        "url": "http://vmus.co/金裝律師訴訟雙雄-suits/",
    }, {
        "name": "new-girl",
        "url": "http://vmus.co/俏妞報到杰茜駕到-new-girl/",
    }, {
        "name": "quantico",
        "url": "http://vmus.co/quantico/",
    }, {
        "name": "bigbang",
        "url": "http://vmus.co/宅男行不行生活大爆炸-the-big-bang-theory/",
    }, {
        "name": "fresh-off-the-boat",
        "url": "http://vmus.co/fresh-off-the-boat/",
    }, {
        "name": "billions",
        "url": "http://vmus.co/billions/",
    }, {
        "name": "rush-hour",
        "url": "http://vmus.co/rush-hour/",
    }, {
        "name": "dr-ken",
        "url": "http://vmus.co/dr-ken/",
    }, {
        "name": "silicon-valley",
        "url": "http://vmus.co/矽谷群瞎傳硅谷矽谷黑歷史-silicon-valley/",
    }, {
        "name": "berlin-station",
        "url": "http://vmus.co/berlin-station/",
    }, {
        "name": "west-world",
        "url": "http://vmus.co/westworld/",
    }, {
        "name": "pure-genius",
        "url": "http://vmus.co/pure-genius/",
    }, {
        "name": "chance",
        "url": "http://vmus.co/chance/",
    }, {
        "name": "entourage",
        "url": "http://vmus.co/entourage/",
    }, {
        "name": "white-collar",
        "url": "http://vmus.co/雅痞神探貓鼠遊戲妙警賊探-white-collar/",
    }, {
        "name": "hawaii-five-0",
        "url": "http://vmus.co/檀島警騎2-0天堂執法者-hawaii-five-0/",
    }
]

def dump_data(data):
    with open('static/json/shows.json', 'w') as f:
        json.dump(data, f, indent=4, separators=(',', ': '))
    print('data imported')

def get_data():
    with open('static/json/shows.json', 'r') as f:
         data = json.load(f)
         return data
    #
    # with open('shows.json', 'r') as f:
    #     data = json.loads(f.read())
    #     return data

def get_desktop_path():

    # Windows desktop path
    # desktop = os.path.join(os.environ["HOMEDRIVE"], os.environ["HOMEPATH"], "Desktop")

    # Mac desktop path
    desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
    return desktop


def BsRequest(url):
    res = requests.get(url)
    source_code = res.content
    soup = BeautifulSoup(source_code, 'html.parser')
    return soup


def get_latest_episode_url(url):
    show_soup = BsRequest(url)
    latest_episode_url = show_soup.find('span', {'class': 'category_nav_prev'}).a['href']
    print(url)
    return show_soup, latest_episode_url


def get_latest_episode_info(show_soup, latest_episode_url):
    # show_url = show_soup.find('meta', {'property': 'og:url'})['content']
    latest_episode_soup = BsRequest(latest_episode_url)
    latest_episode_name = latest_episode_soup.find('h2', {'class': 'post-title'}).text
    latest_episode_name = latest_episode_name.split('線上看')[0]
    latest_post_time = latest_episode_soup.find('time', {'class': 'entry-date'}).text
    show_image = latest_episode_soup.find('img', {'class': 'attachment-featured_image'})['src']
    print('--------------------------------------------------------')
    print(latest_post_time)

    show_dict = {}
    show_dict['latest_episode_name'] = latest_episode_name
    show_dict['latest_episode_url'] = latest_episode_url
    # show_dict['show_url'] = show_url
    show_dict['latest_post_time'] = latest_post_time
    show_dict['show_image'] = show_image
    return show_dict



def shows_latest_episode(url):
    episodes_soup = BsRequest(url)
    latest_episode_url = episodes_soup.find('span', {'class': 'category_nav_prev'}).a['href']
    episodes_url = episodes_soup.find('meta', {'property': 'og:url'})['content']
    latest_episode_soup = BsRequest(latest_episode_url)
    episode_name = latest_episode_soup.find('h2', {'class': 'post-title'}).text
    episode_name = episode_name.split('線上看')[0]
    post_time_text = latest_episode_soup.find('time', {'class': 'entry-date'}).text
    episode_image = latest_episode_soup.find('img', {'class': 'attachment-featured_image'})['src']
    print('--------------------------------------------------------')
    print(post_time_text)
    # print(episode_name.encode('utf-8'))

    show_dict = {}
    show_dict['episode_name'] = episode_name
    show_dict['latest_episode_url'] = latest_episode_url
    show_dict['episodes_url'] = episodes_url
    show_dict['post_time_text'] = post_time_text
    show_dict['episode_image'] = episode_image
    # print(latest_episode_url)
    return show_dict
    # return(post_time_text, latest_episode_url, episode_name, episode_image, episodes_url)


def update_show_html():
    file_place = os.path.join(get_desktop_path(), 'show.html')
    text_file = open(file_place, "w+")
    text_file.close()

    text_file = open(file_place, "a", encoding='utf-8')
    text_file.write(template.get_template())
    text_file.close()

def get_shows_info_arr():
    # data = get_data()
    data = raw_data
    arr = []

    for show in data:
        show_dict = shows_latest_episode(show['url'])
        print(show['name'])
        show_dict['name'] = show['name']
        arr.append(show_dict)
    return arr


if __name__ == "__main__":
    update_show_html()
    # dump_data(raw_data)
