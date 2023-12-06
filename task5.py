
# 1. Counting vowels in a string:

def counting_vowels(string):
    string = string.upper()
    vowel = "AEIOU"
    vowel_count = 0
    for alphabets in string:
        if alphabets in vowel:
            vowel_count+=1

    print("Total number of vowels:", vowel_count)

string = "Guvi Geeks Network Private Limited"

counting_vowels(string)


# 2. Creating a pyramid of numbers from 1 to 20 using for loop:

n = 20 # number of rows

for row in range (1, n+1): 
    for col in range(1,row+1):
        print(row , end=" ")
    print()



# 3. Removing the vowels from the  string:

def remove_vowels(string):
    vowels = "aeiouAEIOU"
    answer = ""
    for alphabets in string:
        if alphabets not in vowels:
            answer+= alphabets
    return answer

string = "This is a python task"
answer = remove_vowels(string)
print (answer)



# 4. To find the length of unique characters in a string:

string = input("Please type the string:")
unique_character = set(string)
print(unique_character)
print(len(unique_character))



# 5. A string is a palindrome or not: 

def is_palindrome(string):
    return string == string[::-1]

string = input()
answer = is_palindrome(string)

print(answer)




# 7. Returns the most frequent character in a string:

def frequent_character(string):

    my_list = {}

    for alphabets in string:
        if alphabets in my_list:
            my_list [alphabets] += 1
    
        else:
            my_list[alphabets] = 1

    frequent_character = max(my_list,key=my_list.get)
    return frequent_character

string = "hello world"
answer = frequent_character(string)
print(answer)



# 8. Check if two strings are anagrams:

def anagrams (string1 , string2):
    string1 = string1.lower()
    string2 = string2.lower()

    if sorted(string1) == sorted(string2):
        print ( "True")
    else: 
        print ("False")

string1 = input("Please enter the first string:")
string2 = input("Please enter the seconf string:")

anagrams(string1,string2)












    

        









