'''
Source data: https://www.kaggle.com/datasets/bittlingmayer/spelling

Files used:
    - aspell.txt
    - birkbeck.txt
    - spell-testset1.txt
    - spell-testset2.txt
    - wikipedia.txt

Task:
    Merge the above files into vocab.txt (unique, sorted words).
'''

data_path1 = 'data/aspell.txt'
data_path2 = 'data/birkbeck.txt'
data_path3 = 'data/spell-testset1.txt'
data_path4 = 'data/spell-testset2.txt'
data_path5 = 'data/wikipedia.txt'

data_path = [ data_path1,
              data_path2,
              data_path3,
              data_path4,
              data_path5 ]

data_src_path = 'data/vocab.txt'

def data_processing(data_path):
    """
    Extract unique words from multiple text files.

    Each line in the source files may contain text in the format "word: info".
    This function removes extra characters, splits at ': ', and keeps only the word part.

    Args:
        data_path (list[str]): List of file paths to process.

    Returns:
        set[str]: A set of unique words collected from all files.
    """

    words = set()
    for data in data_path:
        with open(data, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if ': ' in line:
                    word = line.strip().split(': ')
                    words.add(word[0])
    return words

def write_data(data_path, words):
    """
    Merge new words into vocab.txt and ensure uniqueness.

    Reads the existing vocab.txt, merges with new words, removes duplicates,
    and writes back the combined sorted vocabulary.

    Args:
        data_path (str): Path to the vocab file.
        words (set[str]): A set of new words to add.

    Returns:
        None
    """

    word_src = set()
    with open(data_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            word = line.strip()
            word_src.add(word)    
    
    for word in words:
        word_src.add(word)

    with open(data_path, 'w', encoding='utf-8') as file:
        for word in sorted(word_src):
            file.write(word + '\n')

def main():
    """Main entry: process source files and update vocab.txt."""
    words = data_processing(data_path)
    write_data(data_src_path, words)

main()