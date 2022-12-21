# %%
import pathlib
from collections import Counter

import textacy

import spacy
from spacy import displacy
from spacy.language import Language
from spacy.matcher import Matcher
from spacy.tokenizer import Tokenizer

nlp = spacy.load("en_core_web_sm")

# %% Introduction

introduction_text = (
    "This tutorial is about Natural Language Processing in spaCy."
)
introduction_doc = nlp(introduction_text)

# Extract tokens for the given doc
print([token.text for token in introduction_doc])

# %% Reading text from a file instead

file_name = "introduction.txt"
introduction_file_text = pathlib.Path(file_name).read_text()
introduction_file_doc = nlp(introduction_file_text)

# %% Extracting tokens and reading on one line

# Extract tokens for the given doc
print([token.text for token in nlp(pathlib.Path(file_name).read_text())])

# %% Extracting sentences

about_text = (
    "Gus Proto is a Python developer currently"
    " working for a London-based Fintech"
    " company. He is interested in learning"
    " Natural Language Processing."
)
about_doc = nlp(about_text)
sentences = list(about_doc.sents)
len(sentences)

for sentence in sentences:
    print(f"{sentence[:5]}...")

print(type(sentences))

# %% Customizing sentence boundaries


@Language.component("set_custom_boundaries")
def set_custom_boundaries(doc):
    """Adds support to use `...` as the delimiter for sentence detection"""
    for token in doc[:-1]:
        if token.text == "...":
            doc[token.i + 1].is_sent_start = True
    return doc


ellipsis_text = (
    "Gus, can you, ... never mind, I forgot"
    " what I was saying. So, do you think"
    " we should ..."
)

# Load a new model instance
custom_nlp = spacy.load("en_core_web_sm")
custom_nlp.add_pipe("set_custom_boundaries", before="parser")
custom_ellipsis_doc = custom_nlp(ellipsis_text)
custom_ellipsis_sentences = list(custom_ellipsis_doc.sents)
for sentence in custom_ellipsis_sentences:
    print(sentence)

ellipsis_doc = nlp(ellipsis_text)
ellipsis_sentences = list(ellipsis_doc.sents)
for sentence in ellipsis_sentences:
    print(sentence)

# %% Each token has its index position in the original text

for token in about_doc:
    print(token, token.idx)

# %% Each token has various attributes you can use

print(
    f"{'Text with Whitespace':22}"
    f"{'Is Alphanum?':15}"
    f"{'Is Punctuation?':18}"
    f"{'Is Stop Word?'}"
)

for token in about_doc:
    print(
        f"{str(token.text_with_ws):22}"
        f"{str(token.is_alpha):15}"
        f"{str(token.is_punct):18}"
        f"{str(token.is_stop)}"
    )

# %% Customizing the tokenizer to add a custom infix

custom_about_text = (
    "Gus Proto is a Python developer currently"
    " working for a London@based London-based Fintech"
    " company. He is interested in learning"
    " Natural Language Processing."
)

print([token.text for token in nlp(custom_about_text)[8:15]])

custom_nlp = spacy.load("en_core_web_sm")
prefix_re = spacy.util.compile_prefix_regex(custom_nlp.Defaults.prefixes)
suffix_re = spacy.util.compile_suffix_regex(custom_nlp.Defaults.suffixes)

custom_infixes = [r"@"]
# A more complete regex pattern:
# custom_infixes = [r"(?<=[a-zA-Z_])@(?=[a-zA-Z_])"]

infix_re = spacy.util.compile_infix_regex(
    list(custom_nlp.Defaults.infixes) + custom_infixes
)

custom_nlp.tokenizer = Tokenizer(
    nlp.vocab,
    prefix_search=prefix_re.search,
    suffix_search=suffix_re.search,
    infix_finditer=infix_re.finditer,
    token_match=None,
)

custom_tokenizer_about_doc = custom_nlp(custom_about_text)

print([token.text for token in custom_tokenizer_about_doc[8:15]])

# %% The language model includes stop words

spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
len(spacy_stopwords)

for stop_word in list(spacy_stopwords)[:10]:
    print(stop_word)

# %% Words in `about_doc`` that aren't stop words

for token in about_doc:
    if not token.is_stop:
        print(token)

