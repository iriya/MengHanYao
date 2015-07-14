__author__ = 'iriyadays@gmail.com'

import tornado.httpclient
import settings
import json


def post(url, param):
    http_client = tornado.httpclient.HTTPClient()
    try:
        request = tornado.httpclient.HTTPRequest(url=settings.CLAN_API_SERVER + url,
                                                 method='POST', headers=settings.CLAN_API_HEADERS,
                                                 body=json.dumps(param))
        response = http_client.fetch(request)
        return json.loads(str(response.body, encoding='UTF-8'))
    except Exception as e:
        print("Error: " + str(e))
    http_client.close()


class ClanApi:
    CLAN_SEARCH = "/json/reply/ClanSearch"
    CLAN = "/json/reply/Clan"
    PLAYER = "/json/reply/Player"

    def search(self, name):
        return post(self.CLAN_SEARCH, {'Tag': '', 'Search': name})

    def clan(self, clan_id):
        return post(self.CLAN, {'Id': clan_id})

    def player(self, play_id):
        return post(self.PLAYER, {'Id': play_id})
