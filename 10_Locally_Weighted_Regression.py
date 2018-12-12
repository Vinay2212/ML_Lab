import numpy as np
import matplotlib.pyplot as plt
X=np.linspace(-3,3,1000)
Y=np.log(np.abs((X**2)-1)+0.5)
X+=np.random.normal(scale=0.05,size=1000)
plt.scatter(X,Y,alpha=0.3)
def local_regression(x0,X,Y,tau):
    x0=np.r_[1,x0]
    X=np.c_[np.ones(len(X)),X]
    xw=X.T *radial_kernal(x0,X,tau)
    beta=np.linalg.pinv(xw@X)@xw@Y
    return x0@beta
def radial_kernal(x0,X,tau):
    return np.exp(np.sum((X-x0)**2,axis=1)/(-2*tau**2))
def plot_lwr(tau):
    domain=np.linspace(-3,3,num=300)
    prediction=[local_regression(x0,X,Y,tau) for x0 in domain]
    plt.scatter(X,Y,alpha=0.3)
    plt.plot(domain,prediction,color="red")
    return plt
plot_lwr(0.04)