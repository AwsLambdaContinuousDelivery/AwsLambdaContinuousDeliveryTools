#!/usr/bin/env python

from distutils.core import setup

setup( name='awslambdacontinuousdeliverytools'
     , version = '0.0.2'
     , description = 'AwsLambdaContinuousDeliveryTools'
     , author = 'Janos Potecki'
     , url = 'https://github.com/AwsLambdaContinuousDelivery/AwsLambdaContinuousDeliveryTools'
     , packages = ['awslambdacontinuousdelivery.tools']
     , license='MIT'
     , install_requires = [
          'troposphere', 'awacs'
      ]
     )
