import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, roc_curve, auc

# Example model training results (replace with your actual model outputs)
epochs = list(range(1, 21))
train_acc = [0.75, 0.80, 0.83, 0.85, 0.87, 0.88, 0.89, 0.90, 0.91, 0.91,
             0.92, 0.93, 0.93, 0.94, 0.95, 0.95, 0.96, 0.96, 0.96, 0.97]
val_acc =   [0.70, 0.75, 0.78, 0.80, 0.81, 0.83, 0.84, 0.85, 0.85, 0.86,
             0.86, 0.87, 0.88, 0.88, 0.89, 0.89, 0.90, 0.90, 0.91, 0.91]

# 1. Line Chart: Training vs Validation Accuracy
plt.figure(figsize=(10, 5))
plt.plot(epochs, train_acc, marker='o', label='Training Accuracy')
plt.plot(epochs, val_acc, marker='x', label='Validation Accuracy')
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.title("Model Accuracy over Epochs (Skin Cancer Detection)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# 2. Confusion Matrix Heatmap (Binary classification: 0 = Benign, 1 = Malignant)
y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 1]
y_pred = [1, 0, 1, 0, 0, 1, 1, 0, 1, 1]

cm = confusion_matrix(y_true, y_pred)
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Purples',
            xticklabels=['Benign', 'Malignant'],
            yticklabels=['Benign', 'Malignant'])
plt.title('Confusion Matrix - Skin Cancer Detection')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.tight_layout()
plt.show()


# 3. Pie Chart: Class Distribution in Dataset
labels = ['Benign', 'Malignant']
sizes = [400, 100]  # Replace with your actual counts
colors = ['#8dd3c7', '#fb8072']
explode = (0, 0.1)  # Slightly explode the second slice (Malignant)

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140,
        colors=colors, explode=explode, shadow=True)
plt.title("Class Distribution in Dataset")
plt.axis('equal')
plt.tight_layout()
plt.show()


# 4. ROC Curve (binary classification)
y_true_roc = [0, 0, 1, 1]
y_scores = [0.1, 0.4, 0.35, 0.8]  # Example model probabilities for class 1

fpr, tpr, _ = roc_curve(y_true_roc, y_scores)
roc_auc = auc(fpr, tpr)

plt.figure(figsize=(6, 5))
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (AUC = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([-0.01, 1.01])
plt.ylim([-0.01, 1.01])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC Curve)')
plt.legend(loc="lower right")
plt.tight_layout()
plt.show()
