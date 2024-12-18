#include <stdio.h>

int main (void){
  printf("Hello World\n");
  int age = 20;
  (age > 19) ? printf("Adult") : printf("Teenager");

int myAge = 43;
int*ptr = &myAge;

printf("%d\n", myAge);
printf("%p\n", &myAge);
printf("%p\n", ptr);

age = 18;
    (age > 19) ? printf("Adult") : printf("Teenager");

  printf("ANSI :%d\n", __STDC__);

  return 0;

}

