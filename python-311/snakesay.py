import sys

message = " ".join(sys.argv[1:])
bubble_length = len(message) + 2
print(
    rf"""
       {"_" * bubble_length}
      ( {message} )
       {"‾" * bubble_length}
        \
         \    __
          \  [oo]
             (__)\
               λ \\
                 _\\__
                (_____)_
               (________)Oo°"""
)
