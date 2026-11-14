import numpy as np
from keras.datasets import mnist
import matplotlib.pyplot as plt
##Naming convention used for the project: 
# W[1] = Matrice of weights between layer 0 and 1 


class NeuralNetwork: 
    def __init__(self, sizes = [784, 16, 16, 10] ):
        self.sizes = sizes 
        self.L  = len(sizes) - 1  ##number of layers of neurons
        self.W = None  ##weights and biases will be stored in this list when they exist 
        self.b = None 


    ##All functions used for reshaping, maths, or shuffling 
    @staticmethod
    def sigmoid(z):
        return 1 / (1+np.exp(-z))
    
    @staticmethod 
    def deriv_sigmoid(z): 
        a = NeuralNetwork.sigmoid(z)*(1-NeuralNetwork.sigmoid(z))
        return a 
    @staticmethod
    def to_column_vector(x):  
        return x.reshape(-1,1)
    
    @staticmethod
    def prediction(ans): #take input of the last layer and return predicted digit
        return np.argmax(ans)
    
    @staticmethod
    def shuffle_unison(X,Y):  ##Shuffle the order of the data, making sure that labels and image stay together 
        perm = np.random.permutation(len(X))
        X_shuffle = X[perm]
        Y_shuffle = Y[perm]
        return X_shuffle, Y_shuffle


    def ans_vec(self, ans):  ##creates a vector for the answer (for cost) 
        s = 10,1 
        e = np.zeros(s)
        e[ans] = 1 
        return e

    ##Data functions 
    @staticmethod
    def load_data(): #load mnist dataset
        (t_X, t_y), (tes_X, tes_y) = mnist.load_data() ##training and test data loaded in 
        return (t_X, t_y), (tes_X, tes_y)

    def flatten(self, X): ##Turns all image inputs into flat vectors 
                            #With pixel values 0-->1 (standardised )
        n = int(X.shape[0])
        X_flat = X.reshape(n, self.sizes[0],1)
        X_flat = X_flat / 255 ##standardises pixel values 
        return X_flat 

    ##Parameter functions 
    def set_params(self): #sets random values for weights 
        Weights = [None] # the matrices for the weights are stored in this list where W[0] 
                ##is none and W[1] is the weights between layer 0 and 1 
        bias = [None]
        for i in range(0,self.L): 
            W_ = np.random.uniform(low = -0.5, high= 0.5, size = (self.sizes[i+1],self.sizes[i]))
            Weights.append(W_)
        for j in range(1,self.L + 1):
            s = self.sizes[j],1
            b_ = np.zeros(s)
            bias.append(b_)
        self.W, self.b = Weights, bias 
        self.save_params()
    def load_params(self):
        Weights = [None]
        bias = [None]
        for i in range(1,self.L +1):
            Weights.append(np.loadtxt(f"weights{i}", dtype=float ))
            b = np.loadtxt(f"bias{i}", dtype=float )
            bias.append(self.to_column_vector(b))
        print("Loaded properly")
        self.W, self.b = Weights, bias  
    def save_params(self): 
        for i in range(1, self.L +1):
            np.savetxt(f"weights{i}", self.W[i])
            np.savetxt(f"bias{i}", self.b[i])

    def zeros_params(self): #sets weights and biases to zero for the sum of gradients in training
        s= self.sizes  # each col is the size of the given layer of neurons
        w_z = [None]
        b_z = [None]
        for i in range(0,self.L):
            w_s = s[i+1],s[i]
            w_z.append(np.zeros(w_s, dtype= "float"))
            b_s = s[i+1],1
            b_z.append(np.zeros(b_s, dtype= "float"))
        return w_z, b_z

    
    ##Network functions

    def forward_pass(self, a0): #runs a full forward pass outputing all the neurons' values and their respective z
        a = [a0]
        z_ = [None]
        for i in range(1,self.L +1):
            z_.append(self.W[i]@ a[i-1]+self.b[i])
            a.append(self.sigmoid(z_[i]))
        return a, z_
    
    def cost(self, exp,  a):
        sum = 0
        a3 = a[self.L]
        for i in range(10):
            sum += (a3[i]-exp[i])**2
        return sum

    def backprop(self, e, a, z): #delta refers to the derivative of the cost function with respect to bias
        L  = self.L 
        delta = [None] * (L+1) #initiating the list that will hold the deltas 
        delta[L] = 2*(a[L]-e) * self.deriv_sigmoid(z[L]) #using formula derived 
        for i in range(1,L):
            j = L - i 
            delta[j]= (((self.W[j+1]).transpose()) @ delta[j+1]) * self.deriv_sigmoid(z[j])
        lam_w =  [None,None,None,None]
        for i in range(1,L+1): 
            lam_w[i] = np.outer(delta[i], (a[i-1].transpose()))
        lam_b = delta
        return lam_w, lam_b
     

    def steps(self, lam_w,lam_b, h):  #by how much each weight will shift 
        step = h 
        delt_w = [None] 
        delt_b = [None]
        for i in range(1,4):
            delt_w.append(lam_w[i]*step)
            delt_b.append(lam_b[i]*step)
        return delt_w, delt_b

    def param_updates(self, delta_w,delta_b): #move each weight
        for i in range(1,self.L+1):
            self.W[i] = self.W[i]-delta_w[i]
            self.b[i] = self.b[i]-delta_b[i]

    ##Training functions 
  #train_batch runs ONE mini batch of training and updates the weights and biases once.
    #It holds the batch loop that training() and training_test() both used to have copied out,
    #so any change to how a batch works only has to be made here.
    #Steps:
    #  1. set the sums of the gradients to zero (zeros_params)
    #  2. for each of the batch_size examples starting at item c: forward pass, add the cost,
    #     backprop and add the gradients to the sums
    #  3. divide the sums by batch_size to get the average gradient for the batch
    #  4. scale the average gradient by the step size (steps) and move the parameters (param_updates)
    #Inputs: X = flattened images, Y = labels, c = index of the first example of this batch,
    #        batch_size = number of examples in the batch, step = the step size (learning rate)
    #Returns the new c (so the next batch starts where this one ended) and the average cost of the batch for the graph
    def train_batch(self, X, Y, c, batch_size, step):
        batch_cost= 0
        sum_lambda_w, sum_lambda_b = self.zeros_params() #set of matrices with dimensions of paramters to update for sum
        for k in range(batch_size):
            x = X[c]
            expected = self.ans_vec(Y[c])
            a, z = self.forward_pass(x)
            batch_cost += self.cost(expected, a)
            lambda_w , lambda_b = self.backprop(expected, a, z)
            for l in range(1,self.L+1): #adds the gradient changes for all the parameters
                sum_lambda_w[l] += lambda_w[l]
                sum_lambda_b[l] += lambda_b[l]
            c += 1
        avg_lambda_w = [None]
        avg_lambda_b = [None]
        for n in range(1,self.L+1): #averages the sum of the lambdas to reveal the average shift that can then be applied
            avg_lambda_w.append(sum_lambda_w[n]/batch_size)
            avg_lambda_b.append(sum_lambda_b[n]/batch_size)
        delta_w, delta_b = self.steps(avg_lambda_w,avg_lambda_b, step)
        self.param_updates(delta_w, delta_b)
        return c, batch_cost/batch_size

    ##Function for plotting the cost against batch number 
    @staticmethod
    def plot_cost(cost_list):
        plt.plot(cost_list)
        plt.xlabel("Batch")
        plt.ylabel("Average cost")
        plt.title("Training cost")
        plt.show()

    
    def training(self, step, epochs=20, batch_size=64, p=0.2):  #function for the training of the model
        (train_X, train_y), (bin, bin_) = self.load_data() #store the test in throwaway vars
        train_X_flat = self.flatten(train_X)
        n_training = int(train_X.shape[0])
        cost_list = []

        n_batches = int(n_training/batch_size)
        self.load_params()
        # p is the factor for the degredation of the step size
        for i in range(epochs):
            ##step = (step/ ((i+1)**p))
            train_X_flat, train_y = self.shuffle_unison(train_X_flat, train_y ) #shuffles the order of training examples
            c = 0  #counter to keep track of which item in training set we are at
            for j in range(n_batches):
                c, avg_cost = self.train_batch(train_X_flat, train_y, c, batch_size, step)
                cost_list.append(avg_cost)
        ##self.plot_cost(cost_list)
        self.save_params()
            


    def training_test(self, epochs=1, batch_size=50):  #function to test the training which allows you to set step size and see the loss graphed
        (train_X, train_y), (test_X, test_y) = self.load_data()
        train_X_flat = self.flatten(train_X)
        n_training = int(train_X.shape[0])
        cost_list = []

        s_size = float(input("What would you like the step size to be"))
        n_batches = int(n_training/batch_size)
        self.load_params()
        for i in range(epochs):
            c = 0  #counter to keep track of which item in training set we are at
            for j in range(n_batches):
                c, avg_cost = self.train_batch(train_X_flat, train_y, c, batch_size, s_size)
                cost_list.append(avg_cost)
        self.save_params()
        self.plot_cost(cost_list)

    # Testing functions -- potentially to incldude in a seperate file
    def test_set(self, show_wrong=False): #function to test the model on the test data
        (bin, bin_), (test_X, test_y) = self.load_data()
        correct = 0
        wrong_idx = []                #tracks which answers were wrong
        wrong_pred = []
        n_test = int(test_X.shape[0])
        test_X_flat = self.flatten(test_X)
        self.load_params()
        for i in range(n_test):
            x = test_X_flat[i]
            a, z = self.forward_pass(x)
            pred = self.prediction(a[self.L])
            real = test_y[i]
            if pred == real:
                correct += 1
            else:
                wrong_idx.append(i)
                wrong_pred.append(pred)

        perf = (correct / n_test)*100
        print("The model performance was of", perf, "%")

        return perf

    def check(self, x, exp): ##Check function to approximate the gradient with respect to cost and a weight
        W = self.W
        w0 = W[2][2,4] ##original weight
        a, z = self.forward_pass(x) #where a[0] is the first layer of neurons ie. input layer
        c = self.cost(exp, a) #cost for the original weights
        c = c[0]
        lambda_w , lambda_b= self.backprop(exp, a, z) #run the back prop to reveal the value of derivatives
        dc_rand_w0 = lambda_w[2][2,4] #original value for the gradient of a specific weight
        h = 0.00001 #step size
        W[2][2,4] = w0 + h  #update value of the weight before running a forward pass
        a0 , z0= self.forward_pass(x)
        c0 = self.cost(exp, a0) #cost with +h
        W[2][2,4] = w0 - h
        a_ , zh = self.forward_pass(x) ##forward pass with -h
        c_ = self.cost(exp, a_) #cost with -h
        print(c0[0],c_[0],h)
        dc_rand_approx = (c0[0]-c_[0])/(2*h) #approximate dc/dw using the new acquired values with step sizes
        print(dc_rand_w0, dc_rand_approx)
        W[2][2,4] = w0 #reset the weight value


def main():

    net = NeuralNetwork([784,16,16,10])
    if input("Would you like to randomly set params? y/n  ")== "y":
        net.set_params()
    else: 
        try: 
            net.load_params()
        except: 
            raise(ValueError)
    score = []
    steps_sizes = [0.2, 0.5, 1, 1.5]
    for i in steps_sizes:
        net.set_params()
        net.training(i)
        score.append(net.test_set())
    print(score)
    # plt.plot(steps_sizes, score)
    # plt.xlabel("Step size")
    # plt.ylabel("Score")
    # plt.title("Best step size")
    # plt.show()


if __name__ == "__main__":
    main()