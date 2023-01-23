#include "Chemist.h"


// Name: Chemist() - Default Constructor
  // Desc: Used to build a new Chemist
  // Preconditions - Requires default values
  // Postconditions - Creates a new Chemist (with a default name of "Beaker" and
  //       m_numSubstances = 0
Chemist::Chemist(){
  string m_myName = "Beaker"; 
  Substance m_mySubstances[PROJ2_SIZE] = {}; 
  int m_numSubstances = 0; 
}

// Name: Chemist(name) - Overloaded constructor
  // Desc - Used to build a new Chemist
  // Preconditions - Requires name
  // Postconditions - Creates a new Chemist (with passed name and m_numSubstance = 0)
Chemist::Chemist(string name){
  string m_myName = name; 
  Substance m_mySubstances[PROJ2_SIZE] = {}; 
  int m_numSubstances = 0;
}     
  
string Chemist::GetName(){
  return m_myName;
}
  
void Chemist::SetName(string name){
  m_myName = name;
}

  // Name: CheckSubstance(Substance)
  // Desc - Checks to see if the Chemist has a substance if so, returns
  //        the index where it exists, if not returns -1
  // Preconditions - Chemist already has substance
  // Postconditions - Returns index of substance if Chemist has it else -1
int Chemist::CheckSubstance(Substance sub1){
  for(int i = 0; i < PROJ2_SIZE; i++){
      if(sub1.m_name == m_mySubstances[i].m_name)     // check 
          return i;
  }
  //cout << "Check Substance function: substance not found" << endl;
  return -1;
}
 // Name: AddSubstance(string)
  // Desc - Inserts a material into the Chemist's list of substances. Has
  //        to see if it exists in m_mySubstances first to find location.
  //        Then adds substance and increments m_numSubstances
  // Preconditions - Chemist exists
  // Postconditions - Add a substances to the Chemist's m_mySubstances with a quantity of 0

void Chemist::AddSubstance(Substance sub1){     //ask what it does 
  int checker = CheckSubstance(sub1);
  if(checker == -1){
    m_mySubstances[m_numSubstances] = sub1;
    //cout << m_mySubstances[m_numSubstances].m_name <<':'<< m_mySubstances[m_numSubstances].m_type <<':'<<  m_mySubstances[m_numSubstances].m_formula <<':'<<  m_mySubstances[m_numSubstances].m_substance1 <<':'<<  m_mySubstances[m_numSubstances].m_substance2 << endl;      // testing
    m_numSubstances += 1;
  }
  else{
    cout << "add substance function: substance not found" << endl;   // don't need it just to check
    return;
  }
}

// Name: IncrementQuantity(Substance)
// Desc - Adds quantity to list of substances the chemist knows.
//        Has to find location in array first. Then increments quantity
// Preconditions - Chemist exists
// Postconditions - Increases quantity of material for chemist
void Chemist::IncrementQuantity(Substance sub1){
  int index = CheckSubstance(sub1);
  m_mySubstances[index].m_quantity += 1;
  
}

  // Name: DecrementQuantity(Substance)
  // Desc - Reduces quantity from chemist's inventory with true, if no quantity false
  // Preconditions - Chemist exists
  // Postconditions - Reduces quantity of substance for chemist
bool Chemist::DecrementQuantity(Substance sub1){     // by 1  also change 
  int index = CheckSubstance(sub1);
  if(sub1.m_quantity >= 1){
    m_mySubstances[index].m_quantity -=1;
    return true;
  }
  else{
    cout << "already zero" << endl;
    return false;
  }
}



// Name: CheckQuantity(Substance)
// Desc - Checks to see if quantity of two merge substances is greater than one.
//        if the quantity of substance 1 is greater than one and the
//        quantity of substance two is greater than one, returns true else false
// Preconditions - Chemist exists with substances
// Postconditions - Returns true if both are available

bool Chemist::CheckQuantity(Substance sub1, Substance sub2){
  if(sub1.m_quantity > 0 && sub2.m_quantity > 0){
    cout << "ture" << endl;
    return true;    
  }
  else
    return false;
  }

// Name: GetSubstance(int)
// Desc - Returns a substance at at specific index
// Preconditions - Chemist already has substances
// Postconditions - Returns substance at specific index

Substance Chemist::GetSubstance(int index){
  return m_mySubstances[index];
}
  // Name: GetTotalSubstances
  // Desc - Iterates over m_mySubstances and counts each substance with a quantity higher than 0
  // Preconditions - Chemist may have no substances
  // Postconditions - Returns number of substances with a quantity greater than 0
int Chemist::GetTotalSubstances(){
  return m_numSubstances;
}