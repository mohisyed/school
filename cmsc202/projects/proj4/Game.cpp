#include "Game.h"

  // Name: Game() - Default Constructor
  // Description: Creates a new Game. Welcomes player to UMBC Mario Kart. Initializes laps and racers to 1
  // Preconditions: None
  // Postconditions: m_numLaps and m_numRacers initialized to 1
Game::Game(){
    Track myTrack; 
    vector<Entity*> m_Racers; 
    int m_numLaps = 1; 
    int m_numRacers = 1; 
    string m_playerName;
}
Game::~Game(){
    for(unsigned int i = 0; i < m_numRacers.size(); i++){
        m_Racers.at(i)->GetType();
    }
}

void Game::LoadTrack(){
    int user_input = 0;
    cout << "1.)" << TRACK[0][0] << endl;
    cout << "2.)" << TRACK[1][0] << endl;  
    cout << "3.)" << TRACK[2][0] << endl;
    cout << "please choose the following: " << endl;
    cin >> user_input;
    while(user_input < 1 || user_input > 3){
        cout << "please choose again: " << endl;
        cout << "1.)" << TRACK[0][0] << endl;
        cout << "2.)" << TRACK[1][0] << endl;  
        cout << "3.)" << TRACK[2][0] << endl;
        cin >> user_input;
    }
    cout << "You've chosen " << TRACK[user_input][0] << endl;

    for(int i = 0; i < m_numLaps; i++){
        myTrack.LoadTrack(TRACK[user_input][0]);
        cout << "Loaded Track " << i;
    }
}

 // Name: RaceSetup
  // Description: Asks the user for their name and stores it in local variable
  //              Allows user to choose which racer to use (Mario, Wario, or Toad) using provided name
  //              Allows the user to choose how many other racers to use (no limit) - Randomly assigned (can be duplicates)
  //              Allows the user to choose how many laps to race (no limit)
  // Preconditions: None
  // Postconditions: m_Racers populated with racers, m_numLaps populated
void Game::RaceSetup(){
    //Entity *player, *opp;
    string user_name;
    int userRacerInput, oppRacers, user_track_input;

    cout << "What is your name? " << endl;
    cin >> user_name;
    user_name = m_playerName;

    cout << "1.) Mario" << endl;
    cout << "2.) Wario" << endl;
    cout << "3.) Toad" << endl;
    cin >> userRacerInput;

    while(userRacerInput < 1 || userRacerInput > 3){
        cout << "please choose again: " << endl;
        cin >> userRacerInput;
    }
    if(userRacerInput == 1){
        //player = new Mario(m_playerName,MARIO_STATS[0],MARIO_STATS[2],MARIO_STATS[1]);  // might need to change the way the mario stats is ordered
        m_Racers.push_back(new Mario(m_playerName,MARIO_STATS[0],MARIO_STATS[2],MARIO_STATS[1]));
    }else if(userRacerInput == 2){
        //player = new Wario(m_playerName,WARIO_STATS[0],WARIO_STATS[2],WARIO_STATS[1]);
        m_Racers.push_back(new Wario(m_playerName,WARIO_STATS[0],WARIO_STATS[2],WARIO_STATS[1]));
    }else if(userRacerInput == 3){
        //player = new Toad(m_playerName,TOAD_STATS[0],TOAD_STATS[2],TOAD_STATS[1]);
        m_Racers.push_back(new Toad(m_playerName,TOAD_STATS[0],TOAD_STATS[2],TOAD_STATS[1]));
    }
    
    cout << "Please enter how many opponents you would like to play against? " << endl;
    cin >> oppRacers;
    for(int i = 0; i < oppRacers; i++){
        srand(time(NULL));
        int randX = rand() % 3;
        userRacerInput = randX;
        if(userRacerInput == 1){
            //opp = new Mario("Mario",MARIO_STATS[0],MARIO_STATS[2],MARIO_STATS[1]);  // might need to change the way the mario stats is ordered
            m_Racers.push_back(new Mario("Mario",MARIO_STATS[0],MARIO_STATS[2],MARIO_STATS[1]));
        }else if(userRacerInput == 2){
            //opp = new Wario("Wario",WARIO_STATS[0],WARIO_STATS[2],WARIO_STATS[1]);
            m_Racers.push_back(new Wario("Wario",WARIO_STATS[0],WARIO_STATS[2],WARIO_STATS[1]));
        }else if(userRacerInput == 3){
            //opp = new Toad("Toad",TOAD_STATS[0],TOAD_STATS[2],TOAD_STATS[1]);
            m_Racers.push_back(new Toad("Toad",TOAD_STATS[0],TOAD_STATS[2],TOAD_STATS[1]));
        }
    }
    cout << "How many laps would you like to do (1-3)? " << endl;
    cin >> user_track_input; 
    while(user_track_input < 1 || user_track_input > 3){
        cout << "please choose again: " << endl;
        cin >> user_track_input;
    }
    m_numLaps = user_track_input;
}



 // Name: StartRace()
  // Description: As long as the race isn't over or the user hasn't quit repeat these:
  //              Displays current position in track for user
  //              Shows round number
  //              Displays current piece description on track
  //              Displays the next piece description on track (like what is ahead)
  //              Makes computer racers randomly choose a speed for this round (100%, 75%, 50%, 25%)
  //              Tick (passing max speed)
  //              Reorder vector based on who has moved the most down the track (m_curLocation)
  //              Display the order
  // Preconditions: LoadTrack and RaceSetup must have been completed
  // Postconditions: Continues until race is over. If completed, displays result (who won)
