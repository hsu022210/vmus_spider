import requests
from bs4 import BeautifulSoup
import os
import json
import template

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
    },
]

def dump_data(data):
    with open('shows.json', 'w') as f:
        json.dump(data, f, indent=4, separators=(',', ': '))

def get_data():
    with open('shows.json', 'r') as f:
         data = json.load(f)
         return data
    #
    # with open('shows.json', 'r') as f:
    #     data = json.loads(f.read())
    #     return data

def get_desktop_path():
    desktop = os.path.join(os.environ["HOMEDRIVE"], os.environ["HOMEPATH"], "Desktop")
    return desktop


def BsRequest(url):
    res = requests.get(url)
    source_code = res.content
    soup = BeautifulSoup(source_code, 'html.parser')
    return soup


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
    print(episode_name.encode('utf-8'))
    print(latest_episode_url)
    return(post_time_text, latest_episode_url, episode_name, episode_image, episodes_url)


def update_show_html():
    file_place = os.path.join(get_desktop_path(), 'show.html')
    text_file = open(file_place, "w+")
    text_file.close()

    text_file = open(file_place, "a", encoding='utf-8')
    text_file.write(template.get_template())
    text_file.close()


if __name__ == "__main__":
    update_show_html()
    # dump_data(raw_data)
