Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# -------------------------Q1----------------------
import sys
print(">>>>>>>>>>>>>>>>>>>Q1<<<<<<<<<<<<<<<<<<<<<")

print("Printing Tower Of Hanoi with one disc at a time\n")


def Tower_Of_Hanoi(n, source_Rod, dest_Rod, middle_Rod):
    # for base case works
    if n == 1:
        print("Moving disk 1 from rods", source_Rod, "to  rods", dest_Rod)
        return
    # for assuming  f(n-1) works
    Tower_Of_Hanoi(n-1, source_Rod, middle_Rod, dest_Rod)
    print("Move Disk", n, "from rods", source_Rod, "to rods", dest_Rod)
    # for showing f(n) works using f(n-1)
    Tower_Of_Hanoi(n-1, middle_Rod, dest_Rod, source_Rod)


n = 3
Tower_Of_Hanoi(n, 'A', 'C', 'B')
print("---------------------+++++++++++++++------------------------")


# ----------------------------Q2---------------------------
print(">>>>>>>>>>>>>>>>>>>Q2<<<<<<<<<<<<<<<<<<<<<")
num_row = int(input("Enter number of rows you want\n"))


def RecPascal(n, m=1, prev=[]):
    if m > n+1:
        return []
    elif m == 1:
        return RecPascal(n, m+1, [1])
    else:
        return [prev] + RecPascal(n, m+1, calculate(prev))


def calculate(prev):
    res = [0]*(len(prev)+1)
    res[0], res[-1] = 1, 1
    for i in range(0, len(res)):
        if res[i] == 0:
            res[i] = prev[i-1] + prev[i]
    return res


for line in RecPascal(num_row):
    print(line)

print("---------------------+++++++++++++++------------------------")


# --------------------------Q3--------------------------------------------


print(">>>>>>>>>>>>>>>>>>>Q3<<<<<<<<<<<<<<<<<<<<<")
Ask_1 = int(input("Enter First number as Dividend\n"))
Ask_2 = int(input("Enter Second number as Divider\n"))


def Cal_Remainder(ask_1, ask_2):
    return ask_1 % ask_2


def Cal_Quatation(ask_1, ask_2):
    return ask_1 // ask_2


print("Remainder")
print(Cal_Remainder(Ask_1, Ask_2))
print("Quatation")
print(Cal_Quatation(Ask_1, Ask_2))
print("")

# a)part:---
print("a)part")
print("Checking callabration for Cal_Remainder")
print(callable(Cal_Remainder))
print("Checking callabration for Cal_Quatation")
print(callable(Cal_Quatation))
print("")
# b)part:---
print("b)part")


bool_arr_1 = (Ask_1 != 0)
bool_arr_2 = (Ask_2 != 0)
bool_arr_3 = (Cal_Remainder != 0)
bool_arr_4 = (Cal_Quatation != 0)


print("Checking non-zero value for Dividend ")
print(bool_arr_1)
print("Checking non-zero value for Divider")
print(bool_arr_2)
print("Checking non-zero value for Remainder")
print(bool_arr_3)
print("Checking non-zero value for Quatation")
print(bool_arr_4)
print("")

# c)part
print("c)part")


def Add_Num_1(n):
    return 4 + n


def Add_Num_2(n):
    return 5 + n


def Add_Num_3(n):
    return 6 + n


test_list = [Add_Num_1(Cal_Remainder(Ask_1, Ask_2)), Add_Num_2(Cal_Remainder(Ask_1, Ask_2)), Add_Num_3(Cal_Remainder(
    Ask_1, Ask_2)), Add_Num_1(Cal_Quatation(Ask_1, Ask_2)), Add_Num_2(Cal_Quatation(Ask_1, Ask_2)), Add_Num_3(Cal_Quatation(Ask_1, Ask_2))]


test_list_1 = []
for x in test_list:
    if x > 4:
        test_list_1.append(x)

print("Printing Number greater than 4 ")
print(test_list_1)
print("")

# d) part:--->
print("d)part")
print("Printing Set form")
converted_set = set(test_list_1)
print(converted_set)
print("")

# e)part:)---->
print("e)part")

new_set = frozenset(converted_set)
print(new_set)
print("")

# d)part:)--->>
print("d)part")
print("Max value of set is %d " % (max(new_set)))
# printing Hash value
print("The integer hash value of max number is : " + str(hash(max(new_set))))
print("---------------------+++++++++++++++------------------------")


# ---------------------------------Q4----------------------------
print(">>>>>>>>>>>>>>>>>>>Q4<<<<<<<<<<<<<<<<<<<<<")


class PECStudent:
    # default constructor
    def __init__(self, name, SID):

        self.name = name
        self.SID = SID

    def display(self):
        print("SID: %d \nName: %s" % (self.SID, self.name))

    def __del__(self):
        print("Object has been deleted")


obj_1 = PECStudent("Kanish", 21103070)
obj_2 = PECStudent("Mishank", 21103170)
obj_3 = PECStudent("Vaibhav", 21103071)
obj_4 = PECStudent("Anish", 21103069)
obj_5 = PECStudent("Tanvi", 21103074)
# calling the instance method using the object obj


obj_1.display()
obj_2.display()
obj_3.display()
obj_4.display()
obj_5.display()
print("---------------------+++++++++++++++------------------------")

# ------------------------Q5------------------------


print(">>>>>>>>>>>>>>>>>>>>>>>>>Q5<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")


class Employee:
    # default constructor
    def __init__(self, name_1, Salary):

        self.name_1 = name_1
        self.Salary = Salary

    def display(self):
        print("Employee name : %s\n Salary : %d " % (self.name_1, self.Salary))

    def __del__(self):
        print("Object has been deleted")


Employee_1 = Employee("Mehak", 40000)
Employee_2 = Employee("Ashok", 50000)
Employee_3 = Employee("Viren", 60000)

# calling the instance method using the object obj


Employee_1.display()
Employee_2.display()
Employee_3.display()


# a) updating salary of mehak
print("a)Updating salary of mehak")
Employee_1.Salary = 70000
print("")
Employee_1.display()
# b)Deleting record of Viren
print("")
print("b)Deleting record of Viren")
print("")

del Employee_3
print("")
Employee_1.display()
print("")
Employee_2.display()
print("")
print("---------------------+++++++++++++++------------------------")

# ------------------------Q6------------------------
print(">>>>>>>>>>>>>>>>>>>>>>>>>Q6<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

Georage = input("George Enter a Word\n")
Barbie = input("Barbie Enter a Word\n")


def anagrams(word):
    if word == "":
        return [word]
    else:
        Word_2 = []
        for w in anagrams(word[1:]):
            for pos in range(len(w) + 1):
                Word_2.append(w[:pos] + word[0] + w[pos:])
        return Word_2


lst = anagrams(Georage)
if Barbie in lst:
    print("True Friends")
else:
    print("Fake Friends")
print("---------------------+++++++++++++++------------------------")