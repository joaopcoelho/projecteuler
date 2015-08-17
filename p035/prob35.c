// How many circular primes are there below one million?

// Takes too long! Suggestions:
// - parallelize loops with OpenMP, CUDA
// - if a given number is circular prime, then all its "rotation primes" are also circular primes
// - if a given number has any digit greater than its starting digit, then it is not a circular prime (otherwise it would have already been detected). -> MUST ADD n_digits to the circprimes count when we find first 
// - if any digit is even, then not all rotations are prime

// 9-7-2014
// implemented if digit even, skip -> running time down from ~5 minutes to 38 seconds

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <math.h>
#define ULIMIT 6	// max: 10^6

bool isprime( int );
int get_nrot( int );
int power( int, int);
int check_for_evens( int , int);

int main(){
	
	char str[ULIMIT+1], str2[ULIMIT+1];
	int nrot, num;
	int limite = power(10, ULIMIT);
	int circprimes=1; // total counter; account for 2

	for (num=1; num<limite; num+=2){

		nrot= get_nrot( num);

		if (check_for_evens( num, nrot)) continue;

		if ( isprime( num)){
			int rotnum, rotcnt=0;
			
			
			rotnum=num;
			
			for (int j=0; j<nrot; j++){

				sprintf( str, "%d", rotnum); 
				strcpy( str2, str); 

				int k=1;
				while( k < nrot){
					str[ k] = str2[ k-1];
					k++;
				}
				str[0] = str2[nrot-1];
				rotnum = atoi( str);

				if ( isprime( rotnum)) rotcnt++;
				else 
					break;

			}

			if( rotcnt==nrot) {circprimes++; printf("%d %d\n", circprimes, num);}

		}
	}

	printf("Total circular primes below %d: %d\n", power(10,ULIMIT), circprimes);

	return 0;
}


bool isprime( int num){
	
	bool primeness=true;
	int i;
	
	for (i=num-1; i>1; i--)
		if( num % i == 0) {primeness=false; break;}

	if ( num==1) primeness=false;
	return primeness;
}

int get_nrot( int num){
	
	int nrot, k;

	for (k=0; k<100; k++)
		if( num/power(10, k) == 0) { nrot=k; break;}

	return nrot;
}

int power(int base, int exp)
{
    int result = 1;
    while(exp) { result *= base; exp--; }
    return result;
}

int check_for_evens( int num, int nrot){

	int evens=0, alg;
	char calg, str[ULIMIT+1];
	sprintf( str, "%d", num); 

	for (int i=0; i<nrot; i++){
		calg = str[i];
		alg = atoi( &calg);
		if( alg%2 == 0 || alg==0) {evens=1; break;}
	}

	return evens;
}