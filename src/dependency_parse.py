from pycorenlp import StanfordCoreNLP
import os
import nltk.data

nlp = StanfordCoreNLP("http://localhost:9000")  # this requires a server to run: java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')


def create_files():
    for author in os.listdir("corpus/data"):
        if author.startswith("."):
            continue
        for book in os.listdir("corpus/data/" + author):
            if book.startswith("."):
                continue
            for filename in os.listdir("corpus/data/" + author + "/" + book):
                if filename.endswith(".txt"):
                    print(filename)
                    with open("corpus/data/" + author + "/" + book + "/" + filename, 'r', encoding='utf-8', errors='ignore') as read_file:
                        text = read_file.read()
                    with open("corpus/parsed_data/" + author + "/" + book + "/" + filename, 'w', encoding='utf-8', errors='ignore') as write_file:
                        write_to_file(write_file, text)


def write_to_file(write_file, text):
    # sentences = text.replace(";", ".").split(".")
    sentences = tokenizer.tokenize(text)
    for sent in sentences:
        # print(sent)
        # print("*****")
        sent = sent.strip()
        if not sent:
            continue
        try:
            res = nlp.annotate(sent, properties={'annotators':'parse', 'outputFormat': 'json'})
            write_file.write(res['sentences'][0]['parse'])
            write_file.write("\n~~~~~~\n")
        except TypeError: # if the sentence is too long the StanfordCoreNLP tool throws an exception
            write_file.write("no parsing")
            write_file.write("\n~~~~~~\n")


# create_files()
