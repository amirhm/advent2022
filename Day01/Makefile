
OBJ = Day01.o\

sample1 = "1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000\n"

build: $(OBJ)
	g++ $(OBJ) -o Day01.out


%.o: %.cpp
	g++ -c $< -o $@

clean:
	@rm -rf *.out
	@rm -rf *.o

test: 
	@printf $(sample1) | ./Day01.out
run:
	@./Day01.out < data.txt