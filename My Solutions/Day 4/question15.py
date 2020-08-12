# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
#
# Suppose the following input is supplied to the program:
#
# 9
# Then, the output should be:
#
# 11106

def quick_maths(num):
    result = 0
    for i in range(1, 4 + 1):
        print(i)
        temp_value = num ** i
        print(temp_value)
        result += temp_value
        print(result)

    return result


print(quick_maths(9))

a = input()
total = int(a) + int(2*a) + int(3*a) + int(4*a)  # N*a=Na, for example  a="23", 2*a="2323",3*a="232323"
print(total)
