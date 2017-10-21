#!/usr/bin/python
# -*- coding: utf-8 -*-

'''

    Tudo testa sua fé
    Se treme tu entrega o jogo
    Então levanta as taça nego, eô
    Que isso aqui merece um brinde, eô
    Sei que distante até que tô
    Vi que cê mirou em mim e errou

                    The Cypher MURK! - Costa Gold
'''

import re
from urllib import request


# Base class for working with profiles

class Profile(object):
    # Method for obtaining numeric id of a specified profile (url)
    @staticmethod
    def getId(profileurl: str = 'https://www.fb.com/rique.dev'):

        # Let's split the URL into smaller parts to validate (since mobile links do not work with the preg below)
        parts = profileurl.split('.', 1)
        part_p = parts[0].split('//')

        #  If it's less than two parts, we know it's not a valid URL.
        if len(part_p) < 2:
            print('Invalid URL!')
            exit(0)
        else:
            # If there are any items in the url, we will correct it
            if part_p[1] in ['m']:  # <== Items

                # Fixed URL
                profileurl = 'https://www.' + parts[1]

        # Items confirmed as "valid"
        valid_items = []

        # Pattern
        pattern = '((<meta property=\"al:ios:url\"|\"al:android:url\") ' \
                  'content=\"fb://profile/(.*?)\")|((<meta property=\"al:android:url\")' \
                  ' content=\"fb://page/(.*?)\?)|((meta property=\"al:ios:url\") ' \
                  'content=\"fb://page/\?id=(.*?)\")'

        with request.urlopen(str(profileurl)) as response:

            for item in re.findall(str.encode(pattern), response.read()):

                for sub_item in item:

                    if sub_item.decode().isdigit():
                        valid_items.append(sub_item.decode())

            return valid_items
