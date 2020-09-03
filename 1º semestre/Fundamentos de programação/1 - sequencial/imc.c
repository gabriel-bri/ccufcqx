#include <stdio.h>
#include <math.h>

int main() {
  float P, H, IMC;
  
    scanf("%f", &P);
    scanf("%f", &H);
    IMC = P / (H*H);

    printf("%f", IMC);   
    return 0;
}