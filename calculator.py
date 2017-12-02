import communicator
import numpy as np
'''
wheelID:
		 Forward
	 	----------
		|2      1|
	        |        |
		|        |
		|3      4|
		----------
'''
class Car:
        l=500/2
        w=700/2
        r=40
        a=np.tan(45*np.pi/180.0)
	b=1/(w+l/a)
       

class Position:
    def __init__(self,x0,y0,dir):
        self.x_st=x0
        self.y_st=y0
        self.vec_dir=np.array(deg2vec(dir))
        self.vec_v=np.zeros(3)#include angle_v
        #self.vec_av=0  #clockwise:-,counterclock:+
        self.car=Car()
        self.mat_mul=np.mat([[-car.a,car.a,-car.a,car.a,],[1,1,1,1],[car.b,-car.b,-car.b,car.b]])

    def get_para(self):
        self.whe_av=np.mat(communicator.freshdata)
        self.vec_v

    def deg2vec(self,deg):
        return np.cos(np.pi*deg/180.0),np.sin(np.pi*deg/180.0)

pos=Position(0,0,90)

'''
class Calculator:
    def __init__(self):
        self.
'''
