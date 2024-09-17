# x-download-video
Python to download X videos

### Features
Single Script: Download videos from X with ease.
Automatic Naming: Uses video titles for filenames, cleaned of special characters for compatibility.
No Clutter: Silent download process with only initial input and final confirmation.

### Requirements
Python
requests (pip install requests)
beautifulsoup4 (pip install beautifulsoup4)

### How It Works
Setup: Ensure all required libraries are installed. 
Run the Script: Execute the Python script from your terminal or command prompt.
Enter URL: Copy and paste the URL of the X video you want to download when prompted.

The script will:
- Fetch the video information from the provided X URL.
- Download the video silently, showing no progress in the terminal.
- Save the video with a filename based on the video's title.
- Once the download is complete, you'll see a confirmation message indicating the file has been saved.

### Usage Tips
Error Handling: If there's an issue with fetching or downloading the video, an error message will be displayed explaining what went wrong.
File Location: Videos are saved in the same directory as the script. Make sure you have write permissions for that location.
