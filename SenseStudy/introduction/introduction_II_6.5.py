diff_level = load_private("diff_level")
texts, grades = load_engtext(subset='rdtrain')
text = texts[0]
words = splitwords(text)
print(len(words))

def get_freq_per_grade(article_text, diff_level):
    words = splitwords(article_text)
    grade_freq = [0]*12
    for word in words:
        if word in diff_level:
            grade = diff_level[word]
            grade_freq[grade] += 1
        else:
            continue
    num = sum(grade_freq)
    for i in range(12):
        grade_freq[i] /= num
    return grade_freq

grade_freq = [0]*12
for word in words:
    if word in diff_level:
        grade = diff_level[word]
        grade_freq[grade] += 1
    else:
        continue
print(grade_freq)
num = sum(grade_freq)
for i in range(12):    
    grade_freq[i] /= num
print(grade_freq)

texts, grades = load_engtext(subset='rdtrain')
text1 = texts[1]
grade_freq=get_freq_per_grade(text1,diff_level)

print(grade_freq)
