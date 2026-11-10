"""Exploratory plots. All figures are saved in the outputs/ folder."""
import matplotlib
matplotlib.use("Agg")  # no window needed, just save files
import matplotlib.pyplot as plt

from data_prep import OUTPUT_DIR, TARGET

def _save(name):
    OUTPUT_DIR.mkdir(exist_ok=True)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / name, dpi=120)
    plt.close()
    print(f"Saved outputs/{name}")

def plot_placement_distribution(df):
    counts = df[TARGET].value_counts()
    plt.figure(figsize=(5, 4))
    plt.bar(counts.index, counts.values, color=["#2a9d8f", "#e76f51"])
    plt.title("Placement Status Distribution")
    plt.ylabel("Number of students")
    _save("placement_distribution.png")

def plot_cgpa_by_placement(df):
    plt.figure(figsize=(6, 4))
    for status, color in [("Placed", "#2a9d8f"), ("Not Placed", "#e76f51")]:
        plt.hist(df[df[TARGET] == status]["CGPA"], bins=30, alpha=0.6,
                 label=status, color=color)
    plt.title("CGPA vs Placement")
    plt.xlabel("CGPA")
    plt.ylabel("Students")
    plt.legend()
    _save("cgpa_by_placement.png")

def plot_internships_rate(df):
    # Convert text 'Placed' to numbers 1/0 for calculating the percentage
    df['Is_Placed'] = (df[TARGET] == 'Placed').astype(int)
    rate = df.groupby("Internships")["Is_Placed"].mean() * 100
    
    plt.figure(figsize=(6, 4))
    plt.bar(rate.index.astype(str), rate.values, color="#264653")
    plt.title("Placement Rate by Number of Internships")
    plt.xlabel("Internships")
    plt.ylabel("Placement rate (%)")
    _save("placement_rate_by_internships.png")

def plot_correlation(df):
    # Convert text 'Placed' to numbers 1/0 for the correlation matrix
    df['Is_Placed'] = (df[TARGET] == 'Placed').astype(int)
    
    cols = ["CGPA", "Attendance_Percentage", "Study_Hours_Per_Week",
            "Programming_Skill", "Projects_Completed", "Certifications",
            "Hackathons", "Internships", "Resume_Score", "Is_Placed"]
    corr = df[cols].corr()
    
    plt.figure(figsize=(8, 6))
    plt.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)
    plt.colorbar()
    plt.xticks(range(len(cols)), cols, rotation=90)
    plt.yticks(range(len(cols)), cols)
    plt.title("Correlation Heatmap")
    _save("correlation_heatmap.png")

def make_all_plots(df):
    plot_placement_distribution(df)
    plot_cgpa_by_placement(df)
    plot_internships_rate(df)
    plot_correlation(df)
