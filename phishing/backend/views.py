# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import joblib
import features_extraction
import sys
import numpy as np
from sklearn.externals import joblib
import os
from django.http import HttpResponse


# Create your views here.


def check_website(request):
    """

    """
    # import ipdb; ipdb.set_trace()
    
    url = request.GET.get('url')
    #url='https://www.google.com/'
    features_test = features_extraction.main(url)
    # Due to updates to scikit-learn, we now need a 2D array as a parameter to the predict function.
    features_test = np.array(features_test).reshape((1, -1))
    # import ipdb; ipdb.set_trace()
    clf = joblib.load(os.getcwd() +'/backend/classifier/random_forest.pkl')

    pred = clf.predict(features_test)

    # Print the probability of prediction (if needed)
    # prob = clf.predict_proba(features_test)
    # print 'Features=', features_test, 'The predicted probability is - ', prob, 'The predicted label is - ', pred
    #    print "The probability of this site being a phishing website is ", features_test[0]*100, "%"

    if int(pred[0]) == 1:
        # print "The website is safe to browse"
        print ("SAFE")
        return HttpResponse("SAFE")
    elif int(pred[0]) == -1:
        print(" PHISING")
        # print "The website has phishing features. DO NOT VISIT!"
        return HttpResponse('Phising')

        # print 'Error -', features_test