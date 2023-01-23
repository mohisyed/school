#include "Landmass.h"



Landmass::Landmass(){
    m_myType = "Unknown";
}
 
  // Destructor
  // Preconditions: None
  // Postconditions: None
Landmass::~Landmass(){}
 
  // callMyType() - Prints object's type
  // Preconditions: Object exists
  // Postconditions: Object's type is printed
void Landmass::CallMyType(){
    cout << "My Land Mass is " << m_myType << endl;
}
 
 
  // getType() - returns myType
  // Preconditions: myType is initialized
  // Postconditions: None
string Landmass::GetType(){
    return m_myType;
}
 
  // setType() - sets value of myType
  // Preconditions: None
  // Postconditions: None
void Landmass::SetType(string type){
    m_myType = type;
  }
 
