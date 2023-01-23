#include "Athlete.h"
/**********
* File: Athlete.cpp
* Intended for Lab 5: Classes
**********/

//Default Constructor -- Already Implemented
Athlete::Athlete() {
  cout << "Accessing Athlete Profile..." << endl;
}

//Implement Getters here

string Athlete::GetName(){
  return m_name;
}
string Athlete::GetSport(){
  return m_sportPlayer;
}
double Athlete::GetGPA(){
  return m_gpa;
}
bool Athlete::GetProbation(){
  return m_onProbation;
}

//Implement Setters here
void Athlete::SetName(string name){
  m_name = name;
}
void Athlete::SetSport(string sport){
  m_sportPlayer = sport;
}
void Athlete::SetGPA(double gpa){
  m_gpa = gpa;
}
 
void Athlete::SetProbation(bool onProbation) {
  m_onProbation = onProbation;
}

//Implement IsEligible() here
bool Athlete::IsEligible(){
  if(m_gpa >= 2.0 && m_onProbation != false)
    return true;
  else if(m_gpa >= 3.0 && m_onProbation == true)
    return true;
  else
    return false;
}