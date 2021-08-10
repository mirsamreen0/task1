data=input("Please enter a word you want to count\n ")
def most_frequent(word):
    a = dict()
    for key in word:
        if key not in a:
            a[key] = 1
        else:
            a[key] += 1
    return a
print (most_frequent(data))