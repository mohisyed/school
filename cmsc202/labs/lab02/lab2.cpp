/*
 * lab2.cpp
 * This program practices C++ regarding input/output, loops, functions in C++
 */

#include <iostream>
using namespace std;

// FUNCTION PROTOYPES FOR sumOfDoubles() and greaterThanTwenty() GO HERE  *
double sumOfDoubles();
void greaterThanTwenty(double);

//*******main********
/*
The user should enter their desired amount of numbers, and the program should display the final
value after the operations, as well as if the total is greater than twenty or not.
This logic must be implemented in one line. This means that the main() function can have ONE
statement (and the return 0).
*/
//Implement main here:
int main(){
    greaterThanTwenty(sumOfDoubles());


    return 0;
}

//******sumOfDoubles*****
//The user should be prompted to enter how many doubles they would like to add together
//Afterwards, the user should enter values until the number of specified doubles is reached
//Print and return the sum
//Implement sumOfDoubles() here:
double sumOfDoubles(){
    double num1;
    double num2 = 0.0; 
    int user_input;

    cout << "how many do doubles do you want to add?\n";
    cin >> user_input;
    for(int i = 0; i < user_input; i++){
        cout << "Enter the double you want to add up\n";
        cin >> num1;
        num2 += num1;
        
    }  
    return num2;
}




//******greaterThanTwenty*****
/*
The program should display a message to indicate whether the double passed is greater 
than twenty or not
*/
//Implement greaterThanTwenty here:

void greaterThanTwenty(double sum){
    if (sum > 20)
        cout << sum << " greater than 20\n";
    else if (sum <= 20)
        cout << sum << " less than 20\n";

}