import sys
from matplotlib.pyplot import plot
import numpy as np
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

npz_data = np.load(sys.argv[1])

preds, trues = npz_data["preds"], npz_data["trues"]

conf_mat = confusion_matrix(trues, preds)
disp = ConfusionMatrixDisplay(conf_mat, display_labels=["0", "1", "2"])
disp = disp.plot(cmap="Blues")
plt.savefig("Confusion_matrix.png")