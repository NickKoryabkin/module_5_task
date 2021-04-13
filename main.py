print("Исходные данные")
f = open("1.txt", "r")
print(f.read())



FIND = "tmp"
INFILE = "1.txt"
OUTFILE = "2.txt"
ENC = "utf-8"
print("Данные после выполнения задачи")
with open(INFILE, encoding=ENC) as infile, open(OUTFILE, "w", encoding=ENC) as outfile:
    for line in infile:
        if FIND not in line:
            outfile.write(line)
f = open("2.txt", "r")
print(f.read())