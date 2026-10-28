

import re


# ---------------------------------------
# STEP 1: Read the raw text
# ---------------------------------------

with open("the_verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()


# ---------------------------------------
# STEP 2: Split raw text into tokens
# ---------------------------------------

result = re.split(
    r'([,.:;?!_"()\']|--|\s)',
    raw_text
)

result = [
    item.strip()
    for item in result
    if item.strip()
]


# ---------------------------------------
# STEP 3: Create vocabulary
# ---------------------------------------

all_words = sorted(set(result))

# Add special token for unknown words
all_words.append("<|unk|>")

vocab_size = len(all_words)

vocab = {
    token: integer
    for integer, token in enumerate(all_words)
}

print("Vocabulary size:", vocab_size)


# ---------------------------------------
# STEP 4: Create tokenizer
# ---------------------------------------

class SimpleTokenizer:

    def __init__(self, vocab):

        # token → ID
        self.str_to_int = vocab

        # ID → tokengit branch -M main

        self.int_to_str = {}

        for token, index in vocab.items():
            self.int_to_str[index] = token


    def encode(self, text):

        # Split text
        pre = re.split(
            r'([,.:;?!_"()\']|--|\s)',
            text
        )

        # Remove whitespace
        pre = [
            item.strip()
            for item in pre
            if item.strip()
        ]

        tokens = []

        # Convert token → ID
        for item in pre:

            if item in self.str_to_int:
                tokens.append(self.str_to_int[item])

            else:
                tokens.append(
                    self.str_to_int["<|unk|>"]
                )

        return tokens


    def decode(self, ids):

        words = []

        # Convert ID → token
        for idx in ids:
            words.append(self.int_to_str[idx])

        # Join tokens
        text = " ".join(words)

        # Remove space before punctuation
        return re.sub(
            r'\s+([,.:;!?()"’\'])',
            r'\1',
            text
        )


# ---------------------------------------
# STEP 5: Test tokenizer
# ---------------------------------------

tokenizer = SimpleTokenizer(vocab)

text = "Hello, My name is Ashutosh Kumar"

ids = tokenizer.encode(text)

print("Text:", text)
print("IDs:", ids)

decoded_text = tokenizer.decode(ids)

print("Decoded:", decoded_text)


# --------------------

# --------------------