#include "FriendFinder.h"

// Name: GetDetails
// Desc - Asks user for their first name, last name, age, and ID to populate m_me
// Preconditions - None
// Postconditions - Populates information related to m_me
FriendFinder::FriendFinder(){
    Person m_me; 
    Organization m_organization;
    Start(); 

}
void FriendFinder::GetDetails(){
    string f_name, l_name;
    int intial_ages, intial_id;

    cout << "Enter your first name: " << endl;
    cin >> f_name;

    cout << "Enter your last name: " << endl;
    cin >> l_name;

    cout << "Enter your age: " << endl;
    cin >> intial_ages;

    cout << "Enter your id " << endl;
    cin >> intial_id;

    m_me.SetDetails(f_name,l_name,intial_ages,intial_id);

}

// Name: DisplayMenu
// Desc - Displays main menu for application
// Preconditions - None
// Postconditions - Called from Start updates integer passed

void FriendFinder::DisplayMenu(int &choice){         // what does choice do 
    /*do{ 
        cout << "1.  Display entire organization " << endl; 
        cout << "2.  Display friends list " << endl; 
        cout << "3.  Search for a friend " << endl; 
        cout << "4.  Remove friend " << endl; 
        cout << "5.  Exit " << endl;
    }*/
    int choices = choice;
    while(choice != 5){
        do{
            cout << "1.  Display entire organization " << endl; 
            cout << "2.  Display friends list " << endl; 
            cout << "3.  Search for a friend " << endl; 
            cout << "4.  Remove friend " << endl; 
            cout << "5.  Exit " << endl;
            cout << "Please choose a choice: " << endl;
            cin >> choices;
            cout << "1";
        }while(choice < 1 || choice > 5);
        switch(choices){
            case 1:
            cout << "1";
            m_organization.DisplayRoster();
            break;
            case 2:
            m_me.DisplayFriends();
            break;
            case 3:
            m_organization.GetPerson();
            break;
            case 4:
            m_me.RemoveFriend();
            break;
            case 5:
            cout << "Thank you for using umbc friend finder" << endl;
            break;

        default:
        cout << "try again: " << endl;
        cin >> choices;
        break;
    }
    }
    
    if (choice == 5){
        cout << "Thank you for using umbc friend finder" << endl;
    }
    /*cout << "What you like to do?" << endl; 
    cout << "1.  Display entire organization " << endl; 
    cout << "2.  Display friends list " << endl; 
    cout << "3.  Search for a friend " << endl; 
    cout << "4.  Remove friend " << endl; 
    cout << "5.  Exit " << endl; 

    int choices = choice;
    while(choice <= 0 || choice >= 5){
        cout << "What you like to do?" << endl; 
        cout << "1.  Display entire organization " << endl; 
        cout << "2.  Display friends list " << endl; 
        cout << "3.  Search for a friend " << endl; 
        cout << "4.  Remove friend " << endl; 
        cout << "5.  Exit " << endl;
        cout << "Please choose a choice: " << endl;
        cin >> choices;
    }
    while(choice >= 0 || choice <= 5){
        if(choices == 1)
            m_organization.DisplayRoster();
        else if(choices == 2)
            m_me.DisplayFriends();
        else if(choices == 3)
            m_organization.GetPerson();
        else if(choices == 4){
            cout << "What you like to do?" << endl; 
            cout << "1.  Display entire organization " << endl; 
            cout << "2.  Display friends list " << endl; 
            cout << "3.  Search for a friend " << endl; 
            cout << "4.  Remove friend " << endl; 
            cout << "5.  Exit " << endl; 
            m_me.RemoveFriend();
            }
    } 
    if(choices == 5)
        cout << "Thanks for using UMBC Friend Finder" << endl;*/

}
   



// Name: Start
// Desc - Main function running FriendFinder
//        Calls GetDetails
//        Populates data for organization
//        Continually calls DisplayMenu until someone enters 4 (exit)
// Preconditions - m_me and m_organization are created but not populated
// Postconditions - Runs until user enters 4. Thanks user for usage. Ends application
void FriendFinder::Start(){
    string firstName, secondName;
    int choice, age, id;
    
    cout << "What is your first name: " << endl;
    cin >> firstName;

    cout << "What is your last name: " << endl;
    cin >> secondName;

    cout << "What is your age: " << endl;
    cin >> age;

    cout << "What is your id " << endl;
    cin >> id;
    Organization newOrganization;
    Person newPerson;

    newPerson.SetDetails(firstName,secondName,age,id);
    newOrganization.SetName();
    newOrganization.LoadRoster();

    DisplayMenu(choice); 
}




