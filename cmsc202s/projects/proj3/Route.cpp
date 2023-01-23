#include "Route.h"

Route::Route(){
    m_name = "test";
    m_head = nullptr;
    m_tail = nullptr;
    m_size = 0;
}

// Name: SetName(string)
// Desc: Sets the name of the route (usually first port to last port)
// Preconditions: None
// Postconditions: Sets name of route
void Route::SetName(string name){
    m_name = name;
}

// Name: ~Route() - Destructor
// Desc: Used to destruct a strand of Route
// Preconditions: There is an existing Route strand with at least one port
// Postconditions: Route is deallocated (including all dynamically allocated ports)
//                 to have no memory leaks!
Route::~Route(){
    Port *curr = m_head;
    while(curr != nullptr){
        m_head = curr;
        curr = curr -> GetNext();    
        delete m_head;
    }
    m_head = nullptr;
    m_tail = nullptr;
    m_size = 0;
}

// Name: InsertEnd (string, string, double double)
// Desc: Creates a new port using the data passed to it.
//       Inserts the new port at the end of the route
// Preconditions: Takes in a Port
//                Requires a Route
// Postconditions: Adds the new port to the end of a route
void Route::InsertEnd(string name , string location, double north, double west){
  Port* newNode = new Port(name, location, north, west);
   if(m_size == 0) { //If the list was empty,
    newNode->SetNext(m_head);
    m_head = newNode;
    m_tail = newNode; //Set the tail node to be the new node
    m_size++;
  }else{
    Port* temp = m_head;
    while(temp->GetNext() != nullptr){
      temp = temp->GetNext();
      //temp->SetNext(temp->GetNext());
    }
    //cout << "out of while loop" << endl;
    temp->SetNext(newNode);
    //newNode->SetNext(nullptr);
    SetName(m_head->GetName()+ " to " + newNode->GetName());
    m_tail = newNode;
    m_size++;
  }
}

// Name: RemovePort(int index)
// Desc: Removes a port from the route at the index provided
//       Hint: Special cases (first port, last port, middle port)
// Preconditions: Index must be less than the size of the route
//       Cannot make route less than two ports. If the route has
//       two or fewer ports, fails.
// Postconditions: Name may be updated. Size is reduced. Route has one less port.
void Route::RemovePort(int index){
  if(m_size <= 2)
    cout << "cannot remove port has less than 3 ports" << endl;
  else{
    Port *curr = m_head;
    Port *prev = m_head;
    int counter;
    //cout << "Before the elif statements" << endl;
    if(index+1 == 1){
      //cout << "first if statement: index = 1" << endl;
      m_head = m_head -> GetNext();
      m_size--;
    }else if(index+1 == m_size){
      cout << "Second if statement: index == " << m_size << endl;
      counter = 0;
      cout << " before while " << endl;
      cout << index << endl;
      while(counter != index+1)
        cout << "In the while loop " << endl;
        prev = curr;
        curr = curr -> GetNext();
        cout << prev->GetName() <<  '=' << curr->GetName() << endl;
        cout << counter << endl;
        counter++;
        cout << counter << endl;
      prev->SetNext(curr->GetNext());
      m_tail = curr;
      m_size--;
    }else{
      cout << "Third ifelse statement: ELSE statement" << endl;
      counter = 0;
      Port *prev = m_head;
      while(counter != index+1){
        prev = curr;
        curr = curr->GetNext();
        counter += 1;
      }
      prev->SetNext(curr->GetNext());
      m_size--;
      //prev->GetNext() = curr->GetNext();
    }
    delete curr,prev;
  }
}  

// Name: GetName()
// Desc: Returns the name of the route (Usually starting port to last port)
//       For example: Baltimore to Brunswick
// Preconditions: Requires a Route
// Postconditions: Returns m_name;
string Route::GetName(){
  return m_name;
}

// Name: UpdateName()
// Desc: Updates m_name based on the name of the first port in the route
//       and the last port in the route
//       For example: Baltimore to Brunswick
// Preconditions: Requires a Route with at least two ports
// Postconditions: Returns m_name;
string Route::UpdateName(){
  Port* temp = m_head;
  string strTemp;
  while(temp->GetNext() != nullptr){
    if(temp == m_head)
      strTemp = temp -> GetName();
    temp = temp -> GetNext();
  }
  strTemp += " to "; 
  strTemp += temp -> GetName();
  return strTemp;
}

// Name: GetSize()
// Desc: Returns the number of ports in a route
// Preconditions: Requires a Route
// Postconditions: Returns m_size;
int Route::GetSize(){
  return m_size;
}

// Name: ReverseRoute
// Desc: Reverses a route
// Preconditions: Reverses the Route
// Postconditions: Route is reversed in place; nothing returned
void Route::ReverseRoute(){
  Port* current = m_head;
  Port* prev = nullptr;
  Port* next = nullptr;
  while(current != nullptr){
    next = current -> GetNext();
    prev = current -> GetNext();
    prev = current;
    current = current->GetNext();
  }
  m_head = prev;
  UpdateName();
}

// Name: GetData (int)
// Desc: Returns a port at a specific index
// Preconditions: Requires a Route
// Postconditions: Returns the port from specific item
Port* Route::GetData(int index){
  Port* temp = m_head;
  int counter = 0;
  while(temp != nullptr){
    if(counter == index)
      return temp;
    temp = temp -> GetNext();    // might need to change with the Port::SetNext 
    counter += 1;
  }

}

// Name: DisplayRoute
// Desc: Displays all of the ports in a route
// Preconditions: Requires a Route
// Postconditions: Displays all of the ports in a route
// Formatted: Baltimore, Maryland (N39.209 W76.517)
void Route::DisplayRoute(){
  Port* temp = m_head;
  int i = 0;
  while(temp != nullptr) {
    cout << i+1 << ".) " << temp->GetName() << ", " << temp->GetLocation() << " (N" << temp-> GetNorth() << " W" << temp-> GetWest() << ')' << endl;
    temp = temp->GetNext();
    i++;
  }
  delete temp;
}
