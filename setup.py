import sys

from setuptools import find_packages, setup

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()
with open('LICENSE', 'r', encoding='utf-8') as f:
    lcs = f.read()
info = sys.version_info
setup(
    name='otsunotificationfrequency',
    version='1.0.0',
    url='https://github.com/Otsuhachi/NotificationFrequency',
    description='要素数が確定されたシーケンスの途中で処理を挟むタイミングの判定を補助します。',
    long_description_content_type='text/markdown',
    long_description=readme,
    author='Otsuhachi',
    author_email='agequodagis.tufuiegoeris@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 1 - Planning', 'Natural Language :: Japanese', 'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8', 'Programming Language :: Python :: 3.9', 'Operating System :: Microsoft :: Windows :: Windows 10',
        'License :: OSI Approved :: MIT License'
    ],
    license=lcs,
    keywords='Python Notification Frequency for',
)
