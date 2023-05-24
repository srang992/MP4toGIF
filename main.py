import streamlit as st
import os
from moviepy.editor import VideoFileClip


def convert_mp4_to_gif(input_file, output_file, fps=10):
    clip = VideoFileClip(input_file)
    clip.write_gif(output_file, fps=fps)
    clip.close()


def main():
    st.set_page_config(page_title="MP4 to GIF Converter")
    st.title("🎬 MP4 to GIF Converter")

    # File upload section
    st.subheader("👉 Upload MP4 File")
    uploaded_file = st.file_uploader("Choose a File", label_visibility="collapsed", type=["mp4"])

    if uploaded_file is not None:
        # Save the uploaded MP4 file in the working directory
        file_name = "input.mp4"
        file_path = os.path.join(os.getcwd(), file_name)
        with open(file_path, "wb") as file:
            file.write(uploaded_file.read())

        # Convert and download section
        st.subheader("👉 Convert to GIF")
        fps = st.slider("Select the frame rate (frames per second)", min_value=1, max_value=30, value=10)
        convert_button = st.button("Convert to GIF")

        if convert_button:
            # Convert MP4 to GIF
            gif_file_name = "output.gif"
            gif_file_path = os.path.join(os.getcwd(), gif_file_name)
            convert_mp4_to_gif(file_path, gif_file_path, fps=fps)

            # Download the converted GIF file
            with open(gif_file_path, "rb") as file:
                st.download_button("Download GIF", file.read(), file_name=gif_file_name)

            os.remove(gif_file_path)

        os.remove(file_path)


if __name__ == "__main__":
    main()
