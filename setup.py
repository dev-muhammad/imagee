import setuptools


def readme():
    with open('README.md') as f:
        return f.read()


setuptools.setup(name='imagee',
      version='0.1.1',
      description='Tool for image optimization',
      long_description=readme(),
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Image Processing',
      ],
      keywords='image',
      url='https://github.com/dev-muhammad/imagee',
      author='dev-muhammad',
      author_email='iam.markjobs@gmail.com',
      license='MIT',
      install_requires=[
          "Pillow==8.3.1"
      ],
      package_dir={"": "src"},
      packages=setuptools.find_packages(where="src"),
      zip_safe=False)
