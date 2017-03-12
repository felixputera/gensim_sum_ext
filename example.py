from gensim.summarization import keywords

from summ.summarizer import summarize, get_title


with open('example.txt', encoding="utf8") as opened_txt:
    to_be_summarized = opened_txt.read()

print(to_be_summarized)
print('\n')
print('Title:' + get_title(to_be_summarized))
print('\n')
print(summarize(to_be_summarized, ratio=0.1, omit_placeholders=True))
print('\n')
print('Keywords: \n' + keywords(to_be_summarized, words = 4, pos_filter=['NN']))
