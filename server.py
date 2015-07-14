__author__ = 'iriyadays@gmail.com'

import settings
import clanapi
import tornado.ioloop
import tornado.options
import tornado.web
import json
import helper

from tornado.options import define, options
define("port", default=8888, help="run on the given port", type=int)

clan_api = clanapi.ClanApi()


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        clan = clan_api.search("E7VMK")[0]
        players = clan_api.clan(clan['ClanID'])['Players']
        self.render('index.html', clan=clan, players=players)


class PlayHandler(tornado.web.RequestHandler):
    def get(self, player_id):
        player = clan_api.player(player_id)
        # f=open('test.json')
        # player = json.load(f)
        try:
            print(player)
        except UnicodeEncodeError as e:
            player['Name'] = 'Error resolve response'

        self.render('player.html', player=player,
                    find_hero_level=helper.find_hero_level,
                    find_army_level=helper.find_army_level,
                    find_spell_level=helper.find_spell_level,
                    get_if_hide=helper.get_if_hide,
                    summary_build_level=helper.summary_build_level)

app_settings = {
    "template_path": settings.TEMPLATE_PATH,
    "static_path": settings.STATIC_PATH,
}

application = tornado.web.Application([
    (r"/", IndexHandler),
    (r"/player/(.+)", PlayHandler)
], **app_settings)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    application.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
