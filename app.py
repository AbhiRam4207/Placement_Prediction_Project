import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__, template_folder="templates")

# ✅ Load the models properly
placement_model = pickle.load(open('model.pkl', 'rb'))
salary_model = pickle.load(open('model1.pkl', 'rb'))

@app.route('/')
def h():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Collect input values
    try:
        # Collect input values using POST
        cgpa = float(request.form.get('cgpa', 0))
        projects = int(request.form.get('projects', 0))
        workshops = int(request.form.get('workshops', 0))
        mini_projects = int(request.form.get('mini_projects', 0))
        skills = request.form.get('skills', '')
        communication_skills = float(request.form.get('communication_skills', 0))
        internship = int(request.form.get('internship', 0))
        hackathon = int(request.form.get('hackathon', 0))
        tw_percentage = float(request.form.get('tw_percentage', 0))
        te_percentage = float(request.form.get('te_percentage', 0))
        backlogs = int(request.form.get('backlogs', 0))
        name = request.form.get('name', 'Student')

        # Count skills
        skill_count = skills.count(',') + 1 if skills.strip() else 0 # type: ignore

    # Prepare features
        features = np.array([
            cgpa, projects, workshops, mini_projects,
            skill_count, communication_skills, internship, hackathon,
            tw_percentage, te_percentage, backlogs
        ], dtype=float)

        # Predict placement probability (model returns probabilities for each class)
        # Class 1 is 'Placed'
        probabilities = placement_model.predict_proba([features])[0]
        placed_prob = round(probabilities[1] * 100, 2)
        output = placement_model.predict([features])[0]
        placement_status = str(output)  # "1" or "0"

        # Prepare data for Radar Chart (Radar chart wants labels and values)
        # Choosing meaningful metrics for the chart
        chart_labels = ["CGPA", "Projects", "Certifications", "Skills", "Comm Rating", "Academics"]
        # Normalize academic % to 0-10 scale for the chart (assuming 100% = 10)
        avg_academics = (tw_percentage + te_percentage) / 20 
        chart_values = [cgpa, projects, workshops, skill_count, communication_skills, avg_academics]

        if output == 1:
            # Predict salary only if placed
            salary_features = np.append(features, float(placement_status))
            salary = salary_model.predict([salary_features])[0]
            salary_str = f"{int(salary):,}"
            msg = f"🎉 Congratulations {name}! You have high chances of getting placed!" # type: ignore
            msg2 = f"💰 Your expected salary is ₹{salary_str} per annum."
        else:
            msg = f"⚠️ Sorry {name}, you have low chances of placement. All the best!" # type: ignore
            msg2 = "📈 Improve your skills to increase your chances."

        return render_template('output.html', 
                               output=msg, 
                               output2=msg2, 
                               is_placed=(output==1),
                               probability=placed_prob,
                               chart_labels=chart_labels,
                               chart_values=chart_values)
        
    except ValueError as e:
        return render_template('output.html', output="Error", output2="Please enter valid numerical values.")
    except Exception as e:
        return render_template('output.html', output="Error", output2=f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    app.run(debug=True)
