# 给定一个字符串，只包含字母和数字，按要求找出字符串中的最长（连续）子串的长度，字符串本身是其最长的子串，子串要求：
#1、 只包含1个字母(a~z, A~Z)，其余必须是数字；
#2、 字母可以在子串中的任意位置；
# 如果找不到满足要求的子串，如全是字母或全是数字，则返回-1。

# 输入：字符串(只包含字母和数字)
# 输出：子串的长度

def helper(s):
    n = len(s)
    if n == 0 or n == 1 or s.isalpha() or s.isdigit():
        return -1

    maxlength = -1
    start = 0
    has_letter = False
    end = 0
    while not s[end].isalpha():
        end += 1
    if end != 0:
        maxlength = end - start + 1

    for end in range(n):
        # 如果是字母
        if s[end].isalpha():
            if has_letter:
                while start < end and s[start].isdigit():
                    start += 1
                start += 1  # 跳过这个字母
            else:
                has_letter = True
        # 数字无脑加
        elif not has_letter:
            start = end + 1

        if has_letter and end - start + 1 > maxlength:
            maxlength = max(maxlength, end - start + 1)
    return maxlength

s = "aa234556223141ASAFG32a56tt8910t13k234556223141"
print(helper(s))