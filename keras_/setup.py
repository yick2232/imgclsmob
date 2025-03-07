from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='kerascv',
    version='0.0.37',
    description='Image classification models for Keras',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/osmr/imgclsmob',
    author='Oleg Sémery',
    author_email='osemery@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Image Recognition',
    ],
    keywords='machine-learning deep-learning neuralnetwork image-classification keras keras-mxnet imagenet vgg resnet '
             'resnext senet densenet darknet squeezenet squeezenext shufflenet menet mobilenent igcv3 mnasnet '
             'efficientnet',
    packages=find_packages(exclude=['others', '*.others', 'others.*', '*.others.*']),
    include_package_data=True,
    install_requires=['h5py'],
)
