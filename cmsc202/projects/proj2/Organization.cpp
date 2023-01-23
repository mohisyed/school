#include "Organization.h"


// Name: SetName
// Desc - Sets m_name by asking user for name
// Preconditions - m_name exists
// Postconditions - Asks user for the organization name and populates m_name


Organization::Organization(){
    string m_name; 
    string m_fileName; 
    int m_numRoster; 
    Person m_roster [MAX_PEOPLE]; 
}

void Organization::SetName(){
    cout << "What is the name of the Organization: " << endl;
    getline(cin, m_fileName);
}

// Name: LoadRoster
// Desc - Sets m_fileName by asking user. Then populates all of the people loaded from file
// Preconditions - m_fileName exists. m_roster empty
// Postconditions - Asks user for m_fileName. Loads data from file and populates m_roster
void Organization::LoadRoster(){         //might need to fix 
    fstream inputStream;
    Person temp;
    inputStream.open(FILE_NAME);
    string fileLine;
    string firstName, lastName;
    int age, id;
    for(int i = 0; i < MAX_PEOPLE; i++){
        getline(inputStream, fileLine, ',');
        firstName = fileLine;
        getline(inputStream, fileLine, ',');
        lastName = fileLine;
        getline(inputStream, fileLine, ',');
        cout << fileLine << endl;
        age = stoi(fileLine);
        getline(inputStream, fileLine, '\n');
        cout << fileLine << endl;
        id = stoi(fileLine);
        temp = Person(firstName, lastName, age, id);
        m_roster[i] = temp;
    }
}

// Name: DisplayRoster
// Desc - Displays a numbered list of everyone in the roster (starts at 1)
// Preconditions - m_roster is populated
// Postconditions - Displays a numbered list of people
void Organization::DisplayRoster(){
    string tempFirst;
    string tempLast;
    for(int i = 0; i <= m_numRoster; i++){
        //tempFirst = m_roster[i].m_fName;
        //tempLast = m_roster[i].m_lName;
        cout << i + 1 << '\t';
        m_roster[i].DisplayDetails();
    }
}


// Name: GetPerson
// Desc - Displays a list of people in m_roster and user enters number of desired person.
//        Returns pointer of that person in m_roster
// Preconditions - m_roster is populated
// Postconditions - Returns pointer for the person chosen from list
Person* Organization::GetPerson(){     // get this checked
    DisplayRoster();
    Person* personPtr;
    int user_input = 0; 
    cout << "Enter the number of the person you want to search for: " << endl;
    cin >> user_input;

    while(user_input <= m_numRoster || user_input >= m_numRoster){
        cout << "The number is either too big or to small. " << endl; 
        cout << "Please try again " << endl;
        cin >> user_input;
    }

    //personPtr = m_roster[user_input-1];
    //return personPtr;
    return &m_roster[user_input - 1];
}

