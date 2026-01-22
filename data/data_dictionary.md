# Data Dictionary: YouTube Comments Dataset

## Unit of analysis
- One row = one top-level YouTube comment.

## Video-level fields (from sampling list)
- video_id: YouTube video identifier (string)
- title: Video title (string)
- channel: Channel/uploader name (string)
- category: TED-style talk / short film / personal opinion (string)
- year: Upload year (integer)
- time_bin: 2000–2010 / 2010–2020 / post-2020 (string)
- selection_reason: Brief justification for why the video fits the genre and criteria (string)
- comment_threshold_met: Whether the video meets the minimum comment threshold (yes/no)

## Comment-level fields (from YouTube API)
- comment_id: Unique comment identifier (string)
- text: Comment text (plain text) (string)
- like_count: Number of likes on the comment (integer)
- published_at: Comment timestamp (ISO datetime string)

## Cleaning indicators (created during preprocessing)
- is_deleted_or_empty: 1 if comment text is missing/empty (e.g., removed/deleted)
- is_duplicate: 1 if duplicate text within the same video
- is_too_short: 1 if below minimum word threshold (planned: < 3 words)
- kept_for_analysis: 1 if comment passes all cleaning rules

## Derived measures (later stages)
- word_count: number of words in cleaned comment text
- sentiment_score: sentiment score assigned by a text-as-data method (methods compared in Week 4)
