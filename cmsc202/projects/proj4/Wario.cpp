#include "Wario.h"

Wario::Wario():Character(){
}

Wario::Wario(string name, double top_speed, double handling, double acceleration):Character(name, top_speed, handling, acceleration){
}

Wario::~Wario(){
    cout << "Wario Deallocated" << endl;
}

string Wario::GetType(){
    return Character::GetName();  // might be wrong
}

ostream& Wario::operator<<(ostream& output){
  output << "Wario (" << GetName() << ") has gone" << GetCurLocation() << " meters and is currently going " << GetCurSpeed() << " m/s";
  return output;
}
void Wario::SpecialMove(){}