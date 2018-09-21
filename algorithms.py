def de_dup(_list):
    index = 0
    new_list = []
    for item in _list:
        if item in _list[:index]:
            index += 1
            continue
        else:
            new_list.append(item)
            index += 1
    return new_list

def largest_of(_list):
    _list.sort()
    return _list[-1]

def smallest_of(_list):
    _list.sort()
    return _list[0]

def pyramid_printer(num):
    if num == 1:
        yield "*"

    median = round(num / 2)

    line = " " * num

    white = median - 1
    star = 1
    while white >= 0: 
        line = (" " * white) + ("*" * star) + (" " * white)
        white -= 1
        star += 2
        yield line

if __name__ == "__main__":

    _list = [5,6,1,3,10,20,13,29,3,1,3,4,4]

    print(de_dup(_list))

    print(largest_of(_list))

    print(smallest_of(_list))

    for line in pyramid_printer(20):
        print(line)