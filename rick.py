import webbrowser

def play_rickroll():
    """
    This function opens a web browser and plays the Rick Astley's "Never Gonna Give You Up" video.
    """
    try:
        # URL of the Rick Astley's "Never Gonna Give You Up" video
        rickroll_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        
        # Open the web browser and play the video
        webbrowser.open(rickroll_url)
    except Exception as e:
        # Log the error
        print(f"Error: {e}")
