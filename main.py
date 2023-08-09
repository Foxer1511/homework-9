with open("text_1.txt", "w") as test_file:
    test_file.write("test1test1 test1")

with open("text_1.txt", "a") as test_file:
    test_file.write("\ntest2test2\ntest21234567\nsadfasdfsadfsadf")

with open("text_1.txt", "r") as test_file:
    result = test_file.read()
    print(result)
text_v1 = result.split()
print(text_v1)

#1. Даний текстовий файл. Необхідно створити новий файл,
# який потрібно переписати з першого файлу всі слова,
# що складаються не менше ніж з семи літер.
with open("text_2.txt", "a") as test_file2:
    for i in range(len(text_v1)):
        if len(text_v1[i]) >= 7:
            test_file2.write(f"{text_v1[i]}\n")
        else:
            continue

with open("text_2.txt", "r") as test_file2:
    result2 = test_file2.read()
    print(result2)

# 2. Даний текстовий файл. Підрахувати кількість слів у ньому.
r = 0
with open("text_1.txt", "r") as test_file:
    for i in range(len(text_v1)):
        r += 1
    print(f"{r} слів у першому тексті")
#!!!

