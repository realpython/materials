SNAKE = r"""  \
   \    ___
    \  (o o)
        \_/ \
         λ \ \
           _\ \_
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
    print(bubble(message.replace("s", "ss").replace("S", "SS")))
    print(SNAKE)
