# Markov Text Generator 📜

**A fast, scalable Markov Chain text generator with dynamic N-gram modeling and parallelized NLP preprocessing.**

---

## 🚀 Overview

This project implements a **Markov Chain-based language model** to generate coherent, context-sensitive text.  
It demonstrates key concepts in **Natural Language Processing (NLP)** and **probabilistic modeling**:

- Parallelized loading and cleaning of large text corpora
- Intelligent tokenization preserving sentence boundaries (`.`)
- Dynamic construction of **Unigram, Bigram, and Trigram** chains
- **Weighted next-word prediction** based on real transition probabilities
- Side-by-side comparison of **different N-gram models** to understand how context size impacts text generation

---

## 📚 What is a Markov Chain (Simple Explanation)

A **Markov Chain** is a model that predicts **what comes next** based only on the **current state**, **not the full history**.

> In simple terms:  
> If you know where you are **now**, that's enough to guess what happens **next** — you don't need to remember how you got here.

In language modeling:
- A **Unigram model** picks the next word based only on the current word.
- A **Bigram model** picks the next word based on the last two words.
- A **Trigram model** uses the last three words for even richer predictions.

The more context you use (bigrams, trigrams), the more **coherent and realistic** your generated text becomes.

This project demonstrates these ideas practically by building **weighted Markov Chains** — meaning the next word is chosen based on how often it realistically follows, not randomly.

---

## 📂 Project Structure

```bash
markov-text-generator/
├── src/
│   └── markov_text_generator.py        # Core codebase
├── data/
│   └── sample_texts.txt                 # (Training files)
├── examples/
│   └── output_samples.md                # Generated examples
├── .gitignore
├── requirements.txt
├── LICENSE
└── README.md
```

---

## ▶️ How to Run

```bash
git clone https://github.com/yourusername/markov-text-generator.git
cd markov-text-generator
pip install -r requirements.txt
cd src
python markov_text_generator.py
```

- By default, the script reads all `.txt` files in `data/`
- Generates Unigram, Bigram, and Trigram outputs
- Compares the different outputs starting from the same initial word

---

## Sample Output

> **Starting word:** "the"

- **Unigram Model:**  
  _"the forest was deep and the sun rose above the old hills where the hobbits rested before..."_

- **Bigram Model:**  
  _"the forest was silent as the sun rose over the eastern hills and the travelers rested before continuing..."_

- **Trigram Model:**  
  _"the forest was silent as dawn broke over the misty hills and the travelers prepared for their long journey..."_

(Notice how coherence improves from Unigram ➔ Bigram ➔ Trigram.)

---

##  Skills Demonstrated

- **Natural Language Processing**: Cleaning, tokenization, context-aware generation
- **Markov Chain Modeling**: Understanding state transitions and memoryless processes
- **Weighted Sampling**: Realistic prediction based on transition frequencies
- **Parallel Programming**: Fast text ingestion using `concurrent.futures`
- **Python Engineering**: Clean, modular, efficient code design

---

##  Future Enhancements

- Implement **character-level Markov Chains** for style mimicry
- Add **temperature control** for tuning randomness in text generation
- Build a **Streamlit UI** to interactively generate text
- Save/load trained Markov models for faster runtime

---

##  Learning Outcomes

Building this project deepened my understanding of both **NLP fundamentals** and **probabilistic modeling**:

- I developed a strong intuition for how **Markov Chains** model sequential decision-making, especially how memory length (N-grams) affects the quality of generated text.
- I learned how to **tokenize real-world text corpora** carefully, preserving sentence boundaries and handling encoding inconsistencies across different file types.
- I understood the value of **weighted sampling** in probabilistic models to produce more **natural-sounding** and **realistic** outputs rather than purely random sequences.
- I practiced writing **modular, scalable Python code**, including **parallelized file processing** to handle larger datasets efficiently.
- This project also helped me appreciate the **tradeoffs between model complexity and output quality**, especially when experimenting with Unigram vs Bigram vs Trigram models.

---
