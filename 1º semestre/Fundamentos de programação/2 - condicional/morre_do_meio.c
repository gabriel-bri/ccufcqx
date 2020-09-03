#include <stdio.h>

int main(){
	int n1, n2, n3, meio;
	scanf("%d %d %d", &n1, &n2, &n3);

	if((n1 < n2 && n3 > n2) || (n2 < n1 && n3 < n2)) {
		meio = n2;
	}

	else if((n1 < n2  && n1 > n3) || (n1 < n3 && n1 > n2)) {
		meio = n1;
	}

	else {
		meio = n3;
	}

	printf("%d", meio);

	return 0;
}