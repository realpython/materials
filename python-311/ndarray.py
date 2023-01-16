from typing import Generic, Literal, NewType, TypeVarTuple

Ts = TypeVarTuple("Ts")


class Array(Generic[*Ts]):
    ...  # Not implemented here


Height = NewType("Height", int)
Width = NewType("Width", int)
Channels = NewType("Channels", int)
image: Array[Height, Width, Channels]

video_frame: Array[Literal[1920], Literal[1080], Literal[3]]
