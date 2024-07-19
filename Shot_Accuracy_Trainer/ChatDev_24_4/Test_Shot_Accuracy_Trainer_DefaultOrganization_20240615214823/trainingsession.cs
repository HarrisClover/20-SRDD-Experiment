'''
This file defines the TrainingSession class.
'''
using System;
using System.Collections.Generic;
public class TrainingSession
{
    public Athlete Athlete { get; set; }
    public List<Shot> Shots { get; set; }
    public TrainingSession(Athlete athlete)
    {
        Athlete = athlete;
        Shots = new List<Shot>();
    }
    public void TakeShot(int distance, int targetSize, bool isHit)
    {
        Shot shot = new Shot(distance, targetSize, isHit);
        Shots.Add(shot);
        Console.WriteLine($"{Athlete.Name} takes a shot at a distance of {distance} meters with a target size of {targetSize} cm. Shot was {(isHit ? "successful" : "unsuccessful")}.");
    }
    public void EndSession()
    {
        Console.WriteLine("The training session has ended.");
    }
    public double CalculateAccuracy()
    {
        int successfulShots = Shots.FindAll(s => s.IsHit).Count;
        return (double)successfulShots / Shots.Count;
    }
    public void ProvideFeedback(Shot shot)
    {
        if (!shot.IsHit)
        {
            Console.WriteLine("Try adjusting your aim or power.");
        }
    }
}