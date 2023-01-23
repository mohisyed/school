#include "Island.h"


// Constructor
  // Preconditions: None
  // Postconditions: None
Island::Island(){
    SetType("Island");
    m_myName = "Hawaii";
}
 
  // Destructor
  // Preconditions: None
  // Postconditions: None
Island::~Island(){}
 
  // Overloaded Constructor
  // Preconditions: None
  // Postconditions: Member variables initialized
Island::Island(string name){
    SetType("Island");
    m_myName = name;
}
 
  // callMyName - Prints name
  // Preconditions: Has a name
  // Postconditions: None
void Island::CallMyName(){
    cout << "I am a beautiful island named " << m_myName << endl;
}
void Island::DescribeMe(){
    cout << "I am surrounded by a body of water." << endl;

}
