import numpy as np 
from keras.datasets import mnist
import matplotlib.pyplot as plt

def sigmoid(z): 
    return 1 / (1+np.exp(-z))
def deriv_sigmoid(z): 
    a = sigmoid(z)*(1-sigmoid(z))
    return a 
def to_column_vector(x):  
    return x.reshape(-1,1)
def load_data(): #load mnist dataset
    (t_X, t_y), (tes_X, tes_y) = mnist.load_data()
    return (t_X, t_y), (tes_X, tes_y)

def training(step):  #function for the training of the model 
    (train_X, train_y), (bin, bin_) = load_data() #store the test in throwaway vars 
    n_training = int(train_X.shape[0]) 
    train_X_flat = train_X.reshape(n_training, 784,1) 
    train_X_flat =train_X_flat / 255   #standardise the value of pixels between 0 and 1

    epochs = 20   #how many epochs of training 
    batch_size = 64 
    cost_list = []

    n_batches = int(n_training/batch_size)
    W,b = load_params()
    p = 0.2 #factor for the degredation of the step size 
    for i in range(epochs): 
        step = (step/ ((i+1)**p))
        train_X_flat, train_y = shuffle_unison(train_X_flat, train_y ) #shuffles the order of training examples 
        c = 0  #counter to keep track of which item in training set we are at 
        for j in range(n_batches):
            batch_cost= 0 

            sum_lambda_w, sum_lambda_b = zeros_params() #set of matrices with dimensions of paramters to update for sum 
            for k in range(batch_size):
                x = train_X_flat[c]
                expected = ans_vec(train_y[c])
                a, z = forward_pass(x,W,b)
                batch_cost += cost(expected, a)

                lambda_w , lambda_b = backprop(expected, a, W, z,)
                for l in range(1,4): #adds the gradient changes for all the parameters
                    sum_lambda_w[l] += lambda_w[l]
                    sum_lambda_b[l] += lambda_b[l]
                c += 1 
            avg_lambda_w = [None]
            avg_lambda_b = [None]
            for n in range(1,4): #averages the sum of the lambdas to reveal the average shift that can then be applied 
                avg_lambda_w.append(sum_lambda_w[n]/batch_size)
                avg_lambda_b.append(sum_lambda_b[n]/batch_size)
            delta_w, delta_b = steps(avg_lambda_w,avg_lambda_b, step)
            param_updates(W,b,delta_w, delta_b)
            cost_list.append(batch_cost/batch_size)
    plt.plot(cost_list)
    plt.xlabel("Batch")
    plt.ylabel("Average cost")
    plt.title("Training cost")
    plt.show()
    save_params(W,b)

    
    save_params(W,b)
    
def training_test():  #function to test the training which allows you to set step size and see the loss graphed 
    (train_X, train_y), (test_X, test_y) = load_data()
    n_training = int(train_X.shape[0])
    train_X_flat = train_X.reshape(n_training, 784,1) 
    train_X_flat =train_X_flat / 255  
    cost_list = []

    epochs = 1
    batch_size = 50 
    s_size = float(input("What would you like the step size to be"))
    n_batches = int(n_training/batch_size)
    W,b = load_params()
    for i in range(epochs): 
        c = 0  #counter to keep track of which item in training set we are at 
        for j in range(n_batches):
            sum_lambda_w, sum_lambda_b = zeros_params() #set of matrices with dimensions of paramters to update for sum 
            batch_cost= 0 
            for k in range(batch_size):
                x = train_X_flat[c]
                expected = ans_vec(train_y[c])
                a, z = forward_pass(x,W,b)
                batch_cost += cost(expected, a)
                lambda_w , lambda_b = backprop(expected, a, W, z,)
                for l in range(1,4):
                    sum_lambda_w[l] += lambda_w[l]
                    sum_lambda_b[l] += lambda_b[l]
                c += 1 
            avg_lambda_w = [None]
            avg_lambda_b = [None]
            for n in range(1,4):
                avg_lambda_w.append(sum_lambda_w[n]/batch_size)
                avg_lambda_b.append(sum_lambda_b[n]/batch_size)
            delta_w, delta_b = steps(avg_lambda_w,avg_lambda_b,s_size)
            param_updates(W,b,delta_w, delta_b)
            cost_list.append(batch_cost/batch_size)
    save_params(W,b)
    plt.plot(cost_list)
    plt.xlabel("Batch")
    plt.ylabel("Average cost")
    plt.title("Training cost")
    plt.show()

def test_set(): #function to test the model on the test data 
    (bin, bin_), (test_X, test_y) = load_data()
    correct = 0 
    wrong_idx = []                #tracks which answers were wrong       
    wrong_pred = []    
    n_test = int(test_X.shape[0])
    test_X_flat = test_X.reshape(n_test, 784,1) 
    test_X_flat =test_X_flat / 255  
    W,b = load_params()
    for i in range(n_test): 
        x = test_X_flat[i]
        a, z = forward_pass(x, W,b,)
        pred = prediction(a[3])
        real = test_y[i]
        if pred == real:
            correct += 1 
        else:                          
            wrong_idx.append(i)
            wrong_pred.append(pred)
    

    perf = (correct / n_test)*100
    return perf 
    print("The model performance was of", perf, "%")
    fig, axes = plt.subplots(3, 3, figsize=(7, 7))
    for ax, i, p in zip(axes.flat, wrong_idx[:9], wrong_pred[:9]):
        ax.imshow(test_X[i], cmap="gray")
        ax.set_title(f"pred {p}, true {test_y[i]}")
        ax.axis("off")
    plt.tight_layout()
    plt.show()

