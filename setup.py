import setuptools


def readme():
    with open('README.md') as f:
        return f.read()


setuptools.setup(name='imagee',
      version='1.1',
      description='Tool for image optimization',
      long_description=readme(),
      long_description_content_type='text/markdown',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Image Processing',
      ],
      keywords='image',
      url='https://github.com/dev-muhammad/imagee',
      author='dev-muhammad',
      author_email='iam.markjobs@gmail.com',
      license='MIT',
      package_dir={"": "src"},
      packages=setuptools.find_packages(where="src"),
      install_requires=[
          'markdown',
          'Pillow',
      ],
      include_package_data=True,
      zip_safe=False)
