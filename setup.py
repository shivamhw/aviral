from distutils.core import setup
from os import read

readme = open('README', 'r')
README = readme.read()
setup(
  name = 'aviral',        
  packages = ['aviral_api'],   
  version = '0.1.2',      
  license='MIT',        
  description = 'Api wrapper for IIIT Allahabad aviral portal',   
  long_description_content_type = "text/markdown",
  long_description =README,   
  author = 'Shivam Mishra',                   
  author_email = 'shivamhw0@gmail.com',      
  url = 'https://github.com/shivamhw/aviral',   
  keywords = ['IIITA', 'Aviral', 'IIIT-A'],   
  install_requires=[            
          'requests'
      ],
  classifiers=[
    'Development Status :: 4 - Beta',    
    'Intended Audience :: Developers',    
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3.9',   
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
