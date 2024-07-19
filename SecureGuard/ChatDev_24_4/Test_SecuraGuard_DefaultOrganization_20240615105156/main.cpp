'''
This is the main file for the SecureGuard application. It initializes and manages the other classes.
'''
#include <iostream>
#include "RealTimeMonitor.h"
#include "ThreatNeutralizer.h"
#include "Firewall.h"
#include "PasswordManager.h"
class SecureGuard {
    private:
        RealTimeMonitor monitor;
        ThreatNeutralizer neutralizer;
        Firewall firewall;
        PasswordManager passwordManager;
    public:
        SecureGuard() : monitor(neutralizer), neutralizer(), firewall(), passwordManager() {}
        void start() {
            monitor.startMonitoring();
            firewall.enableFirewall();
        }
};
int main() {
    SecureGuard secureGuard = SecureGuard();
    secureGuard.start();
    return 0;
}