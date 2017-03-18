from distutils.core import setup
setup(
  name = 'gensim_sum_ext',
  packages = ['gensim_sum_ext'],
  version = '0.1.1',
  install_requires=[
        "gensim",
        "pycorenlp",
    ],
  description = 'Extension for gensim summarization library',
  author = 'Felix Putera',
  author_email = 'felixputera@gmail.com',
  url = 'https://github.com/felixputera/gensim_sum_ext/archive/0.1.1.tar.gz',
  download_url = '',
  keywords = '',
  classifiers = [],
)