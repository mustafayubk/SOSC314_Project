# SOSC314_Project  
## Audience Engagement and Emotional Tone Across YouTube Videos

## Project Overview
This project examines how emotional tone in audience responses to expert discourse on YouTube varies over time, using TED and TEDx talks as a clearly defined content population. Using YouTube comments as text-as-data, the project focuses on understanding how public emotional reactions to expert-led talks evolve across publication periods and how different sentiment analysis choices shape our interpretation of audience engagement.

The project is structured around a reproducible, modular data pipeline that supports large-scale comment collection, systematic preprocessing, and comparative sentiment analysis. Early project stages focused on building and validating this pipeline, while later stages apply it to a channel-based sample of TED and TEDx videos to address concerns about representativeness and sampling bias.

## Research Question
How does emotional tone in audience responses to TED talks vary across time, and how do different sentiment operationalizations shape our interpretation of public engagement with expert discourse?

## Data Source
The project uses publicly available YouTube comments collected via the YouTube Data API (v3). Data collection follows a channel-based sampling strategy, focusing on official TED and TEDx YouTube channels. Video metadata and top-level comments are collected programmatically and organized into time-based publication bins to enable longitudinal analysis.

## Unit of Analysis
The primary unit of analysis is the individual top-level YouTube comment. Each comment is linked to video-level metadata, including genre and publication period.

## Analytic Pipeline Development
A central goal of this project is the construction of a scalable and reproducible text-as-data pipeline. The pipeline is designed to operate independently of any specific dataset, allowing analytic methods to be validated before being applied to larger or alternative samples.

Key components of the pipeline include:
- Channel-based video sampling from TED and TEDx YouTube channels
- Time bin assignment based on video publication year
- Collection of top-level comments with controlled caps to ensure comparability and manage API constraints
- Comment-level cleaning and normalization
- Modular sentiment estimation using multiple dictionary-based approaches
- Diagnostic checks assessing sensitivity to preprocessing and methodological choices

This pipeline-first approach ensures that later analytic results reflect substantive patterns in the data rather than artifacts of implementation or sampling decisions.

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

### Week 6: Synthesis, Final Dataset Construction, and Channel-Based Sampling
Week 6 focuses on finalizing the project’s analytic configuration and applying the validated pipeline to a large-scale, channel-based dataset.

Key activities include:
- Scraping a large sample of videos from official TED and TEDx channels
- Constructing a unified, time-stratified comment dataset
- Applying the established preprocessing and sentiment pipeline to the full sample
- Producing near-final figures intended for the final project presentation
- Documenting limitations, scope, and validity considerations

This stage represents the transition from pipeline validation to substantive interpretation, ensuring that final conclusions are grounded in a systematically defined and representative content population.

## Execution Environment
All notebooks are designed to be run in Google Colab. API credentials are stored securely as environment variables within Colab and are not committed to the GitHub repository. Notebooks are uploaded without execution outputs to ensure reproducibility and credential safety.

