index = 10


def func2():
    global index
    index += 1
    print(index)


if __name__ == '__main__':
    func2()
