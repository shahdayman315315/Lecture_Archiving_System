import os
from collections import Counter
import re

input_file = "Outputs/Audio_speech/transcript.txt"
output_folder = "Outputs/Summary"

os.makedirs(output_folder, exist_ok=True)

output_file = f"{output_folder}/summary.txt"

with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

words = re.findall(r'\w+', text.lower())

stop_words = set([
    "the","is","in","and","to","of","a","an","for","on","this",
    "that","it","are","was","were","be","as","with","at","by"
])

filtered = [w for w in words if w not in stop_words]

freq = Counter(filtered)

keywords = freq.most_common(10)

sentences = re.split(r'[.!?]', text)
sentences = [s.strip() for s in sentences if len(s.strip()) > 20]

scores = {}

for s in sentences:
    score = sum(1 for w in s.lower().split() if w in dict(keywords))
    scores[s] = score

top_sentences = sorted(scores, key=scores.get, reverse=True)[:5]   # الملخص
#
questions = [f"What is {k}?" for k, _ in keywords[:5]]

with open(output_file, "w", encoding="utf-8") as f:
    f.write("SMART LECTURE SUMMARY\n\n")

    f.write("SUMMARY:\n")
    for s in top_sentences:
        f.write("- " + s + "\n")

    f.write("\nKEYWORDS:\n")
    for k, v in keywords:
        f.write(f"- {k} ({v})\n")

    f.write("\nQUESTIONS:\n")
    for q in questions:
        f.write("- " + q + "\n")

print(" Summary generated")