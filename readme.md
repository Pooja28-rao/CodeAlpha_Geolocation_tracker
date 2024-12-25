**Geolocation Tracker**

This Python project fetches the user\'s geolocation based on their IP
address and displays it on an interactive map using Selenium and Folium.

**Features**

-   Retrieves the user\'s latitude, longitude, city, and region using
    the ipinfo.io API.

-   Displays the location on a map using the Folium library.

-   Saves the generated map as an HTML file.

-   Automatically opens the map in a browser (via Selenium).

**Requirements**

Ensure you have the following installed:

-   Python 3.7 or higher

-   Pip (Python package installer)

-   A stable internet connection

-   Google Chrome browser

-   Compatible ChromeDriver (matching the version of Chrome installed on
    your system)

**Installation**

1.  Clone the repository or download the script.

2.  Install the required Python libraries:

3.  pip install selenium folium requests

4.  Download and set up ChromeDriver:

    -   Visit the [[ChromeDriver download
        page]{.underline}](https://chromedriver.chromium.org/downloads).

    -   Download the version matching your installed version of Chrome.

    -   Add the chromedriver executable to your system\'s PATH or
        specify its location in the script.

**Usage**

1.  Ensure your system has internet access.

2.  Run the script:

3.  python path.py

4.  The program will:

    -   Fetch your geolocation details.

    -   Save an interactive map in the C:/screengfg/ directory.

    -   Automatically open the map in your browser.

5.  To exit, close the browser manually or press Enter in the terminal.

**Error Handling**

-   If the C:/screengfg/ directory does not exist, it will be created
    automatically.

-   If Selenium fails to open the browser, the program will fall back to
    using the default web browser.

-   Ensure your ChromeDriver version matches your Chrome browser version
    to avoid errors.

**Example Output**

When executed, the program displays your location on an interactive map.
Below is an example of the console output:

Fetching geolocation\...

Location: Bangalore, Karnataka (12.9716, 77.5946)

Map generated at: C:/screengfg/Location_2024-12-24.html

The map is open. Press Enter to close the browser\...

**Troubleshooting**

**Common Issues**

1.  **Yellow Lines Under Imports in VS Code**:

    -   Ensure the correct Python interpreter is selected in your
        editor.

    -   Install required libraries in the active Python environment.

2.  **TimeoutError or Selenium Not Connecting**:

    -   Verify that your ChromeDriver version matches your Chrome
        browser version.

    -   Check your internet connection.

    -   Ensure no firewall or antivirus software is blocking the
        connection.

3.  **Map Not Opening**:

    -   If Selenium fails, the program falls back to the default web
        browser.

    -   Ensure webbrowser works by testing manually:

    -   import webbrowser

    -   webbrowser.open(\"https://www.google.com\")
