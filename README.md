# Site_Checker
This Python script monitors a specified website at set intervals (default is every 6 hours) and displays a popup notification if the website content has changed.

## Features
Automated monitoring: The script runs in the background and checks for updates every 6 hours.
Popup notifications: Alerts you when a change is detected.
Simple configuration: Just set the website URL and monitoring interval.

## Notes
Ensure you have PyQt5 installed for the popup notifications to work.
The script compares the website’s content over time. If the structure of the site changes frequently, consider refining the detection method.
Requires an active internet connection to fetch updates.
License
