print("Исходные данные")
f = open("1.txt", "r")
print(f.read())



a = "tmp"
b = "1.txt"
c = "2.txt"
ENC = "utf-8"
print("Данные после выполения задачи:")
with open(b, encoding=ENC) as b, open(c, "w", encoding=ENC) as c:
    for line in b:
        if a not in line:
            c.write(line)
f = open("2.txt", "r")
print(f.read())