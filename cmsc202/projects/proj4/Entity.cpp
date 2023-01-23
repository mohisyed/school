#include "Entity.h"

  // Name: Entity() - Default Constructor
  // Description: Abstract class - cannot directly instantiate this class
  // Preconditions: None
  // Postconditions: Populates variables used in child classes (not specifically used)
Entity::Entity(){
  m_name = "Default";
}

  // Name: Entity(string) - Overloaded Constructor
  // Description: Abstract class - cannot directly instantiate this class
  // Preconditions: None
  // Postconditions: Populates variables used in child classes
Entity::Entity(string name){
  m_name = name;
}

Entity::~Entity(){
  cout << "Entity deconstructor" << endl;
}
  // Name: GetName()
  // Description: Returns name of entity
  // Preconditions: Entity has name
  // Postconditions: None
string Entity::GetName(){
  return(m_name);
}


 // Name: SetName()
  // Description: Sets name of entity
  // Preconditions: None
  // Postconditions: Name is set
void Entity::SetName(string name){
  m_name = name;
}