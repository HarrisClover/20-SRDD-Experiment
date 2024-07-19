'''
This class holds the user's preferences for the virtual sports arena. It can be used to customize the arena.
'''
using UnityEngine;
using UnityEngine.UI;
public class UserPreferences : MonoBehaviour 
{
    public Dropdown arenaTypeDropdown;
    public Dropdown arenaColorDropdown;
    public Slider arenaSizeSlider;
    public string arenaType;
    public string arenaColor;
    public int arenaSize;
    void Start () 
    {
        // Initialize user preferences with the first option from the dropdowns and the current value of the slider
        arenaType = arenaTypeDropdown.options[arenaTypeDropdown.value].text;
        arenaColor = arenaColorDropdown.options[arenaColorDropdown.value].text;
        arenaSize = (int)arenaSizeSlider.value;
    }
    public void UpdatePreferences()
    {
        // Update user preferences when a UI element changes
        arenaType = arenaTypeDropdown.options[arenaTypeDropdown.value].text;
        arenaColor = arenaColorDropdown.options[arenaColorDropdown.value].text;
        arenaSize = (int)arenaSizeSlider.value;
    }
}