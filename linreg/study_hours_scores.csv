import numpy as np 
import csv 
##going to try to build a linear regression model using similar ideas to ANN 
class LinearReg:
    def __init__(self, x, y, m = 1, c = 0):
        self.x = x
        self.y = y
        self.m  =m
        self.c = c

    def grad_descent(self, b, s):
        for batch in range(b):
            delta_m = 0 
            delta_c = 0 
            for j in range(30): 
                delta_m += 2*self.m*(self.x[j])**2 + 2*(self.c-self.y[j])*self.x[j] ##Derivative of the cost in terms of m (gradient)
                delta_c += 2*(self.m*self.x[j]+self.c-self.y[j]) ##Derivative of the cost in terms of c (y-intercept)
            delta_c_avg = delta_c / 30  ##the average derivative for all 30 points to give the necessary step direction
            delta_m_avg = delta_m / 30 
            shift_m = s * delta_m_avg
            shift_c= s * delta_c_avg
            self.m -= shift_m  ##negative of the shift, essentially gradient descent 
            self.c -= shift_c


def main():        
    x = []  # hours studied
    y = []  # exam score

    with open("study_hours_scores.csv", newline="") as f:
        reader = csv.reader(f)
        next(reader)  # skip the header row
        for row in reader:
            x.append(float(row[0]))
            y.append(float(row[1]))

    lin = LinearReg(x,y)
    batch_n = 10000
    step_size = 0.0159
    lin.grad_descent(batch_n, step_size)
    print(f"The Equation of the line is y= {lin.m}x + {lin.c}")

main()




