# CS2 Project - Data Dictionary
# File I/O, Dictionaries, CSV, and Graphing with Matplotlib

import matplotlib.pyplot as plt

# -------------------------------------------------------
# STEP 1: Open and Read Both Files
# -------------------------------------------------------

macbeth_file = open("macbeth.txt", "r")
macbeth_text = macbeth_file.read()
macbeth_file.close()

caesar_file = open("julius caesar.txt", "r")
caesar_text = caesar_file.read()
caesar_file.close()

print("Files opened successfully!")

# -------------------------------------------------------
# STEP 2: Create the Dictionaries
# -------------------------------------------------------

# Filler words to ignore (called "stop words")
stop_words = [
    # Modern English filler words
    "the", "and", "to", "of", "a", "i", "in", "is", "it", "that",
    "you", "my", "with", "he", "his", "not", "this", "be", "as",
    "for", "but", "have", "your", "we", "so", "are", "was", "at",
    "by", "or", "from", "on", "all", "what", "an", "they", "no",
    "him", "do", "will", "me", "if", "our", "shall", "then",
    "her", "their", "up", "more", "which", "had", "has", "when",
    "there", "would", "she", "them", "were", "who", "come", "than",
    "out", "one", "like", "how", "may", "let", "am", "now", "into",
    "upon", "its", "about", "o", "s", "did", "yet", "could", "these",
    "been", "being", "get", "got", "go", "gone", "going", "here",
    "just", "also", "very", "too", "much", "such", "down", "over",
    "after", "before", "where", "while", "though", "through", "between",
    "each", "own", "other", "must", "can", "said", "say", "says",
    "made", "make", "know", "think", "see", "look", "take", "give",
    # Old English / Shakespearean filler words
    "thou", "thy", "thine", "thyself", "thee", "ye", "hath", "hast",
    "doth", "dost", "tis", "twas", "twere", "twill", "twixt",
    "wherefore", "whither", "thither", "hither", "hence", "thence",
    "wherein", "whereby", "thereof", "therein", "thereby", "thereupon",
    "art", "wilt", "canst", "wouldst", "shouldst", "couldst", "durst",
    "hadst", "didst", "wast", "wert", "mayst", "mightst", "shalt",
    "nay", "yea", "ay", "aye", "fie", "prithee", "forsooth", "marry",
    "ere", "oft", "ne", "tho", "betwixt", "belike", "perchance",
    "haply", "withal", "whereat", "whosoever", "whatsoever", "whoso",
    "methinks", "methought", "quoth", "spake", "mine", "aught",
    "naught", "whence", "thus", "therefore", "thereto", "herein"
]

macbeth_dict = {}
caesar_dict  = {}

# Process Macbeth
macbeth_words = macbeth_text.lower().split()

for word in macbeth_words:
    word = word.strip(".,!?;:\"'()-*")
    if word != "" and word not in stop_words:
        if word in macbeth_dict:
            macbeth_dict[word] += 1
        else:
            macbeth_dict[word] = 1

# Process Julius Caesar
caesar_words = caesar_text.lower().split()

for word in caesar_words:
    word = word.strip(".,!?;:\"'()-*")
    if word != "" and word not in stop_words:
        if word in caesar_dict:
            caesar_dict[word] += 1
        else:
            caesar_dict[word] = 1

print(f"Macbeth Dictionary:       {len(macbeth_dict)} unique words found")
print(f"Julius Caesar Dictionary: {len(caesar_dict)} unique words found")

# -------------------------------------------------------
# STEP 3: Write Key-Value Pairs to CSV Files
# -------------------------------------------------------

macbeth_sorted = sorted(macbeth_dict.items(), key=lambda x: x[1], reverse=True)[:15]
macbeth_out = open("macbeth_wordcount.csv", "w")
macbeth_out.write("Word,Count\n")
for key, value in macbeth_sorted:
    macbeth_out.write(f"{key},{value}\n")
macbeth_out.close()
print("\nMacbeth dictionary written to macbeth_wordcount.csv")

caesar_sorted = sorted(caesar_dict.items(), key=lambda x: x[1], reverse=True)[:15]
caesar_out = open("julius caesar_wordcount.csv", "w")
caesar_out.write("Word,Count\n")
for key, value in caesar_sorted:
    caesar_out.write(f"{key},{value}\n")
caesar_out.close()
print("Julius Caesar dictionary written to julius caesar_wordcount.csv")

# -------------------------------------------------------
# STEP 4: Graph Both Books Side by Side using Matplotlib
# -------------------------------------------------------

# Helper: get top 15 words sorted by count
def top_words(word_dict, n=15):
    sorted_words = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:n]

macbeth_top = top_words(macbeth_dict)
caesar_top  = top_words(caesar_dict)

macbeth_words_top  = [pair[0] for pair in macbeth_top]
macbeth_counts_top = [pair[1] for pair in macbeth_top]

caesar_words_top  = [pair[0] for pair in caesar_top]
caesar_counts_top = [pair[1] for pair in caesar_top]

# Create a figure with two side-by-side charts
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(22, 8))

# ----- Left Chart: Macbeth -----
ax1.bar(macbeth_words_top, macbeth_counts_top, color="steelblue")
ax1.set_title("Macbeth - Top 15 Most Common Words", fontsize=14, fontweight="bold")
ax1.set_xlabel("Word", fontsize=12)
ax1.set_ylabel("Count", fontsize=12)
ax1.tick_params(axis="x", rotation=45)

# ----- Right Chart: Julius Caesar -----
ax2.bar(caesar_words_top, caesar_counts_top, color="firebrick")
ax2.set_title("Julius Caesar - Top 15 Most Common Words", fontsize=14, fontweight="bold")
ax2.set_xlabel("Word", fontsize=12)
ax2.set_ylabel("Count", fontsize=12)
ax2.tick_params(axis="x", rotation=45)

plt.tight_layout()
plt.savefig("shakespeare_comparison_graph.png")
plt.show()
print("\nGraph saved to shakespeare_comparison_graph.png")
