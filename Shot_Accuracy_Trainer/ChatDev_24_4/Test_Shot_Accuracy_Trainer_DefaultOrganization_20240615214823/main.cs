'''
This is the main file that handles user interaction.
'''
using System;
public class Main
{
    static void Main(string[] args)
    {
        // Create a new athlete
        Athlete athlete = new Athlete("John Doe", new Sport("Basketball"));
        // Start a new training session
        TrainingSession session = new TrainingSession(athlete);
        // Take multiple shots
        session.TakeShot(10, 2, true);
        session.TakeShot(15, 3, false);
        session.TakeShot(20, 4, true);
        // Provide feedback
        foreach (Shot shot in session.Shots)
        {
            session.ProvideFeedback(shot);
        }
        // End the session
        session.EndSession();
        // Generate a report
        ReportGenerator reportGenerator = new ReportGenerator(session);
        reportGenerator.GenerateReport();
    }
}