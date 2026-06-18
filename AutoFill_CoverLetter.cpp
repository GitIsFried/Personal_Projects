#include <"../AutoFill_CoverLetter.cpp"
#include <string> 

int main() {
    std::string fullName;

    std::cout << "Enter your full name: ";
    // Reads the entire line including spaces
    std::getline(std::cin, fullName); 

    std::cout << "Hello, " << fullName << "!\n";
    return 0;
}
