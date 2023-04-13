# Code for Build Your Own Face Recognition Tool With Python

This is a small project to demonstrate how to build a face recognition tool using Python. It goes along with the Real Python tutorial [Build Your Own Face Recognition Tool With Python](https://realpython.com/face-recognition-with-python/).

## Dependency Installation

`dlib` requires both CMake and a C++ compiler to be installed before using it. 
Refer to the [CMake documentation](https://cmake.org/install/) and that of your preferred C++ compiler for 
installation instructions. 

The script assumes that the directories `training/`, `output/` and `validation/` exist, so be sure to create those directories before running the code.

## Usage

The three major phases of the machine learning workflow are represented by the program's three switches:

- `--train`: Initiate the model training process.
- `--validate`: Run a trained model on images stored in the `validation` directory. The faces in these images should be known to you so you can debug the model's performance. 
- `--test`: Run a trained model on an image with an unknown face in it. The script will use the model to detect and attempt to identify the face in the image.
- `-m`: Specify the type of model architecture you want to use. `"hog"` is the default and best for CPU-based training, while `"cnn"` is better for GPU training and will generally give better performance.
