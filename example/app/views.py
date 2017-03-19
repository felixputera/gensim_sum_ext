from flask import render_template, jsonify
from gensim.summarization import keywords
from gensim_sum_ext.summarizer import get_title, summarize

from app import app
from .forms import MainForm
from .process import summary_highlight


@app.route('/', methods=['GET'])
def index():
    form = MainForm()
    return render_template('index.html', form=form)

@app.route('/check', methods=['POST'])
def check():
    form = MainForm()
    if form.validate_on_submit():
        title = get_title(form.text.data)
        keyword = keywords(form.text.data, words=form.keywords_no.data)
        summary = summary_highlight(form.text.data, ratio=form.percentage.data/100,
                                    omit_placeholders=form.rm_placeholders.data)
        return jsonify(data={'summary': '{}'.format(summary), 'title': '{}'.format(title),
                             'keywords': '{}'.format(keyword)})
    return jsonify(data=form.errors)
