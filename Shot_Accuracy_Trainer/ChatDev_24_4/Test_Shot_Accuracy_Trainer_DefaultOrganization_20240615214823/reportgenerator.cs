'''
This file defines the ReportGenerator class.
'''
using System;
public class ReportGenerator
{
    public TrainingSession Session { get; set; }
    public ReportGenerator(TrainingSession session)
    {
        Session = session;
    }
    public void GenerateReport()
    {
        Console.WriteLine($"Generating report for {Session.Athlete.Name} who plays {Session.Athlete.Sport.Name}.");
        Console.WriteLine($"Total shots: {Session.Shots.Count}");
        Console.WriteLine($"Successful shots: {Session.Shots.FindAll(s => s.IsHit).Count}");
        Console.WriteLine($"Shot accuracy: {Session.CalculateAccuracy() * 100}%");
    }
}