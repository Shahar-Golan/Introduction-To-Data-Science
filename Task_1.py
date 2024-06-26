import pandas as pd
import collections
import matplotlib.pyplot as plt
import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')


def load_data(filepath, encoding='Windows-1252'):
    return pd.read_csv(filepath, encoding=encoding)


# count how many valid words exists in the data
def count_words(text_series, min_word_length=1):
    word_counts = collections.Counter()
    total_valid_words = 0
    for tokens in text_series:
        valid_words = [word for word in tokens if word.isalpha() and len(word) >= min_word_length]
        total_valid_words += len(valid_words)
        word_counts.update(valid_words)
    return word_counts, total_valid_words


# find the top 10 most common words
def get_top_words(word_counts, total_valid_words, top_n=10):
    """Calculate probabilities for the top N words."""
    top_words = word_counts.most_common(top_n)
    probabilities = [(word, count / total_valid_words) for word, count in top_words]
    return probabilities


# plot function to visualize the data
def plot(words, probabilities, title):
    """Plot the word frequencies with matplotlib."""
    plt.figure(figsize=(10, 6))
    colors = ['red', 'green', 'blue', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']
    bars = plt.bar(words, probabilities, color=colors[:len(words)])
    plt.xlabel('Words')
    plt.ylabel('Probability')
    plt.title(title)

    # Adding decimal probability labels above bars with six decimal places
    for bar, prob in zip(bars, probabilities):
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, f'{prob:.6f}', ha='center', va='bottom')
    plt.show()


# all the functions above are implementing simply their name.
def apply_tokenization(text_series):
    tokenized_data = [word_tokenize(text) for text in text_series]
    return tokenized_data


def remove_stopwords(text):
    """Remove stopwords from a list of tokenized texts."""
    stop_words = set(stopwords.words('english'))
    filtered_texts = [[word for word in tokens if word.lower() not in stop_words] for tokens in text]
    return filtered_texts


def apply_case_folding(text):
    lower_cased_texts = [[word.lower() for word in tokens] for tokens in text]
    return lower_cased_texts


def apply_stemming(text):
    stemmer = PorterStemmer()
    stemmed_texts = [[stemmer.stem(word) for word in tokens] for tokens in text]
    return stemmed_texts


def apply_lemmatization(text):
    lemma = WordNetLemmatizer()
    lemma_texts = [[lemma.lemmatize(word) for word in tokens] for tokens in text]
    return lemma_texts


def prepare_variables(text, title):
    word_counts, total_valid_words = count_words(text)
    probabilities = get_top_words(word_counts, total_valid_words, top_n=10)
    words, probs = zip(*probabilities)
    plot(words, probs, title)


# clean the data from special characters
def clean_text(text_series):
    # Replace HTML entities and other common artifacts
    cleaned_series = text_series.apply(lambda x: re.sub(r'&\w+;', '', x))  # Removes HTML entities like &quot;
    cleaned_series = cleaned_series.apply(lambda x: x.replace('&quot;', '"'))  # Replace specific HTML entity patterns
    cleaned_series = cleaned_series.apply(lambda x: re.sub(r'@[A-Za-z0-9_]+', '', x))  # Remove usernames
    cleaned_series = cleaned_series.apply(lambda x: re.sub(r'http\S+', '', x))  # Remove URLs
    cleaned_series = cleaned_series.apply(lambda x: re.sub(r'[^A-Za-z0-9 ]', '', x))  # Remove special characters
    return cleaned_series


def main():
    # Load the data
    file_path = r"C:\Users\Administrator\PycharmProjects\DS_HW2\Train.csv"
    df = pd.read_csv(file_path, encoding='Windows-1252')

    # Clean text data
    df['SentimentText'] = clean_text(df['SentimentText'])

    # Tokenize the text
    after_tokenize = apply_tokenization(df['SentimentText'])

    # Remove stopwords
    after_stop_words = remove_stopwords(after_tokenize)

    # Apply case folding
    after_case_folding = apply_case_folding(after_stop_words)

    # Apply stemming
    after_stemming = apply_stemming(after_case_folding)

    # Remove stopwords
    after_lemmatization = remove_stopwords(after_stemming)

    # prepare_variables(after_tokenize, "Chart After Tokenization")
    # prepare_variables(after_stop_words, "Chart After Stop Words Removal")
    # prepare_variables(after_case_folding, "Chart After Case Folding")
    # prepare_variables(after_stemming, "Chart After Stemming")
    # prepare_variables(after_lemmatization, "Chart After Lemmatization")


if __name__ == '__main__':
    main()
