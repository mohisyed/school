/*
* Mohiuddin Syed
* Lab 1
* 09/10/21
* Cmsc 202
*/

#include <iostream>
using namespace std;

int main(){
  char user_input[80];
  int cat_age ;
  int user_input_while;
  int choices = 0;
  
  cout << "What is your cat's name: " << endl;  
  cin >> user_input;

  while(cin.fail()){
    cout << "this failed \n";
    cout << "What is your cat's name: " << endl;
    cin.clear();
    cin.ignore(80,'\n');
    cin >> user_input;


  }


 
  cout << "How old is your cat? \n" << "Please enter a integer between 0 and 22\n";
  cin >> cat_age;
  if (cat_age<=0 || cat_age > 22){
    while (cat_age<=0 || cat_age > 22){
      cout << "please enter a integer between 0 and 22\n";
      cin >> cat_age;
    }
  }

  cout << "Cat Name = " << user_input << endl;
  cout << "Cat's age = " << cat_age << endl;


  cout << " What you would you like to do?\n"<< "1.\t Pet "<< user_input<< endl <<"2.\t Feed "<< user_input<< endl <<"3.\t Chase "<< user_input << endl;
  while (choices < 3){
    if (user_input_while >=1 && user_input_while<=3){
      cout << " What you would you like to do?\n"<< "1.\t Pet "<< user_input<< endl <<"2.\t Feed "<< user_input<< endl <<"3.\t Chase "<< user_input << endl;
      cout << " enter your choice (1-3)";   
      cin >> user_input_while;
      if(user_input_while == 1){
       cout << "you pet the cat\n";
       choices +=1;
      }
      else if(user_input_while == 2){
       cout << "you feed the cat\n";
       choices +=1;
      }
      else if(user_input_while == 3){
       cout << "you chase the cat\n";
       choices += 1;
       }
      
    }

    else if(user_input_while < 1 || user_input_while > 3){
        cout << "Choose a number between 1-3 please" << endl;
        cin >> user_input_while;
      if(user_input_while == 1){
       cout << "you pet the cat\n";
       choices +=1;
      }
      else if(user_input_while == 2){
       cout << "you feed the cat\n";
       choices +=1;
      }
      else if(user_input_while == 3){
       cout << "you chase the cat\n";
       choices += 1;
       }

  }
  
  }
  if (choices>=3) 
  cout << "game over" << endl;

  return 0;
}

