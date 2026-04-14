s=list(map(str, input("Enter the words: ").split()))
b=list(set(s))
for i in range(len(b)):
    print(f"""{i+1} --> ["{b[i]}"]""")