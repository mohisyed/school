//File: lab6.cpp                                                                                                              

#include <iostream>
#include <string>
#include <vector>
#include "Groceries.h"
using namespace std;

//COMPLETE THIS FUNCTION                                                                                                      
void fillVector(vector<Groceries> &groceryList){
  string name;
  int numbGroceries, price, quantity;

  cout << "How many Groceries do you want? ";
  cin >> numbGroceries;
  //groceryList.push_back(numbGroceries);

  for(int i = 0; i < numbGroceries; i++){

    cout << "Whats the name? ";
    cin >> name;
    grocery.push_back(name);
    groceryList.setItem(name);

    cout << "Whats the price? ";
    cin >> price;
    //groceryList.push_back(price);
    groceryList.setPrice(price);

    cout << "Whats the quantity? ";
    cin >> quantity;
    //groceryList.push_back(quantity);
    groceryList.setQuantity(quantity);
    
  }
  

  // ask for amount of grocery items                                                                                          
  // ask for name, price, quantity of each item and                                                                           
  // add them to vector                                                                                                       
}

//COMPLETE THIS FUNCTION                                                                                                      
void printVectorWithoutIterator(vector<Groceries> &groceryList){
  for(unsigned int i = 0; i < groceryList.size(); i++){
        cout << groceryList[i] << endl;
    }

  // print each item's name, price, and quantity with correct                                                                 
  // precision for price                                                                                                      
  // DON'T USE ITERATOR                                                                                                       

}

//COMPLETE THIS FUNCTION                                                                                                      
void printVectorWithIterator(vector<Groceries> &groceryList){
  for(vector<Groceries>::iterator it = groceryList.begin(); it != groceryList.end(): ++it){
    cout<< '\t' << groceryList[it]<< endl;
  }
}

  // print each item's name, price, and quantity with correct                                                                 
  // precision for price                                                                                                      
  // USE ITERATOR                                                                                                       


void checkStatus(vector<Groceries> &groceryList){

  //DEFINE ENUM HERE BASED ON NAMES BELOW  
  enum listSize{nonMem, bronze, silver, gold}                                                                                                        
  int listSize = groceryList.size();

  switch (listSize) {
  case nonMem: cout << "You did not purchase enough items to become a member." << endl;
    break;
  case bronze: cout << "You purchased enough items to become a bronze member." << endl;
    break;
  case silver: cout << "You purchased enough items to become a silver member." << endl;
    break;
  default: cout << "You purchased enough items to become a gold member!" << endl;
  }
}

int main(){

  vector<Groceries> groceryList; //Creates a new vector of Groceries

  fillVector(groceryList); //Populates the vector of Groceries
  printVectorWithoutIterator(groceryList); //Displays the contents of the vector
  cout << endl;
  //printVectorWithIterator(groceryList); //Alterate way to display the contents of the vector
  checkStatus(groceryList); //calls function defined above (must define enum)

  return 0;
}
