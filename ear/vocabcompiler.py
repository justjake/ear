"""
Create dicitonaries from arbitrary lists of words
"""
import sys
import os
import g2p

from config import DEFAULT_DICT, DEFAULT_LANG, tmp_path

def compile(words, dict_filename, langmodel_filename):
    """
    Writes the given list of words out as dictionary.dic and languagemodel.ml,
    for use as parameters in Mic
    """

    sentences_file = tmp_path('sentences.txt')
    idgram_file = tmp_path('temp.idgram')

    words = [w.upper() for w in words]
    words = list(set(words))

    # create the dictionary
    pronounced = g2p.translateWords(words)
    zipped = zip(words, pronounced)
    lines = ["%s %s" % (x, y) for x, y in zipped]

    with open(dict_filename, "w") as f:
        f.write("\n".join(lines) + "\n")

    # create the language model
    with open(sentences_file, "w") as f:
        f.write("\n".join(words) + "\n")
        f.write("<s> \n </s> \n")
        f.close()

    # make language model
    os.system(
        "text2idngram -vocab {sentences} < {sentences} -idngram {idgram}".format(
            sentences=sentences_file, idgram=idgram_file))
    os.system(
        "idngram2lm -idngram {idgram} -vocab {sentences} -arpa {langmodel}".format(
            idgram=idgram_file, sentences=sentences_file, langmodel=langmodel_filename))
    return True


def main():
    """
    Compile all command-line parameters into a dictionary and a language model
    """
    if not sys.argv[1:]:
        print "Usage: vocabcompiler.py WORDS WORDS WORDS..."
        sys.exit(1)

    print "Compiling {words} to files {dict_file}, {lm}".format(words=str(sys.argv[1:]), 
            dict_file=DEFAULT_DICT, lm=DEFAULT_LANG)
    files = compile(sys.argv[1:], DEFAULT_DICT, DEFAULT_LANG)
    print "compiled " + str(files)

if __name__ == '__main__':
    main()
