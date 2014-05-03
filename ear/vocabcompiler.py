"""
Create dicitonaries from arbitrary lists of words
"""
import sys
import os
import g2p

def compile(words):
    """
    Writes the given list of words out as dictionary.dic and languagemodel.ml,
    for use as parameters in Mic
    """

    words = list(set(words))

    # create the dictionary
    pronounced = g2p.translateWords(words)
    zipped = zip(words, pronounced)
    lines = ["%s %s" % (x, y) for x, y in zipped]

    with open("./dictionary.dic", "w") as f:
        f.write("\n".join(lines) + "\n")

    # create the language model
    with open("./sentences.txt", "w") as f:
        f.write("\n".join(words) + "\n")
        f.write("<s> \n </s> \n")
        f.close()

    # make language model
    os.system(
        "text2idngram -vocab ./sentences.txt < ./sentences.txt -idngram temp.idngram")
    os.system(
        "idngram2lm -idngram temp.idngram -vocab ./sentences.txt -arpa ./languagemodel.lm")
    return (os.path.abspath('./dictionary.dic'), os.path.abspath('./languagemodel.lm'))


def main():
    """
    Compile all command-line parameters into a dictionary and a language model
    """
    if not sys.argv[1:]:
        print "Usage: vocabcompiler.py WORDS WORDS WORDS..."
        sys.exit(1)

    files = compile(sys.argv[1:])
    print "compiled " + files

if __name__ == '__main__':
    main()
