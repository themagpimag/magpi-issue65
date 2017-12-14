#include <iostream> // we need this to output to console this file contains cout
#include "SimpleObj.h"

using namespace std;
SimpleObj::SimpleObj()
{
	m_Counter = 0; // make sure the counter starts at 0
}

SimpleObj::~SimpleObj() {} // no code yet in the destructor

void SimpleObj::Update()
{// output our name and keep track of our internal counter
	cout << "Hello my name is " + m_MyName + " and I've looped this many times " << m_Counter << endl;
//	cout << this->m_Counter << endl;
	m_Counter = m_Counter + 1;
}

void SimpleObj::Draw() {} // no code yet in the draw
