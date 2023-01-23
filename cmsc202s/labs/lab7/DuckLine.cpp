//File: DuckLine.cpp
//Date: 3/28/2022 - 3/31/2022                                                                                         
//Description: you are working on this file! Adding and removing duck nodes from linked list

#include "DuckLine.h"

//Our linked list is called DuckLine. Think of ducks in a line, how cute is that! 

//PLEASE COMPLETE THIS FUNCTION
//Constructor
//Linked list is empty
DuckLine::DuckLine(){ //Constructor for linked list
  m_head = nullptr;
  m_tail = nullptr;
}


//**Provided**
//Destructor
//Deletes every duck in the linked list (Provided)
DuckLine::~DuckLine(){
  //until my linked list is empty, keep removing a duck!
  while(m_size > 0){
    RemoveLast();
  }
  //reset head and tail of linked list
  m_head = nullptr;
  m_tail = nullptr;
}

//PLEASE COMPLETE THIS FUNCTION
//InsertEnd function
//takes in age of duck to create a duck object. Then insert duck to end of linked list

  //create a new duck object


  //if linked list is empty



  //newly created duck becomes the new tail



  //increment size
void DuckLine::InsertEnd(int data){
  DuckNode* newNode = new DuckNode(data); //Create a pointer to the new node
  if(m_size == 0) { //If the list was empty,
    m_head = newNode;
    m_tail = newNode; //Set the tail node to be the new node
    m_size++;
  }else{
    DuckNode* temp = m_head;
    while(temp->m_next != NULL){
      temp = temp -> m_next;
    }
    temp -> m_next = newNode;
    m_tail = newNode;
    m_size++;
  }
}

//**Provided**
//Removes the last duck in the linked list
//consider special cases: when there is one duck, no duck, more than one duck in linked list 
void DuckLine::RemoveLast(){
  if(m_size == 0){
    //we can't remove anymore ducks if this is case
    cout << "Ducks are all gone" << endl;
  }
  else if (m_size == 1){
    //no need to iterate since there is only one node
    delete m_head;
    m_head = nullptr;
    m_tail = nullptr;
    m_size --;
    
  }else{
    //if more than one duck in linked list, must iterate curr to second to last node
    DuckNode *curr = m_head;
    while(curr -> m_next != m_tail){
      curr = curr->m_next;
    }
    //once curr is at second to last node, we delete its m_next
    delete curr -> m_next;
    //tail has now become curr
    m_tail = curr;
    m_tail -> m_next = nullptr;
    m_size --;
  }
}


//PLEASE COMPLETE THIS FUNCTION
//outputs the linked list which in this case is the duck line!
//Display function

  // make node pointer set to m_head

  // write loop

  // output data

  // move to next node

void DuckLine::Display(){
  DuckNode* temp = m_head; //Create a temp node to move through the list
  while (temp != nullptr) { //For each node, output the data and a separating arrow
    cout << temp -> m_age << " -> ";
    temp = temp -> m_next;
    }
  cout << "END" << endl; //Output the end of the list
  }


//Provided
int DuckLine::GetSize(){
  return m_size;
}
