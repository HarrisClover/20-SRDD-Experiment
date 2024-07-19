/*
This class is responsible for scanning files and directories.
*/
#include <vector>
#include <string>
class Scanner {
private:
    std::vector<std::string> scannedFiles;
public:
    void scan();
    std::vector<std::string> getScannedFiles();
};