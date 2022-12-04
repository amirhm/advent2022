#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<tuple>


class solution
{
public:

    int part1(std::vector<std::string>& data){
        int x0, x1, y0, y1;
        int results1 =0;
        for(auto& l : data)
        {
            sscanf(l.c_str(), "%d-%d,%d-%d", &x0, &x1, &y0, &y1);
            if(((x0 >= y0) & (x1 <= y1)) | ((y0 >= x0) & (y1 <=x1))){
                results1 += 1;
            }
        }
        return results1;
    }
    int part2(std::vector<std::string>& data){
        results2 =0;
        int x0, x1, y0, y1;
        for(auto& l : data)
        {
            sscanf(l.c_str(), "%d-%d,%d-%d", &x0, &x1, &y0, &y1);
            if(((x0 >= y0) & (x1 <= y1)) | ((y0 >= x0) & (y1 <=x1))){
                results2+= 1;
            }else if(((y0 <= x0) & (x0 <= y1)) | ((y0 <= x1) & (x1 <= y1 )))
            {
                results2 +=1;
            } 
        }
        return results2;
    }

private:
    int results1;
    int results2;
};


int main (){
    std::string line;
    std::vector<std::string> data;
    while(std::getline(std::cin, line)){
        data.push_back(line);
    }
    solution day4;
    std::cout << day4.part1(data) << std::endl;
    std::cout << day4.part2(data) << std::endl;

}