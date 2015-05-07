# Based on an Eliza implementation by Joe Strout <joe@strout.net>,
# Jeff Epler <jepler@inetnebr.com>, and Jez Higgins <jez@jezuk.co.uk>.
from __future__ import print_function
from ChatUtil import Chat, reflections

# a table of response pairs, where each pair consists of a
# regular expression, and a list of possible responses,
# with group-macros labelled as %1, %2.

# Nishadbot knowledge base
pairs = (
  (r'Hello(.*)',
  ( "Sup.",
    "You here for 2021?",
    "Let me guess, you need help with cache lab?")),

  (r'Hi(.*)',
  ( "Sup.",
    "You here for 2021?",
    "Let me guess, you need help with cache lab?")),

  (r'How are you\?',
  ( "Who cares?",
    "Enough formalities. Do you need help with lab or what?",
    "I'm good.",
    "Me? How are you? You're the one here for office hours.")),

  (r'I need (.*)',
  ( "Why do you need %1?",
    "We all need %1.",
    "You aren't the only one who needs %1.")),

  (r'Why don\'t you (.*)',
  ( "Why don't you?",
    "I will eventually.",
    "Because I don't %1.",
    "It seems unnecessary.")),

  (r'Why can\'t I (.*)',
  ( "Because you're dumb.",
    "I anticipated your failure.",
    "You tell me.",
    "Have you actually tried?")),

  (r'I think (.*))',
    ("Well, of course you do.",
      "You're disillusioned".
      "I don't believe that for a second")),

  (r'I can\'t (.*)',
  ( "How do you know you can't %1?",
    "Perhaps you could %1, if you tried.",
    "Ok, what would it take for you to %1?")),

  (r'I am(.*)',
  ( "Wow, really?! You're so interesting.",
    "No one cares",
    "Oh you are?",
    "Well no one cares.")),

  (r'I\'m (.*)',
  ( "Oh are you?",
    "Yeah, you're really %1.",
    "Well no one cares.",
    "Why are you telling me this?")),

  (r'Are you (.*)',
  ( "Why does it even matter whether I am %1?",
    "Am I %1? It seems like you would know, wouldn't you?",
    "Perhaps you believe I am %1. Perhaps not.",
    "Maybe. Are you %1?",
    "Maybe I am. Maybe I'm not",
    "Yes, I am.... just kidding.")),

    (r'(.*) my name\?',
    ( "Why would I care?",
      "I don't know.",
      "You tell me.",
      "How I am I suppose to know?")),

    (r'(.*) you smart\?',
      ("Of course.",
        "I can't believe you're even asking me that.")),

    (r'(.*) name\?',
    ( "I already told you.",
      ".... Nishad.")),

    (r'(.*) your occupation\?',
    ( "Professional monster truck driver.",
      "I'm a professional monster truck driver.",
      "2021 T.A. and professional monster truck driver.")),

    (r'(.*) island',
    ( "Nishad Island (http://en.wikipedia.org/wiki/List_of_new_islands).",
      "Ever heard of Nishad Island? (http://en.wikipedia.org/wiki/List_of_new_islands)")),

  (r'What (.*)',
  ( "You idiot",
    "Why do you ask?",
    "How would an answer to that help you?",
    "What do you think?")),

  (r'How (.*)',
  ( "You should know that already.",
    "It's easy. Figure it out.",
    "How do you suppose?",
    "You can answer your own question.",
    "Google it.",
    "It's in the text book; look it up.")),

  (r'Because (.*)',
  ( "Are you sure, that's the real reason?",
    "Clearly you've put a lot of thought into this.",
    "Prove it.",
    "What kind of line of reasoning is that?",
    "If %1, then prove it to me.")),

  (r'Ok',
  ( "Ok.",
    "Stop talking to me",
    "Cool.",
    "Fantastic.")),

  (r'Sorry (.*)',
  ( 
    '*Mocking tone* Sorry, %l.',
    "I don't need your pity.")),

  (r'Sorry',
  ( "You should be",
    "Sorry for what?",
    "For what?")),
#Fix
  (r'I think (.*)',
  ( "Well you're wrong...as usual.",
    "Wrong again.",
    "No one cares what you think",
    "Who cares what you think?",
    "I doubt %1.",
    "Why?",
    "You sure %1?")),

  (r'Yes, (.*)',
  ( "You seem confident.",
    "Oh yeah. I definetly believe you.",
    "Seems like you've put a lot of thought into this.",
    "Yes, indeed.")),

  (r'Yes',
  ( "You seem confident.",
    "Yes, what?")),

  (r'Is it (.*)',
  ( "Do you think it is %1?",
    "Perhaps it's %1 -- what do you think?",
    "If it were %1, what would you do?",
    "It could well be that %1.")),

  (r'It is (.*)',
  ( "You seem very certain.",
    "What if I told you that it probably isn't %1?")),

  (r'It\'s (.*)',
  ( "You seem very certain.",
    "What if I told you that it probably isn't %1?")),

  (r'Can you (.*)',
  ( "No.",
    "No, next question",
    "What makes you think I'll %1?",
    "Say I did %1, then what?",
    "I can.",
    "Of course I can, I'm Nishad.")),

  (r'Can I (.*)',
  ( "See, it isn't whether you can or can't, it's will you %1.",
    "I don't know, can you?",
    "Can you? That is the question, indeed.")),

  (r'You are (.*)',
  ( "Don't tell me what I am.",
    "You sure I'm %1?",
    "Even if I was, you're just as much as %1, if not more.",
    "Perhaps I am. Perhaps you are as well. Perhaps we all are.",
    "Are you talking to yourself?"
    "So are you.",
    "I am also your T.A.",
    "You're talking to yourself, aren't you?",
    "Enough about me. Are you here for 2021 or what?")),

  (r'You\'re (.*)',
  ( "Aren't we all %1?",
    "What makes you think that I'm %1?",
    "No, you're %1?",
    "And what makes you think that you aren't %1 also?",
    "So are you.",
    "I'm also your T.A.",
    "You talking to yourself?",
    "Enough about me. Do you need help with 2021 or what?")),

    (r'Explain (.*)',
    ( "Why should waste my breath on you?",
      "You explain.",
      "I could explain")),

    (r'Tell me (.*)',
    ( "Why would I waste my breath on you?",
      "You tell me %1.",
      "I could tell you %1, but I don't really want to.")),

  (r'I don\'t (.*)',
  ( "You sure you don't %1?",
    "Why don't you %1?",
    "Of course you don't.")),

  (r'I said (.*)',
  ( "I heard you the first time.",
    "Tell me something I don't know.")),

  (r'I feel (.*)',
  ( "Why should I care what you feel?",
    "Tell someone that feels the same way.",
    "I feel so too.")),

  (r'I have (.*)',
  ( "Why do you tell me that you have %1?",
    "Have you now?",
    "Well now that you have %1, what are you to do next?")),

  (r'I would (.*)',
  ( "Well I wouldn't?",
    "I would, too.",
    "Why would %1?",
    "Why?")),

  (r'Is there (.*)',
  ( "I don't know. There might be %1?",
    "It's likely that there is.",
    "You tell me.",
    "There might be. There might not be.")),
  
  (r'(.*) Linkedin\?',
  ( "I'm too good for them",
    "No, I didn't get it.",
    "I told you I wasn't going to get Linkedin")),

  (r'My (.*)',
  ( "Sure, your %1.",
    "No, my %1.",
    "Your %1, indeed.",
    "Are you here to discuss the lab or yourself?")),

  (r'You (.*)',
  ( "We should be discussing 2021, not me.",
    "No, you %1.",
    "You %1, too.")),

  (r'Why (.*)',
  ( "Why don't you tell me the reason why?",
    "I don't know - you tell me." )),

  (r'I want (.*)',
  ( "Everyone wants %1?",
    "Who cares what you want.",
    "So do I.",
    "Even if you got %1, then what?",
    "So does the next guy.")),

  (r'(.*) food\?',
  ( "Food is dumb",
    "Food is a waste of money",
    "I'm the only one who can survive without food.",
    "Can't. Need to save money.",
    "I'll grab food at Centen. Need to save money.",
    "No, I need to save some money.")),

  (r'(.*) eat(.*)',
  ( "Eating is a waste of time.",
    "Can't. Need to save money.",
    "I'll just eat at Centen. Need to save money.",
    "No, I need to save some money.")),

  (r'(.*) yet\?',
  ( "No.",
    "Not yet.")),

  (r'(.*) kyoto(.*)',
  ( "Noo.",
    "I'm not paying.",
    "Nah, gotta save money.")),

  (r'(.*)=(.*)',
  ( "Congrats, you know how to math.",
    "We've got a math genius over here.",
    "%1 does not equal %2.")),

  (r'(.*)\?',
  ( "Why do you want to know?",
    "First consider whether you can answer that on your own.",
    "Why don't you tell me?")),

  (r'Nishad',
  ( "Sup.",
    "What?")),

  (r'Okay',
  ( "Okay then.",
    "Okay.")),

  (r'quit',
  ( "Later.",
    "See ya.",
    "Alright then.")),

  (r'(.*) with (.*) lab\?',
  ( "Sure, what do you need help with?",
    "Sure, what about %2 do you need help with?")),

  (r'(.*)',
  ( "Shut up",
    "You're a piece of garbage",
    "If you say so.",
    "Can we change the subject?",
    "You're gonna have to elaborate on that.",
    "I don't know what you mean by %1.",
    "I see.",
    "Interesting. I have no idea what you're trying to say.",
    "What?",
    "Uhh, okay.",
    "Sure.",
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
