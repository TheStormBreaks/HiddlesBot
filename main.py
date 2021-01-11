import discord
import os
import random
client = discord.Client()
from keep_alive import keep_alive
#import firebase_admin
#from firebase_admin import credentials
#from firebase_admin import db
# Get a database reference to our blog.
#ref = db.reference('server/tha-savage-boi')
#cred = credentials.Certificate(')

members = []
passwords = []
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


twh_hello = ['https://tenor.com/view/hi-hello-tom-hiddleston-baby-gif-3566170', 'https://tenor.com/view/oi-morning-darling-hello-good-morning-gif-9628217', 'https://tenor.com/view/hi-wave-tom-hiddleston-hello-couple-gif-7989197', 'https://tenor.com/view/tom-hiddleston-hay-gurl-hi-hey-hello-gif-4563020', 'https://tenor.com/view/tom-hiddleston-wave-hi-gif-13408214', 'https://tenor.com/view/ilove-you-tom-hiddleston-tom-hiddleston-kiss-gif-7527364', ]

twh_quotes = ["Haters never win. I just think that's true about life, because negative energy always costs in the end.", "I don't think anyone, until their soul leaves their body, is past the point of no return", "I'm an eternal realist and the success rate for being an actor is pretty low.", "I was informed yesterday that there's a Twitter account for my laugh. Very hard to get used to things like that. Pretty amazing.", 
"The dream is to keep surprising yourself, never mind the audience.", 
"Never stop. Never stop fighting. Never stop dreaming."]

twh_loki = ['https://tenor.com/view/tom-hiddleston-loki-thor-ragnarok-tom-gif-10179470',
 'https://tenor.com/view/tom-hiddleston-loki-tom-hiddleston-gif-10179468',
 'https://tenor.com/view/tom-hiddleston-loki-thor-tom-hiddleston-gif-10179471', 
 'https://tenor.com/view/tom-hiddleston-loki-thor-ragnarok-tom-gif-10179464', 
 'https://tenor.com/view/tom-hiddleston-loki-tom-hiddleston-gif-10179462', 
 'https://tenor.com/view/tom-hiddleston-loki-gif-7519582', 
 'https://tenor.com/view/tom-hiddleston-laughing-gif-7519592', 
 'https://tenor.com/view/loki-hair-tom-hiddleston-gif-7519604',
 'https://tenor.com/view/tom-hiddleston-quiet-loki-gif-11884544',
 'https://tenor.com/view/tom-hiddleston-loki-gif-10259484', 
 'https://tenor.com/view/tom-hiddleston-loki-gif-10259481', 
 'https://tenor.com/view/loki-tom-hiddleston-gif-10342777', 
 'https://tenor.com/view/tom-hiddleston-loki-gif-10302664', 
 'https://tenor.com/view/loki-ssh-tom-hiddleston-gif-10342815', 
 'https://tenor.com/view/loki-tom-hiddleston-gif-10342834', 
 'https://tenor.com/view/tom-hiddleston-loki-gif-10347762',
 'https://tenor.com/view/tom-hiddleston-loki-gif-10347813', 
 'https://tenor.com/view/tom-hiddleston-loki-gif-10347822', 
 'https://tenor.com/view/tom-hiddleston-loki-gif-10349035', 
 'https://tenor.com/view/tom-hiddleston-loki-gif-8798528', 
 'https://tenor.com/view/loki-tom-hiddleston-thor-gif-9423972', 
 ]

twh_hal = ['https://tenor.com/view/tom-hiddleston-loki-tom-hiddleston-hollowcrown-gif-8152100', 'henry',
'https://tenor.com/view/loki-thor-tom-hiddleston-gif-10179330',
'https://tenor.com/view/tom-hiddleston-loki-shakespeare-gif-8528200',
'https://tenor.com/view/tom-hiddleston-gif-7446420',
'https://tenor.com/view/tom-hiddleston-tom-hiddleston-loki-gif-7446380'
'https://tenor.com/view/tom-hiddleston-tom-hiddleston-loki-gif-7446388',
'https://tenor.com/view/tom-hiddleston-tom-hiddleston-loki-gif-7446392', 
]

twh_thomas = ['https://tenor.com/view/loki-tom-hiddleston-tom-hiddleston-sleeping-gif-7272192', 
'https://tenor.com/view/tom-hiddleston-thinking-gif-12487329',
'https://tenor.com/view/tom-hiddleston-hot-tom-hiddleston-loki-gif-5456318', 
'https://tenor.com/view/tom-hiddleston-hot-tom-hiddleston-loki-gif-5456318',
'https://giphy.com/gifs/britbox-bbc-classic-cranford-cmNZKzeAlJIQzss2Cg'
'https://giphy.com/gifs/tom-hiddleston-crimson-peak-sir-thomas-sharpe-1dLROJOsvm9xMPQCzv', ]

twh_pine = [
  'https://tenor.com/view/tom-hiddleston-phew-smile-gif-7248309', 'https://tenor.com/view/tom-hiddleston-nom-yum-gif-7248312', 
  'https://tenor.com/view/running-tom-hiddleston-gif-5191226',
  'https://giphy.com/gifs/bbc-one-bbc1-3o7TKM85ozNN4s6pIA'
  'https://giphy.com/gifs/bbc-one-bbc1-3oz8xyUMBzd1GQf8aI'
  'https://giphy.com/gifs/bbc-one-bbc1-l3vRbqMFRpDlzXNlK'
  'https://giphy.com/gifs/reaction-8PsbM0OpqPl9OClfSw',
  'https://giphy.com/gifs/bbc-one-bbc1-l3vRjE70VBIn8hnRS'
  'https://giphy.com/gifs/bbc-one-bbc1-3o7TKnAtkb5Y4ZvPKU' ]

