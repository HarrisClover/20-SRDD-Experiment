'''
This is the main entry point of our application. It initializes the application and starts the main loop.
'''
using UnityEngine;
using System.Collections;
public class Main : MonoBehaviour 
{
    // Use this for initialization
    void Start () 
    {
        // Initialize the Arena Builder
        ArenaBuilder arenaBuilder = new ArenaBuilder();
        // Initialize User Preferences
        UserPreferences userPreferences = new UserPreferences();
        // Build the arena with user preferences
        arenaBuilder.BuildArena(userPreferences);
    }
    // Update is called once per frame
    void Update () 
    {
        // Update the Arena Builder
        ArenaBuilder.Update();
    }
}