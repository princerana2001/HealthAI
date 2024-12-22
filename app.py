import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# Get the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# Load the saved models
diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('HEALTH AI',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')

    diab_diagnosis = ''
    precautions = ''
    if st.button('Diabetes Test Result'):
        try:
            # Convert inputs to float and validate ranges
            user_input = [
                float(Pregnancies), float(Glucose), float(BloodPressure),
                float(SkinThickness), float(Insulin), float(BMI),
                float(DiabetesPedigreeFunction), float(Age)
            ]
            if not (0 <= user_input[0] <= 20):
                st.warning("Number of Pregnancies must be between 0 and 20.")
            elif not (0 <= user_input[1] <= 300):
                st.warning("Glucose Level must be between 0 and 300.")
            elif not (0 <= user_input[2] <= 200):
                st.warning("Blood Pressure must be between 0 and 200.")
            elif not (0 <= user_input[3] <= 99):
                st.warning("Skin Thickness must be between 0 and 99.")
            elif not (0 <= user_input[4] <= 900):
                st.warning("Insulin Level must be between 0 and 900.")
            elif not (0 <= user_input[5] <= 80):
                st.warning("BMI must be between 0 and 80.")
            elif not (0 <= user_input[6] <= 2.5):
                st.warning("Diabetes Pedigree Function must be between 0 and 2.5.")
            elif not (0 <= user_input[7] <= 120):
                st.warning("Age must be between 0 and 120.")
            else:
                diab_prediction = diabetes_model.predict([user_input])
                diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'

                # Provide additional information based on prediction
                if diab_prediction[0] == 1:
                    precautions = '''
                    **Precautions:**
                     - Follow a healthy and balanced diet, focusing on whole grains, vegetables, lean proteins, and healthy fats.
                    - Engage in regular physical activity, such as walking, swimming, or strength training, for at least 30 minutes a day.
                    - Monitor blood sugar levels regularly to ensure they remain within the target range.
                    - Stay hydrated by drinking plenty of water throughout the day.
                    - Maintain a healthy weight to reduce the risk of complications.
                    - Get adequate sleep, as poor sleep can impact blood sugar regulation.
                    - Consult with a healthcare provider regularly to adjust your treatment plan as needed.
                    - Manage stress through relaxation techniques like meditation or yoga, as stress can elevate blood sugar levels.
                    - Limit alcohol intake and avoid smoking, as both can interfere with diabetes management.
                    - Be aware of the signs of high or low blood sugar (e.g., dizziness, fatigue, shaking) and know how to respond.
                    - Consider joining a support group to stay motivated and share experiences with others managing diabetes.
                 '''

                else:
                    precautions = '''
                    "Maintain this healthy life and stay active!"
                    '''
                st.success(diab_diagnosis)
                st.markdown(precautions, unsafe_allow_html=True)
        except ValueError:
            st.warning("Please enter valid numeric values.")

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex (0 = Female, 1 = Male)')
    with col3:
        cp = st.text_input('Chest Pain types (0 to 3)')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholesterol in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (0 = No, 1 = Yes)')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results (0 to 2)')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina (0 = No, 1 = Yes)')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment (0 to 2)')
    with col3:
        ca = st.text_input('Major vessels colored by fluoroscopy (0 to 4)')
    with col1:
        thal = st.text_input('Thal (0 = Normal, 1 = Fixed defect, 2 = Reversible defect)')

    heart_diagnosis = ''
    precautions = ''
    if st.button('Heart Disease Test Result'):
        try:
            # Convert inputs to float and validate ranges
            user_input = [
                float(age), float(sex), float(cp), float(trestbps),
                float(chol), float(fbs), float(restecg), float(thalach),
                float(exang), float(oldpeak), float(slope), float(ca), float(thal)
            ]
            if not (0 <= user_input[0] <= 120):
                st.warning("Age must be between 0 and 120.")
            elif not (0 <= user_input[1] <= 1):
                st.warning("Sex must be 0 or 1.")
            elif not (0 <= user_input[2] <= 3):
                st.warning("Chest Pain types must be between 0 and 3.")
            elif not (0 <= user_input[3] <= 200):
                st.warning("Resting Blood Pressure must be between 0 and 200.")
            elif not (0 <= user_input[4] <= 600):
                st.warning("Serum Cholesterol must be between 0 and 600.")
            elif not (0 <= user_input[5] <= 1):
                st.warning("Fasting Blood Sugar must be 0 or 1.")
            elif not (0 <= user_input[6] <= 2):
                st.warning("Resting ECG results must be between 0 and 2.")
            elif not (0 <= user_input[7] <= 220):
                st.warning("Maximum Heart Rate must be between 0 and 220.")
            elif not (0 <= user_input[8] <= 1):
                st.warning("Exercise Induced Angina must be 0 or 1.")
            elif not (0 <= user_input[9] <= 6.0):
                st.warning("ST Depression must be between 0 and 6.0.")
            elif not (0 <= user_input[10] <= 2):
                st.warning("Slope must be between 0 and 2.")
            elif not (0 <= user_input[11] <= 4):
                st.warning("Major Vessels must be between 0 and 4.")
            elif not (0 <= user_input[12] <= 2):
                st.warning("Thal must be between 0 and 2.")
            else:
                heart_prediction = heart_disease_model.predict([user_input])
                heart_diagnosis = 'The person is having heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease'

                # Provide additional information based on prediction
                if heart_prediction[0] == 1:
                   precautions = '''
                      **Precautions:**
                    - Monitor your cholesterol and blood pressure regularly to keep them within healthy ranges.
                     - Follow a heart-healthy diet, rich in fruits, vegetables, whole grains, lean proteins, and healthy fats (e.g., olive oil, avocados, nuts).
                    - Engage in regular physical activity, aiming for at least 150 minutes of moderate exercise or 75 minutes of vigorous exercise per week.
                    - Avoid smoking and excessive alcohol consumption, as both can increase the risk of heart disease.
                    - Maintain a healthy weight to reduce strain on the heart.
                    - Manage stress through relaxation techniques such as meditation, deep breathing, or yoga.
                    - Ensure adequate sleep each night, as poor sleep can impact heart health.
                    - Stay hydrated, and aim for 6-8 glasses of water a day.
                    - Reduce your intake of processed foods, trans fats, and added sugars.
                    - Regularly check your blood sugar levels if you have diabetes, as it can increase heart disease risk.
                    - Consult with a healthcare provider regularly for personalized treatment and prevention strategies.
                    - Limit your salt intake to help manage blood pressure and reduce fluid retention.
                    '''

                else:
                    precautions = '''
                    "Keep up the good work in maintaining heart health!"
                    '''
                st.success(heart_diagnosis)
                st.markdown(precautions, unsafe_allow_html=True)
        except ValueError:
            st.warning("Please enter valid numeric values.")

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col1:
        RAP = st.text_input('MDVP:RAP')
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
    with col3:
        DDP = st.text_input('MDVP:DDP')
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col1:
        APQ3 = st.text_input('MDVP:APQ3')
    with col2:
        APQ5 = st.text_input('MDVP:APQ5')
    with col3:
        APQ = st.text_input('MDVP:APQ')
    with col4:
        DDA = st.text_input('Shimmer:DDA')
    with col5:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('spread1')
    with col5:
        spread2 = st.text_input('spread2')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')

    parkinsons_diagnosis = ''
    precautions = ''
    if st.button("Parkinson's Test Result"):
        try:
            # Convert inputs to float
            user_input = [
                float(fo), float(fhi), float(flo), float(Jitter_percent), float(Jitter_Abs),
                float(RAP), float(PPQ), float(DDP), float(Shimmer), float(Shimmer_dB),
                float(APQ3), float(APQ5), float(APQ), float(DDA), float(NHR), float(HNR),
                float(RPDE), float(DFA), float(spread1), float(spread2), float(D2), float(PPE)
            ]

            if any(x < 0 or x > 1000 for x in user_input):  # Example range for input values
                st.warning("Please enter values within a reasonable range (0-1000).")
            else:
                parkinsons_prediction = parkinsons_model.predict([user_input])
                parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
                if parkinsons_prediction[0] == 1:
                    precautions = '''
                     **Precautions:**
                     - Follow your doctor’s advice for medication and therapy, including speech and physical therapy, as recommended.
                     - Stay physically and mentally active by engaging in exercises that promote flexibility, strength, and balance.
                     - Maintain a healthy diet, focusing on antioxidant-rich foods, fiber, and healthy fats to support brain health.
                     - Stay hydrated and avoid dehydration, as it can worsen symptoms.
                      - Get adequate rest and avoid sleep disturbances to support brain function.
                     - Establish a regular daily routine to reduce stress and improve motor control.
                    - Join support groups or connect with others who have Parkinson’s to share experiences and coping strategies.
                    - Avoid falls by ensuring your living space is clear of obstacles and using assistive devices if needed.
                     - Manage stress through relaxation techniques like meditation, yoga, or mindfulness.
                    - Stay up-to-date with regular check-ups and adjust treatments as needed to manage symptoms.
                     - Limit caffeine intake as it can sometimes interfere with Parkinson’s medication.
                    - Stay positive and engaged with hobbies, social activities, and interests to boost mental well-being.
                    '''

                else:
                   precautions = '''
                "Maintain your healthy lifestyle and keep active!"
                '''
                st.success(parkinsons_diagnosis)
                st.markdown(precautions, unsafe_allow_html=True)
        except ValueError:
            st.warning("Please enter valid numeric values.")
