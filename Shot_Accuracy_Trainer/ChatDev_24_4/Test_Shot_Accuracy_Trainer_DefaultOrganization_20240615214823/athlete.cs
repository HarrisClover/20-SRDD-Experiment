'''
This file defines the Athlete class.
'''
using System;
public class Athlete
{
    public string Name { get; set; }
    public Sport Sport { get; set; }
    public Athlete(string name, Sport sport)
    {
        Name = name;
        Sport = sport;
    }
}