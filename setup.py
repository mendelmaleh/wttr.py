from setuptools import setup

with open('requirements.txt', encoding='utf-8') as r:
    requires = [i.strip() for i in r]

with open('README.md', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='wttr',
    version='0.4.1',
    description='wttr.in wrapper for cli',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/mendelmaleh/wttr.py',
    author='Mendel E.',
    py_modules=['wttr'],
    scripts=['wttr', 'wttr.py'],
    install_requires=requires,
)
