/*****************************************
** File:    lab3.cpp
** Project: CMSC 202 Lab 3, Fall 2021
**
** Lab 3 involves using arrays. In this file you need to
** implement the flipArray() function as well as populate the array
** and keep track of the length of the array.
**
***********************************************/
#include <iostream>
using namespace std;

// Function Prototype for flipArray HERE********
void flipArray(int array[], int size); //Provided

//Implement global constants HERE********


//Implement main HERE*********
int main(){
    int orig_array[101];
    int user_input;
    int counter;
    while(user_input != 0 && counter <= 100){
        counter = 0;
        cout <<  "Please enter a integer.\n" << "Enter 0 when youre done" << endl;
        cin >> user_input;
        orig_array[counter] = user_input;
        counter++;
    }
    cout << orig_array << endl;
    flipArray(orig_array,counter);
    return 0;
}


// Implement flipArray() here
// Hint: only need to iterate through half of the array.

void flipArray(int array[], int size){
    int flipped[size] = {0};
    for(int i = 0; i <= size; i++) {
        if(i == 0){
            flipped[i] = array[size];
        }
        flipped[i] = array[size - i];
        
    }
}