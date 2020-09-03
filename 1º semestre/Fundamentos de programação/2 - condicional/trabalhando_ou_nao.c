/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{
    int dia, hora, minuto;
    scanf("%d %d %d", &dia, &hora, &minuto);
    
    if (dia == 2 || dia == 3 || dia == 4 || dia == 5 || dia == 6 || dia == 7) {
        if(dia == 7) {
            if(hora >= 8 && hora <= 11 && minuto <= 59) {
                printf("SIM");
            }
            
            else {
                printf("NAO");
            }
        }
        
        else {
            if((hora >= 8 && hora <= 11 && minuto <= 59) || (hora >= 14 && hora <= 17 && minuto <= 59)) {
                printf("SIM");
            }
            
            else {
                printf("NAO");
            }
        }
        
    }
    
    else {
        printf("NAO");
    }
}
