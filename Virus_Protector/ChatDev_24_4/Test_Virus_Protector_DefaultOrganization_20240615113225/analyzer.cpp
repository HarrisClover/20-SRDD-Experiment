/*
This file contains the implementation of the Analyzer class.
*/
#include "Analyzer.h"
#include <fstream>
void Analyzer::analyze(std::vector<std::string> files) {
    for (const auto & file : files) {
        // Open the file and read its contents
        std::ifstream inFile(file);
        std::string line;
        while (std::getline(inFile, line)) {
            // Check each line for known virus signatures
            for (const auto & signature : virusSignatures) {
                if (line.find(signature) != std::string::npos) {
                    // If a virus signature is found, add the file to the detectedThreats vector
                    detectedThreats.push_back(file);
                    break;
                }
            }
        }
        inFile.close();
    }
}
std::vector<std::string> Analyzer::getDetectedThreats() {
    return detectedThreats;
}