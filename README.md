# Gensim Summarization Extension
Python library to extend gensim's *summarization* library

## Features
* Replaced gensim's own regex based sentence splitter with Stanford CoreNLP sentence splitter
* Added functions to get sentence number chosen by the summarizer & replace back sentences using the sentence number
* Added summarizer parameter to give user option to ignore placeholders element inside squarebrackets, i.e. [FORMULA], when calculating sentences scores

## Installation
1. Install Python 3
2. Install setuptools
3. Install dependencies
    ''' pip install requirements.txt '''