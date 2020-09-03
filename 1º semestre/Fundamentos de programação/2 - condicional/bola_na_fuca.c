#include <stdio.h>

int main()
{
    char tipo_saque;
    int tipo_saque_, forca, potencia;
    
    scanf("%c", &tipo_saque);
    scanf("%d", &forca);
    
    tipo_saque_ = (tipo_saque == 'c') ? 18 : 20;
    
    potencia = ((forca * tipo_saque_) - 80) / 10;
    
    if(potencia < 150) {
        printf("Fraco, nem passou\n");
    }
    
    else if(potencia >= 150 && potencia < 180) {
        printf("Perfeito\n");
    }
    
    else if(potencia >= 180 && potencia <= 210) {
        printf("Satisfeito\n");   
    }
    
    else {
        printf("Muito forte, bola fora\n");
    }
    return 0;
}
