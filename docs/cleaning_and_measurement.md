# Data Cleaning and Measurement Strategy

## Overview
This document describes how YouTube comments will be cleaned, filtered, and transformed prior to analysis. The goal is to ensure comparability across videos and genres while removing low-quality or unusable text.

## Cleaning Rules

Each comment will be evaluated using the following rules:

1. **Deleted or unavailable comments**
   - Comments with missing or empty text (e.g., deleted or removed by YouTube) will be flagged and excluded.

2. **Duplicate comments**
   - Exact duplicate comment text within the same video will be flagged.
   - Only one instance of duplicated text will be retained.

3. **Extremely short comments**
   - Comments with fewer than 3 words (e.g., “lol”, “agree”, emojis only) will be flagged as low-information and excluded.

A binary variable (`kept_for_analysis`) will indicate whether a comment passes all cleaning criteria.

## Measurement Strategy

### Emotional tone
- Emotional tone will be operationalized using sentiment scores derived from text-as-data methods.
- Sentiment analysis methods will be implemented and compared in Week 4.

### Audience engagement
- Engagement will be proxied using:
  - Comment word count
  - Comment like count (when available)

These measures allow comparison of how audiences emotionally respond and engage across different video genres.

## Unit of Analysis
The unit of analysis is the individual top-level YouTube comment.
