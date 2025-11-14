thondef parse_video_data(video_data):
"""
Parse raw video data into a structured format.
:param video_data: Dictionary containing raw video data.
:return: Structured dictionary with relevant video information.
"""
parsed_data = {
"id": video_data.get("videoId"),
"title": video_data.get("title", {}).get("runs", [{}])[0].get("text"),
"thumbnail_url": video_data.get("thumbnail", {}).get("thumbnails", [{}])[0].get("url"),
"view_count": video_data.get("viewCountText", {}).get("simpleText"),
"published_time": video_data.get("publishedTimeText", {}).get("simpleText"),
"duration": video_data.get("lengthText", {}).get("simpleText")
}
return parsed_data