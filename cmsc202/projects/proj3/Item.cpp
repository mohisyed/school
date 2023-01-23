#include "Item.h"


Item::Item(){
  m_name = "New Item"; 
  m_time = 0; 
  m_next = nullptr; 
}
Item::Item(string item_name, int time){
    m_name = item_name;
    m_time = time;
    m_next = nullptr;
}
string Item::GetName(){
    return m_name;
}
int Item::GetTime(){
    return m_time;
}

Item* Item::GetNext(){   // double check if this works
    return m_next;
}

void Item::SetName(string itemName){
    m_name = itemName;
}
void Item::SetTime(int itemTime){
    m_time = itemTime;
}
void Item::SetNext(Item* itemNext){      // see if this works
    m_next = itemNext;
}