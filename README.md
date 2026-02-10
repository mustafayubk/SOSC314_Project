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

### Week 5: Diagnostics, Robustness, and Validity Checks

Week 5 focuses on evaluating the robustness and validity of sentiment-based findings through a series of controlled diagnostic analyses. Rather than introducing new data, this stage treats the existing multi-genre comment dataset as a fixed input and tests how sensitive observed patterns are to analytic, preprocessing, and sampling decisions.

Current work includes:
- Treating the existing multi-genre comment dataset as a fixed analytic baseline
- Applying multiple preprocessing pipelines (raw text, basic cleaning, aggressive normalization)
- Recomputing sentiment scores under each preprocessing condition
- Conducting sample-size sensitivity checks using matched top-level comment samples
- Inspecting sentiment score distributions to identify compression, skewness, and mass at neutral values
- Implemented preprocessing sensitivity diagnostics using multiple text normalization pipelines
- Evaluated sample-size robustness by varying the number of comments per video
- Conducted method robustness checks comparing VADER and TextBlob sentiment distributions

Diagnostic focus (Week 5):
- **Preprocessing sensitivity:** Assessing how sentiment estimates shift when URLs, punctuation, casing, and non-alphanumeric characters are progressively removed
- **Sample-size robustness:** Testing whether genre-level sentiment patterns remain stable as the number of comments per video varies
- **Distributional inspection:** Examining sentiment score distributions to evaluate validity and potential measurement artifacts

These diagnostics demonstrate that sentiment estimates are not invariant properties of the data but are shaped by representation, preprocessing, and sampling choices. While absolute sentiment magnitudes change under different conditions, relative genre-level patterns remain largely stable. This strengthens confidence in the substantive interpretation of emotional tone differences across genres.

This week also marks a transition toward a fully modular, reproducible analysis pipeline. Beginning in Week 6, this pipeline will be applied to a channel-based sample focused on TED and TEDx talks, enabling more representative inference while maintaining consistent time-bin stratification.

### Week 6: Channel-Based Data Collection + Pipeline Stabilization (In Progress)

Week 6 focuses on applying our established scraping + preprocessing pipeline to a channel-based sample (TED/TEDx), while maintaining consistent time-bin stratification. The goal is to produce a stable, analysis-ready comment dataset that can support our updated research question about how emotional tone varies over time and across sentiment operationalizations.

Current work includes:

- Running a fault-tolerant YouTube Data API scraping loop (chunked saves + progress logging) for the TED/TEDx channel sample
- Building a raw-to-clean pipeline: merging chunk files, removing empty comments, and dropping duplicate comment IDs
- Verifying time coverage and constructing time bins from observed data availability (current coverage: 2016–2026)
- Creating a processed dataset that is small enough to share and reproducible (raw chunks archived separately)

Time bin operationalization (current):

- 2016–2018 (early YouTube TED)
- 2019–2020 (pre-COVID)
- 2021–2022 (COVID & aftermath)
- 2023–2026 (recent)

Outputs (Week 6):

- Raw chunked comment files (stored locally / zipped backup to prevent data loss)
- Progress logs + scrape summary files for reproducibility and debugging
- Cleaned, deduplicated comments dataset with time-bin variable for analysis-ready use

Next steps:

- Implement multiple sentiment operationalizations (e.g., VADER + TextBlob) on the same cleaned dataset
- Compare sentiment distributions and time-bin patterns across operationalizations
- Begin Week 4 focus: analytic comparison of how measurement choices shape interpretation of public engagement

### Pipeline Development and Planned Sampling Pivot

At this stage, the project prioritizes building a reusable and transparent analysis pipeline for sentiment estimation, preprocessing, and diagnostic evaluation. This pipeline-first approach allows analytic decisions to be tested and validated independently of data expansion.

In later project stages, the pipeline will be applied to a more systematically sampled dataset using channel-based collection (e.g., the TED YouTube channel). This planned pivot addresses representativeness concerns by clearly defining the content population, while preserving methodological continuity across project stages.

## Execution Environment
All notebooks are designed to be run in Google Colab. API credentials are stored securely as environment variables within Colab and are not committed to the GitHub repository. Notebooks are uploaded without execution outputs to ensure reproducibility and credential safety.

