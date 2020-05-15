b=(input('enter a string: '))
def most_frequent(a):
    b=set(a)
    for i in b:
        print(i,'= '+str(a.count(i)))


most_frequent(b)
