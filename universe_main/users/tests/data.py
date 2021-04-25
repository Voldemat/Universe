import datetime

from ..utils import get_image_by_url

user_data = {
    'birth_date':datetime.date.today().strftime('%Y-%m-%d'),

    'about_me':'Albert Einstein \
    (14 March 1879 – 18 April 1955) was a German-born theoretical physicist,[5] widely \
    acknowledged to be one of the greatest physicists of all time. \
    Einstein is known for developing the theory of relativity,\
     but he also made important contributions to the development \
     of the theory of quantum mechanics. Relativity and quantum \
     mechanics are together the two pillars of modern physics.',

    'email':'example@email.com',
    'first_name':'Albert',
    'surname':'Einstein',
    'password':'test_password123',
}