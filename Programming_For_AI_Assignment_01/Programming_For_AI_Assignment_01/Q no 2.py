def analyze_sentence(sentence):
    words = sentence.split()
    unique_words = set(word.lower() for word in words)
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for character in sentence if character in vowels)

    if words:
        longest_word = max(words, key=len)
        shortest_word = min(words, key=len)
    else:
        longest_word = "None"
        shortest_word = "None"

    return words, unique_words, vowel_count, longest_word, shortest_word


sentence = input("Enter a sentence: ")
words, unique_words, vowel_count, longest_word, shortest_word = analyze_sentence(sentence)
sorted_words = sorted(unique_words)

print("\nWORD ANALYSIS")
print("Total words:", len(words))
print("Total characters:", len(sentence))
print("Longest word:", longest_word)
print("Shortest word:", shortest_word)
print("Number of vowels:", vowel_count)
print("Unique words:", unique_words)
print("Words in alphabetical order:", sorted_words)

with open("word_analysis.txt", "w", encoding="utf-8") as file:
    file.write("WORD ANALYSIS\n")
    file.write("Sentence: " + sentence + "\n")
    file.write("Total words: " + str(len(words)) + "\n")
    file.write("Total characters: " + str(len(sentence)) + "\n")
    file.write("Longest word: " + longest_word + "\n")
    file.write("Shortest word: " + shortest_word + "\n")
    file.write("Number of vowels: " + str(vowel_count) + "\n")
    file.write("Unique words: " + str(unique_words) + "\n")
    file.write("Words in alphabetical order: " + str(sorted_words) + "\n")

print("\nAnalysis saved in word_analysis.txt")
