#taking the integer input
n = int(input())
word_list = []
used_words = []
for i in range(n):
    word_list.append(input())
print(len(set(word_list)))
for i in word_list:
    if i not in used_words:
        print(word_list.count(i), end = " ")
        used_words.append(i)
    else:
        pass
    
    
#This is slow so showed run time error
    