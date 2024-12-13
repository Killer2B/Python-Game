import os
from pytube import YouTube
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import ssl
import time

# Ensure SSL support is available in the environment
ssl._create_default_https_context = ssl._create_unverified_context

def download_youtube_video(url, output_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        print(f"Downloading YouTube video: {yt.title}")
        stream.download(output_path)
        print("Download completed!")
    except Exception as e:
        print(f"Error downloading YouTube video: {e}")

def download_tiktok_video(url, output_path):
    driver = None
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://savett.cc/")

        input_box = driver.find_element(By.NAME, "url")  # Adjust selector if necessary
        input_box.send_keys(url)
        input_box.send_keys(Keys.RETURN)

        time.sleep(5)  # Allow time for the page to process the video

        download_button = driver.find_element(By.LINK_TEXT, "Download Without Watermark")
        download_url = download_button.get_attribute("href")

        driver.get(download_url)

        # Instead of saving page source, directly download the file using a request
        import requests
        response = requests.get(download_url, stream=True)
        if response.status_code == 200:
            with open(os.path.join(output_path, "tiktok_video.mp4"), "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            print("TikTok video downloaded!")
        else:
            print("Failed to download TikTok video.")
    except Exception as e:
        print(f"Error downloading TikTok video: {e}")
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    output_directory = "./downloads"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    youtube_url = "https://www.youtube.com/watch?v=EcPMA4DIakM"  # Replace with a test URL
    tiktok_url = "https://www.tiktok.com/@example/video/example"  # Replace with a test URL

    if youtube_url:
        print(f"YouTube URL: {youtube_url}")
        download_youtube_video(youtube_url, output_directory)

    if tiktok_url:
        print(f"TikTok URL: {tiktok_url}")
        download_tiktok_video(tiktok_url, output_directory)
