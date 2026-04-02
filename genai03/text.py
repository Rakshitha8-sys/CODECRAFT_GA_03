import random
import string

# Step 1: Take input from user
text = input("Enter your text:\n")

# Step 2: Preprocess text
text = text.lower()
text = text.translate(str.maketrans('', '', string.punctuation))
words = text.split()

# Step 3: Build Markov Chain
markov_chain = {}

for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]

    if current_word not in markov_chain:
        markov_chain[current_word] = []

    markov_chain[current_word].append(next_word)

# Step 4: Generate Text
current_word = random.choice(words)
generated_text = [current_word]

for _ in range(20):
    if current_word in markov_chain:
        next_word = random.choice(markov_chain[current_word])
        generated_text.append(next_word)
        current_word = next_word
    else:
        break

# Step 5: Print result
print("\nGenerated Text:\n")
print(" ".join(generated_text))