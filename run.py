import numpy as np
import misvm
import time
from data_handle import *

filepath = '/home/scu/misvm_data/ss_tmp_train_bin_classify_cat_1.data'
[bags, labels] = load_data(filepath);


classifier = misvm.MISVM(kernel='linear', C=1.0, max_iters=50)
print "training..."
tbegin = time.time()
classifier.fit(bags, labels)
ttake = time.time() - tbegin
print "using %f secs" % ttake
print "predicting..."
predictions = classifier.predict(bags)
print predictions
ave = np.average(labels == np.sign(predictions))
print 'Accuracy: %.1f' % (ave)
