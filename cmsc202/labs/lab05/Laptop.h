/**********
* File: Laptop.h
*
* Intended for Lab 5: Classes
*
**********/

#ifndef LAPTOP_H //Protects against multiple inclusion
#define LAPTOP_H //Protects against multiple inclusion

#include <iostream>
#include <string>

using namespace std;

//Declare the Laptop class here
//Include a generic constructor, all getters and setters for four variables, and WorthIt function

class Laptop{
    private:
        string m_brand;
        double m_price;
        int m_memory;
        bool m_isBacklist;
    public:
        void change_m_brand(string);   //setters 
        void change_m_price(double);
        void change_m_memory(int);
        void change_m_isBacklist(bool);

        string display_m_brand();      //getters
        double display_m_price();
        int display_m_memory();
        bool display_m_isBacklist();

        bool WorthIt(int,double,bool);



}laptop;


#endif
