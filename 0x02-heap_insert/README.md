# 0x02. Heap Insert

## Tasks
### 0. New node<br/>
	- Write a function that creates a binary tree node:
		* Prototype: binary_tree_t *binary_tree_node(binary_tree_t *parent, int value);
		* parent is a pointer to the parent node of the node to create
		* value is the value to put in the new node
		* When created, a node does not have any children
		* Your function must return a pointer to the new node, or NULL on failure

### 1. Heap - Insert<br/>
	- Write a function that inserts a value into a Max Binary Heap:
		* Prototype: heap_t *heap_insert(heap_t **root, int value);
		* root is a double pointer to the root node of the Heap
		* value is the value to store in the node to be inserted
		* Your function must return a pointer to the inserted node, or NULL on failure
		* If the address stored in root is NULL, the created node must become the root node.
		* You have to respect a Max Heap ordering
		* You are allowed to have up to 6 functions in your file

## Test
### On a terminal
- Compile
> gcc -Wall -Wextra -Werror -pedantic binary_tree_print.c 0-main.c 0-binary_tree_node.c -o 0-node<br> \
> gcc -Wall -Wextra -Werror -pedantic binary_tree_print.c 1-main.c 1-heap_insert.c 0-binary_tree_node.c -o 1-heap_insert
- Execute
> /0-node<br> \
>  ./1-heap_insert
---

## Author
* **Manuel Torres Vesga** - [matcls](https://github.com/matcls)