#include "Navigator.h"



  // Name: Navigator (string) - Overloaded Constructor
  // Desc: Creates a navigator object to manage routes
  // Preconditions:  Provided with a filename of ports to load
  // Postconditions: m_filename is populated with fileName
Navigator::Navigator(string fileName){
  m_ports; //Vector of all ports
  m_routes; //Vector of all routes
  m_fileName = fileName;
}
  // Name: Navigator (destructor)
  // Desc: Deallocates all dynamic aspects of a Navigator
  // Preconditions: There is an existing Navigator
  // Postconditions: All ports and routes are cleared
Navigator::~Navigator(){
  for(unsigned int i = 0; i < m_ports.size() - 1; i++){
    delete m_ports[i];
    m_ports[i] = nullptr;
  }
  for(unsigned int i = 0; i < m_routes.size() - 1 ; i++){
    delete m_routes[i];
    m_routes[i] = nullptr;
  }
  
}


  // Name: Start
  // Desc: Loads the file and calls the main menu
  // Preconditions: m_fileName is populated
  // Postconditions: All ports are loaded and the main menu runs
void Navigator::Start(){
  ReadFile();
  bool GameEnd = false;
  int userInput;
  while(GameEnd != true){
    MainMenu();
    cin >> userInput;
    switch(userInput){
      case 1:
        DisplayPorts();
        InsertNewRoute();
        break;
      case 2:
        DisplayRoute();
        break;
      case 3:
        RemovePortFromRoute();
        break;
      case 4:
        ReverseRoute();
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

  // Name: DisplayPorts
  // Desc: Displays each port in m_ports
  // Preconditions: At least one port is in m_ports
  // Postconditions: Displays all ports. Uses overloaded << provided in Port.h
void Navigator::DisplayPorts(){
    for(unsigned int i = 0; i < m_ports.size() - 1; i++){
        cout << i + 1  << ".) " << *m_ports[i] << endl;
    }
}

  // Name: ReadFile
  // Desc: Reads in a file that has data about each port including name, location, degrees
  //       north and degrees west. Dynamically allocates ports and stores them in m_ports
  //       The vector can hold many ports.
  // Preconditions: Valid file name of ports
  // Postconditions: Dynamically allocates each port and enters it into m_ports
void Navigator::ReadFile(){
    string name,location,north,west;
    double newNorth,newWest;
    ifstream myfile(m_fileName); 

    if(myfile.is_open()){
        while(!myfile.eof()){
            getline(myfile,name,',');
            //cout << name << ',';
            getline(myfile,location,',');
            //cout << location << ',';
            getline(myfile,north,',');
            newNorth = stod(north);
            //cout << newNorth << ',';
            getline(myfile,west,'\n');
            newWest = stod(west);
            //cout << newWest << endl;
            Port* onePort = new Port(name,location,newNorth,newWest);
            //cout << onePort->GetName() << endl;       
            m_ports.push_back(onePort);
            
        }
    }
    myfile.close();
}

  // Name: InsertNewRoute
  // Desc: Dynamically allocates a new route with the user selecting each port in the route.
  //       Route named based on the first and last port automatically
  //       For example, Baltimore to Boston
  //       Once route is created, inserted into m_routes.
  // Preconditions: Populated m_routes
  // Postconditions: Inserts a new route into m_routes
void Navigator::InsertNewRoute(){
  int portIndex = 0;
  Route* newRoute = new Route();
  while(portIndex != -1){
    portIndex = ChooseRoute();
    //cout << "this is the CHOOSE PORT INDEX " << portIndex << endl;
    for(int i = 0; i <= portIndex; i++){
      if(i == portIndex){
        //working
        //cout << m_ports[i]->GetName()<< m_ports[i]->GetLocation()<<m_ports[i]->GetNorth()<<m_ports[i]->GetWest() << endl;
        newRoute->InsertEnd(m_ports[i]->GetName(),m_ports[i]->GetLocation(),m_ports[i]->GetNorth(),m_ports[i]->GetWest());
      }
    }
  }
  //newRoute->SetName(newRoute->UpdateName());
  m_routes.push_back(newRoute);
}

  // Name: MainMenu
  // Desc: Displays the main menu and manages exiting
  // Preconditions: Populated m_ports
  // Postconditions: Exits when someone chooses 5
void Navigator::MainMenu(){
  int userInput;
  cout << "What would you like to do?" << endl;
  cout << "1. Create New Route" << endl
  << "2. Display Route" << endl
  << "3. Remove Port From Route" << endl
  << "4. Reverse Route" << endl
  << "5. End" << endl;
  while(userInput < 0 || userInput > 6){
    cout << "Choose a number between 1-5" << endl;
    cin >> userInput;
  }
}

  // Name: ChooseRoute
  // Desc: Allows user to choose a specific route to work with by displaying numbered list
  // Preconditions: Populated m_routes
  // Postconditions: Returns the index of the selected route minus 1
int Navigator::ChooseRoute(){
  unsigned int userChoice;
  cout << "Enter the number of the port to add to your Route: (-1 to end)" << endl;
  cin >> userChoice;
  while((userChoice < 0 || userChoice > m_ports.size()-1)){
    if(int(userChoice) == -1)
      return -1;
    cout << "Sorry that is out of range" << endl
    << "try again" << endl;
    cin >> userChoice;
  }
  return int(userChoice - 1);
}


  // Name: DisplayRoute
  // Desc: Using ChooseRoute, displays a numbered list of all routes.
  //       If no routes, indicates that there are no routes to display
  //       User selects a route from list to display
  //       Displays numbered list of each port in route
  //       Displays total miles of a route using RouteDistance
  // Preconditions: Routes has more than one port
  // Postconditions: Displays all ports in a route and the total miles of the route
void Navigator::DisplayRoute(){
  if(m_routes.size() == 0)
    cout << "No routes made" << endl;
  else{
    cout << "Which route would you like to choose" << endl;
    for(unsigned int i = 0; i < m_routes.size(); i++){
      cout << i+1 << ".) "<< m_routes[i]->GetName() << endl;
    }
    unsigned int userInput;
    cin >> userInput;
    //cout << m_routes.size() << endl;
    while(userInput < 0 || userInput > m_routes.size()+1){
      cout << "Sorry that is out of range" << endl
      << "try again"<< endl;
      cin >> userInput;
    }
    cout << m_routes[userInput-1]->GetName() << endl;
    m_routes[userInput-1]->DisplayRoute();
    cout << "The total miles of this route is " << RouteDistance(m_routes[userInput-1]) << endl;
  }
}

  // Name: RemovePortFromRoute()
  // Desc: Using ChooseRoute, displays a numbered list of all routes.
  //       User selects one of the routes to remove a port from.
  //       Displays a numbered list of all ports in selected route.
  //       User selects port to remove from list.
  //       Removes port from route. If first or last port removed, updates name of route.
  // Preconditions: Routes has more than one port
  // Postconditions: Displays updated route with removed port and new name
void Navigator::RemovePortFromRoute(){
  cout << "Which route would you like to choose" << endl;
  for(unsigned int i = 0; i < m_routes.size(); i++){
    cout << i + 1 << ".) "<< m_routes[i]->GetName() << endl;
  }
  unsigned int userInput;
  cin >> userInput;
  while(userInput < 0 || userInput > m_routes.size()){
    cout << "Sorry that is out of range" << endl
    << "try again"<< endl;
    cin >> userInput;
  }

  m_routes[userInput-1]->DisplayRoute();
  int secondUserInput = 0;
  cout << "Which port would you like to remove" << endl;
  cin >> secondUserInput;
  while(secondUserInput < 0 || secondUserInput > m_routes[userInput-1]->GetSize()){
    cout << "Sorry that is out of range" << endl
    << "try again"<< endl;
    cin >> secondUserInput;
  }
  m_routes[userInput-1]->RemovePort(secondUserInput-1);
  string holder = m_routes[userInput-1]->UpdateName();
  m_routes[userInput-1]->SetName(holder);
  
}

  // Name: RouteDistance
  // Desc: Calculates the total distance of a route
  //       Goes from port 1 to port 2 then port 2 to port 3 and repeats for
  //       length of route. Calculates the distance using CalcDistance (provided)
  //       Aggregates the total and returns the total in miles
  // Preconditions: Populated route with more than one port
  // Postconditions: Returns the total miles between all ports in a route
double Navigator::RouteDistance(Route* trueRoute){
  double totalDistance;
  int count = trueRoute->GetSize();
  for(int i = 0; i < count-1; i++)
    totalDistance = CalcDistance(trueRoute->GetData(i)->GetNorth(),trueRoute->GetData(i)->GetWest(),trueRoute->GetData(i+1)->GetNorth(),trueRoute->GetData(i+1)->GetWest());
  return totalDistance;
}

  // Name: ReverseRoute
  // Desc: Using ChooseRoute, users chooses route  and the route is reversed
  //       If no routes in m_routes, indicates no routes available to reverse
  //       Renames route based on new starting port and ending port
  //       For example, Baltimore to Boston becomes Boston to Baltimore
  // Preconditions: Populated m_routes
  // Postconditions: Reverses a specific route by reversing the ports in place
  //                 Must move ports, cannot just change data in ports.
void Navigator::ReverseRoute(){
  cout << "Which route would you like to choose" << endl;
  for(unsigned int i = 0; i < m_routes.size(); i++){
    cout << i << ".) "<< m_routes[i]->GetName() << endl;
  }
  unsigned int userInput;
  cin >> userInput;
  while(userInput < 0 || userInput > m_routes.size()){
    cout << "Sorry that is out of range" << endl
    << "try again"<< endl;
    cin >> userInput;
  }
  m_routes[userInput]->ReverseRoute();

}