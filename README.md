# Markov Text Generator

Dynamic N-gram Markov Chain text generator with efficient parallelized NLP preprocessing.

---

## Overview

This project demonstrates core concepts in Natural Language Processing (NLP) and probabilistic modeling:

- Parallelized reading and cleaning of multiple text files
- Tokenization preserving sentence boundaries
- Dynamic Unigram, Bigram, Trigram model construction
- Weighted word prediction based on real transition probabilities
- Side-by-side comparison of different N-gram models

---

## What is a Markov Chain?

A Markov Chain predicts the next step based only on the current state, not the full history.

In text modeling:
- Unigram looks at 1 word.
- Bigram uses 2 words.
- Trigram uses 3 words.

Using more context improves the coherence of generated text.
This project uses weighted chains to reflect real-world transition probabilities.

---

## Project Structure

```
markov-text-generator/
├── src/          # Code
├── data/         # Input texts
├── examples/     # Sample outputs
├── .gitignore
├── requirements.txt
├── LICENSE
└── README.md
```

---

## How to Run

```bash
git clone https://github.com/yourusername/markov-text-generator.git
cd markov-text-generator
pip install -r requirements.txt
cd src
python markov_text_generator.py
```

---

## Sample Output

Starting word: "the"

- Unigram:  
  "the forest was deep and the sun rose above the old hills..."

- Bigram:  
  "the forest was silent as the sun rose over the eastern hills..."

- Trigram:  
  "the forest was silent as dawn broke over the misty hills..."

Notice how text becomes more natural from unigram to trigram.

---

## Skills Demonstrated

- Text preprocessing and tokenization
- Markov Chain modeling
- Weighted sampling
- Parallel file processing
- Clean modular Python coding

---

## Future Enhancements

- Character-level Markov generation
- Temperature control for creative text
- Save/load trained models
- Interactive Streamlit app

---

## Learning Outcomes

Through this project, I:

- Gained intuition about Markov Chains and N-gram context.
- Practiced weighted sampling for realistic text generation.
- Learned parallel processing for faster data handling.
- Designed scalable, modular code for NLP tasks.

---

## License

Licensed under the MIT License.

---

## Connect

[Connect with me on LinkedIn](https://www.linkedin.com/in/jaroh23/)  
or [View more projects](https://github.com/Rohanjain2312)