import streamlit as st
from LevenshteinDistance import levenshtein_distance

def load_vocab(file_path):
	"""
    Load vocabulary from a text file.

    Args:
        file_path (str): Path to the vocabulary file.

    Returns:
        list[str]: A list of words (lowercased, stripped).
    """

	with open(file_path, 'r') as file:
		lines = file.readlines()
		vocabs = [line.strip().lower() for line in lines]
		return vocabs

def back_end(word):
	"""
    Compute Levenshtein distances from the input word to all words in the vocabulary,
    and return a dictionary sorted by distance (ascending).

    Args:
        word (str): Input word to check/correct.

    Returns:
        dict[str, int]: A dictionary {vocab_word: distance}, sorted so that
                        the closest words appear first.
    """

	vocabs = load_vocab('data/vocab.txt')
	check = 1000000
	res = ''
	distances = dict()
	for vocab in vocabs:
		levenshtein = levenshtein_distance(word, vocab)
		distances[vocab] = levenshtein
		if levenshtein < check:
			res = vocab
			check = levenshtein

	sorted_distance = {k: v for k, v in sorted(distances.items(), key=lambda item:item[1])}
	
	return sorted_distance

def front_end():
	"""
    Streamlit front-end for word correction.

    Provides:
        - Text input for the user to enter a word.
        - A button to trigger the correction.
        - Displays the top-5 closest words from the vocabulary
          based on Levenshtein distance.
    """

	st.title('Word Correction using Levenshtein Distance')
	word = st.text_input('Word:')
	if st.button('Predict'):
		sorted_distance = back_end(word)
		i = 1
		for key in sorted_distance.keys():
			st.write(f'Priority prediction {i}: {key}')
			i += 1
			if i == 6:
				break

# Run the Streamlit app
front_end()