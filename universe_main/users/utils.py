import os

from urllib import request

from django.core.files import File


def get_image_by_url(url:str) -> object:
    response = request.urlretrieve(url)

    image_data = open(response[0])

    image = File(image_data)

    return image

