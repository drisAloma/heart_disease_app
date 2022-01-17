def welcome():
   return 'Welcome All'
   
def  heart_disease_diagnosis(Age,Sex,CP,Trestbps,Chol,Fbs,Restecg,Thalach,Exang,CA,Thal):
   prediction=classifier.predict([[Age,Sex,CP,Trestbps,Chol,Fbs,Restecg,Thalach,Exang,CA,Thal]])
   #print(prediction)
   return prediction

def main():
   st.title('Heart_disease_diagnose')
   html_temp='''
   <div style='background-color:tomato; padding:10px'>
   <H2 style='color:white;text-align: center;'>Streamlit Heart_Disease_Diagnosis App</h2>
   </div>
   '''
   st.markdown(html_temp,unsafe_allow_html=True)
   Age= st.text_input('Age','Type Here')
   Sex=st.text_input('Sex','Type Here')
   CP=st.text_input('CP','Type Here')
   Trestbps=st.text_input('Trestbps','Type Here')
   Chol=st.text_input('Chol','Type Here')
   Fbs=st.text_input('Fbs','Type Here')
   Restecg=st.text_input('Restecg','Type Here')
   Thalach=st.text_input('Thalach','Type Here')
   Exang=st.text_input('Exang','Type Here')
   CA=st.text_input('CA','Type Here')
   Thal=st.text_input('Thal','Type Here')
   result=''
   if st.button('Predict'):
       result=heart_disease_diagnosis(Age,Sex,CP,Trestbps,Chol,Fbs,Restecg,Thalach,Exang,CA,Thal)
   st.success('The output is {}'.format(result))
   
if __name__=='__main__':
   main()
