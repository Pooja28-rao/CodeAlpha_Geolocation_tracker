import os
import requests
from selenium import webdriver # type: ignore
import folium # type: ignore
import datetime
import webbrowser

# Ensure the directory exists
def ensure_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Directory created: {directory_path}")

# Get geolocation coordinates
def locationCoordinates():
    try:
        response = requests.get('https://ipinfo.io', timeout=10)
        if response.status_code == 200:
            data = response.json()
            loc = data['loc'].split(',')
            return float(loc[0]), float(loc[1]), data.get('city', 'Unknown'), data.get('region', 'Unknown')
    except Exception as e:
        print(f"Error fetching geolocation: {e}")
        return None

# Generate the map
def gps_locator():
    obj = folium.Map(location=[0, 0], zoom_start=2)
    try:
        coords = locationCoordinates()
        if coords:
            lat, long, city, state = coords
            print(f"Location: {city}, {state} ({lat}, {long})")
            folium.Marker([lat, long], popup="Current Location").add_to(obj)
            directory = "C:/screengfg/"
            ensure_directory(directory)
            fileName = f"{directory}Location_{datetime.date.today()}.html"
            obj.save(fileName)
            return fileName
    except Exception as e:
        print(f"Error generating map: {e}")
    return None

if __name__ == "__main__":
    print("Fetching geolocation...")
    page = gps_locator()
    if page:
        print(f"Map generated at: {page}")
        try:
            # Try opening with Selenium
            dr = webdriver.Chrome()
            dr.get(page)
            input("The map is open. Press Enter to close the browser...")
            dr.quit()
        except Exception as e:
            print(f"Selenium error: {e}. Opening with default browser.")
            webbrowser.open(page)
    else:
        print("Failed to generate the map.")





