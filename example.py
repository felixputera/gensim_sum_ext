from gensim.summarization import keywords

from gensim_sum_ext.summarizer import summarize, get_title


with open('./test_data/book7 - original/1420.txt', encoding="utf8") as opened_txt:
    to_be_summarized = opened_txt.read()

print(to_be_summarized)
print('\n')
print('Title:' + get_title(to_be_summarized))
print('\n')
print(summarize(to_be_summarized, ratio=0.2, omit_placeholders=True))
print('\n')
print('Keywords: \n' + keywords(to_be_summarized, words = 4, pos_filter=['NN']))
