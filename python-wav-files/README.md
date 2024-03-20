# Reading and Writing WAV Files in Python

Sample code and sounds for the [Reading and Writing WAV Files in Python](https://realpython.com/python-wav-files/) tutorial on Real Python.

## Setup

Create and activate a new virtual environment:

```
$ python3 -m venv venv/ --prompt wave
$ source venv/bin/activate
```

Install the required dependencies:

```
(wave) $ python -m pip install -r requirements.txt -c constraints.txt
```

## Usage

### Synthesize Sounds

```
(wave) $ python synth_mono.py
(wave) $ python synth_stereo.py
(wave) $ python synth_beat.py
```

### Synthesize 16-bit Stereo Sounds

```
(wave) $ python synth_stereo_16bits_array.py
(wave) $ python synth_stereo_16bits_bytearray.py
(wave) $ python synth_stereo_16bits_ndarray.py
```

### Plot a Static Waveform

```
(wave) $ python plot_waveform.py sounds/Bicycle-bell.wav
(wave) $ python plot_waveform.py sounds/Bongo_sound.wav -s 3.5 -e 3.65
```

### Animate an Oscilloscope

```
(wave) $ python plot_oscilloscope.py sounds/Bicycle-bell.wav
(wave) $ python plot_oscilloscope.py sounds/Bongo_sound.wav -s 0.005
```

### Animate a Spectrogram

```
(wave) $ python plot_spectrogram.py sounds/Bicycle-bell.wav
(wave) $ python plot_spectrogram.py sounds/Bongo_sound.wav -s 0.0005 -o 95
```

### Record a Radio Stream

```
(wave) $ RADIO_URL=http://prem2.di.fm:80/classiceurodance?your-secret-token
(wave) $ python record_stream.py "$RADIO_URL" -o ripped.wav
```

### Boost the Stereo Field

```
(wave) $ python stereo_booster.py -i sounds/Bicycle-bell.wav -o boosted.wav -s 5
```
