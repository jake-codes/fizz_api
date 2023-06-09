from flask_restx import Namespace, Resource
from flask.wrappers import Response
from random import randrange

import os
import requests


dns = os.getenv('DNS')
api = Namespace("Traffic", description="A modular namespace within Other API")  # noqa

@api.route("/")
class GenerateResource(Resource):
    """Releases"""

    def get(self):
        """Return 200"""
        print('Generating Traffic')

        baseurl = 'http://{}:8080/api/widget/'.format(dns)
        total_iters = 100

        for i in range(total_iters):
            print('{}/{}'.format(i+1, total_iters))
            rand = randrange(34)
            rand2 = randrange(18)

            # Depending on the random numbers generated, hit different urls
            if rand % 4:
                print('Getting all widgets')
                requests.get(baseurl)
            if rand % 3 and rand2 % 3:
                print('Getting 20 random widgets')
                for j in range(20):
                    rand3 = randrange(800, 1100)
                    requests.get(
                        '{}{}'.format(baseurl,rand3)
                    )
        
        return 'Traffic is currently being generated'