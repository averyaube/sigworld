from random import choice, randrange
from google_search import image_search, link_search
from image_crop import process_image, insert_link
from enchant import Dict
import string
import sys


# generate a random made up word
def random_word():
    length = randrange(2, 9)
    seed = ''.join(choice(string.ascii_lowercase) for x in range(length))
    dic = Dict('en_US')
    words = dic.suggest(seed)
    if len(words) == 0:
        return seed
    else:
        return choice(words)


if __name__ == '__main__':
    for term in [random_word() for x in range(5, 10)]:
        print "Searching " + term
        links = [item['link'] for item in link_search(term)]
        for i in range(0, 5):
            link = choice(links)
            print "Inserting " + link
            insert_link(link)
        pics = [item['link'] for item in image_search(term + " png")]
        for i in range(0, 5):
            pic = choice(pics)
            print "Processing " + pic
            try:
                process_image(pic)
            except Exception as e:
                print "Something bust: ", e
