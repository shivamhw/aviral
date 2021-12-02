from distutils.core import setup


setup(
  name = 'aviral',        
  packages = ['aviral_api'],   
  version = '1.0',      
  license='MIT',        
  description = 'Api wrapper for IIIT Allahabad aviral portal',   
  long_description_content_type = "text/markdown",
  long_description ="Use aviral in your python application with ease, check marks, get details or make a sign in with aviral option in your application. \
This bypasses the static content calls so response is much faster then aviral website. Get your marks in less then 1 second even during when the main site is running slow. \
  for full api documentation https://shivamhw.github.io/aviral",   
  author = 'Shivam Mishra',                   
  author_email = 'shivamhw0@gmail.com',      
  url = 'https://github.com/shivamhw/aviral',   
  keywords = ['IIITA', 'Aviral', 'IIIT-A','indian institute of information technology allahabad'],   
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
