
#technical test 1

# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.


def fizzBuzz(n):
    user_range = list(range(1, n+1))
    for i in user_range:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == '__main__':
    n = int(input('select a number: ').strip())
    fizzBuzz(n)