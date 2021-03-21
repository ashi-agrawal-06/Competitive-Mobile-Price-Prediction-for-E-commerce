import pickle
import xgboost as xgb
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
#model=pickle.load(open())

loaded_model = xgb.Booster()
loaded_model.load_model('mobile_pricing.model')

#with open('preproccesors.pk','rb') as file:
  #pickle.load(preproccesors,file)

file_to_read = open("preproccesors.pk", "rb")

loaded_dictionary = pickle.load(file_to_read)

print(loaded_dictionary)



