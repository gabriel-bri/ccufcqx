#include <stdio.h>

int main(){
    
    int num[5];
    int num2[5];    
    for(int i = 0; i < 5; i++) {
        printf("Digite o %d número do primeiro conjunto >", i);
        scanf("%d", &num[i]);
    }
    
    for(int i = 0; i < 5; i++) {
        printf("Digite o %d número do segundo conjunto >", i);
        scanf("%d", &num2[i]);
    }
    
    for(int i = 0; i < 5; i++) {
        if(i == 0) 
            printf("%d - %d = %d \r\n", num[i], num2[4], num[i] - num2[4]);
        
        else
            printf("%d - %d = %d \r\n", num[i], num2[4 - i], num[i] - num2[4 - i] );
            
    }

    return 0;
}
