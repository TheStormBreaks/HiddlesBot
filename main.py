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
"Never stop. Never stop fighting. Never stop dreaming.", '“I am Loki of Asgard and I am burdened with glorious purpose.” - The Avengers', '“You must be truly desperate to come to me for help.” - Thor: The Dark World', '“There are no men like me.” - The Avengers', '“Enough! You are, all of you are beneath me! I am a god, you dull creature, and I will not be bullied" - The Avengers', "“Is not this simpler? Is this not your natural state? It’s the unspoken truth of humanity that you crave subjugation. The bright lure of freedom diminishes your life’s joy in a mad scramble for power. For identity. You were made to be ruled. In the end, you will always kneel.” - The Avengers", "“I never wanted the throne, I only ever wanted to be your equal.” - Thor", "I didn’t do it for him.” - Thor: The Dark World", "“I guess I’ll have to go it alone. Like I’ve always done.” - Thor: Ragnarok", "“I assure you, brother, the sun will shine on us again.” - Avengers: Infinity War", "“So I am no more than another stolen relic, locked up here until you might have use of me?” - Thor", "“It hurts, doesn’t it? Being lied to. Being told you’re one thing and then learning it’s all a fiction.” - Thor: Ragnarok", "“You will never be a god.” - Avengers: Infinity War", "“I have been falling… for 30 minutes!” - Thor: Ragnarok", "“I thought you said you knew how to fly this thing?” - Thor: The Dark World", "“You know this is wonderful! This a tremendous idea! Let’s steal the biggest, most obvious ship in the universe and escape in that! Flying around the city, smash it into everything in sight and everyone will see it! It’s brilliant, Thor!” - Thor: The Dark World", "“You lied to me! I’m impressed.” - Thor: The Dark World", "“If it’s all the same to you, I’ll have that drink now.” - The Avengers", "Well done, you just decapitated your grandfather!” - Thor: The Dark World", "“I have to get off this planet.” - Thor: Ragnarok", "“Oh, this is much better. Costume’s a bit much… so tight. But the confidence, I can feel the righteousness surging. Hey, you wanna have a rousing discussion about truth, honor, patriotism? God bless America…” - Thor: The Dark World", "“Your savior is here!” - Thor: Ragnarok", "“Oh dear. Is she dead?” - Thor: The Dark World"]

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

twh_hal = ['https://tenor.com/view/tom-hiddleston-loki-tom-hiddleston-hollowcrown-gif-8152100', 
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
      await message.channel.send(random.choice(twh_twh))

    if message.content.startswith('/help'):
        embedVar = discord.Embed(
            title="Hello there.",
            description=
            '''Welcome to HiddlesBot!! Commands for this bot are as follows:
      **/hello** : get Hiddleston hello gifs.
      **/quotes** : get Loki and Hiddleston dialogues.
      **/loki** : Get Loki gif
      **/hal** : Get Hal gif
      **/thomas** : Get Sharpes' gif
      **/twh** : Get Hiddleston gif
      
      ''',
            color=0x00ff00)

        await message.channel.send(embed=embedVar)
      
      


    if message.content.startswith('/pine'):
      await message.channel.send( random.choice(twh_pine))

    

  
keep_alive()
client.run(os.getenv('TOKEN'))
