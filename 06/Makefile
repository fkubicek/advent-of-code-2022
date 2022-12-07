CFLAGS = -O1 -Wall

all: clean solution.o solution

solution:
	cat input.txt | ./solution.o

solution.o: clean
	g++ $(CFLAGS) solution.cpp -o solution.o

clean:
	rm -f *.o
