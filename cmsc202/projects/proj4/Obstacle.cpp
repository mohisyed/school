#include "Obstacle.h"

 // Name: Obstacle (Default constructor)
  // Desc: Creates an Obstacle
  // Preconditions:  Abstract class
  // Postconditions: Abstract class so used with child classes only.
Obstacle::Obstacle(){}

  // Name: Obstacle (Overloaded constructor)
  // Desc: Creates an Obstacle with 
  // Preconditions:  Abstract class
  // Postconditions: Abstract class so used with child classes only.
Obstacle::Obstacle(string){}
  
  // Name: ~Obstacle (Destructor
  // Desc: Deletes anything dynamically allocated
  // Preconditions:  Obstacle
  // Postconditions: Can be trivially implemented but required for subclass (tree)
Obstacle::~Obstacle(){}
  
  //Accessors
  
  // Name: GetColor
  // Desc: Returns m_color
  // Preconditions:  None
  // Postconditions: None
string Obstacle::GetColor(){}
  
  // Name: SetColor
  // Desc: Sets the color of an Obstacle
  // Preconditions:  None
  // Postconditions: m_color is set
void Obstacle::SetColor(string color){}
