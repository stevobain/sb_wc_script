# SB Word Count (sb_wc)

`sb_wc.py` is a Python script that mimics the functionality of the Unix `wc` (word count) command. It's capable of counting bytes, lines, words, and characters in text files and standard input, offering a versatile tool for text file analysis.

## Installation

**Prerequisites:** Python 3.x

To use `sb_wc.py`, clone this repository or download the script directly.

```
git clone https://github.com/stevobain/sb_wc.git
``` 

## Usage

Run the script from the command prompt, optionally specifying a file and an option.

### Count Lines, Words, and Bytes (Default Behavior)

```
python sb_wc.py path\to\your\file.txt
``` 

### Count Bytes

```
python sb_wc.py -c path\to\your\file.txt
``` 

### Count Lines

```
python sb_wc.py -l path\to\your\file.txt
``` 

### Count Words

```
python sb_wc.py -w path\to\your\file.txt
``` 

### Count Characters

```
python sb_wc.py -m path\to\your\file.txt
``` 

### Read from Standard Input

```
python sb_wc.py
``` 

Then input your text, press enter, and end the input by pressing Ctrl+Z and then Enter.

## Contributions

Contributions are welcome! If you have suggestions for improvements or bug fixes, please feel free to fork this repository, make changes, and submit a pull request.
