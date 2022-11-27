import codecs
import setuptools
import re
import ast

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('src/icalendar/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


shortdesc = 'iCalendar parser/generator'
longdesc = ''
for fname in ['README.rst', 'CONTRIBUTING.rst', 'CHANGES.rst', 'LICENSE.rst']:
    with codecs.open(fname, encoding='utf-8') as f:
        longdesc += f.read()
        longdesc += '\n'

tests_require = []
install_requires = [
    'python-dateutil',
    'pytz',
    # install requirements depending on python version
    # see https://www.python.org/dev/peps/pep-0508/#environment-markers
    'backports.zoneinfo; python_version == "3.7" or python_version == "3.8"',
]


setuptools.setup(
    name='icalendar',
    version=version,
    description=shortdesc,
    long_description=longdesc,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    keywords='calendar calendaring ical icalendar event todo journal '
             'recurring',
    author='Plone Foundation',
    author_email='plone-developers@lists.sourceforge.net',
    url='https://github.com/collective/icalendar',
    license='BSD',
    packages=setuptools.find_namespace_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.7",
    install_requires=install_requires,
    entry_points = {'console_scripts': ['icalendar = icalendar.cli:main']},
    extras_require={
        'test': tests_require
    },
    test_suite='icalendar.tests'
)
