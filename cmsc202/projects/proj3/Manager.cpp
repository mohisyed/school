#include "Manager.h"


Manager::Manager(string fileName){
  m_fileName = fileName;
  ReadFile(); 
}

Manager::~Manager(){
  for(unsigned int i = 0; i < m_schedules.size();i++){
    delete m_schedules[i];
  }
}


void Manager::DisplaySchedules(){
  for(unsigned int i = 0; i <= m_schedules.size();i++){
    cout << "Schedule " << i << " ->" << m_schedules[i] << endl;
  }
}

void Manager::ReadFile(){
  fstream inputStream;  // reads file 
  string fileLine;
  string scheduleInputName;
  string scheduleInputStringTime;
  string scheduleInputActivity;

  inputStream.open(m_fileName); 


  while(getline(inputStream,scheduleInputName,';')){
    getline(inputStream,scheduleInputStringTime,';');
    getline(inputStream,scheduleInputActivity);
  }
  
  
  inputStream.close(); 

  bool ifFound = false;
  for(unsigned int i = 0; i < m_schedules.size();i++){
    if(scheduleInputName == m_schedules[i]->GetName()){
      Item *event  = new Item(scheduleInputActivity,stoi(scheduleInputStringTime));
      m_schedules[i]->InsertSorted(event);
      ifFound = true;
    }
    if(ifFound == false){
      Item *notFoundEvent = new Item(scheduleInputActivity,stoi(scheduleInputStringTime));
      Schedule *notFoundSchedule = new Schedule(scheduleInputName);
      m_schedules.push_back(notFoundSchedule);
      notFoundSchedule -> InsertSorted(notFoundEvent);
    }
  }
  

}



void Manager::InsertNewItem(){
  string userScheduleName;
  string userScheduleTime;
  string userScheduleActivity;

  cout << "What is the name of the schedule you would like to insert into? " << endl;
  cin >> userScheduleName;
  cout << "What is the start time of the activity?" << endl;
  cin >> userScheduleTime; 
  cout << "What is the name of the activity?" << endl;
  cin >> userScheduleActivity;

  if(FindSchedule(userScheduleName) != -1){
    Item *event  = new Item(userScheduleActivity,stoi(userScheduleTime));
    m_schedules[FindSchedule(userScheduleName)]->InsertSorted(event);
    cout << "new item was created" << endl;
  }else{
    Item *notFoundEvent = new Item(userScheduleActivity,stoi(userScheduleTime));
    Schedule *notFoundSchedule = new Schedule(userScheduleName);
    m_schedules.push_back(notFoundSchedule);
    notFoundSchedule -> InsertSorted(notFoundEvent);
  }
}



int Manager::FindSchedule(string schedName){
  for(unsigned int i = 0; i <= m_schedules.size(); i++){
    if(schedName == m_schedules[i]->GetName()){
      return i;
    }
  }
  return -1;
}



  // Name:  MainMenu
  // Desc: Displays the main menu and manages exiting
  // Preconditions: Populated m_schedules
  // Postconditions: None
void Manager::MainMenu(){
  int userIntInput;
  cout << "What would you like to do? " << endl;
  cin >> userIntInput;
  if(userIntInput < 0 || userIntInput >= 4){
    cout << "Please choose a number between 1-4. " << endl;
    cout << "1. Display Schedules" << endl;
    cout << "2. Reverse Schedules" << endl;
    cout << "3. Insert New Item" << endl;
    cout << "4. Exit" << endl;
    cin >> userIntInput;
  }
  while(userIntInput != 4){
    if(userIntInput == 1){
      DisplaySchedules();
      cout << "its done" << endl;
    }else if(userIntInput == 2){
     ReverseSchedule();
     cout << "reversed the schedule" << endl; 
    }else if(userIntInput == 3){
      InsertNewItem();
      cout << "Inserted a new item" << endl;
  }
  }
  if(userIntInput == 4){
    
    return;
  }
}  



  // Name: ReverseSchedule
  // Desc: User chooses a schedule and the schedule is reversed
  //       If only one schedule in m_schedules, automatically reverses it without prompting the user
  // Preconditions: Populated m_schedules
  // Postconditions: Reverses a specific schedule replacing in place
void Manager::ReverseSchedule(){
  string userInput;
  if(m_schedules.size() != 1){
    cout << "Please chose a schedule: " << endl;
    cin >> userInput;
    while(FindSchedule(userInput) == -1){
      cout << "wrong input retry"<< endl;
      cin >> userInput;
    }
    m_schedules[FindSchedule(userInput)]->ReverseSchedule(); 
  }else{
   m_schedules[0]->ReverseSchedule();
  }
}