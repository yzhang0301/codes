def word_freq(words):
    freq_dict = {}
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    for word, freq in freq_dict.items():
        freq_dict[word] = freq / len(words)
    return freq_dict

texts, grades = load_engtext(subset='textbooks')
text = texts[0]
words = splitwords(text)
freq_dict = word_freq(words)
print(freq_dict)
