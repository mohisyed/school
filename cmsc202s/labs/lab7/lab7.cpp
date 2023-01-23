//File: lab7.cpp
//Date: 3/28/2022 - 3/31/2022                                                                                         
//Description: here we insert and remove ducks to imitate the story of the "Five Little Ducks"
#include "DuckLine.h"

int main(){
  DuckLine ducks;
  //we insert five ducks
  ducks.InsertEnd(1);
  ducks.InsertEnd(2);
  ducks.InsertEnd(3);
  ducks.InsertEnd(4);
  ducks.InsertEnd(5);
  cout << endl;
  cout << ducks.GetSize() << " little ducks went out one day, over the hills and far away" << endl;
  ducks.Display();
  cout << endl;

  //in the nursery song, all five ducks get lost one at a time
  for(int i = 0; i < 5; i ++){
    ducks.RemoveLast();
    cout << "Mother duck said quack quack quack, and ";
    if(ducks.GetSize() == 0){
      cout << "none of the little ducks came back" << endl;
    }else{
      cout << "only " << ducks.GetSize();
      cout << " little ducks came back" << endl;
    }
    //every time we lose a duck, display the linked list
    ducks.Display();
    cout << endl;
  }

  //once all of the ducks are gone, mother duck gets sad
  //but then all of the ducks come back
   if(ducks.GetSize() == 0){
    
    cout << "Sad mother duck went swimming one day, over the hill and far away. Mother duck said quack quack quack" << endl;
    
    ducks.InsertEnd(1);
    ducks.InsertEnd(2);
    ducks.InsertEnd(3);
    ducks.InsertEnd(4);
    ducks.InsertEnd(5);
    ducks.Display();
    cout << "AND ALL " << ducks.GetSize() << " LITTLE DUCKS CAME BACK!" << endl;
    cout << endl;
    }
														      
   return 0;
}
