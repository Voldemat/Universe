import datetime

from ..utils import get_image_by_url

class UserData:
    test_photo_url = 'https://www.cnet.com/a/img/-e95qclc6pwSnGE2YccC2oLDW_8=/1200x675/2020/04/16/7d6d8ed2-e10c-4f91-b2dd-74fae951c6d8/bazaart-edit-app.jpg'
    
    test_photo = get_image_by_url(test_photo_url)

    test_birth_date = datetime.date.today().strftime('%Y-%m-%d')

    test_about_me = 'Albert Einstein \
    (14 March 1879 – 18 April 1955) was a German-born theoretical physicist,[5] widely \
    acknowledged to be one of the greatest physicists of all time. \
    Einstein is known for developing the theory of relativity,\
     but he also made important contributions to the development \
     of the theory of quantum mechanics. Relativity and quantum \
     mechanics are together the two pillars of modern physics.'
