# 0x08. Palindrome integer

## Description
Function in C that checks whether or not a given unsigned integer is a palindrome.
 
 **Prototype:**
```C
int is_palindrome(unsigned long n);
```
* Where n is the number to be checked

* Return ```1``` if ```n``` is a palindrome, and ```0``` otherwise

#### Requirements:
* Not allowed to allocate memory dynamically (malloc, calloc, …)

## Usage
#### In a terminal or emulator:
```bash
# First compile the source code
$ gcc -Wall -Wextra -Werror -pedantic -g3 -o palindrome 0-main.c 0-is_palindrome.c
# Run the program
$ ./palindrome 1
1 is a palindrome.

$ ./palindrome 11
11 is a palindrome.

$ ./palindrome 112
112 is not a palindrome.

$ ./palindrome 121
121 is a palindrome.

$ ./palindrome 12345678987654321
12345678987654321 is a palindrome.

$ ./palindrome 123456789987654321
123456789987654321 is a palindrome.

$ ./palindrome 1234567898654321
1234567898654321 is not a palindrome.
```

## Author
* **Manuel Torres Vesga** - [matcls](https://github.com/matcls)
