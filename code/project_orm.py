import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base= declarative_base()

class UserInput(Base):
    __tablename__="userinputs"

    id= Column(Integer, primary_key= True)

    os=Column(String)
    processor_brand=Column(String)
    battery_power=Column(Float)
    rating=Column(Float)
    inbuilt_storage=Column(Float)
    other_cam_features=Column(String)

class Prediction(Base):
    __tablename__= 'predictions'
    id= Column(Integer, primary_key= True)
    result= Column(Integer)
    input_id =Column(Integer, ForeignKey('userinputs.id'))


if __name__== "__main__":
    engine = create_engine('sqlite:///project_db.sqlite3')
    Base.metadata.create_all(engine)




