#include <iostream>
#include <string>
#include <fstream>
#include <stdio.h>
#include <unistd.h>
#include <crypt.h>

int main()
{
    // open file mots.txt
    std::ifstream file("mots_de_passe.txt");
    if (!file.is_open())
    {
        std::cerr << "Error opening file\n";
        return 1;
    }
    std::string line;
    while (std::getline(file, line))
    {
        printf("%s\n", crypt(line.c_str(), "$3$$796ba5a53df1352e06cc7b0f3ad2a41d"));
    }
}