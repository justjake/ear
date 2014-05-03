"""
Entry point

TODO: event handler to RPC the Wit.ai event
TODO: do we need a different person/default dict? we don't have one
"""

from wit import Wit
from pprint import pprint

from config import (
        DEFAULT_DICT, DEFAULT_LANG,
        PERSONA_DICT, PERSONA_LANG,
        PERSONA, wit_token)

from mic import Mic

def event_loop():

    wit = Wit(wit_token())
    my_mic = Mic(DEFAULT_DICT, DEFAULT_LANG, DEFAULT_DICT, DEFAULT_LANG)

    while True:
        # listen for activation hotword
        try:
            threshold, text = my_mic.passiveListen(PERSONA)
        except:
            continue

        # detected hotword
        if threshold:
            audio_file = activeListenFile(threshold)
            if audio_file:
                data = None
                try:
                    # retrieve wit intent
                    data = wit.post_speech(open(audio_file))
                    # send to handler service
                    raise NotImplementedError('no handler code yet')
                except Exception as e:
                    print "Exception in audio_file handling:"
                    print str(e)
                    if data:
                        print "Data: "
                        print pprint(data)


if __name__ == '__main__':
    event_loop()
