# Gensim Summarization Extension
Python library to extend gensim's *summarization* library

## Features
* Replaced gensim's own regex based sentence splitter with Stanford CoreNLP sentence splitter
* Added functions to get sentence number chosen by the summarizer & replace back sentences using the sentence number
* Added summarizer parameter to give user option to ignore placeholders element inside squarebrackets, i.e. [FORMULA], when calculating sentences scores

## Installation
1. Make sure you have Python 3 & setuptools installed
2. Install [Stanford CoreNLP](http://stanfordnlp.github.io/CoreNLP/)
3. Install with pip</br> `$ pip install gensim_sum_ext `
4. To use the library, run Stanford CoreNLP </br> `$ java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 50000 `

## (Optional) Running Demo Webpage
1. Navigate to *example* directory</br> `$ cd example `
2. Install pip requirements</br> `$ pip install requirements.txt `
3. Run the webserver</br> `$ python run.py `
4. The webpage will be available in *127.0.0.1:5000*