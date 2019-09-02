
from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

# APIキーの情報

key = "25a941cecd9947a335983de832e9e9f1"
secret = "a104178e860782ff"

#保存フォルダの指定
animalname = sys.argv[1]
savedir = "./" + animalname

def pull_data(photos):
    for i, photo in enumerate(photos['photo']):
        url_q = photo['url_q']
        filepath = savedir + '/' + photo['id'] + '.jpg'
        if os.path.exists(filepath):
            continue
        urlretrieve(url_q,filepath)
        time.sleep(1.2)
        print(photo)

flickr = FlickrAPI(key, secret, format='parsed-json')
# pages = 10
# for page_index in range(1, pages):
#     result = flickr.photos.search(
#         text = animalname,
#         per_page = 500,
#         page = page_index,
#         media = 'photos',
#         sort = 'relevance',
#         safe_search = 1,
#         extras = 'url_q, licence'
#     )
#     photos = result['photos']
#     pull_data(photos)

result = flickr.photos.search(
    text = animalname,
    per_page = 500,
    page = 1,
    media = 'photos',
    sort = 'relevance',
    safe_search = 1,
     extras = 'url_q, licence'
)
photos = result['photos']
pull_data(photos)


