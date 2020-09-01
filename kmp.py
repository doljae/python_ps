import sys

r = sys.stdin.readline


def lps(pattern_str):
    pattern_len = len(pattern_str)
    lps_list = [0] * pattern_len
    j = 0

    for i in range(1, pattern_len):
        while j > 0 and pattern_str[i] != pattern_str[j]:
            j = lps_list[j - 1]

        if pattern_str[i] == pattern_str[j]:
            j += 1
            lps_list[i] = j
    return lps_list


def kmp(pattern_str, target_str, lps_list):
    j = 0
    result = []
    pattern_len = len(pattern_str)
    target_len = len(target_str)
    for i in range(target_len):
        while j > 0 and target_str[i] != pattern_str[j]:
            j = lps_list[j - 1]
        if target_str[i] == pattern_str[j]:
            if j == pattern_len - 1:
                result.append(i - pattern_len + 1)
                j = lps_list[j]
            else:
                j += 1
    return result


target_str = r().rstrip()
pattern_str = r().rstrip()

lps_list = lps(pattern_str)
result = kmp(pattern_str, target_str, lps_list)
print(len(result))
for item in result:
    print(item + 1, end=" ")
