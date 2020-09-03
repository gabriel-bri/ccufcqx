#include <stdio.h>

int main()
{
    int n1, n2, n3;
    char l1, l2, l3;
    
    scanf("%d%d%d", &n1, &n2, &n3);
    
    if(n1 > n2 && n2 > n3){
        printf("G M P");
    }
    
    else if(n1 > n3 && n3 > n2) {
        printf("G P M");
    }
    
    else if(n2 > n1 && n1 > n3) {
        printf("M G P");
    }
    
    else if(n2 > n3 && n3 > n1) {
        printf("P G M");
    }
    
    else if(n3 > n1 && n1 > n2) {
        printf("M P G");
    }
    
    else {
        printf("P M G");
    }
    
    return 0;
}
