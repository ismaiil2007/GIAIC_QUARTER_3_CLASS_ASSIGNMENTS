from setuptools import setup, find_packages  

setup(  
    name='personal-library-manager',  
    version='0.1.0',  
    description='A personal library manager to track books and reading progress.',  
    author='Ismail Hussain',  
    author_email='ismail.hussain.qwt+dev@gmail.com',  
    url='https://github.com/yourusername/personal-library-manager',   
    packages=find_packages(),  
    install_requires=[],  # Add any dependencies if required  
    classifiers=[  
        'Programming Language :: Python :: 3',  
        'License :: OSI Approved :: MIT License',  # Update if needed  
        'Operating System :: OS Independent',  
    ],  
    python_requires='>=3.6',  
)  