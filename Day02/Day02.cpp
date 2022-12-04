#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <sstream>
#include <iterator>

class solution
{
public:
    solution(std::vector<std::string> &lines)
    {
        data = &lines; 
        // A Rock B Paper C Scissor
        bord1 = new std::unordered_map<std::string, int>{
        {"A X", 3}, {"A Y", 6}, {"A Z", 0},
        {"B X", 0}, {"B Y", 3}, {"B Z", 6},
        {"C X", 6}, {"C Y", 0}, {"C Z", 3}};
        
        bord2 = new std::unordered_map<std::string, int>{
        {"A X", 0 + 3}, {"A Y", 3 + 1}, {"A Z", 6 + 2},
        {"B X", 0 + 1}, {"B Y", 3 + 2}, {"B Z", 6 + 3},
        {"C X", 0 + 2}, {"C Y", 3 + 3}, {"C Z", 6 + 1}};
    };
    ~solution(){
        delete bord1;
        delete bord2;
    }
    void part1(){
        int total = 0;
        char x, y;
        std::string l1, l2;
        std::unordered_map<char, int> score{{'X', 1}, {'Y', 2}, {'Z', 3}};
        for (auto& line : *data){
            sscanf(line.c_str(), "%c %c", &x, &y);
            total += score[y]; 
            total += bord1->at(line);
        }
        std::cout << total << std::endl;
    }
    void part2(std::vector<std::string>& inputs){
        int total = 0;
        for (auto& line : inputs){
            total += bord2->at(line);
        }
        std::cout << total << std::endl;
    }

private:
    std::vector<std::string>* data;
    std::unordered_map<std::string, int>* bord1;
    std::unordered_map<std::string, int>* bord2;

};

int main(){
    std::string line;
    int total = 0;
    std::vector<std::string> inputs;

    char x = '1' , y = '1';
    while(std::getline(std::cin, line))
    {
        inputs.push_back(line);
    }

    solution day02(inputs);
    day02.part1();
    day02.part2(inputs);



}