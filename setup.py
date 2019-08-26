import setuptools

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='ubermag',
    version='0.1',
    description='Meta package for Ubermag project.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://ubermag.github.io',
    author=('Marijan Beg, Ryan A. Pepper, Thomas Kluyver, '
            'and Hans Fangohr'),
    packages=setuptools.find_packages(),
    include_package_data = True,
    install_requires=['oommfc'],
    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: BSD License',
                 'Programming Language :: Python :: 3 :: Only',
                 'Operating System :: Unix',
                 'Operating System :: MacOS',
                 'Operating System :: Microsoft :: Windows',
                 'Topic :: Scientific/Engineering :: Physics',
                 'Intended Audience :: Science/Research',
                 'Natural Language :: English']
)
