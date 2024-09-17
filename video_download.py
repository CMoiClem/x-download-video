import requests
from bs4 import BeautifulSoup
import re
from os import path
import sys

def get_video():
    url = input("Enter X video URL: ").strip()
    if not url:
        print("No URL entered. Exiting.")
        sys.exit(1)
    
    try:
        resp = requests.get(f"https://twitsave.com/info?url={url}")
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, 'html.parser')
        video_url = soup.select('.origin-top-right a')[0]['href']
        title = soup.select('.leading-tight p')[0].get_text()
        filename = re.sub(r'[^a-zA-Z0-9 ]', '', title).strip() + ".mp4"
        
        if not filename or not video_url:
            raise ValueError("Could not extract video URL or title.")
        
        download(video_url, filename)
    except (IndexError, ValueError) as e:
        print(f"Failed to retrieve video information: {e}")
        sys.exit(1)
    except requests.RequestException as e:
        print(f"Network error occurred: {e}")
        sys.exit(1)

def download(url, filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        file_path = path.join(path.dirname(path.realpath(__file__)), filename)
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk: 
                    f.write(chunk)

if __name__ == "__main__":
    get_video()
    print(f"File downloaded") 