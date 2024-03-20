#include<stdio.h>
#include<stdlib.h>
int main() {
	int all, n;
	scanf("%d%d", &all, &n);
	int* start = (int*)malloc(n * sizeof(int));
	int* end = (int*)malloc(n * sizeof(int));	
	int* list = (int*)malloc(2 * n * sizeof(int));
	int count = 0;
	//int* start = (int*)malloc(n * sizeof(int));
	for (int i = 0; i < n; i++) {
		scanf("%d%d", &start[i], &end[i]);
		list[2*i] = start[i];
		list[2 * i + 1] = end[i];
	}
	for (int i = 0; i < 2n; i++) {
		if (list [i] in )

	}
}