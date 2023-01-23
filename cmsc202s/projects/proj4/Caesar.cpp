#include "Caesar.h"



Caesar::Caesar():Cipher(){
    m_shift = 0;
}

Caesar::Caesar(string message, bool isEncrypted, int shift):Cipher(message,isEncrypted){
    m_shift = shift % 26;
}

Caesar::~Caesar(){
    //possibly change
    cout << "Caesar Deconstructor is called " << endl;
    Caesar.~Cipher();
}


  // Name: Encrypt
  // Desc: Shifts characters right based on shift (lower stay lower, upper stay upper)
  // Preconditions - Message exists
  // Postconditions - Shifts each character "right".
void Caesar::Encrypt(){
    string holder;
    int ascChar;
    for(int i = 0; i < Cipher::GetMessage().length();i++){
        ascChar = Cipher::GetMessage()[i];
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
    }
    Cipher::SetMessage(holder);
}
void Caesar::Decrypt(){
    string holder;
    int ascChar;
    for(int i = 0; i < Cipher::GetMessage().length();i++){
        ascChar = Cipher::GetMessage()[i];
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
    }
    Cipher::SetMessage(holder);
}

  // Name: ToString
  // Desc - A function that returns the string of the object type
  // Preconditions - The object exists
  // Postconditions - The subtype is returned (Caesar in this case)
string Caesar::ToString(){
    return "Caesar";
}

  // Name: FormatOutput()
  // Desc - A function that returns the formatted output for Output function
  // Preconditions - The object exists (use stringstream)
  // Postconditions - c, delimiter, isencrypted, delimiter,
  //                  message, delimiter, m_shift are returned for output
string Caesar::FormatOutput(){
    cout << 
    // come back
}