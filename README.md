# Time and Weather
A clean, dark-themed desktop application that shows current local time and weather information for any city — with large emoji icons and a cyberpunk-inspired design.

## Features
- Enter any city name to fetch current weather conditions
- Displays temperature in Celsius (°C)
- Shows large, expressive weather emoji (thunder, rain, snow, sun, clouds, etc.)
- Displays current local time in 24-hour format for the selected city
- Modern dark UI with cyan glow accents and Comic Sans MS labels
- Clear error messages for invalid cities, no internet, timeouts, etc.
- Simple, centered layout that looks good on any screen size
- Proper GUI using Pyqt5

## How the App Works
1. Type a city name (examples: "Islamabad", "London", "New York", "Tokyo")
2. Click the **Get Weather & Time** button
3. View:
   - Current local time (big cyan numbers)
   - Temperature (very large blue numbers)
   - Matching weather emoji (extra large)
   - Short weather description below

If something goes wrong (wrong spelling, no connection, etc.), an error message appears in the temperature area.

## How to Run the Program
1. Make sure **Python** is installed.
2. Install all required modules using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
3. Run the program
    ```bash
    python Main.py
    ```
    
## File Structure
```bash
project/
│── Main.py
│── README.md
│── requirements.txt
│── Icon.png
```

## Technologies Used
- Python
- PyQt5
- requests
- OpenWeatherMap API
- IPGeolocation API  

## Notes
- Enter your own API keys by siging up for free on both websites and put that in the code
- Temperature is in metric units (°C).
- Weather emojis are Unicode characters

## Author
Muhammad Awais Tariq

---
If you like this project, consider giving it a star on GitHub!