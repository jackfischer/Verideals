import requests, json, operator
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

"""The MIT License (MIT)
Copyright (c) [year] [fullname]
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

class SlickObj(object):
    def __init__(self):
        """Read the current JSON dictionary file (if available)
        and add contents to self.d"""
        self.__readFile__()

    def __str__(self):
        return str(self)

    def __repr__(self):
        return self.__str__()

    def __readFile__(self):
        try:
            rf = open('slick_dict.json', 'r')
        except IOError:
            rf = ''

        try:
            self.d = json.load(rf)
        except AttributeError:
            self.d = {}

    def __writeFile__(self):
        wf = open('slick_dict.json', 'w')

        json.dump(self.d, wf)

        wf.close()

    def __dateLimit__(self, x):
        """Used by the top method to select keys and values added
        during a certain time period."""
        date = datetime.today()
        date -= timedelta(x)
        new_dict = {}

        for item in self.d.iteritems():
            if datetime(int(item[1][3][0:4]),int(item[1][3][5:7]),int(item[1][3][8:])) >= date:
                new_dict[item[0]] = item[1]

        return new_dict

    def update(self):
        """Update the JSON dictionary with new frontpage contents"""
        url = 'http://slickdeals.net/'

        r = requests.get(url)

        soup = BeautifulSoup(r.text, 'html.parser')

        deals = soup.find_all(class_ = 'fpGridBox grid  frontpage firedeal') + \
            soup.find_all(class_ = 'fpGridBox grid  frontpage cat')

        for deal in deals:
            postid = deal.find(class_ = 'likes')['data-postid']

        new_list = []

        try:
            self.d[postid]
        except KeyError:
            item = deal.find(class_ = 'priceLine')['title']
            price = deal.find(class_ = 'itemPrice').text.strip().split()[0]
            rating = int(deal.find('span', {'class':'count'}).text.strip())
            date = str(datetime.now())[:10]

            self.d[postid] = (item, price, rating, date)
            new_list.append(item)

        self.__writeFile__()

        print 'New items:'
        for item in new_list:
            print item

    def top(self, x=5, days=15):
        """Prints the description of items with constraints of
        user-defined days and count of items"""
        limited_dict = self.__dateLimit__(days)

        sorted_dict = sorted(limited_dict.iteritems(), key=lambda x: -x[1][2])[:x]

        for item in sorted_dict:
             print item[1][0]

    def search(self, term='', days=15):
        """Search for single-word terms in the item descriptions of each key"""
        new_dict = {}

        if term != '':
            for items in self.d.iteritems():
                ls = items[1][0].split()

                for item in ls:
                    if term.lower() in item.lower():
                        new_dict[items[0]] = items[1]

        for key in new_dict:
            print new_dict[key][0]
