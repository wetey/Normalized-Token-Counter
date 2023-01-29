# Normalized Token Counter

Simple normalized token counter with Python. </br>

## Description 
This tool normalises text and outputs the frequency of each token. One word is one token, and the punctuation is removed during processing.
There are eight normalizers to choose from:
1. Lower casing
2. Upper casing
3. Stopword removal
4. Stemming
5. Lemmatization
6. Expand contractions

## Setup

### Prerequisites
Before running the program make sure the Contractions package is installed. </br>
To install:
```bash
pip install contractions
```

### To run
Download the token_counter.py file and run the command below:
```
python token_counter.py <path to txt file> <arguments>
```
Available arugments:
1. --lower -> lower casing
2. --upper -> upper casing
3. --stop -> stopword removal
4. --stem -> stemming
5. --lemm -> lemmatization
6. --cont -> expand contractions

## Examples

### Command 
Normalises text by lowercasing all the character, stemming, and expanding contraction.
```bash
python token_counter.py "test.txt" --lower --stem --cont
```

### Input
Text is from the book "Little Women"
```
"Christmas won't be Christmas without any presents," grumbled Jo, lying
on the rug.
```

### Output 
```
christma 2
will 1
not 1
be 1
without 1
ani 1
present 1
grumbl 1
jo 1
lie 1
on 1
the 1
rug 1
```

### Command
Normalises text by lowercasing all the character, removing stopwords, and lemmatizing.
```bash
python token_counter.py "test.txt" --lower --stop --lemm   
```

### Input

Text is from the book "Little Women"
```
"We've got father and mother and each other," said Beth contentedly,
from her corner.
```

### Output 
```
weve 1
got 1
father 1
mother 1
each 1
said 1
beth 1
contentedly 1
her 1
corner 1
```


