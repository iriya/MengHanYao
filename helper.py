__author__ = 'iriyadays@gmail.com'

import collections


def find_hero_level(player, hero_type):
    result = find(player, 'Heros', 'Type', hero_type)
    if result:
        return result
    else:
        return {'Level': ''}


def find_army_level(player, army_type):
    result = find(player, 'Troops', 'Type', army_type)
    if result:
        return result
    else:
        return {'Level': ''}


def find_spell_level(player, spell_type):
    result = find(player, 'Spells', 'Type', spell_type)
    if result:
        return result
    else:
        return {'Level': ''}


def summary_build_level(player):
    counter = collections.Counter()
    for building in player['Buildings']:
        tmp = dict(building)
        counter.update({"%s%s" % (tmp.get('Type'), tmp.get('Level')): 1})
    return counter


def find_building_level(player, building_type):
    # not for walls
    result = find(player, 'Buildings', 'Type', building_type)
    if result:
        return result
    else:
        return {'Level': ''}


def find(player, key, compare_key, compare_value):
    for obj in player[key]:
        if dict(obj).get(compare_key) == compare_value:
            return obj
    return None


# return 'cochide' if not found, else return ''
def get_if_hide(player, key, compare_key, compare_value):
    result = find(player, key, compare_key, compare_value)
    if result:
        return ''
    else:
        return 'cochide'
