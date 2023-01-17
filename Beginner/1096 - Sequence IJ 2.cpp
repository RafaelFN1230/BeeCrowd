#include <stdio.h>
#include <stdlib.h>
/*
Make a program that prints the sequence like the following exemple.

Input
This problem doesn't have input.

Output
Print the sequence like the example below.
*/
int i,j;
main()
{
	i=1;
	j=7;
	for (int a=0; a<=4;a++)
	{
		for (int b=0; b<3; b++)
		{
			printf("I=%d", i);
			printf(" J=%d\n", j);
			j-=1;
		}
		j=7;
		i+=2;
	}
}