import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwards
from nltk.stem import PorterStemmer, WordNetLemmatizer
nltk.download('punkt')
nltk.download('stopwards')
nltk.download('wordnet')
text="Natural Language Processing enables machines to understand and process human languages. It is a
      fascinating field with numerous applications, such as chatbots and language translation."
sentences=sent_tokenize(text)
print("\nSentence Tokenization:")
print(sentences)
words=word_tokenize(text)
print("\nWord Tokenization:")
print(words)

stemmer=PorterStemmer()
stemmed_words=[stemmer.stem(word) for word in words]
print("\nAfter Stemming.")
print(stemmed_words)

lemmatizer=WordNetLemmatizer()
lemmatized_words=[lemmatizer.lemmatize(word) for word in words]
print("\nAfter Lemmatization.")
print(lemmatized_words)

stop_words=set(stopwords.words('english'))
filtered_words=[word for word in words if word.lower() not in stop_words]
print("\nAfter Removing stop words.")
print(filtered_words)
