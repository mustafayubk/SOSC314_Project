# SOSC314_Project  
## Audience Engagement and Emotional Tone Across YouTube Video Genres

## Project Overview
This project examines how audience engagement and emotional tone vary across distinct YouTube video genres, focusing on TED-style talks, short films, and personal opinion videos. Using YouTube comments as text-as-data, the project investigates how differences in content format and communicative intent shape both the volume and emotional characteristics of audience responses.

## Research Question
How do audience engagement and emotional tone in YouTube comments differ across TED-style talks, short films, and personal opinion videos, when engagement is measured using matched top-level comment samples and emotional tone is estimated using text-as-data methods?

## Data Source
The project uses publicly available YouTube comments collected via the YouTube Data API (v3). Comments are collected programmatically for a curated set of videos spanning multiple genres and time periods.

## Unit of Analysis
The primary unit of analysis is the individual top-level YouTube comment. Each comment is linked to video-level metadata, including genre and publication period.

## Project Status

### Week 2
- Research question development
- Genre selection and project scoping
- GitHub repository setup

### Week 3: Data Construction, Cleaning, and Measurement Strategy
Week 3 focuses on constructing a comparable YouTube comment dataset and documenting all data preparation decisions.

- **Video sample:** 45 videos total (15 per genre: TED-style, short film, personal opinion)
- **Time stratification:** Within each genre, videos are evenly divided across three time periods (2000–2010, 2010–2020, post-2020; 5 videos per period)
- **Comment collection:** Up to 500 top-level comments per video collected via the YouTube Data API
- **Raw data:** Over 22,000 comments collected and stored prior to cleaning
- **Cleaning steps:** Removal of empty comments and duplicate comment IDs; construction of basic derived measures (e.g., comment length)
- **Measurement strategy (current):** Audience engagement operationalized as the number of top-level comments per video, with aggregation by genre for exploratory analysis
- **Planned analyses:** Sentiment and emotional tone estimation using text-as-data methods in later project stages
- **Outputs:** Cleaned comment dataset, failure logs for videos below threshold, and a genre-based descriptive figure summarizing engagement

## Execution Environment
All notebooks are designed to be run in Google Colab. API credentials are stored securely as environment variables within Colab and are not committed to the GitHub repository. Notebooks are uploaded without execution outputs to ensure reproducibility and credential safety.

