//
// Created by armau on 23/01/2021.
//
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>

void actividad1();
int **generateMatrix(int rows, int cols, int max_val);
int **allocateMatrix(int rows, int cols);
void initializeRandomMatrix(int **arr, int rows, int cols, int max_val);
void print_matrix(int *arr[], int rows, int cols);
void multiply_serial(int *A[], int *B[], int *C[], int rowsA, int rowsB, int colsB);
void multiply_parallel(int *A[], int *B[], int *C[], int rowsA, int rowsB, int colsB);
void printData(double tiempo_secuencial, double tiempo_paralelo);

void actividad2();
void get_histogram_serial(int **image, int n, int number_of_tones, int *histogram);
void get_histogram_parallel(int **image, int n, int number_of_tones, int *histogram);


void actividad3();
long fib_serial(int n);
long fib_parallel(int n);


int main(void)
{
    actividad1();
    actividad2();
    actividad3();
    return 0;
}



/**
 *
 * Actividad 1
 *
 */

void actividad1()
{
    printf("Actividad 1\n");
    int N = 500;
    int MAX_VAL = 10;

    int **A = generateMatrix(N, N, MAX_VAL),
            **B = generateMatrix(N, N, MAX_VAL),
            **C = allocateMatrix(N, N),
            **C2 = allocateMatrix(N, N);

    double t1_serial = omp_get_wtime();
    multiply_serial(A, B, C, N, N, N);
    double t2_serial = omp_get_wtime();

    double t1_parallel = omp_get_wtime();
    multiply_parallel(A, B, C2, N, N, N);
    double t2_parallel = omp_get_wtime();

    free(A);
    free(B);
    free(C);
    free(C2);
    printData(t2_serial - t1_serial, t2_parallel - t1_parallel);
}

void printData(double tiempo_secuencial, double tiempo_paralelo)
{
    double speedup = tiempo_secuencial / tiempo_paralelo;
    double eficiencia = speedup / omp_get_num_procs();
    double overhead = tiempo_paralelo - tiempo_secuencial / omp_get_num_procs();

    printf("Tiempo secuencial: %f\n", tiempo_secuencial);
    printf("Tiempo paralelo: %f\n", tiempo_paralelo);
    printf("Speedup: %f\n", speedup);
    printf("Eficiencia: %f\n", eficiencia);
    printf("Overhead: %f\n\n", overhead);
}

int **allocateMatrix(int rows, int cols)
{
    int **A = (int**) malloc(rows * sizeof(int *));
    for (int i = 0; i < rows; ++i)
    {
        A[i] = malloc(cols * sizeof (int));
    }

    for (int i = 0; i < rows; ++i)
    {
        for (int j = 0; j < cols; ++j)
        {
            A[i][j] = 0;
        }
    }
    return A;
}

int **generateMatrix(int rows, int cols, int max_val)
{
    int **A = allocateMatrix(rows, cols);
    initializeRandomMatrix(A, rows, cols, max_val);
    return A;
}

void print_matrix(int *arr[], int rows, int cols)
{
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; ++j)
        {
            printf("%d\t", arr[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

void initializeRandomMatrix(int **arr, int rows, int cols, int max_val)
{
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            arr[i][j] = rand() % max_val;
        }
    }
}

void multiply_serial(int *A[], int *B[], int *C[], int rowsA, int rowsB, int colsB)
{
    for (int i = 0; i < rowsA; ++i)
    {
        for (int j = 0; j < colsB; ++j)
        {
            for (int k = 0; k < rowsB; ++k)
            {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

void multiply_parallel(int *A[], int *B[], int *C[], int rowsA, int rowsB, int colsB)
{
    #pragma omp parallel for
    for (int i = 0; i < rowsA; ++i)
    {
        for (int j = 0; j < colsB; ++j)
        {
            for (int k = 0; k < rowsB; ++k)
            {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}



/**
 *
 * Actividad 2
 *
 */
void actividad2()
{
    printf("Actividad 2\n");
    int TONOS_DE_GRIS = 256;
    int N = 1000;
    int **IMAGE = generateMatrix(N, N, TONOS_DE_GRIS);
    int *histogram_serial = (int*) malloc(sizeof(int) * TONOS_DE_GRIS);
    int *histogram_parallel = (int*) malloc(sizeof(int) * TONOS_DE_GRIS);

    int K = 3;
    double t_serial_avg = 0, t_parallel_avg = 0;

    for (int i = 0; i < K; ++i)
    {
        double t1_serial = omp_get_wtime();
        get_histogram_serial(IMAGE, N, TONOS_DE_GRIS, histogram_serial);
        double t2_serial = omp_get_wtime();

        double t1_parallel = omp_get_wtime();
        get_histogram_parallel(IMAGE, N, TONOS_DE_GRIS, histogram_parallel);
        double t2_parallel = omp_get_wtime();

        t_serial_avg += t2_serial - t1_serial;
        t_parallel_avg += t2_parallel - t1_parallel;
    }
    t_serial_avg /= K;
    t_parallel_avg /= K;

    free(histogram_parallel);
    free(histogram_serial);
    free(IMAGE);
    printData(t_serial_avg, t_parallel_avg);
}


void get_histogram_serial(int **image, int n, int number_of_tones, int *histogram)
{
    for (int i = 0; i < number_of_tones; ++i)
    {
        histogram[i] = 0;
    }

    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            histogram[image[i][j]]++;
        }
    }
}

void get_histogram_parallel(int **image, int n, int number_of_tones, int *histogram)
{
    int histop[number_of_tones];
    for (int i = 0; i < number_of_tones; ++i)
    {
        histogram[i] = 0;
    }

    #pragma omp parallel private(histop) num_threads(2)
    {
        for (int i = 0; i < number_of_tones; ++i)
        {
            histop[i] = 0;
        }

        #pragma omp parallel for
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                histop[image[i][j]]++;
            }
        }

        #pragma omp critical
        for (int i = 0; i < number_of_tones; ++i)
        {
            histogram[i] += histop[i];
        }
    }
}

/**
 *
 * Actividad 3
 *
 */
void actividad3()
{
    printf("Actividad 3\n");
    int to_calculate = rand() % 30;

    double t1_serial = omp_get_wtime();
    long serial_fib = fib_serial(to_calculate);
    double t2_serial = omp_get_wtime();

    long parallel_fib;
    double t1_parallel, t2_parallel;
    #pragma omp parallel
    {
        #pragma omp single
        {
            t1_parallel = omp_get_wtime();
            parallel_fib = fib_parallel(to_calculate);
            t2_parallel = omp_get_wtime();
        }
    }

    printf("Fib de %d serial: %ld\n", to_calculate, serial_fib);
    printf("Fib de %d paralelo: %ld\n", to_calculate, parallel_fib);

    printData(t2_serial - t1_serial, t2_parallel - t1_parallel);
}


long fib_serial(int n)
{
    if (n <= 2) return n;

    if (n > 30) return -1;
    long f1 = fib_serial(n - 1);
    long f2 = fib_serial(n - 2);
    return f1 + f2;
}

long fib_parallel(int n)
{
    if (n <= 2) return n;
    if (n > 30) return -1;
    long f1, f2, f;
    printf("Hilo %d calculando %d\n", omp_get_thread_num(), n);
    #pragma omp task shared(f1)
    {
        f1 = fib_parallel(n - 1);
    }
    #pragma omp task shared(f2)
    {
        f2 = fib_parallel(n - 2);
    }
    #pragma omp taskwait
    {
        f = f1 + f2;
    }
    return f;
}
