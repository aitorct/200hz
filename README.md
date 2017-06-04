# 200Hz

Our platform consists of a desktop client, capable of reading audio files, interpreting its frequency spectrum and modifying the values of those frequencies. The key of our idea is to cut out the frequencies from the audio file which are inaudible for the human ear. Then, we add a combination of frequencies in the non-audible range in order to encode a message in the form of text provided by the user. When the encryption is completed, a new audio file is created, which contains the original audio plus the encoded message. At this point, the user sends the audio file to someone, that will proceed with the decoding.

The second step is the decoding of the encrypted file, where the user will open the audio file with our platform and will decode it, receiving the original message.


## Prerequisites

All requirements are packed in the file requirements.txt. Just run the following command to install all needed libraries.

    pip3 install -r requirements.txt

## Usage

    python3 gui.py

## Built with
* [numpy](https://github.com/numpy/numpy)
* Tkinter (Python built-in)
