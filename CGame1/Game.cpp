

#include "Game.h"
#include "SimpleObj.h"

Game::Game() {}; // just need to exist at the moment
Game::~Game() {};

void Game::Update()
{

	SimpleObj Bobby1; // create a Simple Object withe the class name Bobby1
	SimpleObj Bobby2;
	
	Bobby1.m_MyName = "Bobby1"; // Give Bobby 1 his name
	Bobby2.m_MyName = "Bobby2"; // Give Bobby 2 his name
// now we will do a loop;
	for (int i = 0; i < 200; i++)
	{
		Bobby1.Update(); // do Bobby1's update
		Bobby2.Update(); // do Bobby2's update
	}
	return; 
};