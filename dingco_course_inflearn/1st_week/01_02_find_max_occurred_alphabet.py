def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26
    max_index = 0
    max_occurrence = 0

    for alphabet in string:
        if not alphabet.isalpha():
            continue
        index = ord(alphabet) - ord('a')
        alphabet_occurrence_array[index] += 1

    for i in range(len(alphabet_occurrence_array)):
        if alphabet_occurrence_array[i] > max_occurrence:
            max_occurrence = alphabet_occurrence_array[i]
            max_index = i

    return chr(max_index + 97)


result = find_max_occurred_alphabet

print("정답 = i 현재 풀이 값 = ", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 = ", result("we love algorithm"))
print("정답 = b 현재 풀이 값 = ", result("best of best youtube"))

