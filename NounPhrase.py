import nltk
from nltk import Tree
from nltk.stem.wordnet import WordNetLemmatizer

special_words = ['some','all','no','not','n\'t','any','every','each']

grammar =  r"""NP:
{<DT>?<JJ|JJR|VBN|VBG>*<CD><JJ|JJR|VBN|VBG>*<NNS|NN>+}
{<DT>?<JJS><NNS|NN>?}
{<DT>?<PRP|NN|NNS><POS><NN|NNP|NNS>*}
{<DT>?<NNP>+<POS><NN|NNP|NNS>*}
{<DT|PRP\$>?<RB|RBR|RBS>?<JJ|JJR|VBN|VBG>*<NN|NNP|NNS>+}
{<WP|WDT|PRP|EX>}
{<DT><JJ>*<CD>}
{<\$>?<CD>+}"""

chunkParser = nltk.RegexpParser(grammar)
wordnet_lemmatizer = WordNetLemmatizer()

def noun_phrases(sentence):
    '''
    Returns a list with all noun phrases found in the sentence (according to the grammar)
    :param sentence: the sentence from which we want to get the noun phrases
    :return: a list of the noun phrases found in the sentence
    '''
    noun_phrases = []
    tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
    tree = chunkParser.parse(tagged)
    for child in tree:
        if isinstance(child, Tree):
            if child.label() == 'NP':
                full_noun_phrase = ""
                for word in range(len(child)):
                    if len(full_noun_phrase) > 0 and child[word][0] not in special_words:
                        #full_noun_phrase += " " + child[word][0]
                        full_noun_phrase += " " + wordnet_lemmatizer.lemmatize(child[word][0])
                    elif child[word][0] not in special_words:
                        full_noun_phrase = wordnet_lemmatizer.lemmatize(child[word][0])
                noun_phrases.append(full_noun_phrase)
    return noun_phrases

def draw_parse_tree(sentence):
    """
    Draws the parsing tree of the sentence
    :param sentence:  the sentence of which we want to draw the parse tree
    """
    tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
    tree = chunkParser.parse(tagged)
    tree.draw()

def get_grammar_score():
    """
    Prints the score of the grammar. More details available here:
    http://classes.ischool.syr.edu/ist664/NLPFall2014/LabSessionWeek8.10.15.14.pdf
    """
    nltk.download('treebank')
    cp = nltk.RegexpParser(grammar)
    chunkscore = nltk.chunk.ChunkScore()
    for fileid in nltk.corpus.treebank_chunk.fileids()[:5]:
        for chunk_struct in nltk.corpus.treebank_chunk.chunked_sents(fileid):
            test_sent = cp.parse(chunk_struct.flatten())
            chunkscore.score(chunk_struct, test_sent)
    print(chunkscore)


draw_parse_tree("Therefore no wise men are philosophers.")