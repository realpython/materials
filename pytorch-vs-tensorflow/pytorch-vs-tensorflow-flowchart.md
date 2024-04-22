flowchart TD
classDef main font-size: 24px,padding: 10px
B[What data do you have or need?]
B:::main ==> C[Audio]
B ==> E[Images]
B ==> D[Text]

C --> F["`Do you plan on using multiple kinds of data?`"]
F -- Yes --> G[Use TensorFlow]

F --  No --> H["`Do you need to integarate your model into a JS-based or mobile-based platform?`"] 
H --> |Yes|G

H --> |No| I[Use PyTorch]
G -.- R["`TensorFlow's tf.audio, TensorFlow I/O, and TensorFlow Signal are better choices when it comes to advanced audio processing and handling different kinds of data`"]

D --> J["`Do you need to experiment and prototype fast?`"]
J --> |Yes| K[Use PyTorch]
I -.- S["`PyTorch's TorchAudio is an easy-to-use library, perfect for signal processing tasks`"]

J --> |No| M["`Do you need advanced fine-tuning and preprocessing tools?`"]
M --> |No| K
M --> |Yes| N[Use TensorFlow]
N -.- U["`TensorFlow's TensorFlow Text and KerasNLP might be a better choice when it comes to handling complex text processing`"]
K -.- T["`PyTorch's TorchText is easy to use, quick to set up, and great for trying out new ideas`"]

E --> O["`Do you need a specific dataset, pre-trained model or image preprocessing tool in mind?`"] 
O --> |Yes| P["`Check TensorFlow Hub and PyTorch Hub to choose which platform works best for you`"]
O -- No ---> Q[Use PyTorch]
Q -.- W["`PyTorch is generally easier to get started with, and comes with descent image pre-preocessing tools, pre-trained models and datasets`"]