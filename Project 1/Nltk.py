import string 
import nltk
from nltk.corpus import stopwords
import pyttsx3
from pyttsx3 import engine
from collections import Counter
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer

# print(stopwords.words('english'))  # lists all the english stopwords 
text = open('read.txt' , encoding='utf-8').read()
lowered = text.lower()
cleaned_text = lowered.translate(str.maketrans('','' , string.punctuation))
tokens = nltk.word_tokenize(cleaned_text)
# print(tokens)

stop_words = set(stopwords.words('english'))
final_words = []
for w in tokens:
    if w not in stop_words:
        final_words.append(w)

# print(final_words)

lemma_words = []
for word in final_words:
    word = WordNetLemmatizer().lemmatize(word)
    lemma_words.append(word)

emotion_list = []
with open('emotions.txt' , 'r') as emotions:
    for line in emotions:
        clear_line = line.replace('\n', '').replace(',','').replace("'","").strip()
    
        word,emotion = clear_line.split(':')
        # print(f"word = {word} and emotion = {emotion} ")  
        if word in lemma_words:
            emotion_list.append(emotion)
 
print(emotion_list)

print(emotion_list)
w = Counter(emotion_list)
print(w)

sia = SentimentIntensityAnalyzer()
abc = sia.polarity_scores(cleaned_text)
print(abc)

# Displaying the Overall Sentiment from the read.txt file 

def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    if score['neg'] > score['pos']:
        print("Negative Sentiment")
    elif score['neg'] < score['pos']:
        print("Positive Sentiment")
    else:
        print("Neutral Sentiment")


# Optional part to convert our Results from text to speech 

engine=pyttsx3.init()
"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 100)     # setting up new voice rate

engine.say(abc)
engine.runAndWait()
