# Accountable_combinantions
To find all possible combinations from an array of float elements given and a desired final number.

# Below you can see the program:

print("Welcome! \n Here, you will get all possible combinations from an array for a total quantity.\n")

#n = int(input("Input the total number of elements: "))

print("Input the elements (Remember to use space between numbers, \n once ready press enter):\n ")
x = [float(i) for i in input().split()]
obo = float(input("\nInput the total: "))
print("\nLas combinaciones son:\n")
def programa(numbers, target, partial=[]):
    s = sum(partial)
    if s == target:
        print("%s=%s" % (partial, target))
    if s >= target:
        return
        
    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        programa(remaining, target, partial + [n])

if __name__ == "__main__":
    programa(x, obo)
input("\nPress enter to close the program.")

Enjoy!
