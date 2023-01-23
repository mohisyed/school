/*****************************************************************************
 ** File: lab11b.cpp
 ** Lab: CMSC 202 Lab 11b - Templates
 ** Author:  CMSC 202
 **
*****************************************************************************/
#include <iostream>
#include <string>
using namespace std;

/*
Implement the UserArray class that creates a dynamically allocated array
of the given size and performs the functions described in the lab document.
*/
/******Implement UserArray Class here******************/
template <class T>
class UserArray{
  public:
    UserArray(int size);
    ~UserArray();
    void SetArray(T* changedArray);
    void AddToEach(T data);
    T GetItem(int index);
    void DisplayAll();

  private:
    T* m_array;
    int m_size;
};


template <class T>
UserArray<T>::UserArray(int size){
  m_size = size;
  m_array = new T[m_size];
}

template <class T>
UserArray<T>::~UserArray(){
  delete[] m_array;
  m_size = 0;
}

template <class T>
void UserArray<T>::SetArray(T* newArray){
  for(int i = 0; i <m_size; i++){
    m_array[i] = newArray[i];
  }
}
template <class T>
void UserArray<T>::AddToEach(T data){
  for(int i = 0; i < m_size; i++){
    m_array[i] = m_array[i] + data;
  }
}

template <class T>
T UserArray<T>::GetItem(int index){
  return m_array[index];
}
template <class T>
void UserArray<T>::DisplayAll(){
  for(int i = 0; i < m_size; i++){
   cout << m_array[i]<< ", ";
  }
  cout << endl;
}


//int main provided
int main() {
  //Integer array for lab grades
  UserArray<int> labGrades(10);
  int myGrades[10] = { 6,10,10,7,8,10,10,8,9,10 };
  labGrades.SetArray(myGrades);
  cout << "Lab Grades Array:" << endl;
  labGrades.DisplayAll();
  cout << endl;
  
  //Add one to each lab grade
  cout << "Lab Grades Array After Adding 1 to Each:" << endl;
  labGrades.AddToEach(1);
  labGrades.DisplayAll();
  cout << endl;
  
  //String array for courses
  UserArray<string> fallCourses(4);
  string courseList[4] = { "CMSC202", "CMSC203", "PHIL100", "MATH152" };
  fallCourses.SetArray(courseList);
  cout << "Fall Course List:" << endl;
  fallCourses.DisplayAll();
  cout << endl;
  
  //Add -FALL2021 to each course
  cout << "Fall Courses After Adding -FALL2021 to Each:" << endl;
  fallCourses.AddToEach("-FALL2021");
  fallCourses.DisplayAll();
  return 0;
}
