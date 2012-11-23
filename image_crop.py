import Image
import random
import pymongo
import bson
import StringIO
import requests

db = pymongo.Connection()
pics = db.sigs.pics


def get_section(content, size):
    """saves out a fucking section of an image file of the passed in image filename & dimensions"""
    image = Image.open(content)
    # gets the max coordinates we could be
    maxCoords = (image.size[0] - size[0], image.size[1] - size[1])
    # get random coordinates up to max
    randCoords = (random.randint(0, maxCoords[0]), random.randint(0, maxCoords[1]))
    # create cropped region
    region = (randCoords[0], randCoords[1], randCoords[0] + size[0], randCoords[1] + size[1])
    # create brand new image from region
    newImage = image.crop(region)
    # save out image
    buf = StringIO.StringIO()
    newImage.save(buf, format="PNG")
    pics.insert({
        'rand': random.random(),
        'img': bson.binary.Binary(buf.getvalue())
    })

thing = "http://i625.photobucket.com/albums/tt338/candlelight-demise/Horses/Horses.png"

r = requests.get(thing)

content = StringIO.StringIO(r.content)
get_section(content, (325, 60))
