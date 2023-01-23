#include "RailFence.h"

RailFence::RailFence():Cipher(){
    m_rails = 0;
}


RailFence::RailFence(string message, bool isEncrypted, int shift):Cipher(message,isEncrypted){
    m_shift = shift;
}

RailFence::~RailFence(){
    cout << "Railfence Deconstructor is called " << endl;
}

// Name: Encrypt
// Desc: Letters are placed on a fence rail based on the number of rails
//       Letters are read from one rail at a time into a single string
// Preconditions - Message exists
// Postconditions - A single encrypted string is stored
void RailFence::Encrypt(){
    string holder[m_shift][Cipher::GetMessage().length()] = {""};
    int counter = 0; 
    int counter2 = 0;
    //for(int x = 0; i < shift; i++){
    for(int i = 0 i < Cipher::GetMessage().length();i++){
            //ascChar = Cipher::GetMessage()[i]
            //holder = Cipher::GetMessage[]
            if(counter % shift){
                if(counter2 % (shift * 2)){
                    
                }
            }
        } 
        //}
    }
}