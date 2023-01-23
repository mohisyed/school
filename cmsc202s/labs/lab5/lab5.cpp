//Title: lab5.cpp
//Desc: To complete the DisplayProfile() and CheckEligibility() functions

#include <iostream>
#include <string>
#include "Athlete.h"
using namespace std;

//function DisplayProfile() declared here
void DisplayProfile(Athlete ath);

//function CheckEligibility() declared here
void CheckEligibility(Athlete ath);

int main() {
  Athlete Athlete1; //Creates a new Athlete
  Athlete Athlete2; //Creates a new Athlete

  Athlete1.SetName("LeBron"); //Calls the SetName to populate the m_name
  Athlete1.SetSport("Basketball"); //Calls the SetSport to populate the m_sportPlayed
  Athlete1.SetGPA(3.0); //Calls the SetGPA to populate the m_gpa
  Athlete1.SetProbation(true); //Calls the SetProbation to populate the m_onProbation

  Athlete2.SetName("Gronkowski"); //Calls the SetName to populate the m_brand
  Athlete2.SetSport("Football"); //Calls the SetSport to populate the m_price
  Athlete2.SetGPA(1.7); //Calls the SetGPA to populate the m_isBacklit
  Athlete2.SetProbation(true); //Calls the SetProbation to populate the m_onProbation

  cout << endl;
  DisplayProfile(Athlete1); //Calls the function DisplayProfile() (in lap5.cpp)
  cout << endl;
  DisplayProfile(Athlete2); //Calls the function DisplayProfile() (in lap5.cpp)

  cout << endl;
  CheckEligibility(Athlete1); //Calls the function CheckEligibility() (in lap5.cpp)
  CheckEligibility(Athlete2); //Calls the function CheckEligibility() (in lap5.cpp)

  return 0;
}

//Implement DisplayProfile() here
void DisplayProfile(Athlete ath){
  cout << "Name: " << ath.GetName() << endl;
  cout << "Sport: " << ath.GetSport() << endl;
  cout << "GPA: " << ath.GetGPA() << endl;
  cout << "On Probation: " << ath.GetProbation() << endl;
}

//Implement CheckEligibility() here

void CheckEligibility(Athlete ath){
  if(ath.IsEligible() == true)
    cout << ath.GetName() << " is eligbile to play " << ath.GetSport() << '!' << endl;
  else
    cout << ath.GetName() << " is ineligbile to play " << ath.GetSport() << '!' << endl;
}