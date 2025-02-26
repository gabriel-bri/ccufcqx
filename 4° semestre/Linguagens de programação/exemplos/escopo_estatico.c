#include <stdio.h>
int x = 0;
void foo() {
    x++;
}
void bar() {
    int x = 0;
    foo();
}
int main() {
    bar();
    printf("%d", x);
}