void Game::StartRace(){
    // do this at the end will take allot of time
    // FindPlayer()
    int round = 1;
    cout << "you will be racing " << m_numLaps << " laps" << endl;
    cout << "The total Length of the race is " << myTrack.GetTotalLength() << endl;
    myTrack.DisplayPiece(m_Racers.at(FindPlayer())->GetCurLocation());
    cout << endl
         << "*********ON YOUR MARKS*********" << endl
         << "*********GET SET*********" << endl
         << "*********GO! GO! GO!*********" << endl; 
    
    while((CheckFinish() != true) && (Action() != 6)){
        Action();
        if(Action() == 1)
            m_Racers.at(FindPlayer())->CalcSpeed(1.0);   // might need to change the calc speed numbers
        else if(Action() == 2)
            m_Racers.at(FindPlayer())->CalcSpeed(.75);
        else if(Action() == 3)
            m_Racers.at(FindPlayer())->CalcSpeed(.50);
        else if(Action() == 4)
            m_Racers.at(FindPlayer())->CalcSpeed(.25);
        else if(Action() == 5)
            cout << "WORK IN PROGRESS" << endl;
        
        cout << "************************" << endl
             << "Round: " << round << endl
             << "************************" << endl;
        cout << "You currently see:" << endl;
        myTrack.DisplayPiece(m_Racers.at(FindPlayer())->GetCurLocation());
        cout << "Ahead is " << endl;
        myTrack.DisplayPiece(m_Racers.at(FindPlayer())->GetCurLocation());  // change

        CpuRandom();
        Tick(myTrack.GetMaxSpeed(myTrack.GetPiece(m_Racers.at(FindPlayer())->GetCurLocation()))); // change later
        Order();
        Display();
        CheckFinish();
        round ++;
    }
    if((CheckFinish() == true) || (Action() == 6))
        cout << "GAME OVER" << endl;  

}

  // Name: CheckFinish
  // Description: Checks to see if any racer has exceeded total length of the track
  // Precondition: m_Racers has been populated and myTrack has been populated
  // Postcondition: Returns true if race is over; else false
