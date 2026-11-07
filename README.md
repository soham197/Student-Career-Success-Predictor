# Student Career Success Predictor

Predicts student career outcomes and placement success from 50,000 student academic and skill records using Python (pandas, matplotlib, scikit-learn).

* **Course:** AI101: Data Science and AI Essentials with Python, sAIDE, IIT Ropar
* **Team:** Group 27
* **Dataset Source:** [Kaggle - Student Career Success Prediction Dataset](https://www.kaggle.com/datasets/mobeenfatimah/student-career-success-prediction-dataset/data) (50,000 rows, 29 columns)

## Team and roles

| Member | Entry no. | Role | GitHub Handle |
| :--- | :--- | :--- | :--- |
| Soham Prashant Phansekar | 2026EEB1415 | Documentation lead | @[YOUR_GITHUB_USERNAME] |
| Manpreet Kaur | 2026AIB1057 | PPT lead | @[MANPREET_GITHUB_USERNAME] |
| Kanaparthi Siva Sai Tanishq | 2026ESB1478 | Execution lead | @[TANISHQ_GITHUB_USERNAME] |
| Manoj Prajapat | 2026MCB1545 | Video lead | @[MANOJ_GITHUB_USERNAME] |

Code contributions are tracked in the repository commit history.

## Project structure

* `student-career-success-predictor/`
  * `data/student_career_success_dataset.csv` — 50,000 rows, 29 columns (student records)
  * `src/main.py` — Entry point to run preprocessing, model, and plots
  * `src/model.py` — Model training and evaluation functions
  * `outputs/` — Generated plots and evaluation figures saved here
  * `docs/Group27_slides.pdf` — 5-slide project presentation
  * `requirements.txt` — Pinned Python library versions
  * `README.md` — Project documentation and setup guide

## Setup

Tested on Python 3.10 and 3.11 (Windows, macOS, Ubuntu).

    git clone [https://github.com/](https://github.com/)[YOUR_GITHUB_USERNAME]/student-career-success-predictor.git
    cd student-career-success-predictor
    python -m venv venv
    # On Linux/macOS:
    source venv/bin/activate
    # On Windows:
    venv\Scripts\activate
    pip install -r requirements.txt

## How to run

1. Run `python src/main.py` from the repository root folder.
2. The script loads `data/student_career_success_dataset.csv`, trains the machine learning model, prints evaluation metrics, and saves 2 plots in `outputs/`.
3. Expected runtime: under 30 seconds.

## Expected output

    Loaded data/student_career_success_dataset.csv: 50000 rows, 29 columns
    Model trained successfully | Test Score: [SCORE]
    Saved outputs/career_distribution.png
    Saved outputs/feature_importance.png

## Links

* **Slides (5):** `docs/Group27_slides.pdf`
* **Video (max 5:00):** [INSERT UNLISTED YOUTUBE OR PUBLIC DRIVE LINK]

## AI-use disclosure

* **Gemini:** Used to draft the README.md structure and assist with Python script templates; reviewed, tested, and edited by Soham Prashant Phansekar and Manoj Prajapat.
* No AI was used to generate the dataset or the final evaluation results.
