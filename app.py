from flask import Flask,request,jsonify
import numpy as np
import pickle


model = pickle.load(open('model.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

@app.route('/predict',methods=['POST'])
def predict():
    
    Acedamic_percentage_in_Operating_Systems = request.form.get('Acedamic_percentage_in_Operating_Systems')
    percentage_in_Algorithms= request.form.get('percentage_in_Algorithms')
    Percentage_in_Programming_Concepts = request.form.get('Percentage_in_Programming_Concepts')
    Percentage_in_Software_Engineering = request.form.get('Percentage_in_Software_Engineering')
 
    Percentage_in_Computer_Networks= request.form.get('Percentage_in_Computer_Networks')
    Logical_quotient_rating = request.form.get('Logical_quotient_rating')
    
    hackathons = request.form.get('hackathons')
    coding_skills_rating = request.form.get('coding_skills_rating')
    self_learning_capability = request.form.get('self_learning_capability')
    memory_capability_score = request.form.get('memory_capability_score')
    Interested_subjects = request.form.get('Interested_subjects')
    interested_career_area = request.form.get('interested_career_area')
    interested_in_games = request.form.get('interested_in_games')
    Interested_Type_of_Books = request.form.get('Interested_Type_of_Books')

    

    input_query = np.array([[Acedamic_percentage_in_Operating_Systems,percentage_in_Algorithms,Percentage_in_Programming_Concepts,Interested_subjects,
                             Percentage_in_Software_Engineering,Percentage_in_Computer_Networks,Logical_quotient_rating,hackathons,coding_skills_rating,
                             self_learning_capability,memory_capability_score,interested_career_area,interested_in_games,Interested_Type_of_Books]])

    result = model.predict(input_query)[0]

    return jsonify({'Suggested_Job_Role':str(result)})

    #result = {'cgpa': cgpa, 'iq':iq, 'profile_score':profile_score}
    #return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)