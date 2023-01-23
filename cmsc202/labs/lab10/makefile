CXX = g++
CXXFLAGS = -Wall

lab10: Landmass.o Island.o Continent.o lab10.cpp
	$(CXX) $(CXXFLAGS) Landmass.o Island.o Continent.o lab10.cpp -o lab10

Landmass.o: Landmass.h Landmass.cpp
	$(CXX) $(CXXFLAGS) -c Landmass.cpp -o Landmass.o

Island.o: Island.h Island.cpp Landmass.o
	$(CXX) $(CXXFLAGS) -c Island.cpp -o Island.o

Contient.o: Continent.h Continent.cpp Landmass.o
	$(CXX) $(CXXFLAGS) -c Continent.cpp -o Continent.o

run:
	./lab9

clean:
	rm *~
