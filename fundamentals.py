# print a greeting
print("1. Greeting")
print("Hello, Python World!")
print()

# 2. Variables and Output
print("2. Variables and Output")
name = "KIMANI"
age = 32
country = "Kenya"
print(f"My name is {name}, I am {age} years old, and I live in {country}")
print()

# 3. Basic Arithmetic
print("3. Basic Arithmetic")
a = 10
b = 5
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Division:", a / b)
print()

# 4. Even or Odd Checker
print("4. Even or Odd Checker")
num = 8
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")
print()

# 5. Simple Calculator
print("5. Simple Calculator")
num1 = 10
num2 = 5
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print()

# 6. List Operations
print("6. List Operations")
fruits = ["Apple", "Banana", "Mango", "Orange", "Pineapple"]
print("Fruits:", fruits)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

fruits.append("Grapes")
print("After adding:", fruits)

fruits.remove("Banana")
print("After removing:", fruits)
print()

# 7. Loop Through Numbers
print("7. Numbers from 1 to 10")
for i in range(1, 11):
    print(i)
print()

# 8. Sum of Numbers
print("8. Sum from 1 to 20")
total = 0
for i in range(1, 21):
    total += i
print("The sum is:", total)
print()

# 9. Multiplication Table
print("9. Multiplication Table of 5")
for i in range(1, 11):
    print(f"5 x {i} = {5*i}")
print()

# 10. Function: Square of a Number
print("10. Square Function")
def square(num):
    return num * num

print("Square of 4:", square(4))
print()

# 11. Count Vowels
print("11. Count Vowels")
word = "education"
vowels = "aeiou"
count = 0

for letter in word:
    if letter in vowels:
        count += 1

print("Number of vowels:", count)
print()

# 12. Dictionary Practice
print("12. Dictionary Practice")
student = {
    "name": "Lincoln",
    "age": 18,
    "course": "Python"
}

for key, value in student.items():
    print(key, ":", value)
print()

# 13. Find the Largest Number
print("13. Find the Largest Number")
numbers = [4, 7, 1, 9, 3]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number:", largest)
print()

# 14. Password Checker
print("14. Password Checker")
password = "mypassword123"

if len(password) >= 8:
    print("Password is strong")
else:
    print("Password is too short")
print()

# 15. Number Guessing Game
print("15. Number Guessing Game")
secret = 7
guess = int(input("Guess the number: "))

if guess > secret:
    print("Too high")
elif guess < secret:
    print("Too low")
else:
    print("Correct!")
print()

# Optional Challenge: FizzBuzz
print("Optional Challenge: FizzBuzz")
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)