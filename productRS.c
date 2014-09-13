#include <stdio.h>
#include <math.h>
#include "debug.h"

//helper functions
int sgn(int x)
{
	if (x > 0) {
		return 1;
	} else if (x < 0) {
		return -1;
	} else {
		return 0;
	}
}

double hyp(unsigned int x)
{
	double res;
	res = 1.0 / (x + 1);
	return res;
}

double weight(unsigned int x, unsigned int y)
{
	double res;
	res = hyp(x) + hyp(y);
	return res;
}

//
void productRS(int r[], int s[], int R[], int N, double* result)
{
	/*
	 * R = rank vector
	 */

	double res = 0;
	double tmpResult;
	int i, j;

	for (i = 0; i < N; ++i) {
		for (j = 0; j < N; ++j) {
			if (i < j) {
				tmpResult =
				    sgn(r[i] - r[j]) * sgn(s[i] -
							   s[j]) * weight(R[i],
									  R[j]);
				res += tmpResult;
			}
		}
	}
    *result = res;
}

int main(int argc, char *argv[])
{
//
//	int i = 0;
//
//	for (i = 0; i < 3; ++i) {
//		printf("hyp %i: %f\n", i, hyp(i));
//	}
//
//	for (i = 0; i < 3; ++i) {
//		printf("weight%i: %f\n", i, weight(i, i));
//	}

	int a[] = { 3, 7, 9, 3, 5 };
	int b[] = { 11, 6, 6, 3, 5 };
	int abRank[] = { 3, 1, 0, 4, 2 };
    double foo;

    productRS(a, b, abRank, 5, &foo);
    check(fabs(2.016666 - foo) < 0.01, "toy example failed");

    printf("res = %f\n", foo);
	return 0;

error:
    return -1;
}
