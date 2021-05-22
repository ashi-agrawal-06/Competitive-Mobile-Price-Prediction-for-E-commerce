from sqlalchemy.orm import sessionmaker
from project_orm import UserInput,Prediction
from sqlalchemy import create_engine
import streamlit as st

import pickle
import xgboost as xgb
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import numpy as np
from datalist import processors,os,camera

engine = create_engine('sqlite:///project_db.sqlite3')
Session = sessionmaker(bind=engine)
sess = Session()

st.title('Competitive Mobile Price Prediction for E-Commerce')

op_sys= st.selectbox('Enter Operating System with version, ex: Android 11',options=os)
proc_brand= st.selectbox('Select a processsor: Qualcomm Snapdragon 730G',options=processors)
#batt_pow_mah=  st.number_input('Battery power in MaH')
batt_pow_mah = st.slider("Battery power in MaH", 22, 9000)
ratings= st.number_input('Rating',min_value=1.0,max_value=5.0,value=3.0)
storage= st.number_input('Inbuilt storage in GB')
cam_feat=st.selectbox('Camera Featires',options=camera)

submit=st.button("Make Prediction")

#models.py 


#model=pickle.load(open())

loaded_model = xgb.Booster()
loaded_model.load_model('mobile_pricing.model')

#with open('preproccesors.pk','rb') as file:
  #pickle.load(preproccesors,file)

file_to_read = open("preproccesors_n.pk", "rb")

loaded_dictionary = pickle.load(file_to_read)

#print(loaded_dictionary)




sc=loaded_dictionary['Scalers']
lab_os=loaded_dictionary['Label_os']
lab_pc=loaded_dictionary['labdel_proc_bran']
lab_cam=loaded_dictionary['ot_cam_features']

#models.py ended

if submit and op_sys and proc_brand and batt_pow_mah and storage:
    #try:
        # entry= UserInput(os=op_sys,
        #                 processor_brand=proc_brand,
        #                 battery_power=batt_pow_mah,
        #                 rating=ratings,
        #                 inbuilt_storage=storage)
        # sess.add(entry)
        # sess.commit()
        
    
        st.success("Successful Input") #data added to database
        #models code here
        os = lab_os.transform([op_sys])
        brand = lab_pc.transform([proc_brand])
        camera= lab_cam.transform([cam_feat])
        X = np.array([batt_pow_mah,ratings])  
        inpX = np.hstack([os,brand,X,camera,])
        inpX = np.hstack([inpX,np.array(storage)])
        iX=sc.transform(inpX.reshape(1,-1))
        #st.write(iX)
        #st.write(iX.shape)
        entry2=xgb.DMatrix(data=iX)
        p=loaded_model.predict(entry2)
        st.write(f" ₹ {int(p[0])}")
    #except Exception as e:
        # st.error(f"Some error occured : {e}")

