#include <iostream>
#include <fstream>

std::string decypher(std::string input, int key) {
    std::string output = "";
    for (int i = 0; i < input.size(); i++) {
        input[i] = toupper(input[i]);
        if (input[i] == ' ')
            output += ' ';
        else if (input[i] - key < 65)
            output += input[i] + 26 - key;
        else
            output += input[i] - key;
    }
    return output;
}

int main() {
std::string line;

    for (int i = 0; i < 23; i++) {
        std::ifstream file("flag.txt");
        std::cout << decypher("famous man tibu ejsfdumz cfmjfwfe jo ???", i) << std::endl;
        file.close();
    }    
    return 0;
}

