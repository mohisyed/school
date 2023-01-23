#include "Toad.h"

Toad::Toad():Character(){
}

Toad::Toad(string name, double top_speed, double handling, double acceleration):Character(name, top_speed, handling, acceleration){
}

Toad::~Toad(){
  cout << "Toad Deallocated" << endl;
}

string Toad::GetType(){
  return Character::GetName(); 
}

ostream& Toad::operator<<(ostream& output){
  output << "Toad (" << GetName() << ") has gone" << GetCurLocation() << " meters and is currently going " << GetCurSpeed() << " m/s";
  return output;
}

void Toad::SpecialMove(){}