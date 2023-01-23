//Title: lab5.cpp
//Desc: To complete the DisplayDetails and GoodValue functions

#include <iostream>
#include <string>
#include "Laptop.h"
using namespace std;

//Write the functions DisplayDetails and GoodValue here
void DisplayDetails(Laptop);
string GoodValue(Laptop);

int main() {
  Laptop Laptop1; //Creates a new laptop
  Laptop Laptop2; //Creates a new laptop
  cout << endl;

  Laptop1.change_m_brand("Apple"); //Calls the SetBrand to populate the m_brand
  Laptop1.change_m_price(2300); //Calls the SetPrice to populate the m_price
  Laptop1.change_m_memory(16); //Calls the SetMemory to populate the m_memory
  Laptop1.change_m_isBacklist(true); //Calls the SetBacklit to populate the m_isBacklit
  
  Laptop2.change_m_brand("Lenovo"); //Calls the SetBrand to populate the m_brand
  Laptop2.change_m_price(899); //Calls the SetPrice to populate the m_price
  Laptop2.change_m_memory(16); //Calls the SetMemory to populate the m_memory
  Laptop2.change_m_isBacklist(true); //Calls the SetBacklit to populate the m_isBacklit

  DisplayDetails(Laptop1); //Calls the function DisplayDetails (in lap5.cpp)
  DisplayDetails(Laptop2); //Calls the function DisplayDetails (in lap5.cpp)

  GoodValue(Laptop1); //Calls the function GoodValue (in lap5.cpp)
  GoodValue(Laptop2); //Calls the function GoodValue (in lap5.cpp)
  
  return 0;
}

//Implement DisplayDetails here
void DisplayDetails(Laptop Laptop_what){
  cout << "Laptop Brand: " << Laptop_what.display_m_brand() << endl
  << "Cost: " << Laptop_what.display_m_price() << endl << "RAM: " 
  << Laptop_what.display_m_memory() << endl << "Backlit Keyboard: "
  << Laptop_what.display_m_isBacklist() << endl;

}




//Implement GoodValue here
string GoodValue(Laptop Laptop_what){
  if(Laptop_what.WorthIt(Laptop_what.display_m_memory(),Laptop_what.display_m_price(),Laptop_what.display_m_isBacklist()) == true) 
    return "This laptop is totally worth it!";
  else
    return "This laptop is totally not worth it!";
}


