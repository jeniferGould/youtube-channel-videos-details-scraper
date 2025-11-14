thonimport json
from extractors.video_parser import parse_video_data
from outputs.exporters import export_to_json

def main():
    # Sample video data
    video_data = {
        "videoId": "qs16BDaPQjc",
        "thumbnail": {"thumbnails": [{"url": "https://i.ytimg.com/vi/qs16BDaPQjc/hqdefault.jpg", "width": 168, "height": 94}]},
        "title": {"runs": [{"text": "How to scrape all of Crunchbase 😱"}]},
        "viewCountText": {"simpleText": "265 views"},
        "publishedTimeText": {"simpleText": "10 days ago"},
        "lengthText": {"simpleText": "9:46"}
    }
    
    # Process and parse video data
    parsed_data = parse_video_data(video_data)
    
    # Export data
    export_to_json(parsed_data, "output.json")

if __name__ == "__main__":
    main()