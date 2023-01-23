/**********
* File: Athlete.h
* Intended for Lab 5: Classes
**********/

#ifndef ATHLETE_H //Protects against multiple inclusion
#define ATHLETE_H //Protects against multiple inclusion

#include <iostream>
#include <string>

using namespace std;

// Add four private variables as indicated below
// Write all getters and setters for the four variables, and IsEligible function.
// An example getter and setter for m_onProbation has been done for you as an example
class Athlete {
public:
  Athlete(); //Default constructor

  //Write getters here
  string GetName();
  string GetSport();
  double GetGPA();
  bool GetProbation();
  //Write setters here
  void SetName(string name);
  void SetSport(string sport);
  void SetGPA(double gpa);
  void SetProbation(bool onProbation);


  //Write IsEligible here
  bool IsEligible();


private:
  // Create the 4 (name, sport, gpa, onProbation) private member variables here (use m_)
  // the first one has been done for you
  string m_name;
  string m_sportPlayer;
  double m_gpa;
  bool m_onProbation;
};

#endif
