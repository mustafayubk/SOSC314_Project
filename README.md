# SOSC314 Project  
## Emotional Tone and Audience Engagement in YouTube Expert Discourse

**Author:** Mustafa Ayub Khan  
**Course:** SOSC314 – Computational Social Science  

🔗 **Public Project Report (GitHub Pages):**  
https://mustafayubk.github.io/SOSC314_Project/

---

# Project Overview:
This project examines how emotional tone in public responses to expert discourse on YouTube varies over time and how different sentiment measurement strategies affect substantive conclusions about audience engagement.

Using TED and TEDx videos as a clearly defined expert content population, the project builds a fully reproducible text-as-data pipeline to:
- Collect YouTube comments via the YouTube Data API (v3)
- Construct time-stratified video samples
- Clean and preprocess large-scale comment datasets
- Apply multiple sentiment operationalizations (VADER and TextBlob)
- Conduct diagnostic and robustness checks
- Compare methodological sensitivity across preprocessing and model choices

The final analysis evaluates how emotional tone evolves across publication periods and how analytic decisions shape interpretation.

---

# Research Question:
**How does emotional tone in audience responses to TED talks vary across time, and how do different sentiment operationalizations shape our interpretation of public engagement with expert discourse?**

---

# Data:
## Source
- YouTube Data API v3
- Official TED and TEDx YouTube channels

## Unit of Analysis
- Individual top-level YouTube comments
- Linked to video-level metadata (genre and publication period)

## Sampling Design

### Early Pipeline Validation (Weeks 3–5)
- Structured video sampling
- Controlled comment caps
- Multi-genre comparison for methodological validation
  
### Final Analysis Dataset (Week 6)
- Channel-based sampling from TED and TEDx
- Time stratification into publication bins:
  - 2016–2018
  - 2019–2020
  - 2021–2022
  - 2023–2026
- Large-scale comment aggregation
- Sentiment scoring across time bins

Raw comment data are not redistributed due to API and platform policy constraints. Reproduction requires a valid YouTube API key.

---

# Repository Structure:
```
SOSC314_Project/
│
├── .github/workflows/ # GitHub Pages deployment
├── config/ # API configuration templates (no secrets)
├── data/ # Raw and cleaned datasets
├── docs/ # Rendered HTML for GitHub Pages
└── index.html
├── notebooks/ # Data collection + analysis notebooks
├── scripts/ 
└── README.md
```

# Methods
## Sentiment Operationalizations:

1. **VADER**
   - Social-media optimized lexicon
   - Produces compound sentiment scores
2. **TextBlob**
   - Dictionary-based polarity scoring
   - More conservative distribution

## Diagnostics and Robustness Checks:
- Preprocessing sensitivity (raw vs cleaned text)
- Sample-size robustness
- Distributional comparison of sentiment outputs
- Cross-method comparison (VADER vs TextBlob)
- Transformer-based sentiment robustness check (final stage)

The analysis emphasizes that sentiment estimates are not invariant properties of text but depend on methodological choices.

---

# Reproducing the Project
## 1. Environment Setup
Python 3.10+ recommended.
Clone repository:
git clone https://github.com/mustafayubk/SOSC314_Project.git
cd SOSC314_Project

## 2. API Setup
Obtain a YouTube Data API key from:
https://developers.google.com/youtube/v3
Set environment variable:
Mac/Linux:
export YOUTUBE_API_KEY="your_key_here"
Do NOT commit API keys to the repository.

## 3. Execution Order
Run components in the following logical order:
1. Video sampling and metadata construction (`notebooks/`)
2. Cleaning and preprocessing pipeline
3. Sentiment scoring (VADER + TextBlob)
4. Diagnostic and robustness notebooks
5. Final analytic notebook (used to generate `docs/index.html`)

To regenerate the HTML report:
jupyter nbconvert --to html notebooks/SOSC314_FinalReport.ipynb --output ../docs/index.html

# Key Findings:
- Emotional tone varies across publication periods.
- VADER and TextBlob produce systematically different magnitude distributions.
- Absolute sentiment values are sensitive to preprocessing.
- Relative time-bin patterns are more stable across methodological choices.
- Measurement decisions significantly shape interpretations of “public engagement.”

# Ethical Considerations:
- All analyzed comments are publicly available.
- No personally identifying information is redistributed.
- Raw comment data are not included to comply with API and platform policies.
- API credentials are excluded from version control.

# Dependencies:
Core libraries include:
- pandas
- numpy
- matplotlib
- nltk
- vaderSentiment
- textblob
- google-api-python-client
- tqdm

Optional (robustness stage):
- transformers
- torch

# Acknowledgments:
This project uses:
- YouTube Data API v3  
- VADER sentiment lexicon  
- TextBlob sentiment library  

Limited generative AI (ChatGPT) was used for formatting and structural guidance only. All analytic decisions and interpretations were made by the author.

---
