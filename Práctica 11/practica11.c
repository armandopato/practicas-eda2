//
// Created by armau on 08/12/2020.
//

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>
#define N 10
#define NUM_THREADS 2

void llenaArreglo(int *a);
void suma_serial(int *a, int *b, int *c);
void suma_paralela(int *a, int *b, int *c);
void suma_paralela_for(int *A, int *B, int *C);

void actividad6_1();
void actividad6_2();
void actividad7();
void actividad8();

int main(void)
{
    printf("Actividad 6.1\n");
    actividad6_1();
    printf("\nActividad 6.2\n");
    actividad6_2();
    printf("\nActividad 7\n");
    actividad7();
    printf("\nActividad 8\n");
    actividad8();

}

// Actividad 6.1

void actividad6_1()
{
    int *a, *b, *c;
    a = malloc(sizeof(int) * N);
    b = malloc(sizeof(int) * N);
    c = malloc(sizeof(int) * N);

    llenaArreglo(a);
    llenaArreglo(b);
    printf("Suma serial\n");
    suma_serial(a, b, c);
}


void llenaArreglo(int *a)
{
    for (int i = 0; i < N; i++)
    {
        a[i] = rand() % N;
        printf("%d\t", a[i]);
    }
    printf("\n");
}

void suma_serial(int *A, int *B, int *C)
{
    for(int i = 0; i < N; i++)
    {
        C[i] = A[i] + B[i];
        printf("%d\t", C[i]);
    }
    printf("\n");
}


// Actividad 6.2

void actividad6_2()
{
    int *a, *b, *c;
    a = malloc(sizeof(int) * N);
    b = malloc(sizeof(int) * N);
    c = malloc(sizeof(int) * N);

    llenaArreglo(a);
    llenaArreglo(b);
    printf("Suma paralela\n");
    suma_paralela(a, b, c);
}


void suma_paralela(int *A, int *B, int *C)
{
    int i, tid, inicio, fin;
    omp_set_num_threads(NUM_THREADS);
    #pragma omp parallel private(inicio, fin, tid, i)
    {
        tid = omp_get_thread_num();
        inicio = tid * (N / NUM_THREADS);
        fin = (tid + 1) * (N / NUM_THREADS) - 1;
        for (i = inicio; i <= fin; i++)
        {
            C[i] = A[i] + B[i];
            printf("Hilo %d calculo C[%d] = %d\n", tid, i, C[i]);
        }
    }
}

// Actividad 7

void actividad7()
{
    #pragma omp parallel
    {
        printf("Hola mundo\n");
        #pragma omp for
        for (int i = 0; i < N; i++)
        {
            printf("Iteracion: %d\n", i);
        }
    }
    printf("Adios\n");
}

// Actividad 8

void actividad8()
{
    int *a, *b, *c;
    a = malloc(sizeof(int) * N);
    b = malloc(sizeof(int) * N);
    c = malloc(sizeof(int) * N);

    llenaArreglo(a);
    llenaArreglo(b);
    printf("Suma paralela\n");
    suma_paralela_for(a, b, c);
}

void suma_paralela_for(int *A, int *B, int *C)
{
    omp_set_num_threads(NUM_THREADS);
    #pragma omp parallel for
    for (int i = 0; i < N; i++)
    {
        C[i] = A[i] + B[i];
        printf("Hilo %d calculo C[%d] = %d\n", omp_get_thread_num(), i, C[i]);
    }
}