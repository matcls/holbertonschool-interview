
# 0x1B. Radix Sort

## Description

![Radix sort](https://i.imgur.com/EPGR0fQ.png)

Function that sorts an array of integers in ascending order using the Radix sort algorithm
* Must implement the LSD radix sort algorithm
* Assume that array will contain only numbers >= 0
* Allowed to use malloc and free for this task
* Print the array each time you increase your significant digit (See example below)

**Prototype:**
```C
void radix_sort(int *array, size_t size);
```

For this project you are given the following print_array function:

```bash
$ cat `print_array.c`
```

```C
#include <stdlib.h>
#include <stdio.h>

/**
 * print_array - Prints an array of integers
 *
 * @array: The array to be printed
 * @size: Number of elements in @array
 */
void print_array(const int *array, size_t size)
{
    size_t i;

    i = 0;
    while (array && i < size)
    {
        if (i > 0)
            printf(", ");
        printf("%d", array[i]);
        ++i;
    }
    printf("\n");
}
```


```bash

$ cat 0-main.c
```

```C
#include <stdio.h>
#include <stdlib.h>
#include "sort.h"

/**
 * main - Entry point
 *
 * Return: Always 0
 */
int main(void)
{
    int array[] = {19, 48, 99, 71, 13, 52, 96, 73, 86, 7};
    size_t n = sizeof(array) / sizeof(array[0]);

    print_array(array, n);
    printf("\n");
    radix_sort(array, n);
    printf("\n");
    print_array(array, n);
    return (0);
}
```
## Usage
#### In a terminal emulator:

```bash
#First compile the source code
$ gcc -Wall -Wextra -Werror -pedantic 0-main.c 0-radix_sort.c print_array.c -o radix

$ ./radix
# Run the program
19, 48, 99, 71, 13, 52, 96, 73, 86, 7

71, 52, 13, 73, 96, 86, 7, 48, 19, 99
7, 13, 19, 48, 52, 71, 73, 86, 96, 99

7, 13, 19, 48, 52, 71, 73, 86, 96, 99

$
```

## Author
* **Manuel Torres Vesga** - [matcls](https://github.com/matcls)
