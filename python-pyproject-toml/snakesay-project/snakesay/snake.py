SNAKE = r"""  \
   \    __
    \  {oo}
       (__)\
         λ \\
           _\\__
          (_____)_
         (________)=Oo°
"""


def bubble(message):
    bubble_length = len(message) + 2
    return f"""
 {"_" * bubble_length}
( {message} )    
 {"‾" * bubble_length}"""


def say(message):
    print(bubble(message))
    print(SNAKE)