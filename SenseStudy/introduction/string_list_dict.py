string = "Hello World!"
print(string)
print("1234")
print(string[1])
print(string[1:4])

#----------------------------------------------

l1 = [1, 3, 5, 7, 9, 11]
l2 = [1, 'a', ['3.14', 1.5], 'bc']

print(l1[2])
print(l2[3])

l1[1] = 20
print(l1)

print(l2[1:3])
print(l2[:3])
print(l2[-2:])

l2.append('a')
print(l2)

print(len(l1))
print(len(l2))

for i in l1:
    print(i)

l1 = [0]*3 
l2 = ['a']*5 

print(l1)
print(l2)

#----------------------------------------------

word_freq_dict = {'you': 0.098, 'the': 0.020, 'friend': 0.059}
print(word_freq_dict)
print(word_freq_dict['you'])
word_freq_dict['you'] = 0.088
print(word_freq_dict)
word_freq_dict['her'] = 0.0392
print(word_freq_dict)
word_freq_dict = {0: 0.098, 1: 0.020, 2: 0.059}
print(word_freq_dict[1])
a = [0.098,0.020,0.059]
print(a[1])

print('you' in word_freq_dict)
print('he' in word_freq_dict)

for key, value in word_freq_dict.items():    
    print(key+':'+str(value))
