# Student Career Success Predictor

## Team members

| Member | Entry no. | Role | GitHub Handle |
| :--- | :--- | :--- | :--- |
| Soham Prashant Phansekar | 2026EEB1415 | Documentation lead | @soham197 |
| Manpreet Kaur | 2026AIB1057 | PPT lead | @2026aib1057-1762 |
| Kanaparthi Siva Sai Tanishq | 2026ESB1478 | Execution lead | @tanishq7585 |
| Manoj Prajapat | 2026MCB1545 | Video lead | @2026mcb1545-rgb |

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
- `data/student_career_success_dataset.csv` — Raw dataset
- `src/main.py` — Main entry point to run the pipeline
- `src/data_prep.py` — Directory paths and dataset configurations
- `src/plots.py` — Exploratory data analysis and visualization functions
- `src/model.py` — Machine learning model training and evaluation
- `outputs/` — Auto-generated charts and results (`.png` files)
- `docs/Student_Career_Success_Predictor(Group_27).pdf` — Project presentation slides
- `requirements.txt` — Pinned Python dependencies
- `README.md` — Project documentation

**Installation:**

```bash
git clone [https://github.com/soham197/student-career-success-predictor.git](https://github.com/soham197/student-career-success-predictor.git)
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

## Model Evaluation and Results

After removing post-placement variables to prevent data leakage, the models achieved highly realistic predictive performance using strictly pre-placement academic and skill-based features.

* **Best Performing Model:** Logistic Regression
* **Overall Accuracy:** 81.49%
* **Overall F1-Score:** 0.8889

**Key Metrics (Logistic Regression):**
* **Placed Students:** 84% Precision | 95% Recall
* **Not Placed Students:** 65% Precision | 34% Recall

**Key Insights:**
* Logistic Regression slightly outperformed the Random Forest classifier (which achieved 80.75% accuracy).
* The model is exceptionally strong at identifying students who will successfully secure placement (95% recall for the 'Placed' class).
* Based on feature importance analysis, the top 5 most critical predictors for student placement are: **CGPA, Attendance Percentage, Resume Score, Study Hours Per Week, and Projects Completed**.

## Presentation and demonstrations
* **Presentation slides:** `docs/Student_Career_Success_Predictor(Group_27).pdf`
* **Demonstration video:** https://drive.google.com/drive/folders/1o-h6EfeleglocYYfeaSDLOE2paJuvBON

## AI usage disclosure
- **ChatGPT:** Used for PPT drafts and slide outlines.
- **Gemini:** Used to draft the README.md structure, assist with Python script organization, and write the exploratory data analysis and plotting functions; reviewed, tested, and edited by the team.
- No AI was used to generate the dataset or falsify the final evaluation results.

## Acknowledgment
Developed for the AI101 course at the Indian Institute of Technology Ropar.