print(list(filter(lambda t: not t.is_stop, about_doc)))

print([token for token in about_doc if not token.is_stop])

about_no_stopword_doc = [token for token in about_doc if not token.is_stop]
print(about_no_stopword_doc)

# %% Lemmas and lemmatization

conference_help_text = (
    "Gus is helping organize a developer"
    " conference on Applications of Natural Language"
    " Processing. He keeps organizing local Python meetups"
    " and several internal talks at his workplace."
)
conference_help_doc = nlp(conference_help_text)
for token in conference_help_doc:
    if str(token) != str(token.lemma_):
        print(f"{str(token):>20} : {str(token.lemma_)}")

# %% Making use of stop words to count words that aren't stop words

complete_text = (
    "Gus Proto is a Python developer currently"
    " working for a London-based Fintech company. He is"
    " interested in learning Natural Language Processing."
    " There is a developer conference happening on 21 July"
    ' 2019 in London. It is titled "Applications of Natural'
    ' Language Processing". There is a helpline number'
    " available at +44-1234567891. Gus is helping organize it."
    " He keeps organizing local Python meetups and several"
    " internal talks at his workplace. Gus is also presenting"
    ' a talk. The talk will introduce the reader about "Use'
    ' cases of Natural Language Processing in Fintech".'
    " Apart from his work, he is very passionate about music."
    " Gus is learning to play the Piano. He has enrolled"
    " himself in the weekend batch of Great Piano Academy."
    " Great Piano Academy is situated in Mayfair or the City"
    " of London and has world-class piano instructors."
)

complete_doc = nlp(complete_text)
# Remove stop words and punctuation symbols
words = [
    token.text
    for token in complete_doc
    if not token.is_stop and not token.is_punct
]
word_freq = Counter(words)
# 5 commonly occurring words with their frequencies
common_words = word_freq.most_common(5)
print(common_words)

# Unique words
unique_words = [word for (word, freq) in word_freq.items() if freq == 1]
print(unique_words)

# %% What the same count would look like with stop words included

words_all = [token.text for token in complete_doc if not token.is_punct]
print(
    Counter(
        [token.text for token in complete_doc if not token.is_punct]
    ).most_common(5)
)

# %% Part-of-speech tagging

for token in about_doc[:5]:
    print(
        f"""
        TOKEN: {str(token)}
        =====
        TAG: {str(token.tag_):10} POS: {token.pos_}
        EXPLANATION: {spacy.explain(token.tag_)}"""
    )

# %% Categorizing words based on their POS

nouns = []
adjectives = []
for token in about_doc:
    if token.pos_ == "ADJ":
        adjectives.append(token)

    elif token.pos_ == "NOUN":
        nouns.append(token)

print(f"{nouns = }")

print(f"{adjectives = }")

# %% Using displaCy to visualize text structure

# Windows server needs to be manually changed to 127.0.0.1

about_interest_text = (
    "He is interested in learning Natural Language Processing."
)
about_interest_doc = nlp(about_interest_text)
displacy.serve(about_interest_doc, style="dep")

# %% Displaying in a Jupyter notebook instead

displacy.render(about_interest_doc, style="dep", jupyter=True)

# %% Preprocessing functions


def is_token_allowed(token):
    """
    Only allow valid tokens which are not stop words
    and punctuation symbols.
    """
    return bool(
        token
        and str(token).strip()
        and not token.is_stop
        and not token.is_punct
    )


def preprocess_token(token):
    # Reduce token to its lowercase lemma form
    return token.lemma_.strip().lower()


complete_filtered_tokens = [
    preprocess_token(token)
    for token in complete_doc
    if is_token_allowed(token)
]

print(complete_filtered_tokens)

# %% Rule-based matching

matcher = Matcher(nlp.vocab)


def extract_full_name(nlp_doc):
    pattern = [{"POS": "PROPN"}, {"POS": "PROPN"}]
    matcher.add("FULL_NAME", patterns=[pattern])
    matches = matcher(nlp_doc)
    for _, start, end in matches:
        span = nlp_doc[start:end]
        return span.text


print(extract_full_name(about_doc))

# %% Extracting phone numbers from text with patterns

