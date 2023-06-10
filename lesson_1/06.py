import locale

def_coding = locale.getpreferredencoding()
print(def_coding)

with open("test_file.txt") as f_n:
    for el_str in f_n:
        print(el_str)

with open('test_file.txt', encoding='utf-8') as f_n:
    for el_str in f_n:
        print(el_str, end='')