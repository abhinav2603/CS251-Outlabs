/*!
	\file stud_rec.cpp
	\brief A student record maintaining program.
*/

/**
This Code is taken from http://www.worldbestlearningcenter.com for learning/teaching purpose
**/

#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <string.h>
using namespace std;

/*!
 \struct student
 \brief An object of this struct will contain a student's record i.e. his personal details(id, name, gender) and 
  marks scored by him/her in various exams.
*/

struct student
{
	string stnumber; /*!< id of the student */
	string stname; /*!< name of the student */
	char sex; /*!< gender of the student */
	float quizz1; /*!< marks scored in quiz1 */
	float quizz2; /*!< marks scored in quiz2 */
	float assigment; /*!< marks scored in assignment */
	float midterm; /*!< marks scored in midterm */
	float final; /*!< marks scored in final exam */
	float total; /*!< total marks scored in all exams */
	int numberOfitem; /*!< redundant variable of no use */
};

int search(struct student st[],string id, int itemcount);
void clean(struct student st[],int deleteitem);

/*!
 \fn void displaymenu()
 \brief Prints all the operations we need to carry out and functions are defined for each point printed
 \bug In 7th point, max should be replaced by min
 \return void
*/

void displaymenu(){
	cout<<"=========================================="<<"\n";
	cout<<" MENU "<<"\n";
	cout<<"=========================================="<<"\n";
	cout<<" 1.Add student records"<<"\n";
	cout<<" 2.Delete student records"<<"\n";
	cout<<" 3.Update student records"<<"\n";
	cout<<" 4.View all student records"<<"\n";
	cout<<" 5.Calculate average score of a student"<<"\n";
	cout<<" 6.Show student who gets the max total score"<<"\n";
	cout<<" 7.Show student who gets the max total score"<<"\n"; 
	cout<<" 8.Find a student by ID"<<"\n"; 
	cout<<" 9.Sort records by TOTAL"<<"\n"; 
}

/*!
 \fn void add_rec(struct student st[], int& itemcount)
 \brief A function to add record of a student
 	
 	At first, it takes as input the id and checks whether this student is in the record or not.If not, then
    it adds an object to the st array by taking input all the properties and assigning them to the new student
    and then increases itemcount i.e. the length of the array by one. 

 \param st[], itemcount -> an array of objects of struct student and a reference to length of the array filled with students
 \return void 
 */

void add_rec(struct student st[],int& itemcount){
	again:
	cout<<"\nEnter student's ID:";
	cin>>st[itemcount].stnumber;
	if(search(st,st[itemcount].stnumber,itemcount)!=-1){
		cout<<"This ID already exists\n";goto again;
	}
	cout<<"Enter student's Name:"; 
	cin>>st[itemcount].stname;
	cout<<"Enter student's Sex(F or M):";cin>>st[itemcount].sex;
	cout<<"Enter student's quizz1 score:";cin>>st[itemcount].quizz1;
	cout<<"Enter student's quizz2 score:";cin>>st[itemcount].quizz2;
	cout<<"Enter student's assigment score:";cin>>st[itemcount].assigment;
	cout<<"Enter student's mid term score:";cin>>st[itemcount].midterm;
	cout<<"Enter student's final score:";cin>>st[itemcount].final;
	st[itemcount].total=st[itemcount].quizz1+st[itemcount].quizz2+st[itemcount].assigment+st[itemcount].midterm+st[itemcount].final;

	++itemcount;
}

/*!
 \fn int search(struct student st[], string id,int itemcount)
 \brief Search for a student in the record

 It finds and prints the array index of the student whose id matches the given id, if no such student, then print -1
 
 \param st[], id, itemcount -> an array of objects of struct student, a string id of student and integer length of the array filled with students
 \return void 
 */

int search(struct student st[], string id,int itemcount){
	int found =-1;
	for (int i = 0; i < itemcount && found==-1; i++)
	{
		if (st[i].stnumber == id) found=i;
		else found=-1 ;
	}

	return found;
}

/*!
 \fn void viewall(struct student st[], int itemcount)
 \brief Prints all data member's values of all the objects of struct student present in the array 
 \bug In the condition inside while, it should be i < itemcount instead of <= 
 \param st[], itemcount -> an array of objects of struct student and integer length of the array filled with students
 \return void 
 */

