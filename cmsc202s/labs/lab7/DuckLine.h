//File: duckline.h
//Date: 3/28/2022 - 3/31/2022
//Description: header file for linked list and duck nodes
#ifndef DUCKLINE_H_
#define DUCKLINE_H_
#include <iostream>
using namespace std;

//Our nodes in the linked list will be little ducks!
struct DuckNode {
  //duck constructor
  DuckNode(){
    m_age = 1; // Sets default duck age to 1
    m_next = nullptr; //Sets m_next to nullptr
  }
  //overloaded constructor
  DuckNode(int age){
    m_age = age; //Sets m_age based on age passed
    m_next = nullptr; //Sets m_next to nullptr
  }
  int m_age; //our node's data (duck age)
  DuckNode * m_next; //pointer to next node which is duck's sibling
};

class DuckLine {
 public:
  DuckLine(); //Constructor for our linked list (You)
  ~DuckLine(); //Destructor for our linked list (Provided)
  void Display(); //outputs the linked list (You)
  void RemoveLast(); //removes the last duck object in linked list (Provided)
  void InsertEnd(int); //inserts duck object to end of linked list (You)
  int GetSize(); //size of linked list (Provided)
 private:
  int m_size; //number of ducks that are in our duckline
  DuckNode *m_head; //points to beginning of linked list/first ducky
  DuckNode *m_tail; //points to end of linked list/the last ducky!
};

#endif
