#include "Lab.h"

// Name: Lab() Default Constructor
  // Desc - Instantiates an object of type Lab
  // Preconditions - None
  // Postconditions - None
Lab::Lab(){  //Default Constructor
    Chemist m_myChemist; //Player's Chemist for the game
    Substance m_substances[PROJ2_SIZE];    
  
}


// Name: LoadSubstances
// Desc - Loads each substance into m_substances from file
//        The loads all substances from m_substances into m_myChemist's substance array
// Preconditions - Requires file with valid substance data
// Postconditions - m_substance is populated with substance structs
void Lab::LoadSubstances(){
    string name,type,formula,subElement1,subElement2; 
    ifstream myfile("proj2_data.txt");       
    int counter = 0;
    if(myfile.is_open()){
        for(int i = 0; i < START_ELEMENTS; i++){
            getline(myfile,name,',');
            getline(myfile,type,',');
            getline(myfile,formula,',');
            getline(myfile,subElement1,',');
            getline(myfile,subElement2,'\n');
            m_substances[i] = Substance(name,type,formula,subElement1,subElement2,0);
            //cout << m_substances[i].m_name <<':'<< m_substances[i].m_type <<':'<< m_substances[i].m_formula <<':'<< m_substances[i].m_substance1 <<':'<< m_substances[i].m_substance2 << endl;      // testing
            counter = i;
        }
        cout << counter << " substances are loaded" << endl;
    }
    myfile.close();
}   





  // Name: StartLab()
  // 1. Displays Lab Title (as implemented below)
  // 2. Loads all substances and their recipes into m_substances (Load Substances)
  // 3. Asks user for their chemist's name (store in m_myChemist as m_myName)
  // 4. Copies all substances from m_substances into the chemist's substance array
  // 5. Manages the game itself including win conditions continually calling the main menu 
  // Preconditions - None
  // Postconditions - m_substances and m_myChemist's substances populated
void Lab::StartLab(){
    LabTitle();
    LoadSubstances();

    string userName;
    
    cout << "What is the Chemist name? " << endl;
    cin >> userName;

    bool GameEnd = false;

    m_myChemist.SetName(userName);

    for(int i = 0; i < START_ELEMENTS; i++){
      //cout << m_substances[i].m_name << endl;
      m_myChemist.AddSubstance(m_substances[i]);
    }

  int userInput;
  while(GameEnd != true){
    userInput = MainMenu();
    switch(userInput){
      case 1:
        DisplaySubstances();
        break;
      case 2:
        SearchSubstances();
        break;
      case 3:
        CombineSubstances();
       break;
      case 4:
        CalcScore();
        break;
      case 5:
        cout << "Thanks for playing " << endl;
        GameEnd = true;
        break;
      default:
        cout << "Choose a number between 1-5" << endl;
        cin >> userInput;
    }
  }  
}

  // Name: DisplayMySubstances()
  // Desc - Iterates over m_myChemist's substances
  // Preconditions - Player's chemist has substances
  // Postconditions - Displays a numbered list of substances
void Lab::DisplaySubstances(){
    for(int i = 0; i < START_ELEMENTS; i++){
        cout << i + 1 << ".) "<< m_myChemist.GetSubstance(i).m_name << "\t" << m_myChemist.GetSubstance(i).m_formula << "\t"<<m_myChemist.GetSubstance(i).m_quantity << endl;
    }
}
  // Name: MainMenu()
  // Desc - Displays and manages menu
  // Preconditions - Player has an Chemist
  // Postconditions - Returns number including exit
int Lab::MainMenu(){
  int choice;
  cout << "What would you like to do?" << endl;
  cout << "1. Display your Chemist's Substances" << endl;
  cout << "2. Search for Elements" << endl;
  cout << "3. Attempt to Merge Substances" << endl;
  cout << "4. See Score" << endl;
  cout << "5. Quit" << endl;
  cin >> choice;
  while(choice < 0 || choice > 6){
    cout << "Choose a number between 1-5" << endl;
    cin >> choice;
  }
  //return choice;
}
  // Name: SearchSubstances()
  // Desc - Attempts to search for raw substances (must be type "element")
  // Preconditions - Raw substances loaded
  // Postconditions - Increases quantity in Chemist's posession of substances
