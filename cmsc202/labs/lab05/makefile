CXX = g++
CXXFLAGS = -Wall
lab5: Laptop.o lab5.cpp
	$(CXX) $(CXXFLAGS) Laptop.o lab5.cpp -o lab5
labtop.o: Laptop.o Laptop.h
	$(CXX) $(CXXFLAGS) -c Laptop.cpp

run:
		./lab5