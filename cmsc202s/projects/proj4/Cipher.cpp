#include "Cipher.h"

  // Name: Cipher (Default Constructor)
  // Desc - Stores a message and if it is encrypted (or not)
  // Preconditions - None
  // Postconditions - A message is stored in a Cipher object
Cipher::Cipher(){
    m_message = "this is just a test";
    m_isEncrypted = false;
}
Cipher::Cipher(string message, bool isEncrypted){
    m_message = message
    m_isEncrypted = isEncrypted;
}
virtual Cipher::~Cipher(){
    cout << "cipher is getting deconstructed" << endl;
    delete Cipher;
}
string Cipher::GetMessage(){
    return m_message;
}
bool Cipher::GetIsEncrypted(){
    return m_isEncrypted;
}
void Cipher::SetMessage(string){
    m_message = string;
}
void Cipher::ToggleEncrypted(){
    if(m_isEncrypted == false){
        m_isEncrypted = true;
    }else{
        m_isEncrypted = false;
    }
}

  // Name: Overloaded << Operator
  // Desc - Outputs the message
  // Preconditions - The object exists
  // Postconditions - The message from the object is returned
ostream& Cipher::operator<<( ostream &output, Cipher &C){
    // come back need help
    cout <<  c.message << "|" << c.m_isEncrypted;
}