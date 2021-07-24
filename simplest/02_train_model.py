import sys
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data_npz = np.load(sys.argv[1])

train_X, test_X, train_y, test_y = train_test_split(
    data_npz["data"], data_npz["labels"], test_size=0.3, stratify=data_npz["labels"]
)

model = RandomForestClassifier().fit(train_X, train_y)
test_preds = model.predict(test_X)

np.savez("model_results.npz", preds=test_preds, trues=test_y)
