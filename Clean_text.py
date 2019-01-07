### Clean text adn extract unique word_list

import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

stop_words = list(set(stopwords.words('english')))+['']
word_list = []
lemmatizer = WordNetLemmatizer()
def clean(tweet):
    filtered_sentence = []
    tweet = re.sub('[^\x00-\x7F]','',tweet)
    tweet = re.sub('@|#|%|&|\(|\)|\'|!|~|\/|\.|\[|\]|\?|\:|\-|\"|\$|\*','',tweet)
    tweet = re.sub('\d+','',tweet)
    word_tokens = re.split(' |,',tweet)
    filtered_sentence = [lemmatizer.lemmatize(w.lower()) for w in word_tokens if not w in stop_words and not w.isdigit()]
    word_list.extend(filtered_sentence)    
    return ','.join(filtered_sentence)

## tf-idf transformation
unique_word_list = list(set(word_list))
tfidf = TfidfVectorizer(vocabulary=unique_word_list,min_df=1)
X_train=tfidf.fit_transform(df_train['clean_tags'].tolist())
# Transform a document into TfIdf coordinates
X_test = tfidf.transform(df_test['clean_tags'].tolist())