def levenshtein_distance(word1, word2):
	"""
    Compute the Levenshtein distance (edit distance) between two words.

    The Levenshtein distance is defined as the minimum number of
    single-character edits (insertions, deletions, substitutions)
    required to change one word into the other.

    Args:
        word1 (str): First input word.
        word2 (str): Second input word.

    Returns:
        int: The Levenshtein distance between word1 and word2.
    """
	
	length_of_word1 = len(word1)
	length_of_word2 = len(word2)

	levenshtein_matrix = [[0] * (length_of_word2+1) for _ in range(length_of_word1+1)]

	dict_for_word1 = dict()
	dict_for_word2 = dict()

	for i in range(length_of_word2+1):
		levenshtein_matrix[0][i] = i
		if i > 0:
			dict_for_word2[i] = word2[i-1]

	for i in range(length_of_word1+1):
		levenshtein_matrix[i][0] = i
		if i > 0:
			dict_for_word1[i] = word1[i-1]

	height = len(levenshtein_matrix)
	width = len(levenshtein_matrix[0])

	for i in range(1, height):
		for j in range(1, width):
			if dict_for_word1[i] == dict_for_word2[j]:
				levenshtein_matrix[i][j] = levenshtein_matrix[i-1][j-1]
			else:
				levenshtein_matrix[i][j] = min(levenshtein_matrix[i][j-1], levenshtein_matrix[i-1][j], levenshtein_matrix[i-1][j-1]) + 1
			
	return levenshtein_matrix[height-1][width-1]