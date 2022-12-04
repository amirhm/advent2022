
OBJ = Day02.o\

sample1 = "A Y\nB X\nC Z\n"
CCFLAG = --std=c++17

build: $(OBJ)
	g++ $(OBJ) -o Day02.out


%.o: %.cpp
	g++ $(CCFLAG) -c $< -o $@


clean:
	@rm -rf *.out
	@rm -rf *.o

test: 
	@printf $(sample1) | ./Day02.out

run:
	@./Day02.out < data.txt