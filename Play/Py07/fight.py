"""
Write a Python function fight(heroes, villain) that, given a list of heroes and a villain, checks if the good side can prevail. Each hero in the list has a set of properties stored in a dictionary: name, health, category and score (number of victories). The villain has a similar structure, but does not record his score. The fight occurs within the following set of restrictions:

    The villain only fights heroes of the same category as him.
    The villain fights the heroes in the order they appear in the list.
    In a hero versus villain fight, the winner is the one with bigger health (in case of a tie, hero wins). If the villain wins, diminish his health by half of the hero's health.
    The fight ends when the villain dies or there are no more heroes.

The function should return a properly formatted string according to the fight result (hero or villain win), respectively:

<h> defeated the villain and now has a score of <s>

or

<v> prevailed with <hp>HP left

where <h> is the name of the hero that (finally) defeated the villain, <s> his updated score, <v> the name of the villain and <hp> his final remaining health (a decimal rounded to 1 decimal point).

For example:

    fight([{'name': 'Genos', 'health': 3000, 'category': 'S', 'score': 0}, {'name': 'Blizzard of Hell', 'health': 1000, 'category': 'B', 'score': 0}, {'name': 'Saitama', 'health': 9001, 'category': 'C', 'score': 0}, {'name': 'King', 'health': 3750, 'category': 'S', 'score': 1}], {'name': 'Hero Killer', 'health': 4000, 'category': 'S'}) returns the string: King defeated the villain and now has a score of 2
    fight([{'name': 'Genos', 'health': 3000, 'category': 'S', 'score': 0}, {'name': 'Blizzard of Hell', 'health': 1000, 'category': 'B', 'score': 0}, {'name': 'Saitama', 'health': 9001, 'category': 'C', 'score': 0}, {'name': 'King', 'health': 2000, 'category': 'S', 'score': 1}], {'name': 'Hero Killer', 'health': 4000, 'category': 'S'}) returns the string: Hero Killer prevailed with 1500.0HP left

"""

def fight(heroes, villain):
    defeated = False
    for hero in heroes:
        if hero['category'] == 'S':
            if hero['health'] >= villain['health']:
                return "{0} defeated the villain and now has a score of {1}".format(hero['name'], hero['score'] + 1)
            else:
                villain['health'] -= hero['health'] / 2
    return "{0} prevailed with {1}HP left".format(villain['name'], round(villain['health']/1.0, 1))
