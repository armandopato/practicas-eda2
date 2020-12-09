//
// Created by armau on 08/12/2020.
//

#include <stdio.h>

int main()
{
    #pragma omp parallel
    {
        printf("Hola mundo\n");
        for (int i = 0; i < 10; i++)
        {
            printf("Iteracion %d\n", i);
        }
    }
    printf("A la verga\n");
    return 0;
}