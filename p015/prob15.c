#include <stdio.h>
#include <stdlib.h>
int main() {

	int size, i, j, ndim=20;
	unsigned long long *k;

	k = (unsigned long long *) malloc(ndim * ndim +1); 

	for (i=0; i<=ndim; i++)
		for (j=0; j<ndim; j++)
			if( i==0 || j==0) k[ i*ndim + j] = 1;

	for (i=0; i<=ndim; i++)
		for (j=0; j<ndim; j++)
			if( !( i==0 || j==0) ) k[ i*ndim + j] = k[ (i-1)*ndim + j] + k[ i*ndim + (j-1)];

	printf("Grid size: ");
	scanf("%d", &size);
	printf("k=%llu\n", 2*k[ (size)*ndim + (size-1) ]);

	return 0;
}
