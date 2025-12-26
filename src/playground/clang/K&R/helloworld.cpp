#include <iostream>
#include <vector>
#include <string>

#include "utils.h"

using namespace std;

int main()
{
    vector<string> msg{"Hello", "C++", "World", "from", "VS Code", "and the C++ extension!"};

    printMessage(msg);

    cout << endl;
    const float PI = 3.14;
    cout << "Value of PI: " << PI << endl;
    printf("Press Enter to continue...");
    cin.get();
    
    cout << "Sum of 3 and 4: " << add(3, 4) << endl;
    return 0;
}
