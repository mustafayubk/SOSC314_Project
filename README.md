# SOSC314_Project  
## Emotional Tone and Audience Engagement in YouTube Comments

## Project Overview
This project examines how emotional tone and audience engagement differ across YouTube video genres, including TED-style talks, short films, and personal opinion videos. Using YouTube comments as text-as-data, the project aims to understand how communication norms and emotional expression vary depending on media context.

## Research Question
How does emotional tone and audience engagement differ across YouTube video genres such as TED-style talks, short films, and personal opinion videos?

## Data Source
The project uses publicly available YouTube comments collected via the YouTube Data API. Initial data collection focuses on a pilot sample of videos from each category to assess data feasibility and scope.

## Unit of Analysis
The unit of analysis is individual YouTube comments.

## Current Status
Week 2: Research question defined, GitHub repository created, and initial data exploration planned.

Week 3: Data Construction, Cleaning, and Measurement Strategy

Week 3 focuses on constructing the YouTube comment dataset, documenting data cleaning and preprocessing decisions, and defining measurement strategies.

- Dataset: 9 videos (3 per category: TED-style talk, short film, personal opinion)
- Time stratification: videos selected across three periods (2000–2010, 2010–2020, post-2020)
- Collection goal: up to 500 top-level comments per video using the YouTube Data API
- Cleaning plan: removal of deleted or removed comments, duplicate entries, and extremely short comments
- Measurement plan: sentiment scores as a proxy for emotional tone and word count as a proxy for engagement

### Execution Environment

All notebooks are designed to be run in Google Colab. API credentials are stored securely within the Colab environment and are not committed to the GitHub repository. Notebooks in this repository are uploaded without execution outputs to ensure reproducibility and protect credentials.

