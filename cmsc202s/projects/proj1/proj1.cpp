/*
* File: proj1.cpp
* Project: CMSC 202 Project 1 
* Date: 3/1/22
* Section: 
* Email: msyed2@umbc.edu
*
* This file contains the code to wordle
*
*/

#include <iostream>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <string>

using namespace std;

const int FILE_WORDS = 5; // how many letters are in the word
const int FILE_ARRAY_ONE = 2315;  // the length of words in the text file
const int DISPLAY_ARRAY_LENGTH = 12;    // 6 turns max for a player but need 12 lines to display both guess and result

// Name: load_file
// PreCondition: empty array with length of the load file
// PostCondition: populate the array with the strings to the array 
void load_file(string array[]);

// Name: random_word
// PreCondition: Array with text file strings
// PostCondition: randomly selects a integer between zero and FILE_ARRAY_ONE that will be the index for the random word
int random_word(string array[]);

// Name: guess_word
// PreCondition: Array with text file strings
// PostCondition: Returns the user acceptable string that they want to guess
string guess_word(string array[]);

// Name: check_FileArray
// PreCondition: user guessed word and load file array
// PostCondition: check if the user guess word is in the array (helper function for guess word)
bool check_FileArray(string guess ,string array[]);

// Name: creatingDisplayArray
// PreCondition: empty array
// PostCondition: populates the array with "_____"
void creatingDisplayArray(string array[]);

// Name: currentUserArray
// PreCondition: display array
// PostCondition: display the current display array
void currentUserArray(string array[]);

// Name: checkWord
// PreCondition: user guessed word, target word, display array and counter
// PostCondition: check the guess word to the target word and add its to the display array
void checkWord(string guess, string actualWord, string array[],int counter);    

// Name: win
// PreCondition: user guessed word, target word
// PostCondition: checks if the user guessed word and target word are the same returns a bool to see if its true or not 
bool win(string guess, string targetWord); 

// Name: reset 
// PreCondition: int main
// PostCondition: will reset the game by calling recalling the main function
void reset(int main);


int main(){
    string loadArray[FILE_ARRAY_ONE]; //load file array

    int targetWordIndex = 0; // the index of the word the cpu chooses
    string targetWord = "";   // the word of the cpu chooses 

    bool gameEnd = false;  // game ending boolean if condition is true game will end
    int userChoice; // user choice if the game counter goes over 12

    string displayArray[DISPLAY_ARRAY_LENGTH]; // display array 
    string userWord = "" ; // user guessed word

    int counter = 1; // how many times the user has guessed  starts at one cause in the display array each turn is 2 lines
        

    load_file(loadArray);   // loading the file array
    creatingDisplayArray(displayArray); // creating the display array
    targetWordIndex = random_word(loadArray); // find the random word index
    targetWord = loadArray[targetWordIndex];   // set the random word to a variable
    // cout << targetWord << endl;      // prints out the expected word

    while(gameEnd != true && counter <= 12){      // game loop 
        userWord = guess_word(loadArray);         // ask the user for a guess
        checkWord(userWord,targetWord,displayArray,counter);    // check the word to see if its accurate
        counter += 2;      
        currentUserArray(displayArray);  // display the current display array
        gameEnd = win(userWord,targetWord); //check if the game has ended
    }
    if(gameEnd == true){
        cout << "Good Job. The game has ended" << endl; 
    }
    else if(counter >= 12){
        cout << "You took 6 turns. " << endl << "Would you like to reset? (1 to reset, 2 to end)" << endl; 
        cin >> userChoice;
        while(userChoice != 1 && userChoice != 2){     // to reset the game or not
            cout << "Please choose either 1 or 2" << endl;
            cin >> userChoice;
        }
        if(userChoice == 1){
            cout << "reset" << endl; 
            reset(main());     // resets the function
        }
        else if (userChoice == 2)
            cout << "Thanks for playing " << endl;
    }

}

void load_file(string array[]){
    string sampleWords;    // string to hold the text file strings
    int x = 0; // to count and access the array
    ifstream myfile("proj1_data.txt");  

    if(myfile.is_open()){    
        while(myfile >> sampleWords){
            array[x] = sampleWords;    // add it to the array
            x +=1;   
        }
        cout << x << " are imported." << endl;     
    }
    else{
        cout << "file cannot open" << endl;
    }
}

void creatingDisplayArray(string array[]){
    for(int i = 0; i < DISPLAY_ARRAY_LENGTH; i++){
        array[i] = "_____";     // creating the ______ rows in the display array
    }
}

int random_word(string array[]){
    srand(time(NULL));      
    return rand() % FILE_ARRAY_ONE + 1;    // 0 to 2315

}

bool check_FileArray(string guess ,string array[]){
    for(int i = 0; i < FILE_ARRAY_ONE;i++){  
        if(guess == array[i])
            return true;
    }
    return false;
}

string guess_word(string array[]){   
    string guess;
    cout << "What word would you like to guess?" << endl;
    cin >> guess;
    while(guess.size() != 5 || check_FileArray(guess,array) == false){         
        cout << "Please try again" << endl;
        cout << "word not in list" << endl;
        cin >> guess; 
    }
    return guess;
}

void currentUserArray(string array[]){
    for(int i = 0; i < DISPLAY_ARRAY_LENGTH; i++){
        cout << array[i] << endl;
    }
}

void checkWord(string guess, string actualWord, string array[],int counter){  
   // compare the guess with the actual word
   string holder = "_____";
   for(int x = 0; x < FILE_WORDS; x++){       // comparing one letter of guess to the all the letters of target word need a 2d array
       for(int y = 0; y < FILE_WORDS; y++){ 
            if(guess[x] == actualWord[y] && x == y){
                holder[x] = '!';    // green 
            }
            else if(guess[x] == actualWord[y] && x != y){
                holder[x] = '&';    // yellow
            }
       }
   }
    // adds it to the display array 
    array[counter-1] = guess;
    array[counter] = holder;
    

} 

bool win(string guess, string targetWord){
    if(guess == targetWord){
        return true;
    }
    return false;
}

void reset(int main){
    main;       // the main function
}
