// add util functions within headers
// utility functions here
#pragma once
#include <iostream>
#include <vector>
#include <string>

using namespace std;

// function to print a vector of strings
void printMessage(const vector<string>& msg)
{
    for (const string& word : msg)
    {
        cout << word << " ";
    }
    cout << endl;
}

// add two nums
int add(int a, int b)
{
    return a + b;
}



