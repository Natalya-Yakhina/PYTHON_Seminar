# 22. Напишите программу, удаляющую из текста все слова, содержащие "абв".

# def find_num(lst):
#     for i in range(1, len(lst)):
#         if lst[i] - lst[i - 1] > 1:
#             return i, lst[i] - 1
#     return -1, -1


# with open("data.txt", "r") as fin:
#     lst = [int(i) for i in fin.readline().split()]
#     print(lst)
#     pos, num = find_num(lst)
#     print(pos,num)
#     if (pos != -1):
#         lst.insert(pos, num)
#     print(lst)

with open("words.txt", "r") as fin:
    for line in fin:
        words = line.split()
        for word in words:
            if "абв" in word:
                words.remove(word)
        sentence = " ".join(words)
        print(sentence)