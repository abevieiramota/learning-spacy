import pandas as pd

# https://spacy.io/api/annotation#pos-tagging
POS_TAGS = \
{'ADJ': 'adjective',
 'ADP': 'adposition',
 'ADV': 'adverb',
 'AUX': 'auxiliary',
 'CONJ': 'conjunction',
 'CCONJ': 'coordinating conjunction',
 'DET': 'determiner',
 'INTJ': 'interjection',
 'NOUN': 'noun',
 'NUM': 'numeral',
 'PART': 'particle',
 'PRON': 'pronoun',
 'PROPN': 'proper noun',
 'PUNCT': 'punctuation',
 'SCONJ': 'subordinating conjunction',
 'SYM': 'symbol',
 'VERB': 'verb',
 'X': 'other',
 'SPACE': 'space'}
DEP_TAGS = {'acl': 'Clausal modifier of noun',
 'acomp': 'Adjectival complement',
 'advcl': 'Adverbial clause modifier',
 'advmod': 'Adverbial modifier',
 'agent': 'Agent',
 'amod': 'Adjectival modifier',
 'appos': 'Appositional modifier',
 'attr': 'Attribute',
 'aux': 'Auxiliary',
 'auxpass': 'Auxiliary (passive)',
 'case': 'Case marker',
 'cc': 'Coordinating conjunction',
 'ccomp': 'Clausal complement',
 'compound': 'Compound modifier',
 'conj': 'Conjunct',
 'csubj': 'Clausal subject',
 'csubjpass': 'Clausal subject (passive)',
 'dative': 'Dative',
 'dep': 'Unclassified dependent',
 'det': 'Determiner',
 'dobj': 'Direct Object',
 'expl': 'Expletive',
 'intj': 'Interjection',
 'mark': 'Marker',
 'meta': 'Meta modifier',
 'neg': 'Negation modifier',
 'nounmod': 'Modifier of nominal',
 'npmod': 'Noun phrase as adverbial modifier',
 'nsubj': 'Nominal subject',
 'nsubjpass': 'Nominal subject (passive)',
 'nummod': 'Number modifier',
 'oprd': 'Object predicate',
 'parataxis': 'Parataxis',
 'pcomp': 'Complement of preposition',
 'pobj': 'Object of preposition',
 'poss': 'Possession modifier',
 'preconj': 'Pre-correlative conjunction',
 'predet': 'Pre-determiner',
 'prep': 'Prepositional modifier',
 'prt': 'Particle',
 'punct': 'Punctuation',
 'quantmod': 'Modifier of quantifier',
 'relcl': 'Relative clause modifier',
 'root': 'Root',
 'xcomp': 'Open clausal complement'}
MAP_0_1 = {0: '--', 1: 'X'}
COLUMNS = ["Text", "POS", "Dep", "Lemma", "Tag", "Shape", "Alpha", "Stop", "Head", "Left", "Right", "Entity", "EntIOB", "Lemma"]

def doc_to_df(doc):
    
    data = []
    for token in doc:
        
        data.append((token.text, POS_TAGS[token.pos_], token.dep_, token.lemma_, token.tag_, 
                         token.shape_, MAP_0_1[token.is_alpha], MAP_0_1[token.is_stop],
                         token.head.text, token.left_edge.text, token.right_edge.text,
                         token.ent_type_, token.ent_iob_, token.lemma_))
        
    return pd.DataFrame(data, columns=COLUMNS)

def match_results(nlp, doc, pattern):
    
    matcher = Matcher(nlp.vocab)
    matcher.add('pattern', None, pattern)

    for match_id, start, end in matcher(doc):

        string_id = nlp.vocab.strings[match_id]
        span = doc[start:end]

        print(span.text)