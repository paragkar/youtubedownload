import streamlit as st
from pytube import YouTube
import tempfile
import shutil

def download_youtube_video(url):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    return stream

def main():
    st.title("YouTube Video Downloader")
    
    youtube_url = st.text_input("Enter the YouTube video URL")

    if youtube_url:
        with st.spinner('Downloading YouTube video...'):
            try:
                video_stream = download_youtube_video(youtube_url)
                video_title = video_stream.title
                # Use a temporary file to download the video
                with tempfile.NamedTemporaryFile(delete=False) as tmp:
                    video_stream.download(output_path=tmp.name)
                    tmp_file_name = tmp.name

                # Display the video title and offer it for download
                st.success(f"Downloaded '{video_title}' successfully.")
                with open(tmp_file_name, "rb") as file:
                    btn = st.download_button(
                        label="Download Video",
                        data=file,
                        file_name=f"{video_title}.mp4",
                        mime="video/mp4"
                    )
            except Exception as e:
                st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