bool Game::CheckFinish(){
    for(unsigned int i = 0; i < m_Racers.size(); i++){
        if (m_Racers.at(i)->GetCurLocation() > myTrack.GetTotalLength())
            return true;
    }
    return false;
}

  // Name: CpuRandom
  // Description: Iterates over all computer m_Racers and uses CalcSpeed to randomly assign either (100%, 75%, 50%, 25%)
  // Precondition: m_Racers has been populated
  // Postcondition: Using CalcSpeed, updates racer's speeds
void Game::CpuRandom(){
    srand(time(NULL));
    for(unsigned int i = 0; i < m_Racers.size(); i++){
        double randX = (rand()% 4 + 1) * .25;
        m_Racers.at(i)->CalcSpeed(randX);
    }
}
  // Name: Tick
  // Description: Iterates over all computer m_Racers and calls Tick and passes the maxSpeed of the current piece of track that racer is on
  // Precondition: m_Racers has been populated and myTrack has been populated
  // Postcondition: Checks to see if the racer crashes by exceeding the max limit of that track piece

void Game::Tick(double maxCurrentSpeed){ // need to change this function 
    for(unsigned int i = 0; i < m_Racers.size(); i++){
        if(m_Racers.at(i)->GetCurSpeed() > maxCurrentSpeed)
            cout << m_Racers.at(i)->GetType() << "has crashed" << endl;
            // might need to create an another else statement
    }
}

  // Name: Order
  // Description: Uses a simple bubble sort (nested for loops) to reorder who has traveled the farthest
  // Precondition: m_Racers has been populated
  // Postcondition: m_Racers is sorted from highest distance traveled to lowest distance traveled
void Game::Order(){
  for(unsigned int i = 0; i < m_numRacers.size(); i++){
    (m_Racers.at(i))->SetCurLocation(((m_Racers.at(i))->GetCurLocation()) + ((m_Racers.at(i))->GetCurSpeed()));
  }
  for(unsigned int i = 0; i < m_numRacers.size(); i++){
    for(unsigned int i = 0; i < m_numRacers.size(); j++){
      if(((m_Racers.at(i))->GetCurLocation()) < ((m_Racers.at(j))->GetCurLocation())){
        swap(m_Racers[i], m_Racers[j]);
      }
    }
  }
}

}

  // Name: Display
  // Description: Displays each racer in m_Racers by using overloaded << operator
  // Precondition: m_Racers has been populated
  // Postcondition: Usage is *m_Racers.at(i) << cout << endl;
void Game::Display(){
    for(unsigned int i = 0; i < m_Racers.size(); i++){
        *m_Racers.at(i) << cout << endl;
    }
    // need help 
}

  // Name: Action()
  // Description: Menu for game
  //              Required to implement cases 1-4 and 6.
  //              Choice 5 (Attack) is optional and is part of the extra credit
  //              Asks the user if they want to change their speed
  // Preconditions: Everything in start has been completed
  // Postconditions: Game continues until someone finishes race
int Game::Action(){
    int userChoice;
	cout << "What would you like to do?: " << endl
		 << "1. Max Speed" << endl
		 << "2. Pretty Fast" << endl
		 << "3. Fast" << endl
		 << "4. Slow" << endl
		 << "5. Use Obstacle" << endl
		 << "6. Quit" << endl;
    cin >> userChoice; 
    while(userChoice < 1 || userChoice > 6){
        cout << "wrong choice try again " << endl;
        cin >> userChoice;
    }
    return userChoice;
}


  // Name: FindPlayer
  // Description: Iterates over all racers in m_Racers to return the index of where the player's racer exists (after sort)
  // Precondition: m_Racers has been populated and sort has been called
  // Postcondition: Returns the index of where the player's racer exists
int Game::FindPlayer(){
    for(unsigned int i = 0; i < m_Racers.size(); i++){
        if(m_playerName == m_Racers.at(i)->GetType())
        return i;
    }
    cout << "no player" << endl;
    return 0;

}