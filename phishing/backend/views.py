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
from django.shortcuts import render
from models import *


# Create your views here.

def dash(request):
    """
    """
    data = []
    websites = Website.objects.all().order_by('-time')
    for website in websites:
        features = Feature_score.objects.filter(website=website).order_by('position')
        features_obj = []
        for feature in features:
            features_obj.append(get_feature_detail(feature))
        data.append({
        'id': website.id,
        'url': website.url,
        'status': website.status,
        'features': features_obj
        })

    return render(request, 'dash.html', {'data': data})

def get_feature_detail(feature):
    """
    """

    return({
    'feature': feature.feature_name,
    'score': feature.score
    })

def check_website(request):
    """

    """
    # import ipdb; ipdb.set_trace()

    url = request.GET.get('url')
    #url='https://www.google.com/'
    data = features_extraction.main(url)
    features_test = data[0]
    feature_result = data[1]
    print data
    # Due to updates to scikit-learn, we now need a 2D array as a parameter to the predict function.
    features_test = np.array(features_test).reshape((1, -1))
    # import ipdb; ipdb.set_trace()
    clf = joblib.load(os.getcwd() +'/backend/classifier/random_forest.pkl')

    pred = clf.predict(features_test)

    # Print the probability of prediction (if needed)
    # prob = clf.predict_proba(features_test)
    # print 'Features=', features_test, 'The predicted probability is - ', prob, 'The predicted label is - ', pred
    #    print "The probability of this site being a phishing website is ", features_test[0]*100, "%"
    print features_test
    if int(pred[0]) == 1:
        # print "The website is safe to browse"

        message = 'SAFE'
        status_const = WEBSITE_SAFE
    elif int(pred[0]) == -1:
        print(" PHISING")
        # print "The website has phishing features. DO NOT VISIT!"
        message = 'UNSAFE'
        status_const = WEBSITE_UNSAFE

        # print 'Error -', features_test

    website = Website(
    url=url,
    status=status_const
    )
    website.save()

    for i in range(0,22):
        data_obj = feature_result[i]
        feature = Feature_score(
        website=website,
        position=i,
        score=data_obj['score'],
        feature_name=data_obj['feature']
        )
        feature.save()


    return HttpResponse(message)
