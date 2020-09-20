from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
sys.path.append('..')
from packages.classifier import training

datadir = 'pre_img'
modeldir = 'model'
classifier_filename = 'class/classifier_36.pkl'
print ("Training Start")
obj=training(datadir,modeldir,classifier_filename)
get_file=obj.main_train()
print('Saved classifier model to file "%s"' % get_file)
sys.exit("All Done")
