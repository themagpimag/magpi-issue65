/*
Simple example of a main function creating a game class and updating it
*/

#include "Game.h"


int main(int argc, char *argv[])
{
	Game TheGame; // create an instance of game.

	for (int i = 0; i < 10; i++)
	{
		TheGame.Update();
	}

}
