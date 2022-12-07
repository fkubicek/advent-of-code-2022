#include <iostream>
#include <cstring>
#include <string>

const int windowLen = 14;
short charCountsInWindow[128];

int main() {
    memset(charCountsInWindow, 0, sizeof(charCountsInWindow));

    std::string input;
    std::getline(std::cin, input);

    int differentChars = 0;

    for (size_t i = 0; i < input.size(); i++) {
        char c = input[i];

        if (i >= windowLen) {
            char lostChar = input[i-windowLen];
            charCountsInWindow[lostChar]--;

            if (charCountsInWindow[lostChar] == 1) {
                    differentChars++;
            } else if (charCountsInWindow[lostChar] == 0) {
                    differentChars--;
            }
        }

        charCountsInWindow[c]++;

        if (charCountsInWindow[c] == 1) {
            differentChars++;
        } else if (charCountsInWindow[c] == 2) {
            differentChars--;
        }

        // std::cout << i << ": " << c << ' ' << differentChars << std::endl;

        if (differentChars == windowLen) {
            std::cout << "Result: " << i + 1 << std::endl;
            return 0;
        }
    }

    return 0;
}
