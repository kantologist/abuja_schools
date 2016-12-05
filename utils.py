import urllib

url = 'http://www.finelib.com/cities/abuja/education'
base_url = 'http://www.finelib.com'

school_types = ['pre-school',
                'private-tutoring',
                'international-schools',
                'nursery-and-kindergarten',
                'primary-schools',
                'secondary-schools',
                ]

def next_page(type):
        new_url = url + "/%s" % (type)
        return new_url
