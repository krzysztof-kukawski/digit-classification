import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

mnist = fetch_openml('mnist_784', as_frame= False)

pictures, labels = mnist.data, mnist.target

x_train, x_test, y_train, y_test = train_test_split(pictures,labels)
def plot_digit(image_data):
    image = image_data.reshape(28,28,1)
    plt.imshow(image, cmap='binary')
    plt.axis('off')

plot_digit(pictures[9])
pictures.shape
svm_clf = SVC()
y_train.shape
x_train.shape
svm_clf.fit(x_train,y_train)