void Lab::SearchSubstances(){
    int index;
    Substance holder;
    for(int i = 0; i < START_ELEMENTS; i++){
        if(m_myChemist.GetSubstance(i).m_type == "element"){
            index = rand() % NUM_ELEMENT;
            holder = m_myChemist.GetSubstance(index);
            m_myChemist.IncrementQuantity(holder);
            cout << m_myChemist.GetSubstance(index).m_name << endl;
            cout << m_myChemist.GetSubstance(index).m_quantity << endl;
            return;
        }
    }
}
  // Name: CombineSubstances()
  // Desc - Attempts to combine known substances. If combined, quantity of substance decreased
  // 1. Requests user to choose two substances (RequestSubstance)
  // 2. Checks to see if formula exists for combining two chosen substances
  //     (checks sub1, sub2 and sub2, sub1) using SearchFormula
  // 3. If there is an available formula for two chosen substances, checks
  //     quantity for two chosen substance.
  // If no quantity for two substances, tells user that there is no available quantity
  // If quantity is available, decreases quantity for two chosen substances
  //     from the chemist then increases new substance
  // 4. If there is no available formula, tells user that nothing happens when you try and merge two chosen substances
  // Preconditions - Chemist is populated with substances
  // Postconditions - Increments quantity of substance "made", decreases quantity of source items
void Lab::CombineSubstances(){
  int userChoice1;   // index
  int userChoice2;   

  RequestSubstance(userChoice1);
  userChoice1 = userChoice1 - 1;
  RequestSubstance(userChoice2);
  userChoice2 = userChoice2 - 1;

  int index = SearchFormulas(m_myChemist.GetSubstance(userChoice1).m_formula,m_myChemist.GetSubstance(userChoice2).m_formula);
  if(index > 0){
    if(m_myChemist.CheckQuantity(m_myChemist.GetSubstance(userChoice1),m_myChemist.GetSubstance(userChoice2)) == false)
      cout << "No available quanity for " << m_myChemist.GetSubstance(userChoice1).m_name << " and " << m_myChemist.GetSubstance(userChoice2).m_name << endl;
    else{
      m_myChemist.DecrementQuantity(m_myChemist.GetSubstance(userChoice1));
      m_myChemist.DecrementQuantity(m_myChemist.GetSubstance(userChoice2));
      m_myChemist.IncrementQuantity(m_myChemist.GetSubstance(index));
      cout << "Your Chemist has made " << m_myChemist.GetSubstance(index).m_name << endl;
    }
  }
  else{
    cout << "nothing happens when you try to merge "<< m_myChemist.GetSubstance(userChoice1).m_name << " and "<< m_myChemist.GetSubstance(userChoice2).m_name << endl;
  }
    
}
  // Name: RequestSubstance()
  // Desc - Allows the user to choose a substance to try and merge.
  //        Returns the index of chosen substance
  // Preconditions - Chemist has substances to try and merge
  // Postconditions - Returns integer of substance selected by user
void Lab::RequestSubstance(int &choice){
    cout << "Which substances would you like to merge? (choose -1 to display the list of of elements and compounds) " << endl;
    cin >> choice;
    while(choice < 0 || choice >= START_ELEMENTS + 1){
      if(choice == -1){
        DisplaySubstances();
        cout << "Which substances would you like to merge? (choose -1 to display the list of of elements and compounds) " << endl;
        cin >> choice;
      }else{
        cout << "Need to choose an number in between 1 - " << START_ELEMENTS << endl;
        cin >> choice;
      }
    }
}
  // Name: SearchFormula()
  // Desc - Searches formulas for two strings (name of item)
  // Preconditions - m_substances is populated
  // Postconditions - Returns int index of matching formula
int Lab::SearchFormulas(string form1, string form2){
  for(int i = 0; i < START_ELEMENTS; i++){
    if((form1 == m_substances[i].m_substance1 ||form1 == m_substances[i].m_substance2) && (form2 == m_substances[i].m_substance1 ||form2 == m_substances[i].m_substance2))
      return i;
  }
  return 0;
}
  // Name: CalcScore()
  // Desc - Displays current score for Chemist
  // Preconditions - Chemist is populated with substances
  // Postconditions - Displays total number of substances found. Displays
  //        percentange found as number found divided by total available
void Lab::CalcScore(){
  int counter = 0;
  double percent = 0.0;
  for(int i = 0; i < START_ELEMENTS; i++){
    if(m_myChemist.GetSubstance(i).m_quantity >0)
      counter += 1;
  }
  percent = (counter/double(START_ELEMENTS)) * 100;
  cout << "The Great Chemist " << m_myChemist.GetName() << endl;
  cout << "They're " << START_ELEMENTS << " Substances avialbe to find" << endl;
  cout << "You have found " << counter << " so far" << endl;
  cout << "This is " << percent << '%' << endl;
}

  // Name: LabTitle()
  // Desc - Title for Lab (Do not edit)
  // Preconditions - None
  // Postconditions - None