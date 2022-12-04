#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <sstream>
#include <iterator>
#include <algorithm>
#include <numeric>

class solution
{
public:
    solution(){}
    ~solution(){delete data;}
    void part1(std::vector<std::string> &lines){
        data = new std::vector<int>(100) ;
        int total = 0;
        for (auto& line : lines){
            if(line.size() > 0)
            {
                total += std::stoi(line);
            }
            else{
                data->push_back(total);
                total = 0;
            }
        }
        data->push_back(total);
        std::sort(data->begin(), data->end());
        std::cout << data->at(data->size() - 1) << std::endl;
    }
    void part2(std::vector<std::string>& inputs){
        int result = std::accumulate(data->end() - 3, data->end(), 0);
        std::cout << result << std::endl;
    }

private:
    std::vector<int>* data;
};

int main(){
    std::string line;
    std::vector<std::string> inputs;

    while(std::getline(std::cin, line))
    {
        inputs.push_back(line);
    }

    solution day01;
    day01.part1(inputs);
    day01.part2(inputs);
}