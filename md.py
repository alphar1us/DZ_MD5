import hashlib


def hash_chek(path):
    m = hashlib.md5()

    with open(path, encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            m.update(line.encode('utf-8'))
            yield m.hexdigest()

if __name__ == '__main__':
    generator = hash_chek('countries_with_links.txt')

    for item in generator:
        print(item)
    print('файл прочитан')



