# Student Career Success Predictor

## Team members
* **Soham Prashant Phansekar** (2026EEB1415) - Documentation lead
* **Manpreet Kaur** (2026AIB1057) - PPT lead
* **Kanaparthi Siva Sai Tanishq** (2026ESB1478) - Execution lead
* **Manoj Prajapat** (2026MCB1545) - Video lead
*(Note: Active development is currently being managed by Soham and Manoj).*

## Project statement
Predicting student career outcomes and placement success based on academic performance, skills, and extracurricular activities.

## Dataset information and project objectives
* **Dataset:** `data/student_career_success_dataset.csv` (50,000 rows, 29 columns)
* **Source:** [Kaggle - Student Career Success Prediction Dataset](https://www.kaggle.com/datasets/mobeenfatimah/student-career-success-prediction-dataset/data)
* **Target variable:** `Placement_Status` (Placed / Not Placed)
* **Objective:** To build a complete machine learning pipeline that preprocesses student data, performs exploratory data analysis (EDA), and trains a classification model to predict placement outcomes.

## Project workflow
1. **Data loading and preprocessing:** Read the CSV using pandas, handle categorical variables, and define the target.
2. **Exploratory data analysis (EDA):** Generate visualizations for status distribution, CGPA impact, internship rates, and feature correlations.
3. **Model training:** Split the data into training and testing sets, then train a machine learning classification model.
4. **Evaluation:** Output accuracy metrics and save all visualization plots automatically.

## Technologies used
* **Language:** Python 3.10+
* **Libraries:** pandas, matplotlib, scikit-learn

## Project structure, installation and execution

**Structure:**
* `data/student_career_success_dataset.csv` — Raw dataset
* `src/main.py` — Main entry point to run the pipeline
* `src/data_prep.py` — Directory paths and dataset configurations
* `src/plots.py` — Exploratory data analysis and visualization functions
* `src/model.py` — Machine learning model training and evaluation
* `outputs/` — Auto-generated charts and results (`.png` files)
* `docs/Group27_slides.pdf` — Project presentation slides
* `requirements.txt` — Pinned Python dependencies
* `README.md` — Project documentation

**Installation:**
    git clone https://github.com/[YOUR_GITHUB_USERNAME]/student-career-success-predictor.git
    cd student-career-success-predictor
    python -m venv venv
    # On Linux/macOS:
    source venv/bin/activate
    # On Windows:
    venv\Scripts\activate
    pip install -r requirements.txt

**Execution:**
    python src/main.py

*(All generated plots will automatically save to the `outputs/` folder without requiring manual uploads).*

## Model evaluation and result
* **Model used:** [Insert Model Name, e.g., Random Forest Classifier]
* **Accuracy score:** [Insert Accuracy Score]%
* **Key findings:** [Insert a 1-sentence summary, e.g., CGPA and Internship counts were the strongest predictors of placement success].

## Presentation and demonstrations
* **Presentation slides:** `docs/Group27_slides.pdf`
* **Demonstration video:** [Insert Unlisted YouTube or Google Drive Link Here]

## AI usage disclosure
* **Gemini:** Used by Soham Prashant Phansekar to draft the README.md structure and assist with Python script organization.
* **Claude:** Used by Manoj Prajapat to write the exploratory data analysis and plotting functions (`src/plots.py`).
* No AI was used to generate the dataset or falsify the final evaluation results.

## Acknowledgment
Developed for the AI101 course at the Indian Institute of Technology Ropar.
