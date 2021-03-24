#Functions

#Palindrome count method
def num_palindromes(list):
    count = 0
    for i in list:
        if str(i) == str(i)[::-1]:
            count += 1
    return count

#Palindrome write to list
def write_palindrome(list):
    palindrom_list = []
    for i in list:
        if str(i) == str(i)[::-1]:
            palindrom_list = palindrom_list.append(i)
            return palindrom_list
        
f = open("word_list.txt", "r")
content = f.read()

#Creates a list from the contents of the text file
content_list = content.splitlines()

#Prints the count of palindromes
print(num_palindromes(content_list))

#Prints the list of palindrome
print(write_palindrome(content_list))

f.close()