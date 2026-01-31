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


## Week 4: Sentiment Measures and Preprocessing Variants

The following sentiment measures were constructed for Week 4 analysis to examine how different operationalization and preprocessing choices affect observed emotional tone.

### Sentiment Methods

- **sentiment_vader / sent_raw**  
  Sentiment scores generated using the VADER sentiment analyzer applied to raw comment text. VADER is designed for short, informal online text and returns a compound score ranging from -1 (negative) to +1 (positive).

- **sentiment_textblob**  
  Sentiment polarity scores generated using TextBlob. TextBlob relies on a lexicon-based approach and produces polarity scores on a similar scale but with different sensitivity to wording and context.

### Preprocessing Variants

To assess how text preprocessing choices affect sentiment estimates, multiple text representations were created:

- **text_raw**  
  Original comment text with no preprocessing applied.

- **text_basic**  
  Light preprocessing including lowercasing and removal of punctuation and extra whitespace.

- **text_aggressive**  
  More aggressive preprocessing including stopword removal and normalization, designed to reduce noise but potentially remove contextual cues.

Corresponding sentiment scores (`sent_raw`, `sent_basic`, `sent_aggressive`) were computed using VADER on each text variant.

### Analytical Purpose

These multiple sentiment representations allow controlled comparisons of how preprocessing intensity and sentiment method choice influence genre-level sentiment patterns.
