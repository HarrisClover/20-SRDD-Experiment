/*
This file contains the implementation of the Cleaner class.
*/
#include "Cleaner.h"
#include <filesystem>
void Cleaner::clean(std::vector<std::string> threats) {
    for (const auto & threat : threats) {
        // Remove or quarantine the threat based on the severity of the threat
        std::filesystem::remove(threat);
    }
}