#importing necessary packages
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
import sys
import collections
import string
import contractions

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

#global variables 
acceptedArguments = ["--lower", "--upper", "--stem", "--stop", "--lemm", "--cont"]
stopWords = set(stopwords.words('english'))
punctuation = string.punctuation + '\u2018\u2019\u201A\u201B\u201C\u201D\u201E\u201F'
#name of textfile for processing
textFile = sys.argv[1]

#all the processing arguments specified
arguments = sys.argv[2:]

#check all the arguments entered are valid
if not set(arguments).issubset(set(acceptedArguments)):
    print("ERROR invalid arguments")
    print("available arugments:")
    print("--lower: make all characters lower case")
    print("--upper: make all characters upper case")
    print("--stem: stemming")
    print("--stop: remove stop words")
    print("--lemm: lemmatization")
    print("--cont: expand contractions")
    exit()

#open text file and store the contents in a variable
textFile = open(textFile, mode = "r", encoding="utf-8")
corpus = textFile.read()
textFile.close()

#if '--cont' was passed as an arugment, it will be exectued first
if '--cont' in arguments:
    corpus = contractions.fix(corpus)

#the text is split into sentence. Each line is considered a sentence
lines = corpus.splitlines()

words = []
for line in lines:

    #if the line has hyphens they will be removed and replaced with spaces
    line = line.replace('-', ' ')
    line = line.split()

    #remove punctuation
    line = [word.translate(str.maketrans(' ', ' ', punctuation)) for word in line]

    #add the words to the larger list
    words.extend(line)
#applying operations
for argument in arguments:
    if argument == '--lower':
        words = [word.lower() for word in words]
    elif argument == '--upper':
        words = [word.upper() for word in words]
    elif argument == '--stop':
        words = [word for word in words if word not in stopWords]
    elif argument == '--stem':
        ss = SnowballStemmer("english")
        words = [ss.stem(word) for word in words]
    elif argument == '--lemm':
        wnl = WordNetLemmatizer()
        words = [wnl.lemmatize(word) for word in words]


#store the tokens in a collection and find the frequency of each token
uniqueTokens = collections.defaultdict(int)
for word in words:
    uniqueTokens[word] += 1

#sort the frequencies from largest to slowest
uniqueTokens = sorted(uniqueTokens.items(), key = lambda x:x[1], reverse= True)

#print the tokens and their frequency
for token in uniqueTokens:
    print(token[0], token[1])
