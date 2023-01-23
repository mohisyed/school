#include <iostream>
using namespace std;
/*
const int WORD_INPUT = 4;     // needs to turn into an int error 1 

void populateArray(char array[WORD_INPUT]);
void printArray(char array[WORD_INPUT]);
int main(){
  char myWord[WORD_INPUT];        // need to define the length of the array
  populateArray(myWord);
  printArray(myWord);
  return 0;
}
void populateArray(char array[WORD_INPUT]){
  char tempWord[WORD_INPUT];
  cout << "Enter a " << WORD_INPUT << " letter word: "<< endl;
  cin >> tempWord;
  for(int i =0; i <= WORD_INPUT; i++){
    array[i] = tempWord[i];
  }
}

void printArray(char array[WORD_INPUT]){
  int i = (WORD_INPUT);
  while(i >=0){
    cout << array[i];
    i++;
  }
  cout << endl;
}
*/

int main(){
  char array1[] = "First Array";
  char array2[] = "Second Array";
  cout << "These arrays are " << (array1==array2?" not ":"") << "equal." << endl;
}