thondef format_duration(duration_text):
"""
Format video duration into a more user-friendly string.
:param duration_text: Video duration as a string (e.g., "9:46").
:return: Formatted duration (e.g., "9 minutes 46 seconds").
"""
minutes, seconds = map(int, duration_text.split(":"))
return f"{minutes} minutes {seconds} seconds"