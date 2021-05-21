# 0x04. Sandpiles sum

## Description
### Function that computes the sum of two sandpiles
* Prototype:
```C
void sandpiles_sum(int grid1[3][3], int grid2[3][3]);
```
* both grid1 and grid2 are individually stable
* A sandpile is considered stable when none of its cells contains more than 3 grains
* When done, grid1 must be stable
* Not allowed to allocate memory dynamically

## Usage
```sh
mat@~/0x04-sandpiles$ gcc -Wall -Wextra -Werror -pedantic 0-main.c 0-sandpiles.c -o 0-sandpiles
mat@~/0x04-sandpiles$ ./0-sandpiles
3 3 3   1 3 1
3 3 3 + 3 3 3
3 3 3   1 3 1
=
4 6 4
6 6 6
4 6 4
...
```

```bash
mat@~/0x04-sandpiles$ gcc -Wall -Wextra -Werror -pedantic 1-main.c 0-sandpiles.c -o 0-sandpiles
mat@~/0x04-sandpiles$ ./0-sandpiles 
0 0 0   3 3 3
0 0 0 + 3 3 3
0 0 0   3 3 3
=
3 3 3
3 3 3
3 3 3
```
---

## Author
* **Manuel Torres Vesga** - [matcls](https://github.com/matcls)