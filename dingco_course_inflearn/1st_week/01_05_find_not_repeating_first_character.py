def find_not_repeating_first_character(string):
    alphabet_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        index = ord(char) - ord('a')
        alphabet_array[index] += 1

    for char in string:
        if not char.isalpha():
            continue

        index = ord(char) - ord('a')
        if alphabet_array[index] == 1:
            return chr(index + ord('a'))

    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 = _ 현재 풀이 값 =", result("aaaaaaaa"))