void viewall(struct student st[], int itemcount){
	int i=0;
	cout<<left<<setw(5)<<"ID"<<setw(20)<<"NAME"<<setw(5)<<"SEX"

	<<setw(5)<<"Q1"
	<<setw(5)<<"Q2"<<setw(5)<<"As"<<setw(5)<<"Mi"<<setw(5)<<"Fi"
	<<setw(5)<<"TOTAL"<<"\n";
	cout<<"==============================================\n";
	while(i<=itemcount){
		if(st[i].stnumber!=""){
			cout<<left<<setw(5)<<st[i].stnumber<<setw(20)<<st[i].stname<<setw(5)

			<<st[i].sex;
			cout<<setw(5)<<st[i].quizz1<<setw(5)<<st[i].quizz2<<setw(5)<<st[i].assigment
			<<setw(5)<<st[i].midterm<<setw(5)<<st[i]. final<<setw(5)
			<<st[i].total;

			cout<<"\n";
		}
		i=i+1;
	}
}

/*!
 \fn void delete_rec(struct student st[], int& itemcount)
 \brief A function to delete a student's record

 	Takes input a student id, if student with that id is present, deletes the record of that student and decreases
        length of array

 \param st[], itemcount -> an array of objects of struct student and a reference to length of the array filled with students
 \return void 
 */

void delete_rec(struct student st[], int& itemcount){
	string id;
	int index;
	if (itemcount > 0)
	{
		cout<<"Enter student's ID:";
		cin>>id;
		index = search(st, id,itemcount); 

		if ((index!=-1) && (itemcount != 0)){
			if (index == (itemcount-1)){ 

				clean(st, index);
				--itemcount;

				cout<<"The record was deleted.\n";
			}
			else{ 
				for (int i = index; i < itemcount-1; i++){
					st[i] = st[i + 1];
					clean(st, itemcount);
					--itemcount ;
				}
			}
		}
		else cout<<"The record doesn't exist.Check the ID and try again.\n";
	}
	else cout<<"No record to delete\n";
}

/*!
 \fn void clean(struct student st[],int deleteitem)
 \brief Given an index of the array, it cleans the record of the student present at that index in the array
 \param st[], deleteitem -> an array of objects of struct student and integer
 \return void 
 */

void clean(struct student st[],int deleteitem){
	st[deleteitem].stnumber = "";
	st[deleteitem].stname = "";
	st[deleteitem].sex = 'X';
	st[deleteitem].quizz1 = 0;
	st[deleteitem].quizz2 = 0;
	st[deleteitem].assigment = 0;
	st[deleteitem].midterm = 0;
	st[deleteitem].final = 0;
	st[deleteitem].total = 0;
}

/*!
 \fn void update_rec(struct student st[], int itemcount)
 \brief A function to update a student's record

 	At first, it takes as input an id, if a student with that id is present in the array, then it asks a column_index
        for input, and updates a particular property of student depending on the column_index, i.e. if column_index=1,
        it updates name or if column_index=2, it updates sex or if column_index=3, it updates quizz1 or if column_index=4,
        it updates quizz2 or if column_index=5, it updates assignment or if column_index=6, it updates midterm or
        if column_index=7, it updates final, and then updates total accordingly

 \param st[], itemcount -> an array of objects of struct student and integer length of the array filled with students
 \return void 
 */

void update_rec(struct student st[],int itemcount){
	string id;
	int column_index;
	cout<<"Enter student's ID:";
	cin>>id;
	cout<<"Which field you want to update(1-7)?:";
	cin>>column_index;

	int index = search(st, id,itemcount);

	if (index != -1)
	{
		if (column_index == 1){
			cout<<"Enter student's Name:";
			cin>>st[index].stname;
		}

		else if (column_index == 2){
			cout<<"Enter student's Sex(F or M):";
			cin>>st[index].sex;
		}
		else if (column_index == 3){
			cout<<"Enter student's quizz1 score:";
			cin>>st[index].quizz1;
		}
		else if (column_index == 4){
			cout<<"Enter student's quizz2 score:";
			cin>>st[index].quizz2;
		}
		else if (column_index == 5){
			cout<<"Enter student's assigment score:";
			cin>>st[index].assigment;
		}
		else if (column_index == 6){
			cout<<"Enter student's mid term score:";
			cin>>st[index].midterm;
		}
		else if (column_index == 7)	{
			cout<<"Enter student's final score:";
			cin>>st[index].final;
		}
		else cout<<"Invalid column index";

		st[index].total = st[index].quizz1 + st[index].quizz2 + st[index].assigment

		+ st[index].midterm + st[index].final;
	}
	else cout<<"The record deosn't exits.Check the ID and try again.";
}

/*!
 \fn void showmax(struct student st[], int itemcount)
 \param st[], itemcount -> an array of objects of struct student and integer length of the array filled with students
 \brief Finds the id of the student who has maximum total score and prints id and the maximum score
 \return void 
 */

