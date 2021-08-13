#from nltk import book


from nltk.corpus import gutenberg
from nltk.corpus.reader import *
from nltk.corpus.util import LazyCorpusLoader
import nltk.data
from nltk.tokenize import *

from nltk.corpus.reader.util import *
from nltk.corpus.reader.api import *


class CustomReader(PlaintextCorpusReader):
    def __init__(
        self,
        root,
        fileids,
        word_tokenizer=WordPunctTokenizer(),
        sent_tokenizer=nltk.data.LazyLoader("tokenizers/punkt/english.pickle"),
        para_block_reader=read_blankline_block,
        encoding="utf8",
    ):
        super().__init__(root,
            fileids,
            word_tokenizer,
            sent_tokenizer,
            para_block_reader,
            encoding
            )

loader = LazyCorpusLoader(
    "gutenberg", CustomReader, r"(?!\.).*\.txt", encoding="latin1"
)

print(max(loader.sents("austen-sense.txt"), key = lambda x: len(x)))


#if any(i in x[-1] for i in ['.', '!', '?']) else 0