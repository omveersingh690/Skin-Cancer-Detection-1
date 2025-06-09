import matplotlib.pyplot as plt

epochs = list(range(1, 21))
train_acc = [0.75, 0.80, 0.83, 0.85, 0.87, 0.88, 0.89, 0.90, 0.91, 0.91, 0.92, 0.93, 0.93, 0.94, 0.95, 0.95, 0.96, 0.96, 0.96, 0.97]
val_acc =   [0.70, 0.75, 0.78, 0.80, 0.81, 0.83, 0.84, 0.85, 0.85, 0.86, 0.86, 0.87, 0.88, 0.88, 0.89, 0.89, 0.90, 0.90, 0.91, 0.91]

plt.plot(epochs, train_acc, label='Training Accuracy')
plt.plot(epochs, val_acc, label='Validation Accuracy')
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.title("Model Accuracy over Epochs")
plt.legend()
plt.grid(True)
plt.show()
