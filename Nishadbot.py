# Based on an Eliza implementation by Joe Strout <joe@strout.net>,
# Jeff Epler <jepler@inetnebr.com>, and Jez Higgins <jez@jezuk.co.uk>.
from __future__ import print_function
from ChatUtil import Chat, reflections

# a table of response pairs, where each pair consists of a
# regular expression, and a list of possible responses,
# with group-macros labelled as %1, %2.

pairs = (
#Good
  (r'Hello(.*)',
  ( "Sup.",
    "You here for 2021?",
    "Let me guess, you need help with cache lab?")),
#Good
  (r'Hi(.*)',
  ( "Sup.",
    "You here for 2021?",
    "Let me guess, you need help with cache lab?")),
#Good
  (r'Nishad',
  ( "Sup.",
    "What?")),
#Fix
  (r'I need (.*)',
  ( "Why do you need %1?",
    "Would it really help you to get %1?",
    "Are you sure you need %1?")),
#Fix
  (r'Why don\'t you (.*)',
  ( "Do you really think I don't %1?",
    "Perhaps eventually I will %1.",
    "Do you really want me to %1?")),
#Fix
  (r'Why can\'t I (.*)',
  ( "Do you think you should be able to %1?",
    "If you could %1, what would you do?",
    "I don't know -- why can't you %1?",
    "Have you really tried?")),
#Fix
  (r'I can\'t (.*)',
  ( "How do you know you can't %1?",
    "Perhaps you could %1 if you tried.",
    "What would it take for you to %1?")),
#Fix
  (r'I am (.*)',
  ( "Did you come to me because you are %1?",
    "How long have you been %1?",
    "How do you feel about being %1?")),
#Fix
  (r'I\'m (.*)',
  ( "How does being %1 make you feel?",
    "Do you enjoy being %1?",
    "Why do you tell me you're %1?",
    "Why do you think you're %1?")),
#Fix
  (r'Are you (.*)',
  ( "Why does it matter whether I am %1?",
    "Would you prefer it if I were not %1?",
    "Perhaps you believe I am %1.",
    "I may be %1 -- what do you think?")),
#Fix
  (r'What (.*)',
  ( "Why do you ask?",
    "How would an answer to that help you?",
    "What do you think?")),
#Fix
  (r'How (.*)',
  ( "How do you suppose?",
    "Perhaps you can answer your own question.",
    "What is it you're really asking?")),
#Fix
  (r'Because (.*)',
  ( "Is that the real reason?",
    "What other reasons come to mind?",
    "Does that reason apply to anything else?",
    "If %1, then do something about it.")),
#Fix
  (r'(.*) sorry (.*)',
  ( "Stop apologizing.",
    "It's alright, I guess.")),
#Fix
  (r'I think (.*)',
  ( "I doubt %1.",
    "Do you really think that?",
    "You sure %1?")),
#Fix
  (r'Yes',
  ( "You seem confident.",
    "Okay, but can you elaborate on that?")),
#Fix
  (r'Is it (.*)',
  ( "Do you think it is %1?",
    "Perhaps it's %1 -- what do you think?",
    "If it were %1, what would you do?",
    "It could well be that %1.")),
#Fix
  (r'It is (.*)',
  ( "You seem very certain.",
    "If I told you that it probably isn't %1, what would you feel?")),
#Fix
  (r'Can you (.*)',
  ( "What makes you think I'll %1?",
    "Say I did %1, then what?")),
#Fix
  (r'Can I (.*)',
  ( "Perhaps you don't want to %1.",
    "Do you want to be able to %1?",
    "If you could %1, would you?")),
#Fix
  (r'You are (.*)',
  ( "Why do you think I am %1?",
    "Does it please you to think that I'm %1?",
    "Perhaps you would like me to be %1.",
    "Perhaps you're really talking about yourself?")),
#Fix
  (r'You\'re (.*)',
  ( "Why do you say I am %1?",
    "Why do you think I am %1?",
    "Are we talking about you, or me?")),
#Good
  (r'I don\'t (.*)',
  ( "You sure you don't %1?",
    "Why don't you %1?",
    "Of course you don't.")),
#Good
  (r'I feel (.*)',
  ( "Why should I care what you feel?",
    "Tell someone that feels the same way.",
    "I feel so too.")),
#Good
  (r'I have (.*)',
  ( "Why do you tell me that you have %1?",
    "Have you now?",
    "Well now that you have %1, what are you to do next?")),
#Fix
  (r'I would (.*)',
  ( "Could you explain why you would %1?",
    "Why would you %1?",
    "Who else knows that you would %1?")),
#Fix
  (r'Is there (.*)',
  ( "Do you think there is %1?",
    "It's likely that there is %1.",
    "Would you like there to be %1?")),
#Good
  (r'My (.*)',
  ( "Sure, your %1.",
    "No, my %1.",
    "Your %1, indeed.",
    "Are you here to discuss the lab or yourself?")),
#Good
  (r'You (.*)',
  ( "We should be discussing 2021, not me.",
    "No, you %1.",
    "You %1, too.")),
#Good
  (r'Why (.*)',
  ( "Why don't you tell me the reason why?",
    "I don't know - you tell me." )),
#Good
  (r'I want (.*)',
  ( "Everyone wants %1?",
    "Who cares what you want.",
    "So do I.",
    "Even if you got %1, then what?",
    "So does the next guy")),
#Good
  (r'(.*) food\?',
  ( "Can't. Need to save money.",
    "I'll grab food at Centen. Need to save money.",
    "No, I need to save some money.")),
#Good
  (r'(.*) eat(.*)',
  ( "Can't. Need to save money.",
    "I'll just eat at Centen. Need to save money.",
    "No, I need to save some money.")),
#Good
  (r'(.*) yet\?',
  ( "No.",
    "Not yet.")),
#Good
  (r'(.*) kyoto(.*)',
  ( "Noo.",
    "I'm not paying.",
    "Nah, gotta save money.")),
#Good
  (r'(.*) = (.*)',
  ( "Congrats, you know how to math.")),
#Good
  (r'(.*)\?',
  ( "Why do you want to know?",
    "First consider whether you can answer your own question.",
    "Why don't you tell me?")),
#Good
  (r'quit',
  ( "Later.",
    "See ya.",
    "Alright then.")),
#Good
  (r'(.*)',
  ( "If you say so.",
    "Can we change the subject?",
    "You're gonna have to elaborate on that.",
    "What do you mean %1?",
    "I see.",
    "Interesting. I have no idea what you're trying to say.",
    "What?",
    "Uhh, okay...",
    "Sure...",
    "I don't know too much about %1?"))
)

nishad_chatbot = Chat(pairs, reflections)

def nishad_chat():
    print('='*73)
    print(' '*29 + "Nishad-bot Demo" + ' '*29)
    print('='*73)
    print("Talk to the program by typing in plain English, using normal upper-")
    print('and lower-case letters and punctuation.  Enter "quit" when done.')
    print('='*73)
    print("I'm Nishad, the T.A. for 2021. Ask me anything.")
    """
    for i in pairs:
        print(i[0] + ',')
        for j in i:
            print('\t' + j[0] + ',')
    """
    nishad_chatbot.converse()

def demo():
    nishad_chat()

if __name__ == "__main__":
    demo()
