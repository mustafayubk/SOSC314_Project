# Data Dictionary: YouTube Comments Dataset

## Unit of analysis
One row represents one **top-level YouTube comment**.

---

## Video-level fields (from sampling list)

- video_id: YouTube video identifier (string)
- title: Video title (string)
- channel: Channel/uploader name (string)
- category: TED-style talk / short film / personal opinion (string)
- year: Upload year (integer)
- time_bin: 2000–2010 / 2010–2020 / post-2020 (string)
- selection_reason: Brief justification for why the video fits the genre and selection criteria (string)
- comment_threshold_met: Whether the video meets the minimum comment threshold (yes/no)

---

## Comment-level fields (from YouTube API)

- comment_id: Unique comment identifier (string)
- text: Comment text (plain text) (string)
- like_count: Number of likes on the comment (integer)
- published_at: Comment timestamp (ISO datetime string)

---

## Cleaning indicators (created during preprocessing)

- is_deleted_or_empty: 1 if comment text is missing or unavailable (e.g., removed/deleted)
- is_duplicate: 1 if duplicate comment text within the same video
- is_too_short: 1 if below minimum word threshold (planned: < 3 words)
- kept_for_analysis: 1 if comment passes all cleaning rules

---

## Derived measures (computed in later stages)

- word_count: Number of words in cleaned comment text
- sentiment_score: Sentiment score assigned using a text-as-data method (to be implemented and compared in Week 4)
