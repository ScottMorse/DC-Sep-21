WORDS = [
    (
        "zero","one","two","three",
        "four","five","six",
        "seven","eight","nine"
    ),
    [
        (
            "ten","eleven","twelve",
            "thirteen","fourteen","fifteen",
            "sixteen","seventeen","eighteen",
            "nineteen",
        ),
        
        (
            "twenty","thirty","forty",
            "fifty","sixty","seventy",
            "eighty","ninety"
        )
    ],
    "hundred",
    "thousand","thousand","thousand",
    "million","million","million",
    "billion","billion","billion",
    "trillion","trillion","trillion",
    "quadrillion","quadrillion","quadrillion",
    "quintillion","quintillion","quintillion",
    "quintrillion","quintrillion","quintrillion", 
    "sextillion","sextillion", "sextillion", 
    "septillion","septillion", "septillion", 
    "octillion","octillion","octillion",
    "nonillion","nonillion","nonillion",
    "decillion","decillion","decillion",
]

def num_description(num):

    num_str = str(num)
    length = len(num_str)

    try:

        level = WORDS[length - 1]
    except IndexError:
        raise Exception("Number too large.")
    
    if length == 1:
        return level[num]

    elif length == 2:
        if num < 20:
            return level[0][num - 10]
        else:
            if num_str[1] == "0":
                return level[1][int(num_str[0]) - 2]
            else:
                return ("-").join((level[1][int(num_str[0]) - 2],
                                    WORDS[0][int(num_str[1])]))

    elif length == 3:

        if num_str[:2] == "00":
            return num_description(int(num_str[-1]))

        if num_str[-2:] == "00":
            return ("-").join((num_description(int(num_str[0])),level,))

        return ("-").join(
            (
                num_description(int(num_str[0])),
                level,
                num_description(int(num_str[-2:])))
            )
    
    else:

        separators = length // 3
        if length % 3 == 0:
            separators -= 1
        index = length % 3
        if index == 0:
            index = 3
        result = num_description(int(num_str[:index])) + "-" + level
        rng = range(1) if separators == 1 else range(separators-1,-1,-1)
        n = 1
        for i in rng:
            next_section = int(num_str[-3 * (i+1):(-3 * i) if i > 0 else None])
            if next_section == 0:
                n += 1
                continue
            result += "-" + num_description(next_section)
            if separators > 1:
                if i < separators and i > 0:
                    result += "-" + WORDS[length - 1 - (3 * n)]
            n += 1
        return result
    
if __name__ == "__main__":

    while True:
        try:
            user_input = input("Enter any number (up to 999,99..decillion): ").strip()
            if user_input == "q":
                break
            user_input = int(user_input)
        except:
            print("Error, invalid number.")
            continue
        try:
            print(num_description(user_input).capitalize())
        except Exception:
            print("Number too large.")
            continue