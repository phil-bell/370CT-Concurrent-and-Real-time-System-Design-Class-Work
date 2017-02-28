#include <iostream>
#include <stdio.h>

int main(){
    int m = 100;
    int n = 100;
    #pragma omp parallel
    {
        #pragma omp section
        {
            something(m,n);
        }
        #pragma omp section
        {
            something(m,n);
        }
    }

}
int something(m,n){
    const int num_steps = 10000;
    double x, sum = 0.0;
    const double step = 1.0/double(num_steps);
    for(int i=1;i<= num_steps; i++){
        x = double(i-0.5)*step;
        sum += 4.0/(1.0+x*x);
    }
    const double pi = step * sum;
    std::cout<<"Pi is: "<<pi<<std::endl;
}

int something2(m,n){
    for (int x=0; x<m; x++){
        for(int y=0;y<n;y++){
            int z=x+y;
            printf ("Total: %d\n",z);
        }
    }  
}
