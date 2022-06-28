from fileinput import filename
from os import access 
from prompt_toolkit import prompt
import openai, tweepy, random, accessapi, time, train

client = tweepy.Client(consumer_key = accessapi.api_key, consumer_secret= accessapi.api_key_secret, access_token = accessapi.access_token, access_token_secret =accessapi.access_token_secret)
auth = tweepy.OAuthHandler(consumer_key = accessapi.api_key, consumer_secret= accessapi.api_key_secret, access_token = accessapi.access_token, access_token_secret =accessapi.access_token_secret)
openai.api_key = accessapi.openai_api_key

def bot(user_input):
    response = openai.Completion.create(
        engine = "text-davinci-002",
        prompt =  user_input,
        max_tokens = 60,
        temperature=0.5,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )

    text = response.choices[0].text
#    print_quote = quotes.quote
    print(text)

    reply_y_or_n= input("Shall I print the tweet?")
    if reply_y_or_n == 'y':
#        tweet = client.create_tweet(text = text)
        tweet = client.create_tweet(text = text)

        print("Tweet successful!")
    else:
        bot(user_input)


if __name__ == "__main__":
#    prompt = "You: What time is it? \n\n Dorian: "
#    prompt = input('Ask a question : \n')
#    bot(prompt)
     bot('A quote from The Picture of Dorian Gray, by Oscar Wilde, not in quotes')
