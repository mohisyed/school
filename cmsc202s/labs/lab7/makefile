CXX = g++
CXXFLAGS = -Wall

lab7: DuckLine.o lab7.cpp
	$(CXX) $(CXXFLAGS) DuckLine.o lab7.cpp -o lab7

DuckLine.o: DuckLine.cpp DuckLine.h
	$(CXX) $(CXXFLAGS) -c DuckLine.cpp

run:
	./lab7

clean:
	rm *~
