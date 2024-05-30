from setuptools import setup, find_packages

# Load README.md for long description
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pythonCheatsheet',
    version='0.1',
    author='therulerplayback',
    author_email='the@ruler.com',
    description='A Python cheatsheet package for The Ruler',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/therulerplayback/pythonCheatsheet',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='python cheatsheet utilities',
    project_urls={
        'Bug Reports': 'https://github.com/therulerplayback/pythonCheatsheet/issues',
        'Source': 'https://github.com/therulerplayback/pythonCheatsheet',
    },
    python_requires='>=3.6',
    license='MIT',
)
