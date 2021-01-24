from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='testing_package',
    url='https://github.com/osultan94/testing_package.git',
    author='Omar Sultan',
    author_email='omar.sultan@basharsoft.com',
    # Needed to actually package something
    packages=['testing'],
    # Needed for dependencies
    install_requires=['numpy'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='An example of a python package from pre-existing code',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.txt').read()
)
