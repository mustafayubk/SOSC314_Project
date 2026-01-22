"""
01_collect_comments.py

Collect up to N top-level YouTube comments per video using the YouTube Data API.
Reads input video list from: data/video_list.csv
Writes raw output to:       data/raw/comments_raw_baseline.csv

NOTE:
- Do NOT hardcode your API key here.
- In Colab, set your API key as an environment variable: YOUTUBE_API_KEY
"""

import os
import time
import pandas as pd
from googleapiclient.discovery import build


# ----------------------------
# Config
# ----------------------------
INPUT_VIDEO_LIST = "data/video_list.csv"
OUTPUT_PATH = "data/raw/comments_raw_baseline.csv"
MAX_COMMENTS_PER_VIDEO = 500
SLEEP_BETWEEN_CALLS_SEC = 0.1  # small delay to be polite / avoid quota spikes


def get_youtube_client():
    api_key = os.environ.get("YOUTUBE_API_KEY")
    if not api_key:
        raise ValueError(
            "Missing YOUTUBE_API_KEY environment variable. "
            "In Colab, set it with: os.environ['YOUTUBE_API_KEY'] = 'YOUR_KEY'"
        )
    return build("youtube", "v3", developerKey=api_key)


def fetch_comments_for_video(youtube, video_id: str, max_comments: int = 500):
    """
    Fetch up to max_comments top-level comments for a single video_id.
    Returns list of dict rows.
    """
    rows = []
    next_page_token = None

    while len(rows) < max_comments:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100,          # API max per page
            pageToken=next_page_token,
            textFormat="plainText",
            order="relevance"        # common choice; consistent across videos
        )
        response = request.execute()

        items = response.get("items", [])
        for item in items:
            snippet = item["snippet"]["topLevelComment"]["snippet"]

            rows.append({
                "video_id": video_id,
                "comment_id": item["snippet"]["topLevelComment"]["id"],
                "text": snippet.get("textDisplay", ""),
                "like_count": snippet.get("likeCount", 0),
                "published_at": snippet.get("publishedAt", ""),
            })

            if len(rows) >= max_comments:
                break

        next_page_token = response.get("nextPageToken", None)
        if not next_page_token:
            break

        time.sleep(SLEEP_BETWEEN_CALLS_SEC)

    return rows


def main():
    # Load video list
    videos = pd.read_csv(INPUT_VIDEO_LIST)

    # If video_id column is empty right now, we will need to fill it later.
    # For now, we still keep the structure and fail clearly if missing IDs.
    if "video_id" not in videos.columns:
        raise ValueError("video_list.csv is missing 'video_id' column.")
    if videos["video_id"].isna().all() or (videos["video_id"].astype(str).str.strip() == "").all():
        raise ValueError(
            "All video_id values are blank. "
            "You must fill video_id (YouTube video IDs) before collecting comments."
        )

    youtube = get_youtube_client()

    all_rows = []
    for _, row in videos.iterrows():
        video_id = str(row["video_id"]).strip()
        if not video_id:
            continue

        print(f"Collecting comments for video_id={video_id} ...")
        rows = fetch_comments_for_video(youtube, video_id, MAX_COMMENTS_PER_VIDEO)
        all_rows.extend(rows)
        print(f"  -> got {len(rows)} comments")

    df = pd.DataFrame(all_rows)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"\nSaved: {OUTPUT_PATH}")
    print(df.head())


if __name__ == "__main__":
    main()
