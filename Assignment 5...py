def factorial(i):
    if i == 0:
        return 1
    else:
        return i * factorial(i - 1)


n = int(input("Input a number to compute the factorial : "))
print(factorial(n))


def string_test(s):
    d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"] += 1
        elif c.islower():
            d["LOWER_CASE"] += 1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["UPPER_CASE"])
    print("No. of Lower case Characters : ", d["LOWER_CASE"])


string_test('Hello This is Pakistan')

list1 = [10, 21, 4, 45, 66, 93, 57, 89, 56, 94]

for num in list1:

    if num % 2 == 0:
        print(num, end=" ")


def isPalindrome(string):
    left_pos = 0
    right_pos = len(string) - 1

    while right_pos >= left_pos:
        if not string[left_pos] == string[right_pos]:
            return False
        left_pos += 1
        right_pos -= 1
    return True


print(isPalindrome('madam'))


def test_prime(i):
    if i == 1:
        return False
    elif i == 2:
        return True;
    else:
        for x in range(2, i):
            if i % x == 0:
                return False
        return True


print(test_prime(13))


def shopping(*items):
    for item in items:
        print("You Selected", item)

        shopping('Mango', 'Banana', 'Apple')
