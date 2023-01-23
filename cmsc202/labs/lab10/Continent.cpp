#include "Continent.h"

 // Constructor
  // Preconditions: None
  // Postconditions: None
Continent::Continent(){
    SetType("Continet");
    m_myName = "North America";
}
 
  // Destructor
  // Preconditions: None
  // Postconditions: None
Continent::~Continent(){}
 
  // Overloaded Constructor
  // Preconditions: None
  // Postconditions: Member variables initialized
Continent::Continent(string name){
    SetType("Continet");
    m_myName = name;
}
 
  // callMyName - Prints name
  // Preconditions: Has a name
  // Postconditions: None
void Continent::CallMyName(){
    cout << "I am the contienet of " << m_myName << endl;
}

 
  // describeMe() - gives description of given landmass
  // Preconditions: None
  // Postconditions: None
void Continent::DescribeMe(){
    cout <<"I am one of the seven continets! " << endl;
}