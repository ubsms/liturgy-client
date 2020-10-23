from setuptools import setup

setup(
    name='liturgyclient',
    version='0.1.0',    
    description='A liturgy client for CasparCG',
    url='https://github.com/ubsms/liturgyclient',
    author='Richard Franks',
    author_email='richard@ubsms.org.uk',
    license='MIT',
    packages=['liturgyclient'],
    install_requires=['ruamel.yaml',
                      'amcp-pylib',
                      'wxpython',                    
                      ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: X11 Applications',
        'Intended Audience :: Religion',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
    ],
)