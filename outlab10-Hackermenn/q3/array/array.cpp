/** \file */
#include <iostream>
#include <stdlib.h>

using namespace std;

/*!
 \fn int fillArray(int myArr[7][7])
 \param myArr[7][7] -> a multidimensional integer array of size 7*7
 \brief Initializes the array with random values in [20,420)
 \return 0
 */

int fillArray(int myArr[7][7])                 
{
	for(int i=0;i<7;i++)
	{
		for(int j=0;j<7;j++)                    
		{
			myArr[i][j]=20+rand()%400;              
		}
	}
	return 0;
}

/*!
 \fn void printSpiral(int myArr[7][7])
 \param myArr[7][7] -> a multidimensional integer array of size 7*7
 \brief prints the array elements traversing anticlockwise along boundaries in a contracting spiral form
 \return void 
 */

void printSpiral(int myArr[7][7])
{
	cout << "Array Spiral Function." << endl;
	for(int j=0;j<1;j++)                           
    {                                              
        for(int i=0;i<7;i++)
        {
            cout<< myArr[i][j]<< "  ";
        }

    }
    cout << endl;

    for(int i=6;i<7;i++)                          
    {                                            
        for(int j=1;j<7;j++)
        {
            cout << myArr[i][j] << "  ";
        }
    }
    cout << endl;

    for(int j=6;j<7;j++)                          
    {                                             
        for(int i=5;i>=0;i--)
        {
            cout << myArr[i][j] << "  ";
        }
    }
    cout << endl;

    for (int i=0;i<1;i++)                          
    {                                              
        for (int j=5;j>=1;j--)
        {
            cout << myArr[i][j] << "  ";
        }
    }
    cout << endl;

    for (int j=1; j<2;j++)
    {                                             
        for (int i=1; i<6;i++)
        {
            cout << myArr[i][j] << "  ";
        }
    }
    cout << endl;

    for (int i=5; i<6;i++)                        
    {
        for (int j=2; j<6; j++)
        {
            cout << myArr[i][j] << "  ";
        }
    }
    cout << endl;

    for (int j=5; j<6; j++)                        
    {
        for (int i=4; i>0; i--)
        {
            cout << myArr[i][j] << "  ";
        }
    }
    cout << endl;

    for (int i=1; i<2; i++)                        
    {
       for (int j=4; j>1; j--)
       {
           cout << myArr[i][j] << "  ";
       }
    }
    cout << endl;

    for (int j=2; j<3; j++)                        
    {
        for (int i=2; i<5; i++)
        {
            cout << myArr[i][j] << "  ";
        }
    }
    cout << endl;

    for (int i=4; i<5; i++)                        
    {
        for (int j=3; j<5; j++)
        {
            cout << myArr[i][j] << "  ";
        }
    }
    cout << endl;

    for (int j=4; j<5; j++)                        
    {
        for (int i=3; i>1; i--)
        {
            cout << myArr[i][j] << "  ";
        }
    }
    cout << endl;

    for (int i=2; i<3; i++)                        
    {
        for (int j=3; j<4; j++)
        {
            cout << myArr[i][j] << "  ";
        }
    }
    cout << endl;

    for (int i=3; i<4; i++)                         
    {
        for (int j=3; j<4; j++)
        {
            cout << myArr[i][j] << "  ";
        }
    }
  cout << endl << endl;
}

/*!
 \fn void printCol(int myArr[7][7], int s, int e)
 \param myArr[7][7],s,e -> a multidimensional integer array of size 7*7 and two integers
 \brief prints columns with index (s-1)...(e-2) of the array
 \return void
 */
void printCol(int myArr[7][7], int s, int e)                     
{  
	cout << "Column Output" << endl;                
	for (int j=s-1; j<e-1; j++)
	{                                               
		for (int i=0; i<7; i++)
		{
			cout << myArr[i][j] << " ";
		}
		cout << endl;
	}
	cout << endl << endl;
}

/*!
 \fn int findMin (int myArr[7][7])
 \param myArr[7][7] -> a multidimensional integer array of size 7*7
 \brief finds minimum element in the integer array
 \return minimum element
 */

int findMin (int myArr[7][7])
{
	int i,j;
	int min = myArr[0][0];

	for (i=0; i<7; i++)                             
	{
		for (j=0; j<7; j++)
		{
			if(myArr[i][j] < min)                   
			{                                       
				min = myArr[i][j];
			}                                       
		}                                           

	}
    return min;
}

/*!
 \fn int findAverage (int myArr[7][7])
 \param myArr[7][7] -> a multidimensional integer array of size 7*7
 \brief finds average of all elements in the integer array
 \return average of all elements
 */

int findAverage (int myArr[7][7])                  
{                                                   
	int i,j;
	int sum = 0;

	for (i=0; i<7; i++)                             
	{
	    for (j=0; j<7; j++)
	    {
	        sum = sum + myArr[i][j];
	    }

	}
    return sum/49;       
}

/*!
 \fn void printArray(int myArr[7][7])
 \param myArr[7][7] -> a multidimensional integer array of size 7*7
 \brief prints all the elements in the array along the rows
 \return void 
 */

void printArray (int myArr[7][7])                     
{
    cout << "Normal Array Output" << endl;

    for (int i =0; i<7; i++)
    {
        for (int j=0; j<7; j++)
        {
            cout << myArr[i][j] << "  ";
        }
        cout << endl;
    }
    cout << endl;                                   
    cout << endl;
}

/*!
 \fn int main()
 \brief Driver function of the program. 

 It allocates the memory needed to create a multidimensional integer array of size 7*7 named myArr[7][7].
 		Then it calls the function fillArray which initialises the array. Then it calls the function printArray
 		which prints the array. Then it calls the function printSpiral which . Then it calls the function printCol
 		to prints the columns 1,2,3 of the array. Then it calls the function findMin to print the minimum element
 		in the array. Then it calls the function findAverage to print the average of all elements in the array.
 
 \return 0
*/

int main(){
	
	int myArr [7][7];
	fillArray(myArr);                               
	printArray(myArr);
	printSpiral(myArr);
	printCol(myArr, 2, 5);
	cout<<"Min:"<<findMin(myArr);
	cout<<" Average:"<<findAverage(myArr);
    cout<<endl;

	return 0;
}
 