/* 

This is a program to find the shift of row and column for Number : 1 to reach the center of a 5 X 5 matrix
  
                   1 0 0 0 0     
                   0 0 0 0 0    
Example Matrix     0 0 0 0 0 
                   0 0 0 0 0 
                   0 0 0 0 0 

                   1 0 0 0 0 
                   0 0 0 0 0 
Center Matrix      0 0 X 0 0 
                   0 0 0 0 0 
                   0 0 0 0 0 

In the center center matrix the center is denoted by 'X'.Task is to find the total shift of rows and col for example matrix
to get to the center of the matrix.

In this example : the example matric required 4 moves to to the center.

*/

#include <iostream>
#include <stdio.h>

int main()
{
    int row,col;
    std::cout<<"Enter row and col: \n";
    std::cin>>row>>col;
    int b[row][col];
    int i,j;
    printf("Enter elements into 2-D array: ");
    for(i=0;i<row;i++) {
        for(j=0;j<col;j++) {
            std::cin>>b[i][j];
            std::cout<<b[i][j]<<" ";

        }
        std::cout<< "\n";
    }
    int counter = 0;
    int number = 1;
    for (int i = 0;i < row; i++){
        for( int j = 0; j < col;j++) {
            if(b[i][j] == number){
                int rowDiff = abs(2 - i);
                int colDiff = abs(2 - j);
                counter += (rowDiff + colDiff);
            }
        }
        }
    std::cout<<counter<<"\n";

    }
