#include <iostream>
#include <istream>
#include <string>
using namespace std;


  // Name: Decrypt
  // Desc: Shifts characters left based on shift (lower stay lower, upper stay upper)
  // Preconditions - Message exists
  // Postconditions - Shifts each character "left".

string encrypt(string test);
string dencrypt(string test);
void RailEncrypt(string test);

int main(){
    string test = "If you want to lift yourself up, lift up someone else. (Booker T. Washington)";
    string test2 = "do what you can, with what you have, where you are. (Theodore Roosevelt)";

    // int ascChar = 0;
    // int shift = 3 % 26;
    // for(int i = 0; i < test.length();i++){
    //     ascChar = test[i];
    //     if(ascChar >= 65 && ascChar <= 90){
    //         if(ascChar > 88)
    //             ascChar = (ascChar + 3) - 25;
    //         else
    //             ascChar +=3;
    //     }else if(ascChar >= 97 && ascChar <= 122){
    //         if(ascChar > 119)
    //             ascChar = (ascChar + 3) - 25;
    //         else
    //             ascChar +=3;
    //     }
    //     cout << (char)ascChar;
    // }

    // string holder = encrypt(test);
    // cout << holder << endl;
    // holder = dencrypt(holder);
    // cout << holder << endl << endl << endl;
    RailEncrypt(test2);

    return 0; 
}

string encrypt(string test){
    int ascChar = 0;
    int shift = 3;
    string holder;
    for(int i = 0; i < test.length();i++){
        ascChar = test[i];
        if(ascChar >= 65 && ascChar <= 90){
            if(ascChar > 88)
                ascChar = (ascChar + 3) - 25;
            else
                ascChar +=3;
        }else if(ascChar >= 97 && ascChar <= 122){
            if(ascChar > 119)
                ascChar = (ascChar + 3) - 25;
            else
                ascChar +=3;
        }
        holder += (char)ascChar;
        //cout << holder;
    }
    return(holder);
}

string dencrypt(string test){
    string holder;
    int ascChar = 0;
    for(int i = 0; i < test.length();i++){
        ascChar = test[i];
        if(ascChar >= 65 && ascChar <= 90){
            if(ascChar <= 67)
                ascChar = (ascChar - 3) + 25;
            else
                ascChar -= 3;
        }else if(ascChar >= 97 && ascChar <= 122){
            if(ascChar <= 99)
                ascChar = (ascChar - 3) + 25;
            else
                ascChar -=3;
        }
        holder += (char)ascChar;
        
    }
    return holder;
}


void RailEncrypt(string test){
    string holder[4][test.lenght()];
    int counter = 0; 
    //string returnString = "";
    //int counter2 = 0;
    //for(int x = 0; i < shift; i++){
    cout << "WOrkig" << endl;
    for(int i = 0;i < test.length();i++){
        //ascChar = Cipher::GetMessage()[i]
        //holder = Cipher::GetMessage[]
        if(i % (4*2)){
            if(i <= 4){
                holder[counter][] += test[i];
                cout << holder[counter];
                counter +=1;
            }else{
                holder[counter][] += test[i];
                cout << holder[counter];
                counter -=1;
            }  
        }
    }
    //cout << holder << endl;
    //return holder;
} 
    
