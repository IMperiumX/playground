/*

**1. Fundamentals (Chapters 1 & 2)**

* **Data Types & Constants:** The program uses `unsigned int` for flags, hexadecimal constants (`0x01`), and symbolic constants (`MAXLINE`) defined via the preprocessor.
* **Bitwise Operators:** The variables `options` and `OPT_...` demonstrate bitwise OR (`|`) to set flags and bitwise AND (`&`) to test them.
* **Ternary Operator:** The line `printf( (len > 80) ? ...` uses the conditional operator from Chapter 2.

**2. Control Flow (Chapter 3)**

* **Switch:** The argument parsing loop uses a `switch` statement to handle different command-line flags (`-r`, `-u`, `-x`).
* **Loops:** It utilizes `while` and `for` loops. The `get_line` function demonstrates the compact loop style `while (--lim > 0 ...)` preferred in C.

**3. Program Structure (Chapter 4)**

* **Scope:** The variable `options` is declared `static` external. This restricts its visibility to this source file, hiding it from other potential files.
* **Recursion:** The function `recursive_int_print` mimics the `printd` example from Chapter 4, calling itself to print integers character by character.
* **Register Variables:** The `to_upper` function requests a `register int` for speed, a suggestion the compiler may ignore.

**4. Pointers and Arrays (Chapter 5)**

* **Command Line Arguments:** The program reads `argc` and `argv`. It uses the pointer expression `(*++argv)` to navigate the argument vector, a key concept in Chapter 5.
* **Pointer Arithmetic:**
  * `get_line` uses pointer subtraction (`s - t`) to calculate string length.
  * `reverse` uses pointers (`s` and `t`) moving toward each other (`s < t`) rather than array indexing.
* **Function Pointers:** The variable `func_ptr` is declared as a pointer to a function. In the main loop, it is assigned the address of `to_upper` and called via `(*func_ptr)(line)`, demonstrating that functions are not variables but their addresses can be manipulated.


*/ 

#include <stdio.h>
#include <ctype.h>

/* CHAPTER 1 & 4: Symbolic Constants and Macros */
#define MAXLINE 1000
#define YES 1
#define NO  0

/* CHAPTER 2: Bitwise Masks for options */
#define OPT_REVERSE  0x01
#define OPT_UPPER    0x02
#define OPT_HEX      0x04

/* CHAPTER 4: Function Prototypes */
int get_line(char *s, int lim);
void reverse(char *s);
void to_upper(char *s);
void print_hex(char *s);
void recursive_int_print(int n); /* Recursion example */

/* CHAPTER 4: External Static Variable 
   Visible only in this source file, retains value. */
static unsigned int options = 0; 

/* CHAPTER 5: Command-line Arguments */
main(int argc, char *argv[])
{
    char line[MAXLINE];     /* Ch 1: Character Array */
    int len;
    
    /* CHAPTER 5: Pointer arithmetic to process argv 
       Check for flags like -r (reverse), -u (upper), -x (hex) */
    while (--argc > 0 && (**++argv) == '-') {
        int c;
        char *p = *argv + 1; /* Pointer to first char after '-' */
        
        /* CHAPTER 3: Switch statement inside loop */
        while (c = *p++) {
            switch (c) {
            case 'r':
                options |= OPT_REVERSE; /* Ch 2: Bitwise OR */
                break;
            case 'u':
                options |= OPT_UPPER;
                break;
            case 'x':
                options |= OPT_HEX;
                break;
            default:
                printf("Unknown option: -%c\n", c);
                return 1;
            }
        }
    }

    /* CHAPTER 5: Pointers to Functions
       We define a pointer 'func_ptr' that can point to a function 
       taking a char* and returning void. */
    void (*func_ptr)(char *); 

    /* CHAPTER 1: Main Processing Loop */
    while ((len = get_line(line, MAXLINE)) > 0) {
        
        /* CHAPTER 2: Conditional Expression (Ternary) */
        printf("Line Length: ");
        recursive_int_print(len); /* Ch 4: Recursion */
        printf( (len > 80) ? " (Long)\n" : " (Short)\n");

        /* Apply transformations based on bitwise flags */
        if (options & OPT_UPPER) {
            func_ptr = to_upper;    /* Assign address of function */
            (*func_ptr)(line);      /* Call via pointer */
        }
        
        if (options & OPT_REVERSE) {
            reverse(line);          /* Standard call */
        }

        if (options & OPT_HEX) {
            print_hex(line);
        } else {
            printf("%s", line);
        }
    }
    return 0;
}

/* CHAPTER 5: Pointer Version of getline 
   Uses pointers instead of array indexing */
int get_line(char *s, int lim)
{
    int c;
    char *t = s; /* Save start address */

    /* Ch 2: Precedence of operators */
    while (--lim > 0 && (c = getchar()) != EOF && c != '\n')
        *s++ = c;
    
    if (c == '\n')
        *s++ = c;
    
    *s = '\0';
    return s - t; /* Ch 5: Pointer Subtraction returns length */
}

/* CHAPTER 5: Pointer Arithmetic */
void reverse(char *s)
{
    int c;
    char *t;

    /* Find the end of the string using pointers */
    for (t = s; *t != '\0'; t++)
        ;
    t--; /* Back up from '\0' */
    
    /* Ch 5: Comparing pointers */
    if (*t == '\n') t--; /* Leave newline in place */

    /* Swap characters */
    while (s < t) {
        c = *s;
        *s++ = *t;
        *t-- = c;
    }
}

/* CHAPTER 2: Character Handling and Types */
void to_upper(char *s)
{
    /* Ch 4: Register variable hint */
    register int c; 

    while (*s) {
        c = *s;
        /* Ch 2: ctype.h usage was introduced early 
           but logic here mimics Ch 2 lower() example */
        if (c >= 'a' && c <= 'z')
            *s = c - 'a' + 'A';
        s++; /* Increment pointer */
    }
}

/* CHAPTER 2: Hexadecimal Constants and Casting */
void print_hex(char *s)
{
    while (*s) {
        /* Cast to unsigned char to avoid sign extension issues */
        printf("%02X ", (unsigned char)*s++); 
    }
    printf("\n");
}

/* CHAPTER 4: Recursion */
void recursive_int_print(int n)
{
    if (n < 0) {
        putchar('-');
        n = -n;
    }
    if (n / 10)
        recursive_int_print(n / 10);
    putchar(n % 10 + '0');
}


/*

Example Usage:

$ ./text_processor -u -r
input: Hello World 
output: DLROW OLLEH

$ ./text_processor -x
input: Hi
output: 48 69 0A

*/