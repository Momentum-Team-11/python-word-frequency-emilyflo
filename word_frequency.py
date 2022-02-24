STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as file:
        text_string = file.read()
        # remove the punctuation
        for char in '-—.,\n?!':
            text_string = text_string.replace(char, ' ')
        # normalize all words to lowercase and 
        text_string = text_string.lower().split()
        # remove stop words
        text_string = [word for word in text_string if word not in STOP_WORDS]
        # count the words
        word_count = {}
        for word in text_string:
            word_count[word] = word_count.get(word, 0) + 1
        # sort the dictionary in ascending values
        word_freq = []
        word_freq = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))
        # format the report
        for key,value in word_freq.items():
            print(f"{key:>20} | {(value * '*'):<20}")
        return word_freq

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)