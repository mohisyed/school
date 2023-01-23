#include "Track.h"
// Name: Track
  // Precondition: None
  // Postcondition: Creates a new empty track
Track::Track(){
    m_name = "Unknown";
    m_desc = "Unknown";
    m_fileName = "Unknown";
    vector<Piece*> m_track;
    m_totalLength = 0;
}

Track::~Track(){
    for(unsigned int i = 0; i < m_track.size();i++){
        delete m_track.at(i);
        m_track.at(i) = NULL;
    }
}

void Track::LoadTrack(string fileName){
    Piece* newPiece;
    fstream inputStream;
    string desc,length,numBox,pieceMaxSpeed; 

    inputStream.open(fileName);

    if(inputStream.is_open()){
        getline(inputStream,m_name, '\n');
        getline(inputStream,m_desc);
        while(!inputStream.eof()){
            getline(inputStream, length, '|');
            int convertLength = stoi(length);
            m_totalLength += convertLength;

            getline(inputStream, desc, '|');
            getline(inputStream, numBox, '|');
            int convertNumBox = stoi(numBox);
            //cout << "Num Box " << convertNumBox << endl;

            getline(inputStream, pieceMaxSpeed, '|');
            int convertMaxPiece = stoi(pieceMaxSpeed);
           // cout << "maxpiece " << pieceMaxSpeed << endl;

            cout << length << '|' << numBox << '|' << desc << '|' << pieceMaxSpeed << '|' << endl;
            newPiece = new Piece(convertLength,desc,convertNumBox,convertMaxPiece);
            m_track.push_back(newPiece);

            
        }
        
    }
    cout << "Finshed Loading " << fileName << endl;
    cout << fileName << "is " << m_totalLength << " Meters" << endl;
    inputStream.close();
}

 // Name: GetPiece (int)
  // Description: At a specific distance, the corresponding index of the piece is returned
  // For example, if 300 is passed, iterates through vector adding distance until 300 is reached
  // If next piece of the track exceeds the end, returns the end
  // Precondition: Must have valid track and provided distance
  // Postcondition: Travels through track to described distance
int Track::GetPiece(int distance){
    int distanceCounter = 0; 
    int vectorIterator = 0;
    while(distanceCounter < distance){
        m_track.at(vectorIterator)->m_length += distanceCounter;
        vectorIterator ++;
    }
    if(vectorIterator > int(m_track.size()))
        vectorIterator --;

    return vectorIterator;
}

 // Name: DisplayPiece
  // Description: At a specific index, returns the m_desc from a particular piece of track
  // Precondition: Track loaded and a valid index passed
  // Postcondition: Returns id of track in that direction if the exit exists
void Track::DisplayPiece(int index){
    cout << m_track.at(index)->m_desc << endl;
}

  // Name: GetMaxSpeed
  // Description: At a specific index, returns the m_maxSpeed from a particular piece of track
  // Precondition: Track loaded and a valid index passed
  // Postcondition: Returns double which is max speed before racer crashes
double Track::GetMaxSpeed(int index){
    return m_track.at(index)->m_maxSpeed;
}
  // Name: GetTotalLength()
  // Description: Returns m_totalLength
  // Precondition: Track loaded
  // Postcondition: Returns int for total length
int Track::GetTotalLength(){
    return m_totalLength;
}

  // Name: GetDesc()
  // Description: Returns m_desc
  // Precondition: Track loaded
  // Postcondition: Returns desc
string Track::GetDesc(){
    return m_desc;
}