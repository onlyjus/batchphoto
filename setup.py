from setuptools import setup
from batchphoto import __version__

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='batchphoto',
      version=__version__,
      description='Python library for batch processing of photos',
      long_description=readme(),
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
      ],
      keywords='image processing batch',
      url='https://github.com/onlyjus/batchphoto',
      download_url = 'https://github.com/onlyjus/batchphoto/archive/0.1.tar.gz',
      author='Justin Weber',
      author_email='onlyjus@gmail.com',
      license='MIT',
      packages=[
        'batchphoto',
        'batchphoto.crop'
        ],
      platforms=['any'],
      environments=["python_version >= '3.4'",
                    "'3.0' > python_version >= '2.7'"],
      #install_requires=[],
      zip_safe=False,
      #test_suite='pytest',
      tests_require=['pytest'],
      include_package_data=True,
      entry_points={
          'console_scripts': [
              'batchphoto=batchphoto.__main__:main',
              ]
          }
      )
