''''
Have the function ArrayAdditionI(arr) take the array of numbers stored in arr
and return the string true if any combination of numbers in the array can be
added up to equal the largest number in the array, otherwise return the string
false. For example: if arr contains [4, 6, 23, 10, 1, 3] the output should
return true because 4 + 6 + 10 + 3 = 23. The array will not be empty, will not
contain all the same elements, and may contain negative numbers.
Examples:
Input: [5, 7, 16, 1, 2]
Output: false
Input: [3, 5, -1, 8, 12]
Output: true
'''

def AddLargestNum(arr):
    arr = sorted(arr)
    maximum = arr[-1]
    arr = arr[:1]
    total = 0

    for i in range(len(arr)):

        total = total + arr[i]
        if total == maximum:
            return 'true'

        for j in range(len(arr)):
            if j != i:
                total = total + arr[j]
                if total == maximum:
                    return 'true'

        for k in range(len(arr)):
            if k != i:
                total = total + arr[k]
                if total == maximum:
                    return 'true'

        return 'false'

'''
Have the function CommandLine(str) take the
str parameter being passed which represents the
parameters given to a command in an old PDP
system. The parameters are alphanumeric tokens
(without spaces) followed by an equal sign and by
their corresponding value. Multiple parameters/value
pairs can be placed on the command line with a single
space between each pair. Parameter tokens and values
cannot contain equal signs but values can contains 
spaces. The purpose of the function is to isolate
the parameters and values to return a list of 
parameter and value lengths. It must provide its
result in the same format and in the same order
by replacing each entry (tokens and values) by its
corresponding length.
For example, if str is: "SampleNumber=3234 provider=
Dr. M. Welby patient=John Smith priority=High" then
your function should return the string "12=4 8=12 
7=10 8=4" because "SampleNumber" is a 12 character
token with a 4 character value("3234") followed by 
"provider" which is an 8 character token by a 12
character value ("Dr. M. Welby"), etc.
Examples:
Input: "letters=A B Z T numbers=1 2 26 20 combine=true"
Output "7=7 7=9 6=4"
'''
def CommandLine(strParam):
    str_arr = strParam.split("=")
    right_side = []
    solutions = []
    count = 1
    for i in range(len(str_arr)):
        if str_arr[i].count(" ") > 1:
            right_side.append((str_arr[i])[:str_arr[i].rfind(' ')].strip())
            right_side.append((str_arr[i])[str_arr[i].rfind(' '):].strip())
        else:
            right_side.append(str_arr[i])
    for i in range(0, len(right_side), 2):
        sol = str(len(right_side[i])) + "=" + str(len(right_side[count]))
        solutions.append(sol)
        count = count + 2
    return " ".join(solutions)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(AddLargestNum([2, 4, 7 ,15 ,2] ))
    print(CommandLine("letters=A B Z T numbers=1 2 26 20 combine=true"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
