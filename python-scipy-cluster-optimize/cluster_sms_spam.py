"""
Clustering example using an SMS spam dataset with SciPy.

Associated with the Real Python article
Scientific Python: Using SciPy for Optimization
Available at: https://realpython.com/python-scipy-cluster-optimize/
"""
from pathlib import Path
import numpy as np
from scipy.cluster.vq import whiten, kmeans, vq

HERE = Path(__file__).parent

data = HERE.joinpath("SMSSpamCollection").read_text().strip().split("\n")

digit_counts = np.empty((len(data), 2), dtype=int)
for i, line in enumerate(data):
    case, message = line.split("\t")
    num_digits = sum(c.isdigit() for c in message)
    digit_counts[i, 0] = 0 if case == "ham" else 1
    digit_counts[i, 1] = num_digits

unique_counts = np.unique(digit_counts[:, 1], return_counts=True)
unique_counts = np.transpose(np.vstack(unique_counts))

whitened_counts = whiten(unique_counts)
codebook, _ = kmeans(whitened_counts, 3)
codes, _ = vq(whitened_counts, codebook)

ham_code = codes[0]
spam_code = codes[-1]
unknown_code = list(set(range(3)) ^ set((ham_code, spam_code)))[0]

print("definitely ham:", unique_counts[codes == ham_code][-1])
print("definitely spam:", unique_counts[codes == spam_code][-1])
print("unknown:", unique_counts[codes == unknown_code][-1])

digits = digit_counts[:, 1]
predicted_hams = digits == 0
predicted_spams = digits > 20
predicted_unknowns = np.logical_and(digits > 0, digits <= 20)

ham_cluster = digit_counts[predicted_hams]
spam_cluster = digit_counts[predicted_spams]
unknown_cluster = digit_counts[predicted_unknowns]

print("hams:", np.unique(ham_cluster[:, 0], return_counts=True))
print("spams:", np.unique(spam_cluster[:, 0], return_counts=True))
print("unknowns:", np.unique(unknown_cluster[:, 0], return_counts=True))
