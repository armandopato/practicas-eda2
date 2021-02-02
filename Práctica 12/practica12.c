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
int maximo_serial(int *a, int n);
int maximo_paralelo(int *a, int n);
int producto_punto_serial(int *a, int *b, int n);
int producto_punto_paralelo1(int *a, int *b, int n);
int producto_punto_paralelo2(int *a, int *b, int n);

void actividad1();
void actividad2();
void actividad3();
void actividad5();

int main(void)
{
    printf("Actividad 1\n");
    actividad1();
    printf("\nActividad 2\n");
    actividad2();
    printf("\nActividad 3\n");
    actividad3();
    printf("\nActividad 5\n");
    actividad5();

}

// Actividad 1

void llenaArreglo(int *a)
{
    for (int i = 0; i < N; i++)
    {
        a[i] = rand() % N;
        printf("%d\t", a[i]);
    }
    printf("\n");
}

// Actividad 1

void actividad1()
{
    int *a = malloc(sizeof(int) * N);
    llenaArreglo(a);
    printf("Obteniendo maximo...\n");
    printf("Version serial:\n");
    printf("%d\n", maximo_serial(a, N));
    printf("Version paralela:\n");
    printf("%d\n", maximo_paralelo(a, N));
}

int maximo_serial(int *a, int n)
{
    int max = a[0];
    for (int i = 0; i < n; i++)
    {
        if (a[i] > max) max = a[i];
    }
    return max;
}

int maximo_paralelo(int *a, int n)
{
    int max = a[0];
    #pragma omp parallel for
    for (int i = 0; i < n; i++)
    {
        #pragma omp critical
        if (a[i] > max) max = a[i];
    }
    return max;
}

// Actividad 2

void actividad2()
{
    int *a = malloc(sizeof(int) * N);
    llenaArreglo(a);
    int *b = malloc(sizeof(int) * N);
    llenaArreglo(b);

    printf("Obteniendo producto punto...\n");
    printf("Version serial:\n");
    printf("%d\n", producto_punto_serial(a, b, N));
    printf("Version paralela 1:\n");
    printf("%d\n", producto_punto_paralelo1(a, b, N));
    printf("Version paralela 2:\n");
    printf("%d\n", producto_punto_paralelo2(a, b, N));
}

int producto_punto_serial(int *a, int *b, int n)
{
    int result = 0;
    for (int i = 0; i < n; i++)
    {
        result += a[i] * b[i];
    }
    return result;
}
int producto_punto_paralelo1(int *a, int *b, int n)
{
    int result = 0, results[NUM_THREADS];
    omp_set_num_threads(NUM_THREADS);
    #pragma omp parallel
    {
        int tid = omp_get_thread_num();
        results[tid] = 0;
        #pragma omp for
        for (int i = 0; i < n; i++)
        {
            results[tid] += a[i] * b[i];
        }
    }
    for (int i = 0; i < NUM_THREADS; i++)
    {
        result += results[i];
    }
    return result;
}
int producto_punto_paralelo2(int *a, int *b, int n)
{
    int result = 0;
    #pragma omp parallel for reduction(+:result)
    for (int i = 0; i < n; i++)
    {
        result += a[i] * b[i];
    }
    return result;
}


// Actividad 3

void actividad3()
{
    long long num_steps = 100000000;
    double step = 1.0 / num_steps, empezar = omp_get_wtime(), terminar, pi, sum = 0.0;
    #pragma omp parallel for reduction(+:sum)
    for (int i = 0; i < num_steps; i++)
    {
        double x = (i + 0.5) * step;
        sum += 4.0 / (1 + x*x);
    }
    pi = sum * step;
    terminar = omp_get_wtime();

    printf("El valor de pi es %15.12f\n", pi);
    printf("El tiempo de calculo de pi es: %lf segundos\n", terminar - empezar);
}

// Actividad 5

void actividad5()
{
    int a[5];
    #pragma omp parallel
    {
        #pragma omp for
        for (int i = 0; i < 5; i++)
        {
            a[i] = i * i;
        }
        #pragma omp single
        for (int i = 0; i < 5; ++i)
        {
            printf("a[%d] = %d\n", i, a[i]);
        }

        #pragma omp for
        for (int i = 0; i < 5; ++i)
        {
            a[i] += i;
        }
    }
}
