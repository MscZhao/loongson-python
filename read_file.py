file = open("file.txt", "r")
print(file.read())
file.close()

file = open("file.txt", "rb")
print(file.read().decode("utf8"))
file.close()

with open("file.txt", "r") as f:
    n=1
    while 1:
        content = f.readline()
        if content:
           print(f"第{n}行: {content}")
           n = n + 1
        else:
            break