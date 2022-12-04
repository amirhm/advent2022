#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<set>
#include<map>
#include<numeric>

class solution{
public:
	solution(){
		map = new std::map<char, int>;
		for(int i =0; i < 26; i++)
		{
			map->insert({(i + 65) , i + 27});
			map->insert({(i + 97) , i + 1});
		}
	}
	~solution(){
		delete map;
	}
	int part1(std::vector<std::string>& data){
		results1 = 0;
		for(auto& l: data){
			int n = l.size() / 2;
			std::set<char> s1_s(l.begin(), l.begin() + n);
			std::set<char> s2_s(l.begin() + n, l.end());
			std::set<char> inter;
			std::set_intersection(
				s1_s.begin(), s1_s.end(), s2_s.begin() , s2_s.end(),
				std::inserter( inter, inter.end() )
			);
			int total = 0;

			for(auto&c : inter){
				total += map->at(c); 
			}
			results1 += total;
		}
		return results1;
	}
	int part2(std::vector<std::string>& data){
		for(int i = 0; i < data.size(); i+= 3)
		{
			std::set<char> s1(data[i].begin(), data[i].end());
			std::set<char> s2(data[i + 1].begin(), data[i + 1].end());
			std::set<char> s3(data[i + 2].begin(), data[i + 2].end());
			std::set<char> inter1;
			std::set<char> inter2;
			std::set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(), std::inserter(inter1, inter1.end()));
			std::set_intersection(s3.begin(), s3.end(), inter1.begin(), inter1.end(), std::inserter(inter2, inter2.end()));
			int total =0;
			for(auto&c : inter2){
				total += map->at(c); 
			}
			results2 += total;
		}
		return results2;
	}
private:
	int results1;
	int results2;
	std::map<char, int>* map;
};


int main(){
	std::string line;
	std::vector<std::string> data;
	while(std::getline(std::cin, line)){
		data.push_back(line);
	}
	solution day3;
	std::cout << day3.part1(data) << std::endl;

	std::cout << day3.part2(data) << std::endl;
	return 0;
}