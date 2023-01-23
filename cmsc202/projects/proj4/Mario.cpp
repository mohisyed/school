#include "Mario.h"



Mario::Mario():Character(){
  // maybe change
}

Mario::Mario(string name, double top_speed, double handling, double acceleration): Character(name, top_speed, handling, acceleration){
}

Mario::~Mario(){
  cout << "Mario Deallocated" << endl;
}

string Mario::GetType(){
  return Character::GetName();
}
ostream& Mario::operator<<(ostream& output){
  output << "Mario (" << GetName() << ") has gone" << GetCurLocation() << " meters and is currently going " << GetCurSpeed() << " m/s";
  return output;
}
void Mario::SpecialMove(){}
  