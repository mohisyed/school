#include "Banana.h"
  
  // Name: ~Banana
  // Desc: Destructor for banana
  // Preconditions:  Banana exists
  // Postconditions: Banana is cleared
Banana::Banana(){

}

  // Name: Tick
  // Desc: A turn triggers
  // Preconditions: Banana exists
  // Postconditions: Checks to see if a racer runs into a banana
void Banana::Tick(bool){

}

  // Name: Crash
  // Desc: Decreases speed of racer and makes them spin out
  // Preconditions:  Banana exists
  // Postconditions: Speed returned is amount of speed reduced
int Banana::Crash(){}

  // Name: GetType
  // Desc: Returns the name of the subtype (Banana)
  // Preconditions:  None
  // Postconditions: Returns string name of the subtype (Banana)
string Banana::GetType(){}
  
  // Name: overloaded operator<<
  // Desc: Allows Banana objects to be outputted
  // Preconditions:  None
  // Postconditions: Outputs banana description
ostream& Banana::operator<<(ostream&){}
