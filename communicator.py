from serial import Serial
import numpy as np
class Communicator:
    def __init__(self,enc_com):
        self.ser=Serial(mec_com,9600)
       	self.raw_da=np.zero(4)
    
    def __get_All(self):
       for ID in range(4):
            return self.raw_da

    def fresh_data(self):
       return self.__get_All() 
