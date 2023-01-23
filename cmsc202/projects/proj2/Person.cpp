#include "Person.h"
 
Person::Person(){
    string m_fName; 
    string m_lName; 
    int m_age; 
    int m_ID; 
    Person* m_friends[MAX_FRIENDS]; 
    int m_friendCount;
}

void Person::AddFriend(Person*){
    int numbFriends = this->m_friendCount;
    bool personExists = false;
    bool maxNum = false;
    string personName = this->m_fName + this->m_lName;
    if (numbFriends > MAX_FRIENDS){
        cout << "Can't add anymore friends. Already at max capacity" << endl;
        maxNum = true;
    }

    if (maxNum != true){
        for (int i = 0; i < numbFriends; i++){ // Iterate through person's friend list
            if (m_friends[i]->m_fName == this->m_fName && m_friends[i]->m_lName == this->m_lName){
                personExists = true;
                cout << "Person already exists in list" << endl;
            }
        }
    }

    if (maxNum == false && personExists == false){
        m_friends[m_friendCount+1] = this;
    }
 }
// Name: RemoveFriend
// Desc - Removes a person pointer from this person's m_friend array
// Preconditions - Person pointer exists in m_friend
// Postconditions - Person is removed from m_friend and all pointers are moved towards front



void Person::RemoveFriend(){
    this->DisplayFriends();
    int removedFriend = 0;
    cout << "Who would you like to remove?" << endl;
    cin >> removedFriend;

    this->m_friends[removedFriend-1] = nullptr; // "deletes" the Person from the array
    Person temp;
    // TODO: move person's over
    for (int i = m_friendCount; i < this->m_friendCount; i--){
        if (m_friends[i] == nullptr){
            *m_friends[i] = *m_friends[i + 1];
        }
        temp = *m_friends[i];
        

    }
}
// work on remove functions


Person::Person(string firstName, string lastName, int age, int id){
    m_fName = firstName;
    m_lName = lastName;
    m_age = age;
    m_ID = id;
    //m_friends[MAX_FRIENDS];  might need to add this later right now getting a warning for having zero effect
    m_friendCount = 0;
}

bool Person::CheckID(int id){
    if(m_friendCount > 0 && m_friendCount < MAX_FRIENDS){
        for(int i = 0; i <= m_friendCount; i++){
            if(m_friends[i]->m_ID == id)
                return true;
        }
        return false;
    }
    return false;
}

void Person::DisplayFriends(){
    for(int i = 0; i <= m_friendCount; i++){
        cout << m_friends[i]-> m_fName << '\t' <<  m_friends[i]-> m_lName << endl;
    }
}

void Person::DisplayDetails(){
    for(int i = 0; i <= m_friendCount; i++){
        cout << m_friends[i]-> m_fName << '\t' <<  m_friends[i]-> m_lName
        << endl << m_friends[i] -> m_age << endl << m_friends[i] -> m_ID
        << endl << m_friends[i] -> m_friendCount << endl;
    }
}

void Person::SetDetails(string firstName, string lastName, int age, int id){
    m_fName = firstName;
    m_lName = lastName;
    m_age = age;
    m_ID = id;

}

