#include <cstdio>

int main () {
    int x;

    while (scanf("%d", &x) == 1){
        if (x == 0) {
            printf("vai ter copa!\n");
        } else {
            printf("vai ter duas!\n");
        }
    }
    return 0;
}