from gensim.summarization.summarizer import _format_results
from gensim_sum_ext.summarizer import summarize
from gensim_sum_ext.get_sentences import get_extracted_number,get_sentence_from_number
from gensim_sum_ext.cleaner import clean_text_by_sentences as _clean_text_by_sentences


def summary_highlight(text, ratio, omit_placeholders):
    sum_text = summarize(text, ratio=ratio, omit_placeholders=omit_placeholders)
    extracted_sentences_number = get_extracted_number(sum_text, text)

    original_sentence_list = _format_results(_clean_text_by_sentences(text), True)
    extracted_sentence_list = _format_results(_clean_text_by_sentences(sum_text), True)

    index = 0
    for i in original_sentence_list:
        try:
            if i == extracted_sentence_list[index]:
                original_index = original_sentence_list.index(i)
                i = '<mark><em>' + i + '</em></mark>'
                original_sentence_list[original_index] = i
                if index < len(extracted_sentence_list)-1:
                    index += 1
        except IndexError:
            pass

    return " ".join(original_sentence_list)
