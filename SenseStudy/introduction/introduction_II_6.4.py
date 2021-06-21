texts,grades=load_engtext(subset='textbooks')
print(len(texts))
#print(texts[0:4])
print(grades[0:4])

def get_diff_level(article_list, grade_list):
    diff_level = {}
    for text, grade in zip(article_list, grade_list):
        words = splitwords(text)
        for word in words:
            if word in diff_level and diff_level[word] <= grade:
                continue
            else:
                diff_level[word] = grade
    return diff_level

diff_level=get_diff_level(texts,grades)
print(diff_level)

save_private(diff_level, "diff_level")
