#include <iostream>
#include <string>
#include <fstream>
#include <ctime>
using namespace std;


int main(){
    fstream inputStream;
    string track_name, track_description;

    string desc,length,numBox,pieceMaxSpeed; //Description of the piece of the track
    srand(time(NULL));
    double x = (rand()% 4+1)*.25;
    cout << x << endl;


    inputStream.open("proj4_trac1.txt");
    if(inputStream.is_open()){
        getline(inputStream,track_name, '\n');
        cout << track_name << endl;
        getline(inputStream,track_description);
        cout << track_description << endl;
        while(!inputStream.eof()){
            getline(inputStream, length, '|');
            getline(inputStream, numBox, '|');
            getline(inputStream, desc, '|');
            getline(inputStream, pieceMaxSpeed, '|');
            //cout << length << '|' << numBox << '|' << desc << '|' << pieceMaxSpeed << '|' << endl;
            //cout << length << endl;

        }
    }   
    inputStream.close();
}
