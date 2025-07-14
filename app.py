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

@app.route('/predict', methods=['GET'])
def predict():
    # Collect input values
    cgpa = request.args.get('cgpa', '0')
    projects = request.args.get('projects', '0')
    workshops = request.args.get('workshops', '0')
    mini_projects = request.args.get('mini_projects', '0')
    skills = request.args.get('skills', '')
    communication_skills = request.args.get('communication_skills', '0')
    internship = request.args.get('internship', '0')
    hackathon = request.args.get('hackathon', '0')
    tw_percentage = request.args.get('tw_percentage', '0')
    te_percentage = request.args.get('te_percentage', '0')
    backlogs = request.args.get('backlogs', '0')
    name = request.args.get('name', 'Student')

        # Count skills
    skill_count = skills.count(',') + 1 if skills.strip() else 1 # type: ignore

    # Prepare features
    features = np.array([
        cgpa, projects, workshops, mini_projects, # type: ignore
        skill_count, communication_skills, internship, hackathon, # type: ignore
        tw_percentage, te_percentage, backlogs # type: ignore
    ], dtype=float)

    # Predict placement (model returns 1 or 0)
    output = placement_model.predict([features])[0]
    placement_status = str(output)  # "1" or "0"

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
        
    return render_template('output.html', output=msg, output2=msg2)


if __name__ == "__main__":
    app.run(debug=True)
