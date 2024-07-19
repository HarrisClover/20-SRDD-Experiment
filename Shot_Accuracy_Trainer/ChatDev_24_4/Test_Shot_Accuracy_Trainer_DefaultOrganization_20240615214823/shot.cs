'''
This file defines the Shot class.
'''
using System;
public class Shot
{
    public int Distance { get; set; }
    public int TargetSize { get; set; }
    public bool IsHit { get; set; }
    public Shot(int distance, int targetSize, bool isHit)
    {
        Distance = distance;
        TargetSize = targetSize;
        IsHit = isHit;
    }
}