def prediction(ans): #take input of the last layer and return predicted digit
    return np.argmax(ans)




def shuffle_unison(X,Y): 
    perm = np.random.permutation(len(X))
    X_shuffle = X[perm]
    Y_shuffle = Y[perm]
    return X_shuffle, Y_shuffle



def ans_vec(ans): 
    s = 10,1 
    e = np.zeros(s)
    e[ans] = 1 
    return e

def zeros_params(): #sets weights and biases to zero for the sum of gradients in training 
    s= sizes  # each col is the size of the given layer of neurons
    w_z = [None] 
    b_z = [None]
    for i in range(0,3): 
        w_s = s[i+1],s[i]
        w_z.append(np.zeros(w_s, dtype= "float"))
        b_s = s[i+1],1
        b_z.append(np.zeros(b_s, dtype= "float"))
    return w_z, b_z


def check(x, W, b, exp): ##Check function to approximate the gradient with respect to cost and a weight
    w0 = W[2][2,4] ##original weight
    a, z = forward_pass(x, W, b) #where a[0] is the first layer of neurons ie. input layer 
    c = cost(exp, a) #cost for the original weights 
    c = c[0]
    lambda_w , lambda_b= backprop(exp, a, W, z,) #run the back prop to reveal the value of derivatives 
    dc_rand_w0 = lambda_w[2][2,4] #original value for the gradient of a specific weight
    h = 0.00001 #step size
    W[2][2,4] = w0 + h  #update value of the weight before running a forward pass 
    z = [None]
    a0 , z0= forward_pass(x,W,b)
    c0 = cost(exp, a0) #cost with +h
    W[2][2,4] = w0 - h
    z = [None]
    a_ , zh = forward_pass(x,W,b) ##forward pass with -h
    c_ = cost(exp, a_) #cost with -h
    print(c0[0],c_[0],h)
    dc_rand_approx = (c0[0]-c_[0])/(2*h) #approximate dc/dw using the new acquired values with step sizes 
    print(dc_rand_w0, dc_rand_approx)
    W[2][2,4] = w0 #reset the weight value  




def set_params(): #sets random values for weights 
    Weights = [None] # the matrices for the weights are stored in this list where W[0] 
            ##is none and W[1] is the weights between layer 0 and 1 
    bias = [None]
    for i in range(0,3): 
        W_ = np.random.uniform(low = -0.5, high= 0.5, size = (sizes[i+1],sizes[i]))
        Weights.append(W_)
    for j in range(1,4):
        s = sizes[j],1
        b_ = np.zeros(s)
        bias.append(b_)
    for i in range(1,4): 
        np.savetxt(f"weights{i}", Weights[i])
        np.savetxt(f"bias{i}", bias[i])
def load_params(): 
    Weights = [None]
    bias = [None]
    for i in range(1,4):
        Weights.append(np.loadtxt(f"weights{i}", dtype=float ))
        b = np.loadtxt(f"bias{i}", dtype=float )
        bias.append(to_column_vector(b))
    print("Loaded properly")
    return Weights, bias
def save_params(Weights,bias): 
    for i in range(1,4): 
        np.savetxt(f"weights{i}", Weights[i])
        np.savetxt(f"bias{i}", bias[i])



def forward_pass(a0, W,b): #runs a full forward pass outputing all the neurons' values and their respective z
    a = [a0]
    z_ = [None]
    for i in range(1,4):
        z_.append(W[i]@ a[i-1]+b[i])
        a.append(sigmoid(z_[i]))
    return a, z_ 
def cost(exp, a):
    sum = 0
    a3 = a[3]
    for i in range(10):
        sum += (a3[i]-exp[i])**2
    return sum

def backprop(e, a, W, z): #delta refers to the derivative of the cost function with respect to bias
    delta = [None,None,None,None] #initiating the list that will hold the deltas 
    delta[3] = 2*(a[3]-e) * deriv_sigmoid(z[3]) #using formula derived 
    for i in range(1,3):
        j = 3 - i 
        delta[j]= (((W[j+1]).transpose()) @ delta[j+1]) * deriv_sigmoid(z[j])
    lam_w =  [None,None,None,None]
    for i in range(1,4): 
        lam_w[i] = np.outer(delta[i], (a[i-1].transpose()))
    lam_b = delta
    return lam_w, lam_b 

def steps(lam_w,lam_b, h):  #by how much each weight will shift 
    step = h 
    delt_w = [None] 
    delt_b = [None]
    for i in range(1,4):
        delt_w.append(lam_w[i]*step)
        delt_b.append(lam_b[i]*step)
    return delt_w, delt_b
def param_updates(W,b,delta_w,delta_b): #move each weight 
    for i in range(1,4):
        W[i] = W[i]-delta_w[i]
        b[i] = b[i]-delta_b[i]

def main():
    # if input("Would you like to randomly set params? y/n  ")== "y": 
    #      set_params()
    score = []
    steps_sizes = [0.2]
    for i in steps_sizes:
        set_params()
        training(i)
        score.append(test_set())
    print(score)
    # plt.plot(steps_sizes, score)
    # plt.xlabel("Step size")
    # plt.ylabel("Score")
    # plt.title("Best step size")
    # plt.show()
    # test_set()

    # training()

    # test_set()


sizes= [784,16,16,10]  # each col is the size of the given layer of neurons
if __name__ == "__main__":
    main()



