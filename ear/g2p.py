import os
import subprocess
import re

from config import data_path, tmp_path, G014B2B_FST


TEMP_FILENAME = tmp_path('g2ptemp')
PHONE_MATCH = re.compile(r'<s> (.*) </s>')


def parseLine(line):
    return PHONE_MATCH.search(line).group(1)


def parseOutput(output):
    return PHONE_MATCH.findall(output)


def translateWord(word):
    out = subprocess.check_output(['phonetisaurus-g2p', '--model=%s' %
                                  (G014B2B_FST), '--input=%s' % word])
    return parseLine(out)


def translateWords(words):
    full_text = '\n'.join(words)

    f = open(TEMP_FILENAME, "wb")
    f.write(full_text)
    f.flush()

    output = translateFile(TEMP_FILENAME)
    os.remove(TEMP_FILENAME)

    return output


def translateFile(input_filename, output_filename=None):
    """
    Translates a text file of sentences into a dictionary.
    """
    out = subprocess.check_output(['phonetisaurus-g2p', '--model=%s' % (G014B2B_FST),
            '--input=%s' % (input_filename), '--words', '--isfile'])
    out = parseOutput(out)

    if output_filename:
        out = '\n'.join(out)

        f = open(output_filename, "wb")
        f.write(out)
        f.close()

        return None

    return out

if __name__ == "__main__":

    translateFile(os.path.expanduser(data_path("/sentences.txt")),
                  os.path.expanduser(data_path("/dictionary.dic")))
