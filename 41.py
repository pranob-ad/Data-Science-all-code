import matplotlib.pyplot as plt

# Enable sketch-style drawing
from matplotlib import rcParams
rcParams['path.sketch'] = (1, 100, 2)  # (scale, length of the wiggle, randomness)

epochs = [1, 2, 3, 4, 5]
training_accuracy = [0.6, 0.72, 0.80, 0.85, 0.88]
validation_accuracy = [0.58, 0.70, 0.78, 0.82, 0.84]

plt.plot(epochs, training_accuracy, marker='o',linestyle='-', label='Training Accuracy')
plt.plot(epochs, validation_accuracy, marker='s',linestyle='--', label='Validation Accuracy')
plt.plot(training_accuracy, validation_accuracy,linestyle='-', marker='s', label=' Accuracy')
plt.title('Model Accuracy Over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.grid(True)
plt.show()