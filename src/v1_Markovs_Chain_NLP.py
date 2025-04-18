"""
Markov Chain Text Generator
--------------------------
This script implements a Markov chain-based text generator that can create text using
n-gram models (unigram, bigram, and trigram). It processes multiple text files in parallel
and generates new text based on the statistical patterns found in the input data.
"""

import random
import os
import chardet  # For detecting file encodings
import re
import concurrent.futures

def process_single_file(file_path):
    """
    Process a single text file: detect encoding, read content, and clean text.
    
    Args:
        file_path (str): Path to the text file to process
        
    Returns:
        tuple: (list of cleaned words, number of lines in file)
    """
    try:
        # Step 1: Detect file encoding
        with open(file_path, 'rb') as f:
            raw_data = f.read()
            result = chardet.detect(raw_data)
            encoding = result['encoding'] if result['encoding'] else 'utf-8'

        # Step 2: Read file content with detected encoding
        with open(file_path, 'r', encoding=encoding) as f:
            file_content = f.read()

        # Step 3: Process non-empty files
        if file_content.strip():
            cleaned_words = clean_txt(file_content)
            line_count = file_content.count('\n') + 1
            print(f"Processed '{os.path.basename(file_path)}' with {line_count} lines.")
            return cleaned_words, line_count
        else:
            return [], 0

    except Exception as e:
        print(f"Error processing '{os.path.basename(file_path)}': {str(e)}")
        return [], 0

def read_all_text_files(folder_path):
    """
    Read and process all .txt files in the specified folder using parallel processing.
    
    Args:
        folder_path (str): Path to folder containing .txt files
        
    Returns:
        list: Combined list of cleaned words from all files
        
    Raises:
        ValueError: If folder doesn't exist or no .txt files found
    """
    all_words = []
    total_lines = 0

    # Validate folder path
    if not os.path.exists(folder_path):
        raise ValueError(f"Folder path '{folder_path}' does not exist")

    # Get list of .txt files
    txt_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.txt')]
    if not txt_files:
        raise ValueError(f"No .txt files found in '{folder_path}'")

    # Process files in parallel using ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(process_single_file, txt_files))

    # Combine results from all files
    for cleaned_words, line_count in results:
        all_words.extend(cleaned_words)
        total_lines += line_count

    if not all_words:
        raise ValueError("No valid text content found in files")

    print(f"\nTotal lines read: {total_lines}")
    print(f"Total words after cleaning: {len(all_words)}\n")

    return all_words

def clean_txt(txt):
    """
    Clean and tokenize input text.
    
    Args:
        txt (str): Input text to clean
        
    Returns:
        list: Cleaned and tokenized words
    
    Processing steps:
    1. Convert to lowercase
    2. Standardize apostrophes
    3. Remove special characters
    4. Tokenize into words
    5. Filter out invalid tokens
    """
    if not isinstance(txt, str) or not txt.strip():
        return []

    cleaned_txt = []
    lines = txt.splitlines()
    for line in lines:
        if line.strip():  # Skip empty lines
            # Text normalization steps
            line = line.lower()
            line = line.replace("'", "'").replace("'", "'").replace("`", "'")
            line = line.replace("'", "")  # Remove apostrophes in contractions
            line = re.sub(r'[^\w\s\.]', '', line)  # Keep periods
            tokens = re.findall(r'\b[a-z]+\b|\.', line)  # Match words or periods
            words = [word for word in tokens if len(word) > 0]
            cleaned_txt.extend(words)
    return cleaned_txt

def build_ngram_chain(words, n=1):
    """
    Build an n-gram Markov chain from the input words.
    
    Args:
        words (list): List of input words
        n (int): The 'n' in n-gram (1 for unigram, 2 for bigram, etc.)
        
    Returns:
        dict: Markov chain as a nested dictionary with frequency counts
        
    Raises:
        ValueError: If insufficient words for n-gram
    """
    if len(words) < n + 1:
        raise ValueError(f"Need at least {n+1} words to build a {n}-gram chain")
    
    chain = {}
    # Build chain with frequency counts
    for i in range(len(words) - n):
        current_words = tuple(words[i:i+n]) if n > 1 else words[i]
        next_word = words[i+n]
        if current_words not in chain:
            chain[current_words] = {}
        chain[current_words][next_word] = chain[current_words].get(next_word, 0) + 1
    return chain

def generate_text(chain, length=50, ngram=1, start=None):
    """
    Generate text using the Markov chain.
    
    Args:
        chain (dict): Markov chain dictionary
        length (int): Desired length of output text in words
        ngram (int): The 'n' in n-gram used
        start: Starting word(s) for generation (optional)
        
    Returns:
        str: Generated text
        
    Raises:
        ValueError: If chain is empty
    """
    if not chain:
        raise ValueError("Empty Markov chain")

    # Initialize starting state
    if start:
        current_state = start
    else:
        current_state = random.choice(list(chain.keys()))

    output = list(current_state) if isinstance(current_state, tuple) else [current_state]

    # Generate text
    while len(output) < length:
        key = tuple(output[-ngram:]) if ngram > 1 else output[-1]

        if key in chain:
            # Select next word based on frequency weights
            next_words_dict = chain[key]
            words, weights = zip(*next_words_dict.items())
            next_word = random.choices(words, weights=weights)[0]
            output.append(next_word)
        else:
            break

    return ' '.join(output)

if __name__ == "__main__":
    """
    Main execution block:
    1. Sets up data folder
    2. Reads and processes text files
    3. Builds unigram, bigram, and trigram models
    4. Generates sample text using each model
    """
    try:
        # Create path to data folder relative to the script location
        script_dir = os.path.dirname(os.path.abspath(__file__))
        data_folder = os.path.join(os.path.dirname(script_dir), 'data')
        
        # Ensure data folder exists
        if not os.path.exists(data_folder):
            os.makedirs(data_folder)
            print(f"Created data folder at: {data_folder}")
            print("Please add your .txt files to this folder and run the script again.")
            exit()
            
        print(f"Reading files from: {data_folder}")
        words = read_all_text_files(data_folder)

        # Randomly select starting word from the processed words
        starting_word = random.choice(words)
        print(f"\n[Starting word selected: '{starting_word}']")

        unigram_chain = build_ngram_chain(words, n=1)
        bigram_chain = build_ngram_chain(words, n=2)
        trigram_chain = build_ngram_chain(words, n=3)

        start_unigram = starting_word
        start_bigram = next((key for key in bigram_chain.keys() if key[0] == starting_word), random.choice(list(bigram_chain.keys())))
        start_trigram = next((key for key in trigram_chain.keys() if key[0] == starting_word), random.choice(list(trigram_chain.keys())))

        unigram_text = generate_text(unigram_chain, length=50, ngram=1, start=start_unigram)
        bigram_text = generate_text(bigram_chain, length=50, ngram=2, start=start_bigram)
        trigram_text = generate_text(trigram_chain, length=50, ngram=3, start=start_trigram)

        print("\nGenerated Text:\n")
        print(f"Unigram Text: {unigram_text}\n")
        print(f"Bigram Text: {bigram_text}\n")
        print(f"Trigram Text: {trigram_text}\n")

    except Exception as e:
        print(f"Error: {str(e)}")