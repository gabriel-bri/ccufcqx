#include <stdio.h>
#include <ctype.h>
int main() {
  char jog1, jog2, r1, r2;

  scanf("%c %c", &jog1, &jog2);
  r1 = toupper(jog1);
  r2 = toupper(jog2);

  if((r1 == 'P' && r2 == 'R') || (r1 == 'S' && r2 == 'P') || (r1 == 'R' && r2 == 'S')) {
    printf("jog1");
  }

  else if((r2 == 'P' && r1 == 'R') || (r2 == 'S' && r1 == 'P') || (r2 == 'R' && r1 == 'S')) {
    printf("jog2");
  }

  else {
    printf("empate");
  }
  return 0;
}