twh_twh = ['https://tenor.com/view/tom-hiddleston-cranford-return-to-cranford-bbc-britbox-gif-13992228', 
'https://tenor.com/view/hiddleston-tom-hiddleston-gif-9192394', 'https://tenor.com/view/tom-hiddleston-gif-7446430', 
'https://tenor.com/view/tom-hiddleston-dancing-dance-man-dancing-tom-hiddleston-dancing-gif-12004527',
'https://giphy.com/gifs/tom-hiddleston-deal-with-it-goofy-ZRX5APU39mHq8', 
'https://giphy.com/gifs/tom-hiddleston-deal-with-it-and-no-you-dont-have-to-credit-me-UokoSTIh4U1cQ',
'https://tenor.com/view/tom-hiddleston-gif-7446414', 'https://tenor.com/view/tom-hiddleston-gif-7446422',
'https://tenor.com/view/tom-hiddleston-gif-8462711', 
'https://tenor.com/view/tom-hiddleston-gif-8462710', 
'https://tenor.com/view/tom-hiddleston-gif-8185714', 
'https://tenor.com/view/loki-tom-hiddleston-ehehehehe-tom-hiddleston-gif-5954631', 
'https://tenor.com/view/loki-tom-hiddleston-tom-hiddleston-ehehehehe-gif-5954635', 
'https://tenor.com/view/tom-hiddleston-tom-hiddleston-loki-gif-7446404', 
'https://giphy.com/gifs/goldenglobes-3oz8xLfjsVb8WCtZm0', 
'https://tenor.com/view/tom-hiddleston-tom-hiddleston-loki-gif-7446391', 
'https://tenor.com/view/tom-hiddleston-tom-hiddleston-loki-gif-7446408', 
'https://tenor.com/view/tom-hiddleston-tom-hiddleston-loki-gif-7446394', 
'https://tenor.com/view/tom-hiddleston-tom-hiddleston-loki-gif-7519589', 
'https://tenor.com/view/tom-hiddleston-tom-hiddleston-loki-gif-7519599', 
'https://tenor.com/view/tom-hiddleston-cute-loki-glasses-gif-5129820', 
'https://tenor.com/view/bleh-funny-reaction-tom-hiddleston-gif-4751296', 
'https://tenor.com/view/tom-hiddleston-loki-tom-hiddleston-gif-7652072', 
'https://tenor.com/view/funny-adorable-laughing-tom-hiddleston-tom-gif-4751288', 
'https://tenor.com/view/rawr-roar-tom-hiddleston-tom-hiddleston-gif-4751295',
'https://tenor.com/view/tom-hiddleston-loki-amazing-tom-hiddleston-gif-8152154',
'https://tenor.com/view/tom-tom-hiddleston-hiddleston-laugh-haha-gif-7813117', 
'https://tenor.com/view/tom-hiddleston-loki-nope-tom-hiddleston-gif-7835058', 
'https://tenor.com/view/tom-hiddleston-loki-nope-tom-hiddleston-gif-7835061', 
'https://tenor.com/view/tom-hiddleston-laugh-lol-ehehe-gif-3408029', 
'https://tenor.com/view/tom-hiddleston-happy-tom-hiddleston-gif-5129860', 
'https://tenor.com/view/tom-hiddleston-tom-hiddleston-in-charge-boss-gif-7226761', 
'https://tenor.com/view/tom-hiddleston-loki-tom-hiddleston-awesome-gif-8152149', 
'https://tenor.com/view/dance-tom-hiddleston-gif-4912273', 
'https://tenor.com/view/tom-hiddleston-happy-smile-gif-8729199',
'https://tenor.com/view/tom-hiddleston-love-gif-10858364', 
'https://tenor.com/view/tom-hiddleston-sorry-oops-gif-10365845']





@client.event
async def on_message(message):
    if message.author == client.users:
        return

    

    if message.content.startswith('/hello'):
        await message.channel.send(random.choice(twh_hello))
    
    if message.content.startswith('/quotes'):
      await message.channel.send(random.choice(twh_quotes))
     
    if message.content.startswith('/loki'):
      await message.channel.send( random.choice(twh_loki))

    if message.content.startswith('/hal'):
      await message.channel.send( random.choice(twh_hal))

    if message.content.startswith('/thomas'):
      await message.channel.send( random.choice(twh_thomas))

    if message.content.startswith('/twh'):
      await message.channel.send( random.choice(twh_twh))


    if message.content.startswith('/help'):
      await message.channel.send(
      "This bot is solely for Hiddlesfans! The commands are as follows: /twh for gif of Hiddleston")
      
      await message.channel.send("1) /hello for twh hello gif and /quotes for tom's famous dialogues")
      
      await message.channel.send("3) /loki for loki gif")
     
      await message.channel.send("4) /hal for prince henry's gif")
     
      await message.channel.send("5) /thomas for sir sharpe's gif")
     
      


    if message.content.startswith('/pine'):
      await message.channel.send( random.choice(twh_pine))

    if message.content.startswith('/twh'):
      await message.channel.send( random.choice(twh_twh))

  
keep_alive()
client.run(os.getenv('TOKEN'))
