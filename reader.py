from sklearn.datasets import fetch_openml
import matplotlib.pyplot as plt
from keras.api.models import Sequential
from keras.api.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from sklearn.model_selection import train_test_split
mnist = fetch_openml('mnist_784', as_frame= False)

pictures, labels = mnist.data, mnist.target

x_test, y_test, x_train, y_train = train_test_split(pictures,labels)
def plot_digit(image_data):
    image = image_data.reshape(28,28,1)
    plt.imshow(image, cmap='binary')
    plt.axis('off')

plot_digit(pictures[9])    


model = Sequential()

model.add(Conv2D(32, (1), activation='relu', input_shape=(28,28,1)))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(64, (1), activation='relu'))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(64, (1), activation='relu'))

model.add(Flatten())

model.add(Dense(64, activation='relu'))

model.add(Dropout(0.5))

model.add(Dense(10, activation='softmax'))
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(x_train, x_test, epochs=20, batch_size=64, validation_split=0.2)

test_loss, test_accuracy = model.evaluate(x_test, y_test)
print(f"Test Loss: {test_loss:.4f}")
print(f"Test Accuracy: {test_accuracy:.4f}")