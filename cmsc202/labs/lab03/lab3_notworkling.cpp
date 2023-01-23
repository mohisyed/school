
#include <iostream>
using namespace std;


void flipArray(int array[], int size);


int main(){
    int orig_array[101];
    int user_input;
    int counter = 0;
    while(user_input != 0 && counter <= 100){
        cout <<  "Please enter a integer.\n" << "Enter 0 when youre done" << endl;
        cin >> user_input;
        orig_array[counter] = user_input;
        counter++;
    }
    flipArray(orig_array,counter);
    return 0;
}
void flipArray(int array[], int size){
    int flipped[size];
    for(int i = 0; i <= size; i++) {
        if(i == 0){
            flipped[i] = array[size];
        }
        flipped[i] = array[size - i];
        
    }
    cout << flipped << endl;

}