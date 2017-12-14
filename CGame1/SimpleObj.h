#pragma once
#include <string> // we're going to use strings so need the header
class SimpleObj
{
public:
	SimpleObj(); //standard constructor
	~SimpleObj(); //standard destructor
//list the functions we want to have (called methods in C++)	
	void Update();
	void Draw();
// list the variables we want our instances to have (called members in C++)	
	int m_Counter;
	std::string m_MyName ;
};