import logging
import re

from gensim.summarization.pagerank_weighted import pagerank_weighted as _pagerank
from gensim.summarization.commons import build_graph as _build_graph
from gensim.summarization.commons import remove_unreachable_nodes as _remove_unreachable_nodes
from gensim.summarization.bm25 import get_bm25_weights as _bm25_weights
from gensim.summarization.summarizer import _build_corpus, _format_results, _extract_important_sentences, summarize_corpus
from gensim.corpora import Dictionary

from .cleaner import clean_text_by_sentences as _clean_text_by_sentences
from .get_sentences import get_extracted_number,get_sentence_from_number

INPUT_MIN_LENGTH = 10

WEIGHT_THRESHOLD = 1.e-3

logger = logging.getLogger(__name__)



def summarize(text, ratio=0.2, word_count=None, split=False, omit_placeholders=False):
    """
    This is a improved version of gensim's summarization library. It includes 
    the option to exclude placeholders from summary generation & implemented 
    Stanford's CoreNLP sentence splitter for better sentence splitting 
    performance
    """
    """
    Returns a summarized version of the given text using a variation of
    the TextRank algorithm.
    The input must be longer than INPUT_MIN_LENGTH sentences for the
    summary to make sense and must be given as a string.

    The output summary will consist of the most representative sentences
    and will also be returned as a string, divided by newlines. If the
    split parameter is set to True, a list of sentences will be
    returned.

    The length of the output can be specified using the ratio and
    word_count parameters:
        ratio should be a number between 0 and 1 that determines the
    percentage of the number of sentences of the original text to be
    chosen for the summary (defaults at 0.2).
        word_count determines how many words will the output contain.
    If both parameters are provided, the ratio will be ignored.
    
    split must be set to true if you want the result in list of sentences,
    else the result will be returned in chunk of text

    omit_placeholders is set to true if you want the system to not compute the 
    placeholders: text descriptions in square bracket, i.e. [FORMULA].
    """
    # Gets a list of processed sentences.
    sentences = _clean_text_by_sentences(text)

    # If need to omit [placeholders], delete the [placeholders] first
    if omit_placeholders:
        sentences_list = _format_results(sentences, True)
        sentences_original = list(sentences_list)
        for i in range(len(sentences_list)):
            sentences_list[i] = re.sub(r'\[.*?\]', '', sentences_list[i])
        temp_sentences = ' '.join(sentences_list)
        sentences = _clean_text_by_sentences(temp_sentences)
    
    # If no sentence could be identified, the function ends.
    if len(sentences) == 0:
        logger.warning("Input text is empty.")
        return ""

    # If only one sentence is present, the function raises an error (Avoids ZeroDivisionError).
    if len(sentences) == 1:
        logger.warning("input must have more than one sentence")
        return ""
    
    # Warns if the text is too short.
    if len(sentences) < INPUT_MIN_LENGTH:
        logger.warning("Input text is expected to have at least " + str(INPUT_MIN_LENGTH) + " sentences.")

    corpus = _build_corpus(sentences)

    most_important_docs = summarize_corpus(corpus, ratio=ratio if word_count is None else 1)

    # Extracts the most important sentences with the selected criterion.
    extracted_sentences = _extract_important_sentences(sentences, corpus, most_important_docs, word_count)

    # Sorts the extracted sentences by apparition order in the original text.
    extracted_sentences.sort(key=lambda s: s.index)

    # If omit_placeholders set to true, after processing replace back to original to preserve the [placeholders]
    if omit_placeholders:
        extracted_sentences = _format_results(extracted_sentences, False)
        sentences_list = '\n'.join(sentences_list)
        sentences_original = '\n'.join(sentences_original)
        extracted_sentences_number = get_extracted_number(extracted_sentences, sentences_list) 
        print(extracted_sentences_number)
        extracted_sentences = get_sentence_from_number(extracted_sentences_number, sentences_original)
        if split:
            return extracted_sentences
        else:
            return '\n'.join(extracted_sentences)
    else:
        return _format_results(extracted_sentences, split)