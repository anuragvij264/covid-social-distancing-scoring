import tweepy,json
from config import CONFIG_PATH
from tweepy import OAuthHandler
import wget
import os
import re
import argparse
from datetime import datetime, timedelta
import configparser
import pandas as pd

from db.queries import engine

def authorize_twitter_api(config):
    auth = OAuthHandler(config['DEFAULT']['consumer_key'], config['DEFAULT']['consumer_secret'])
    auth.set_access_token(config['DEFAULT']['access_token'], config['DEFAULT']['access_secret'])
    return auth

def tweet_media_urls(tweet_status):
  media = tweet_status._json.get('quoted_status', {}).get('extended_entities', {}).get('media', [])

  if (len(media) == 0):
    return []
  else:
    return [item['media_url'] for item in media]

def create_folder(output_folder):
  if not os.path.exists(output_folder):
      os.makedirs(output_folder)


def download(status,num_tweets, output_dir):
    create_folder(output_dir)
    downloaded = 0

    df = pd.DataFrame()


    stop_date = datetime.utcnow() - timedelta(days=1)
    for tweet_status in status:

        image_urls_list = list()
        tweet_urls = list()

        if (downloaded >= num_tweets):
            break

        # if status.created_at < stop_date:
        #     break


        loc = tweet_status.full_text

        tweetId = tweet_status.id

        tweet_url = re.search(r'https:\/\/t.co\/[a-zA-z0-9]+',loc).group()

        loc = re.sub(r'https:\/\/t.co\/[a-zA-z0-9]+','',loc).lower()
        created = tweet_status.created_at.strftime('%d-%m-%y at %H.%M.%S')

        tweet_urls.append(tweet_url)

        print(loc,tweet_url)

        for count, media_url in enumerate(tweet_media_urls(tweet_status)):
            # Only download if there is not a picture with the same name in the folder already

            image_urls_list.append(media_url)
            file_name = "{}_({}).jpg".format(created, count + 1)
            if not os.path.exists(os.path.join(output_dir, file_name)):
                print(media_url)
                wget.download(media_url, out=output_dir + '/' + file_name)
                downloaded += 1

        df=pd.concat([df,pd.DataFrame.from_records({'id':int(tweetId),'district':loc,'image_urls':image_urls_list,"created_at": created,"tweet_url": tweet_url})])

        df.to_sql(name='images2', con=engine, if_exists='append', index=False)


def download_images_by_user(api, username, retweets, replies, num_tweets, output_folder):
  status = tweepy.Cursor(api.user_timeline,
                         screen_name=username, include_rts=retweets,
                         exclude_replies=replies, tweet_mode='extended').items()
  download(status, num_tweets, output_folder)

def download_images_by_tag(api, tag, retweets, replies, num_tweets, output_folder):
  status = tweepy.Cursor(api.search,
                         '#'+tag, include_rts=retweets,
                         exclude_replies=replies, tweet_mode='extended').items()
  download(status, num_tweets, output_folder)

def parse_config(config_file):
  config = configparser.ConfigParser()
  config.read(config_file)
  return config



def main():
    config_file_path =  CONFIG_PATH
    parse_config(config_file=config_file_path)
    config = parse_config(config_file_path)
    auth = authorize_twitter_api(config)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    username = config['BOT']['username']
    retweets =  config['BOT']['retweets']
    replies = config['BOT']['replies']
    num_tweets = int(config['BOT']['num_tweets'])
    output_folder = config['BOT']['output_dir']
    hashtag = False

    if hashtag:
        download_images_by_tag(api, hashtag, retweets, replies, num_tweets, output_folder)
    else:
        download_images_by_user(api, username, retweets, replies, num_tweets, output_folder)


if __name__=='__main__':
    main()
