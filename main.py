# lekir74088@godpeed.com
#tewovam682
import os
if os.path.isfile("path/to/config/tewovam682_uuid_and_cookie.json"):
    os.remove("path/to/config/tewovam682_uuid_and_cookie.json")
from instabot import Bot

bot = Bot()
bot.login(username="tewovam682", password="Admin1234")

USERNAME = bot.search_users('Temirlan Aktay')[0]

user_following = bot.get_user_following(USERNAME)
user_followers = bot.get_user_followers(USERNAME)

total_medias = bot.get_total_user_medias(USERNAME)
twony_last_medias = bot.get_user_medias(USERNAME)

location = []
avr_likers = []
twony_avr_likers = []

if total_medias:
    for i in range(len(total_medias)):
        liked = bot.get_media_likers(total_medias[i])
        avr_likers.append(len(liked))
    avr_likers = sum(avr_likers)/len(avr_likers)

if twony_avr_likers:
    for media in twony_avr_likers:
        liked = bot.get_media_likers(media)
        twony_avr_likers.append(len(liked))
    avr_like = sum(twony_avr_likers)/len(twony_avr_likers)


print('total_avr_likers', avr_likers)
print('twony_avr_likers', twony_avr_likers)
print('following', len(user_following))
print('followers', len(user_followers))
print('media_count', len(total_medias))
print('all_location',
        )
'''print(location['name'], '\n',
      location['address'], '\n',
      location['city'], '\n',
      )
'''
bot.logout()
