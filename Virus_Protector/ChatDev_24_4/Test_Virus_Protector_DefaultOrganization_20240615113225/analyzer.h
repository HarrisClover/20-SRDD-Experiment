/*
This class will analyze files and detect potential threats.
*/
#include <vector>
#include <string>
class Analyzer {
private:
    std::vector<std::string> detectedThreats;
    std::vector<std::string> virusSignatures;
public:
    void analyze(std::vector<std::string> files);
    std::vector<std::string> getDetectedThreats();
};