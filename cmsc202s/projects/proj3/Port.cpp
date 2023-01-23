#include "Port.h"

  // Name: Port() - Default Constructor
  // Desc: Used to build a new empty port
  // Preconditions: None
  // Postconditions: Creates a new Port for use in a Route
Port::Port(){
    m_name = "New Port";
    m_location = "New Location";
    m_north = 0; 
    m_west = 0; 
    m_next = nullptr; 
}
Port::Port(string name, string location, double north, double west){
    m_name = name;
    m_location = location;
    m_north = north; 
    m_west = west; 
    m_next = nullptr; 
}
  // Name: ~Port() - Destructor
  // Desc: Used to destruct a port
  //**This function should be empty but must be implemented
  // Preconditions: There is an existing port
  // Postconditions: Port is deallocated and has no memory leaks!
Port::~Port(){
    cout << "PORT DESTRUCTOR IS CALLED" << endl;
}
string Port::GetName(){
    return m_name;
}

 // Name: GetNext()
  // Desc: Returns the pointer to the next port
  // Preconditions: None (may return either port or nullptr)
  // Postconditions: Returns m_next;
Port* Port::GetNext(){
    return m_next;
}
double Port::GetNorth(){
    return m_north;
}
double Port::GetWest(){
    return m_west;
}
string Port::GetLocation(){
    return m_location;
}
void Port::SetNext(Port* nextPort){
    m_next = nextPort;
}
