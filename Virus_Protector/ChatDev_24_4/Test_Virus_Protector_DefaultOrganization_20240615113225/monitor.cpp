/*
This file contains the implementation of the Monitor class.
*/
#include "Monitor.h"
#include "Scanner.h"
#include "Analyzer.h"
#include "Cleaner.h"
#include <thread>
void Monitor::start() {
    // Start a process that continuously monitors the system for any suspicious activities
    // Trigger the scan, analyze, and clean process if any suspicious activity is detected
    while(true) {
        Scanner scanner;
        Analyzer analyzer;
        Cleaner cleaner;
        scanner.scan();
        analyzer.analyze(scanner.getScannedFiles());
        cleaner.clean(analyzer.getDetectedThreats());
        std::this_thread::sleep_for(std::chrono::minutes(10));
    }
}