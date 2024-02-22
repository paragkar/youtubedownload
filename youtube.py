import streamlit as st
from pytube import YouTube
import tempfile
import shutil
import os

def download_youtube_video(url, tempdir):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    file_path = stream.download(output_path=tempdir)
    return file_path

def main():
    st.title("YouTube Video Downloader and Processor")

    youtube_url = st.text_input("Enter the YouTube video URL")

    if youtube_url:
        with tempfile.TemporaryDirectory() as tempdir:
            # Download the video to a unique temporary directory
            with st.spinner('Downloading YouTube video...'):
                try:
                    video_path = download_youtube_video(youtube_url, tempdir)
                    video_title = os.path.basename(video_path)
                    st.success(f"Downloaded '{video_title}' successfully.")
                    
                    # Offer the video for download by reading it into memory
                    with open(video_path, "rb") as video_file:
                        btn = st.download_button(
                            label="Download Video",
                            data=video_file,
                            file_name=video_title,
                            mime="video/mp4"
                        )
                except Exception as e:
                    st.error(f"Error: {e}")

            # No need to manually delete the temp directory or files;
            # 'with tempfile.TemporaryDirectory() as tempdir' handles cleanup

if __name__ == "__main__":
    main()
