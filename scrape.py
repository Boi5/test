from telethon import TelegramClient, events
from datetime import datetime, timedelta, timezone
from telethon.network import ConnectionTcpFull
import tweepy
import socks
import os 

import TxtProcess

api_id: int = 26017213
api_hash: str = '9627de4b8f3172991251a1f5b8d09967'

my_id: int = 1433639923

channels_ids= [ 'rtnews', 'vertigo_world_news']#'telegram', 'Alarabiya', 'BBCArabic']

proxy = (socks.SOCKS5, '127.0.0.1', 10808, True)
phone_number = '+963998174915'

client = TelegramClient('anon', api_id=api_id, api_hash=api_hash)

News={}

message_list = []
index = 0

consumer_key= "W1aqpojI0BqYjyZTqFfQ7DfKS"
consumer_secret ="aj334GW0s5ErYxXXEQcXiKRNPqpW5Pt4WbFbNWyOdBQoRJMx8Y"
access_token ="1690789574992158721-LEGZVzA7lCIHgP0BpjUFa9zq8Dsxfu"
access_token_secret ="qQrO1nMehoccABwy1RoxYXhjhXc8N97zlTaDasrAZR0zV"
Bearertoken = r"AAAAAAAAAAAAAAAAAAAAALqsqAEAAAAABuDcQp6RBvglsDMFeIGjJK%2FvCCQ%3DGJqZDdw1q6RhQ05xROAc5CK07BAMEoKG4uN5EoefJjMB7vMxFJ"

 
async def post(text, message=None):
    client = tweepy.Client(bearer_token=Bearertoken, consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)
    auth = tweepy.OAuth1UserHandler(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)

    api = tweepy.API(auth)

    await message.download_media(file='redw.mp4')

    if message :
        media= api.media_upload('redw.mp4')
        client.create_tweet(text=text, media_ids=[media.media_id])
    else:
        client.create_tweet(text=text)

 

@client.on(events.NewMessage(chats = [my_id]))
async def receive_messeges(event):
    global message_list
    global index

    if event.raw_text == "Hi":
        message_list = await get_messages()
        await client.forward_messages(my_id, message_list[index])

    elif event.raw_text == "1":
        text = TxtProcess.remove_debris(message_list[index].raw_text)
        text = TxtProcess.paraphrase(text)
        text = TxtProcess.translate(text)
    
        await post(text,message_list[index])

        index += 1
        await client.forward_messages(my_id, message_list[index])
        
    elif event.raw_text == "2":

        index += 1
        await client.forward_messages(my_id, message_list[index])

    elif event.raw_text == "Stop":
        await client.disconnect()

    else :
        post(event.raw_text)

async def get_messages():
    #me = await client.get_me()
    #print(me.stringify())
    news = {channels_ids[i] : [] for i in range(len(channels_ids))}
    messege_list: list = []
    for channel_id in channels_ids:
        async for messege in client.iter_messages(channel_id, offset_date=datetime.now(tz=timezone.utc) - timedelta(hours=24), reverse=True):
            #messege_list.append(f"t.me/{channel_id}/{messege.id}")
            messege_list.append(messege)
            #print(messege.raw_text)
            #if messege.media:
            #    print("media found")
            #    path = await messege.download_media(f"{messege.text} media")
            #await client.forward_messages("@solozeusbot", messege)


            
        news[channel_id] += messege_list 
        #messege_list.clear()
    return messege_list
    

async def main():
    #phone_number = 963998174915
    #assert await client.connect()
    #if not client.is_user_authorized():
    #    await client.send_code_request(phone_number)
    #    me = await client.sign_in(phone=phone_number)

    await fetch()  


def run():
        with client:
            return 

async def fetch():
    async with client:
        await client.start()
        
        global message_list
        global index
        message_list = await get_messages()

        await client.run_until_disconnected()
        #await client.forward_messages(my_id, News['solozeusbot'][0])



def get_code():
    code = "90225"
    return code

#client.start(phone=phone_number)
with client:
    client.loop.run_until_complete(main())
    

