/*
This is the main file that will initialize and coordinate the other components of the Virus Protector.
*/
#include "Scanner.h"
#include "Analyzer.h"
#include "Cleaner.h"
#include "Monitor.h"
int main() {
    Scanner scanner;
    Analyzer analyzer;
    Cleaner cleaner;
    Monitor monitor;
    // Start the real-time monitor
    monitor.start();
    // Perform an initial scan
    scanner.scan();
    // Analyze the scanned files
    analyzer.analyze(scanner.getScannedFiles());
    // Clean any detected threats
    cleaner.clean(analyzer.getDetectedThreats());
    return 0;
}