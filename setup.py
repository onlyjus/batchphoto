from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='batchphoto',
      version='0.1',
      description='Python library for batch processing of photos',
      long_description=readme(),
      classifiers=[
        'Development Status :: 4 - Beta',
        'LLicense :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
      ],
      keywords='image processing batch',
      url='https://github.com/onlyjus/batchphoto',
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
