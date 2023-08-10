from nltk.corpus import stopwords
engStopWords = stopwords.words('english')

from nltk import WordNetLemmatizer, PorterStemmer
lemmatizer=WordNetLemmatizer()

import regex as re

def open_hour_fix(x): 
    """
    fix user inputted open hours outside of 7am and 7pm (opening hours)
    """
    # before 7 AM
    if x < 7: 
        return x + 12 
    # after 7 PM
    elif x > 19:
        return x - 12
    else:
        return x

def del_punct(text):
    """delete punctuation"""
    punct = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    new_text = ''
    for char in text:
        if char not in punct:
            new_text += char
        else:
            new_text += " "
    return new_text

def lowercase(text):
    """lower case text"""
    text=text.lower()
    return text


def del_stopWords(text):
    """deletes stop words"""
    word_list = text.split()
    text = " ".join([word for word in word_list if word not in engStopWords])
    return text

def lem_text(text):
    """lemmatize words, removing plural"""
    word_list = text.split()
    text = " ".join([lemmatizer.lemmatize(word) for word in word_list])
    return text


def remove_specific(text):
    """removing common words"""
    text = text.replace('please', '')
    text = text.replace('you', '')
    text = text.replace('thank', '')
    text = text.replace('dozen', '')
    text = text.replace('order', '')

    """spelling and plurals"""
    text = text.replace('doughnut', 'donut')
    text = text.replace('donuts', 'donut')
    text = text.replace('pies', 'pie')
    text = text.replace('muffins', 'muffin')
    text = text.replace('empanadas', 'empanada')
    text = text.replace('enseymada', 'ensaymada')
    text = text.replace('biscuits', 'biscuit')
    text = text.replace('tarts', 'tart')
    text = text.replace('cooky', 'cookie')

    """for vectorizing to match"""
    text = text.replace(r'\b(cup)\b', 'cupcake ')
    text = text.replace('loaf', 'loaf bread ')
    text = text.replace('boston', 'boston donut ')
    text = text.replace('dipped', 'dipped donut ')
    text = text.replace('jelly', 'jelly donut ')
    text = text.replace('dutchies', 'dutchie ')
    text = text.replace('chicken', 'chicken empanada ')
    text = text.replace('pork', 'pork empanada ')
    text = text.replace('spinach', 'spinach empanada ')
    return text

def remove_digits(text):
    text_noNum = re.sub(r'\d+', '', text)
    return text_noNum

def preprocess_text(text):
    """combines all pre-processing to one"""
    text = lowercase(text)
    text = del_punct(text)
    text = remove_digits(text)
    text = del_stopWords(text)
    text = lem_text(text)
    text = remove_specific(text)
    # text = stem_text(text)
    text_noSpace = re.sub(r'\s+', ' ', text).strip()
    return text_noSpace