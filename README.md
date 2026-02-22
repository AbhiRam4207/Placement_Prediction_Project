# Placement Prediction using Machine Learning

This project aims to predict student placement outcomes and expected salary using machine learning. It is designed to help students—especially from Tier-2 and Tier-3 colleges—understand how their academic background, technical skills, and extracurricular activities impact their placement chances.

## ✨ Final Output

<img src="static/images/placement_screenshot_1.png" alt="Placement Screenshot 1" width="100%">
<img src="static/images/placement_screenshot_2.png" alt="Placement Screenshot 2" width="100%">
<img src="static/images/placement_screenshot_3.png" alt="Placement Screenshot 3" width="100%">
---

## 📚 Table of Contents
- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Dataset](#dataset)
- [Installation](#installation)
- [Folder Structure](#folder-structure)
- [Data Preprocessing](#data-preprocessing)
- [Model Training](#model-training)
- [Evaluation](#evaluation)
- [Results](#results)
- [Flask App](#flask-app)
- [Contributing](#contributing)
- [License](#license)

---

## 🧠 Overview

Campus placements are one of the most critical phases for engineering students. This project provides a smart prediction tool using machine learning algorithms (Random Forest Classifier and Decision Trees) to predict:

- Whether a student will be placed.
- Expected salary if placed.

The project also includes a web app built with Flask for real-time predictions.

---

## ❓ Problem Statement

Many students from Tier-2 and Tier-3 colleges face difficulty in understanding how their profile affects their placement outcomes. Institutions also lack predictive systems for early career guidance. This project addresses the gap by building a data-driven placement and salary prediction system.

---

## 📊 Dataset

The datasets include the following student features:

- CGPA (Cumulative GPA)
- Technical and soft skills
- Internships and hackathon participation
- Communication skills (rating)
- Academic percentages (10th & 12th)
- Number of projects, certifications, backlogs, etc.

The data is stored in:

- Datasets/Placement_Prediction_data.xlsx
- Datasets/Salary_prediction_data.xlsx

---

## 💻 Installation

To run this project locally:

1. Clone the repository:

```bash
git clone https://github.com/yourusername/Placement_Prediction_Project.git
cd Placement_Prediction_Project
