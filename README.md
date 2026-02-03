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

### Week 2:
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

### Week 4: Operationalization and Representation 
Week 4 focuses on operationalizing emotional tone in YouTube comments and comparing how different analytic and representation choices affect observed genre-level patterns.

Current work includes:
- Preparing an analysis-ready comment dataset for Week 4
- Implementing multiple sentiment operationalizations (VADER and TextBlob)
- Comparing preprocessing and representation decisions under controlled conditions
- Producing a genre-level comparison figure and analytic report

### Analytic Comparisons (Week 4 Focus)

Week 4 explicitly evaluates how analytic and representation choices affect sentiment estimates. Two types of controlled comparisons are implemented:

1. **Method comparison:** Sentiment scores are computed using two dictionary-based approaches (VADER and TextBlob) on the same set of comments to assess agreement and divergence across genres.

2. **Preprocessing comparison:** Sentiment is computed on multiple versions of the same text (raw, basic preprocessing, aggressive preprocessing) to examine how cleaning and normalization decisions shift genre-level sentiment patterns.

These comparisons demonstrate that sentiment estimates are not fixed properties of the data but depend on methodological choices, which has implications for interpreting emotional tone across YouTube genres.


## Execution Environment
All notebooks are designed to be run in Google Colab. API credentials are stored securely as environment variables within Colab and are not committed to the GitHub repository. Notebooks are uploaded without execution outputs to ensure reproducibility and credential safety.

### Week 5: Diagnostics, Robustness, and Validity Checks (In Progress)

Week 5 focuses on evaluating the robustness and validity of sentiment-based findings by conducting diagnostic analyses under controlled conditions. Rather than introducing new data, this stage tests how sensitive observed patterns are to analytic and preprocessing decisions.

Current work includes:
- Treating the existing multi-genre comment dataset as a fixed input
- Applying multiple preprocessing pipelines (raw text, basic cleaning, aggressive normalization)
- Recomputing sentiment scores under each preprocessing condition
- Comparing genre-level sentiment summaries across preprocessing variants

### Diagnostic Focus (Week 5)

Week 5 explicitly evaluates whether genre-level sentiment patterns are stable or fragile with respect to analytic choices. Diagnostics include:

- **Preprocessing sensitivity:** Assessing how sentiment estimates shift when URLs, punctuation, casing, and non-alphanumeric characters are progressively removed
- **Distributional inspection:** Examining sentiment score distributions to identify compression, skewness, and mass at neutral values
- **Comparability checks:** Ensuring that all comparisons are conducted on identical comment samples to isolate analytic effects from sampling effects

These diagnostics demonstrate that sentiment estimates are not invariant properties of the data but are shaped by representation and preprocessing choices. This has direct implications for the validity of genre-level emotional comparisons.

### Pipeline Development and Planned Sampling Pivot

At this stage, the project prioritizes building a reusable and transparent analysis pipeline for sentiment estimation, preprocessing, and diagnostic evaluation. This pipeline-first approach allows analytic decisions to be tested and validated independently of data expansion.

In later project stages, the pipeline will be applied to a more systematically sampled dataset using channel-based collection (e.g., the TED YouTube channel). This planned pivot addresses representativeness concerns by clearly defining the content population, while preserving methodological continuity across project stages.
