/*
This file contains the implementation of the Scanner class.
*/
#include "Scanner.h"
#include <filesystem>
void Scanner::scan() {
    for (const auto & entry : std::filesystem::recursive_directory_iterator("./")) {
        if(entry.path().extension() == ".exe") {
            scannedFiles.push_back(entry.path().string());
        }
    }
}
std::vector<std::string> Scanner::getScannedFiles() {
    return scannedFiles;
}