matcher = Matcher(nlp.vocab)
conference_org_text = (
    "There is a developer conference"
    " happening on 21 July 2019 in London. It is titled"
    ' "Applications of Natural Language Processing".'
    " There is a helpline number available"
    " at (123) 456-7891"
)


def extract_phone_number(nlp_doc):
    pattern = [
        {"ORTH": "("},
        {"SHAPE": "ddd"},
        {"ORTH": ")"},
        {"SHAPE": "ddd"},
        {"ORTH": "-", "OP": "?"},
        {"SHAPE": "ddd"},
    ]
    matcher.add("PHONE_NUMBER", patterns=[pattern])
    matches = matcher(nlp_doc)
    for _, start, end in matches:
        span = nlp_doc[start:end]
        return span.text


conference_org_doc = nlp(conference_org_text)
print(extract_phone_number(conference_org_doc))

# %% Dependency parsing

piano_text = "Gus is learning piano"
piano_doc = nlp(piano_text)
for token in piano_doc:
    print(
        f"""
TOKEN: {token.text}
=====
{token.tag_ = }
{token.head.text = }
{token.dep_ = }"""
    )

displacy.serve(piano_doc, style="dep")

# %% Navigating the parsed tree and subtree

one_line_about_text = (
    "Gus Proto is a Python developer"
    " currently working for a London-based Fintech company"
)
one_line_about_doc = nlp(one_line_about_text)

# %% Extract children of `developer`
print([token.text for token in one_line_about_doc[5].children])

# %% Extract previous neighboring node of `developer`
print(one_line_about_doc[5].nbor(-1))

# %% Extract next neighboring node of `developer`
print(one_line_about_doc[5].nbor())

# %% Extract all tokens on the left of `developer`
print([token.text for token in one_line_about_doc[5].lefts])

# %% Extract tokens on the right of `developer`
print([token.text for token in one_line_about_doc[5].rights])

# %% Print subtree of `developer`
print(list(one_line_about_doc[5].subtree))

# %% Print flattened subtree of `developer`


def flatten_tree(tree):
    return "".join([token.text_with_ws for token in list(tree)]).strip()


print(flatten_tree(one_line_about_doc[5].subtree))

# %% Shallow parsing and noun phrase detection

conference_text = (
    "There is a developer conference happening on 21 July 2019 in London."
)
conference_doc = nlp(conference_text)

# Extract noun phrases
for chunk in conference_doc.noun_chunks:
    print(chunk)

# %% Verb phrase detection

about_talk_text = (
    "In this talk, the speaker will introduce the audience to the use"
    " cases of Natural Language Processing in Fintech, making use of"
    " interesting examples along the way."
)

patterns = [{"POS": "AUX"}, {"POS": "VERB"}]
about_talk_doc = textacy.make_spacy_doc(about_talk_text, lang="en_core_web_sm")
verb_phrases = textacy.extract.token_matches(about_talk_doc, patterns=patterns)

# Print all verb phrases

for chunk in verb_phrases:
    print(chunk.text)

# %% Extract noun phrases to explain what nouns are involved

for chunk in about_talk_doc.noun_chunks:
    print(chunk)

# %% Named-entity recognition

piano_class_text = (
    "Great Piano Academy is situated"
    " in Mayfair or the City of London and has"
    " world-class piano instructors."
)
piano_class_doc = nlp(piano_class_text)

for ent in piano_class_doc.ents:
    print(
        f"""
{ent.text = }
{ent.start_char = }
{ent.end_char = }
{ent.label_ = }
{spacy.explain(ent.label_) = }"""
    )

displacy.serve(piano_class_doc, style="ent")
# %% Use NER to redact names in document

survey_text = (
    "Out of 5 people surveyed, James Robert,"
    " Julie Fuller and Benjamin Brooks like"
    " apples. Kelly Cox and Matthew Evans"
    " like oranges."
)


def replace_person_names(token):
    if token.ent_iob != 0 and token.ent_type_ == "PERSON":
        return "[REDACTED] "
    return token.text_with_ws


def redact_names(nlp_doc):
    with nlp_doc.retokenize() as retokenizer:
        for ent in nlp_doc.ents:
            retokenizer.merge(ent)
    tokens = map(replace_person_names, nlp_doc)
    return "".join(tokens)


survey_doc = nlp(survey_text)
print(redact_names(survey_doc))