void showmax(struct student st[], int itemcount){
	float max = st[0].total;
	int index=0;

	if (itemcount >= 2){
		for (int j = 0; j < itemcount-1; ++j)
			if (max < st[j+1].total) {
				max = st[j+1].total;
				index = j+1;
			}
	}
	else if (itemcount == 1){
		index = 0;
		max = st[0].total;
	}
	else 
		cout<<"Not record found!\n";

	if (index != -1) 
		cout<<"The student with ID "<<st[index].stnumber<<" gets the highest score "<<max<<endl;
}

/*!
 \fn void showmin(struct student st[], int itemcount)
 \param st[], itemcount -> an array of objects of struct student and integer length of the array filled with students
 \brief Finds the id of the student who has minimum total score and prints id and the minimum score
 \bug In the print message, there should be "lowest score" instead of "highest score"
 \return void 
 */

void showmin(struct student st[], int itemcount){

	float min = st[0].total;
	int index = 0;

	if (itemcount >= 2){
		for (int j = 0; j < itemcount-1; ++j)
			if (min > st[j+1].total){
				min = st[j+1].total;
				index = j+1;
			}
	}
	else if (itemcount == 1){
		index = 0;
		min = st[0].total;
	}
	else 
		cout<<"No record found!\n";

	if (index != -1) cout<<"The student with ID "<<st[index].stnumber<<" gets the highest score "<<min<<endl;

}

/*!
 \fn void find(struct student st[], int itemcount)
 \param st[], itemcount -> an array of objects of struct student and integer length of the array filled with students
 \brief Takes input a student id, if student with that id is present, prints all data member's values of that student object.
 \return void 
 */

void find(struct student st[], int itemcount){
	string id;
	cout<<"Enter student's ID:";
	cin>>id;

	int index=search(st,id,itemcount);
	if (index != -1) { 								
		cout<<left<<setw(5)<<st[index].stnumber<<setw(20)<<st[index].stname<<setw(5)<<st[index].sex;
		cout<<setw(5)<<st[index].quizz1<<setw(5)<<st[index].quizz2<<setw(5)

		<<st[index].assigment
		<<setw(5)<<st[index].midterm<<setw(5)<<st[index].final<<setw(5)
		<<st[index].total;
		cout<<"\n"; 

	}
	else cout<<"The record doesn't exits.";

}

/*!
 \fn void bubblesort(struct student dataset[], int n)
 \param dataset[], n -> an array of objects of struct student and integer length of the array filled with students
 \brief Sorts the array on basis of increasing order of total marks
 \return void 
 */

void bubblesort(struct student dataset[], int n){
	int i, j;
	for (i = 0; i < n; i++)
		for (j = n - 1; j > i; j--)
			if (dataset[j].total < dataset[j - 1].total ){
				student temp = dataset[j];
				dataset[j] = dataset[j - 1];
				dataset[j - 1] = temp;
			}

}

/*!
 \fn void average(struct student st[], int itemcount)
 \brief A function to find average marks of a student

 Takes input a student id, if student with that id is present, prints the average of marks scored in
        quiz1, quiz2, assignment, midterm, final exams

 \param st[], itemcount -> an array of objects of struct student and integer length of the array filled with students
 \return void 
 */

void average(struct student st[], int itemcount){
	string id;
	float avg=0;
	cout<<"Enter students'ID:";
	cin>>id;
	int index = search(st, id,itemcount);
	if (index != -1 && itemcount>0)
	{
		st[index].total = st[index].quizz1 + st[index].quizz2 + st[index].assigment
			+ st[index].midterm + st[index].final;
		
		avg = st[index].total /5;
	}

	cout<<"The average score is "<<avg;
}

/*!
 \fn int main(int argc, char *argv[])
 \brief Driver function of the program

	Takes as input a choice from the user and executes a task corresponding to the choice. Program execution ends
	when a key not same as 'y' or 'Y' is given otherwise execution keeps on going.

 \sa add_rec(), delete_rec(), update_rec(), viewall(), average(), showmax(), showmin(), find(), bubblesort()
 \return EXIT_SUCCESS
 */

int main(int argc, char *argv[]){

	student st[80];
	int itemcount=0;

	int yourchoice;
	char confirm;
	do{
	
		displaymenu();
		cout<<"Enter your choice(1-9):";
		cin>>yourchoice;

		switch(yourchoice){
			case 1:add_rec(st, itemcount);break;
			case 2:delete_rec(st, itemcount);break;
			case 3:update_rec(st, itemcount);break;
			case 4:viewall(st, itemcount);break;
			case 5:average(st, itemcount);break;
			case 6:showmax(st, itemcount);break;
			case 7:showmin(st, itemcount);break;
			case 8:find(st, itemcount);break;

			case 9:bubblesort(st,itemcount);break;
			default:cout<<"invalid";
		}

		cout<<"Press y or Y to continue:";
		cin>>confirm;
	}while(confirm=='y'||confirm=='Y');

	system("PAUSE");
	
	return EXIT_SUCCESS;
}