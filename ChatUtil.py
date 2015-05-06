# Based on an Eliza implementation by Joe Strout <joe@strout.net>,
# Jeff Epler <jepler@inetnebr.com>, and Jez Higgins <jez@jezuk.co.uk>.
from __future__ import print_function

import re
import random
from nltk import compat

reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}

class Chat(object):
    def __init__(self, pairs, reflections={}):
        """
        Initialize the chatbot.  Pairs is a list of patterns and responses.  Each
        pattern is a regular expression matching the user's statement or question,
        e.g. r'I like (.*)'.  For each such pattern a list of possible responses
        is given, e.g. ['Why do you like %1', 'Did you ever dislike %1'].  Material
        which is matched by parenthesized sections of the patterns (e.g. .*) is mapped to
        the numbered positions in the responses, e.g. %1.

        :type pairs: list of tuple
        :param pairs: The patterns and responses
        :type reflections: dict
        :param reflections: A mapping between first and second person expressions
        :rtype: None
        """
        self._pairs = [(re.compile(x, re.IGNORECASE),y) for (x,y) in pairs]
        self._reflections = reflections
        self._regex = self._compile_reflections()
        # If user keeps repeating himself one/more times
        self._repition_count = 1
        self._repeated_input = ""
        self._repeated_input_response = ["Stop repeating yourself.",
                                         "Stop saying that.",
                                         "Is that all you're going to say?",
                                         "Say something else.",
                                         "You said that already.",
                                         "I heard you the first time."]
        self._repeated_input_response_Q = ["Stop repeating yourself.",
                                           "Stop asking me that.",
                                           "Is that all you're going to ask?",
                                           "Ask something else.",
                                           "You asked that already.",
                                           "I heard you the first time."]


    def _compile_reflections(self):
        sorted_refl = sorted(self._reflections.keys(), key=len,
                reverse=True)
        return  re.compile(r"\b({0})\b".format("|".join(map(re.escape,
            sorted_refl))), re.IGNORECASE)

    def _substitute(self, str):
        """
        Substitute words in the string, according to the specified reflections,
        e.g. "I'm" -> "you are"

        :type str: str
        :param str: The string to be mapped
        :rtype: str
        """
        return self._regex.sub(lambda mo:
                self._reflections[mo.string[mo.start():mo.end()]],
                    str.lower())

    def _sanitize_punctuation(self, subject):
        chars_to_remove = ['.', '!', '?']
        return subject.translate(None, ''.join(chars_to_remove))

    def _wildcards(self, response, match):
        pos = response.find('%')
        while pos >= 0:
            num = int(response[pos+1:pos+2])
            sub = self._substitute(match.group(num))
            response = response[:pos] + \
                self._sanitize_punctuation(sub) + \
                response[pos+2:]
            pos = response.find('%')
        return response

    def respond(self, str):
        """
        Generate a response to the user input.

        :type str: str
        :param str: The string to be mapped
        :rtype: str
        """
        
        # check for repititious user inputs
        if str.lower() == self._repeated_input.lower():
            self._repition_count += 1
            if self._repition_count >= 2 and '?' not in str:
                return random.choice(self._repeated_input_response)
            elif self._repition_count >= 2 and '?' in str:
                return random.choice(self._repeated_input_response_Q)
        else:
            self._repition_count = 1
            self._repeated_input = str

        # check each pattern
        for (pattern, response) in self._pairs:
            match = pattern.match(str)

            # did the pattern match?
            if match:
                resp = random.choice(response)      # pick a random response
                resp = self._wildcards(resp, match) # process wildcards

                # fix munged punctuation at the end
                if resp[-2:] == '?.': resp = resp[:-2] + '.'
                if resp[-2:] == '??': resp = resp[:-2] + '?'
                return resp

    # Hold a conversation with a chatbot
    def converse(self, quit="quit"):
        input = ""
        while input != quit:
            input = quit
            try: input = compat.raw_input(">")
            except EOFError:
                print(input)
            if input:
                while input[-1] in "!.": input = input[:-1]
                print(self.respond(input))
