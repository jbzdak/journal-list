from distutils.core import setup

setup(
    name='journal_list',
    version='1.0',
    packages=['journal_list', 'journal_list_app', 'journal_list_app.management',
              'journal_list_app.management.commands',
              'journal_list_app.migrations'],
    url='',
    license='Apache License 2.0',
    author='Jacek Bzdak',
    author_email='jbzdak@gmail.com',
    description='',
     classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: Polish',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7'
    ]
)
