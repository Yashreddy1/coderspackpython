def most_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    dict=sorted(dict.items(), key=lambda kv: kv[1],reverse=True)
    return dict
print(most_frequency(input("enter a string: ")))
