CXX = g++
CXXFLAGS = -Wall

lab6: lab6.cpp Groceries.o
	$(CXX) $(CXXFLAGS) lab6.cpp Groceries.o -o lab6
	
Groceries.: Groceries.o Groceries.h
	$(CXX) $(CXXFLAGS) -c Groceries.cpp

run:
		./lab5
clean:
		rm *~