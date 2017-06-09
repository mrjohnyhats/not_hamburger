from nn import Nn
import os

predictor = Nn()

predictions = []
burgers = ['./test_burgers/'+b for b in os.listdir('./test_burgers')]
for b in burgers:
    predictions.append(predictor.check_if_hamburger(b))

for p in predictions:
    print(p)
