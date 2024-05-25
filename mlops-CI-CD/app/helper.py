import pickle
import sys, os


class Naive_Bayes():
    def __init__(self):
        self.gnb = None
        self.labelencode = None
        self.scaler = None

        # with open('model/gnb.pkl' , 'rb') as f:
        #     self.gnb = pickle.load(f)
        # with open('model/labelencoder.pkl' , 'rb') as f:
        #     self.labelencode = pickle.load(f)
        # with open('model/scaler.pkl' , 'rb') as f:
        #     self.scaler = pickle.load(f)

    def prediction(self, data):
        # test = self.scaler.transform(data)
        # out = self.gnb.predict(test)
        # out = self.labelencode.inverse_transform(out)
        # return out.tolist()
        return [0.1,0.0,1.0]