#!/usr/bin/env python

from distutils.core import setup

setup( name='AwsLambdaContinuousDeliveryTools'
     , version = '0.0.1'
     , description = 'AwsLambdaContinuousDeliveryTools'
     , author = 'Janos Potecki'
     , url = 'https://github.com/AwsLambdaContinuousDelivery/pyAwsLambdaContinuousDeliveryTools'
     , packages = ['awslambdacontinuousdelivery.tools']
     , license='MIT'
     , install_requires = [
          'troposphere', 'awacs'
      ]
     )
