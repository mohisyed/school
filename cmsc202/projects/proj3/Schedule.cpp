#include "Schedule.h"  
  

Schedule::Schedule(){
    m_name = "default"; 
    m_head = nullptr; 
    m_tail = nullptr; 
    m_size = 0;
}
Schedule::Schedule(string scheduleName){
    m_name = scheduleName; 
    m_head = nullptr; 
    m_tail = nullptr; 
    m_size = 0;
}
Schedule::~Schedule(){      
    Item *curr = m_head;
    while(curr != nullptr){
        m_head = curr;
        curr = curr -> GetNext();    
        delete m_head;
    }
    m_head = nullptr;
    m_tail = nullptr;
    m_size = 0;
}

  // Name: InsertSorted
  // Desc: Inserts a new item into the schedule. Inserts it from earliest time (0) to highest time (2359) ascending
  //       Does NOT insert at correct location when reversed
  // Preconditions: Takes in an Item pointer. Inserts the node based on time.
  //                Requires a Schedule
  // Postconditions: Adds the new item into the Schedule.
void Schedule::InsertSorted(Item* newItem){   
    //newItem = new *Item();
    // to hold the node you're going to replace

    Item *curr = m_head; // the node that is going to replace
    Item *prev = m_head; // the node that looks one space behind
    m_size++; // just adding one node

    //newItem -> m_next = nullptr;
    if(m_head == nullptr){
        m_head = newItem;
        m_tail = newItem;  //change to nullptr?
        return;
    }while(curr != nullptr){ // while current is not null pointer
        if(newItem -> GetTime() < curr -> GetTime()){
            if(newItem -> GetTime() < prev -> GetTime()){
                m_head = newItem;
                newItem -> SetNext(curr);
                curr -> SetNext(m_tail);
                return;
            }
            prev -> SetNext(newItem);
            newItem -> SetNext(curr);
            return;
        }
        prev = curr;
        curr = curr -> GetNext();
    }
    prev -> SetNext(newItem);
    m_tail = newItem;

}

string Schedule::GetName(){
    return m_name;
}

int Schedule::GetSize(){
    return m_size;
}


// Name: ReverseSchedule
// Preconditions: Reverses the Schedule
// Postconditions: Schedule is reversed in place; nothing returned
void Schedule::ReverseSchedule(){ 
    Item *curr = m_head;
    Item *prev = nullptr;
    Item *next = nullptr;

    while(curr != nullptr){
        next = curr -> GetNext();
        curr -> SetNext(prev);
        prev = curr;
        curr = next;
    }
    m_tail = m_head;   // check
    m_head = prev;
}


// Name: GetData
// Desc: Returns the time at a specific location in the Schedule
//       Pass 
// Preconditions: Requires a Schedule
// Postconditions: Returns data from specific item
// Note: May not be used in project but still required
Item* Schedule::GetData(int nodeNum){
    Item* temp = m_head;
    for(int i = 0; i < nodeNum; i++){
        if(i == nodeNum){
            return temp;
        }
        temp = temp -> GetNext();
    }
    return nullptr;
}




