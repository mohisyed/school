/*
* Mohiuddin Syed
* Project 1 
* 09/18/21
* Cmsc 202
*/

#include <iostream>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <string>

using namespace std;



const int FILE_WORDS = 10;      // length of the words
const int FILE_ARRAY = 15;      // length of the file array
const int NUMBER_ARRAY_LENGTH = 15;    // length of the number array


string get_file_name();         // get file name
void load_file(string file_name, string file_words[], char file_array[][NUMBER_ARRAY_LENGTH]);      // loads the file 
void numbers_arrays(int array[]);   // create a number array 

void display_puzzle(string file_words[], char file_array[][NUMBER_ARRAY_LENGTH],string number_array[]);   //displays the file 
string build_word(char file_array[][FILE_ARRAY]);      // builds the word that user inputs
bool check_word(string placeholder_word,string textfile_words[],int counter[FILE_WORDS]);     // checks to see if the word is correct or not


int main(){
    string COOR_ARRAY_NUMBER[NUMBER_ARRAY_LENGTH] = {"0","1","2","3","4","5","6","7","8","9","10","11","12","13","14"};
    string file_words[FILE_WORDS];
    char file_array[FILE_ARRAY][FILE_ARRAY];
    int counter[] = {0};
    load_file(get_file_name(), file_words, file_array);

    do{      // loop for the game terminates when the counter = 10
        display_puzzle(file_words, file_array, COOR_ARRAY_NUMBER);
        cout << counter[0] << endl;
        if(check_word(build_word(file_array), file_words, counter) == true)
            cout << endl << "Word is found "<< endl << endl;
        else if(check_word(build_word(file_array), file_words, counter) == false){
            display_puzzle(file_words, file_array, COOR_ARRAY_NUMBER);
            check_word(build_word(file_array), file_words, counter);
        }   
    }while(counter[0] < FILE_WORDS);                        // make a do while loop
    
    cout << "CONGRATS!! you have beaten the game" << endl;

    return 0;
}
string get_file_name(){            
    string txtfile_1 = "proj1_p1.txt";   // the 2 txt files that the user must input
    string txtfile_2 = "proj1_p2.txt";
    
    string user_input;        // user input variable
    cout << "please input the file you want to display: " << endl;
    getline(cin,user_input);            
    while(user_input != txtfile_1 && user_input != txtfile_2){
        user_input = "";
        cout << "please input the file you want to display: " << endl;
        cin >> user_input;
    }
    return user_input;



}
void load_file(string file_name, string file_words[], char file_array[][FILE_ARRAY]){
    ifstream inputStream;     // opens the file 
    string file_words_reader;      // reads the strings from the file (file words)
    int counter = 0;   // to track the while loop
    char individual_char;        // variable that holds the char from text file

    inputStream.open(file_name);  

    for(int i = 0; i < FILE_ARRAY; i++) { 
        for(int j = 0; j < FILE_ARRAY; j++) {      // to grab the 2d array 
            inputStream >> individual_char;      
            file_array[i][j] = individual_char;
        }
    }
    while(inputStream >> file_words_reader){      // for the strings
        file_words[counter] = file_words_reader;
        counter++;
    }


    inputStream.close();     

}
void display_puzzle(string file_words[],char file_array[][FILE_ARRAY], string number_array[]){
    for(int i = 0; i < 15; i++){
        if (i == 1)
            cout << number_array[0];
         for(int z = 0; z < 15; z++){
             if(i == 0){
                if(z == 14){
                    cout << '\t' << number_array[z] << "\n";
                    }
                else if(z != 14){
                    cout << '\t' << number_array[z];
                    }
                }
            else if(i != 0){
                if(z == 14){
                    cout << '\t' << file_array[i-1][z] << endl;
                    }
                else if (z != 14){
                    cout << "\t" << file_array[i-1][z];
                }
            }
        }
        if(i > 0){
            if (i == 1){
                cout << number_array[1];

            }else if(i > 1)
                cout  << number_array[i];

            }
    }
    for(int z = 0; z < 15; z++){
        if(z == 14){
            cout << '\t' << file_array[14][z] << endl;
        }
        else if (z != 14){
            cout << "\t" << file_array[14][z];
        }
    }

    for(int x = 0; x <= FILE_WORDS; x++){
        if(x == 0){
            cout << "----------REMMAINING WORDS----------" << "\n"
            << file_words[x] << endl;
        }
        else{
            cout << file_words[x] << endl;
        }

    }  

}
string build_word(char file_array[][FILE_ARRAY]){     
    int x1, y1, x2, y2; 
    string placeholder_word = "";     // empty string 
    
    cout << "what is the starting X Y coordinate (seperate with space): " << endl;           
    cin >> x1 >> y1;
    cout << "what is the ending X Y coordinate (seperate with space): " << endl;
    cin >> x2 >> y2;
    if(x1 > 15, y1 > 15, x2 > 15, y2 > 15 || x1 < 0, y1 < 0, x2 < 0, y2 < 0 ){   // to make sure it stays in bound 
        cout << "out of bounds" << endl;          
        cout << "what is the starting X Y coordinate (seperate with space): " << endl;
        cin >> x1 >> y1;
        cout << "what is the ending X Y coordinate (seperate with space): " << endl;
        cin >> x2 >> y2;
    }
    if(x1 == x2){    // this is the if statement for straight line 
        if(y1 > y2){       // this is supposed to read left 
          for(int i = y1, q = 0; i >= y2; i--, q++){
            //cout << i << '\t';
            //cout << file_array[x1 - 1][i - 1] << endl;
            //cout << q << endl << file_array[x1][i] << endl;
            placeholder_word = placeholder_word + file_array[x1][i];
            cout<< "this is : " << placeholder_word << endl;;
            //counter = q;
          }
          return placeholder_word;          
          
        }else if(y1 < y2){     // this is supposed to read right
            for(int i = y1, q = 0; i <= y2; i++, q++){
                //cout << file_array[x1][i] << endl;
                placeholder_word = placeholder_word + file_array[x1][i];
                //counter = q;
                //cout << "this is the letter: " << placeholder_word[q] << endl;
            }

            //return counter;
            return placeholder_word; 
        }   
    }else if(x1 > x2){   // looks up
        if(y1 == y2){
            for(int i = x1, q = 0; i >= x2; i--, q++){
                //cout << file_array[i][y1] << endl;
                placeholder_word = placeholder_word + file_array[i][y1];
                //counter = q;
            }
            //return counter;
            return placeholder_word; 

        }else if(y1 > y2){      // looks up diagonally to the left 
            for(int i = x1, z = y1, q = 0; i >= x2 && z >= y2; i--,z--,q++){
                //cout << "Letter " << file_array[i][z] << endl;
                placeholder_word = placeholder_word + file_array[i][z];
            }    
            return placeholder_word; 
            
        }else if (y1 < y2){    // looks up diagonally to the right
            for(int i = x1, z = y1, q = 0; i >= x2 && z <= y2; i--, z++, q++){
                //cout << "Letter " << file_array[i][z] << endl;
                placeholder_word = placeholder_word + file_array[i][z];
                //counter = q;
            }
            return placeholder_word; 
            //return counter;
        }
    }else if(x1 < x2){  // looks down 
        if(y1 == y2){
            for(int i = x1, q = 0; i <= x2; i++, q++){ 
                //cout << file_array[i][y1] << endl;
                placeholder_word = placeholder_word +file_array[i][y1];
                //counter = q;
            }
            return placeholder_word; 
            //return counter;

        }else if(y1 > y2){      // looks down diagonally to the left 
            for(int i = x1, z = y1, q = 0; i <= x2 && z >= y2; i++, z--, q++){
                //cout << "Letter " << file_array[i][z] << endl;
                placeholder_word = placeholder_word + file_array[i][z];
                //counter = q;
            }    
            return placeholder_word; 
            //return counter;

        }else if (y1 < y2){    // looks down diagonally to the right
            for(int i = x1, z = y1, q = 0; i <= x2 && z <= y2; i++, z++, q++){
                //cout << "Letter " << file_array[i][z] << endl;
                placeholder_word = placeholder_word +file_array[i][z];
                //counter = q;
            }
            return placeholder_word; 
            //return counter;
        }  
    }
    return "test";       
}
bool check_word(string placeholder_word, string textfile_words[],int counter[]){       
    bool checker = false;  // to see if the word is true
    for(int i = 0; i < FILE_WORDS; i++){              
        if(placeholder_word == textfile_words[i]){    // if its equal we change the array and return true          
            textfile_words[i] = " ";
            counter[0]++; 
            return checker = true;
        }
    }
    if(checker == false){          // try again 
        cout << "doesn't move, try again" << endl;     
        return checker;
    }
    return checker; 
}
