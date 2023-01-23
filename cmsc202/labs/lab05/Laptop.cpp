#include "Laptop.h"
/**********
* File: Laptop.cpp
*
* Intended for Lab 5: Classes
*
**********/

//Constructor -- Already Implemented
/*
Laptop::Laptop() {
  cout << "Manufacturing a Laptop..." << endl;
}
*/
//Implement Getters here


bool Laptop::display_m_isBacklist() {
  return m_isBacklist;
}
string Laptop::display_m_brand(){
  return m_brand;
}
double Laptop::display_m_price(){
  return m_price;
}
int Laptop::display_m_memory(){
  return m_memory;
}


//Implement Setters here

void Laptop::change_m_isBacklist(bool isBacklit) {
  m_isBacklist = isBacklit;
}
void Laptop::change_m_brand(string mbrand){
  m_brand = mbrand;
}
void Laptop::change_m_price(double price){
  m_price = price;
}
void Laptop::change_m_memory(int mem){
  m_memory = mem;
}



//Implement WorthIt here
//Should be greater than or equal to 8gb memory, less than $1000, and backlit to be "worth it

bool Laptop::WorthIt(int mem ,double price ,bool backlit){
  if(mem >= 8 && price < 1000 && backlit == true)
    return true;
  else 
    return false;
}
