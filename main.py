while True:
    answer = int(input("what is the product of 7 * 24 ? "))
    if answer == 168:
        print("You answered this Question correctly")
        break
    else:
        print("Your Answer is wrong try again..")


n = int(input("\nEnter a positive integer: "))

even_sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum += i


print(f"The sum of even numbers between 1 and {n} is {even_sum}.")