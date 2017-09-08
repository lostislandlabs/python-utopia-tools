import json
import urllib2



def get_sentiment(category, user, articles):
    url = 'https://utopia.cs.manchester.ac.uk/thumbd/{0}/get'.format(str(category))
    query = {
        'user': str(user),
        'articles': [str(article) for article in articles]
    }
    data = json.load(urllib2.urlopen(url, data=json.dumps(query), timeout=8))
    return data



def set_sentiment(category, user, sentiment):
    url = 'https://utopia.cs.manchester.ac.uk/thumbd/{0}/set'.format(str(category))
    query = {
        'user': str(user),
        'sentiment': {str(article): value for article, value in sentiment.items()}
    }
    data = json.load(urllib2.urlopen(url, data=json.dumps(query), timeout=8))
    return data



def unset_sentiment(category, user, articles):
    url = 'https://utopia.cs.manchester.ac.uk/thumbd/{0}/unset'.format(str(category))
    query = {
        'user': str(user),
        'articles': [str(article) for article in articles]
    }
    data = json.load(urllib2.urlopen(url, data=json.dumps(query), timeout=8))
    return data
