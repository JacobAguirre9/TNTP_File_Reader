from setuptools import setup, find_packages

setup(
    name='tntp_file_reader',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            # If you have command-line scripts, specify them here
            # 'script_name = module:function',
        ],
    },
    url='https://github.com/JacobAguirre9/TNTP_File_Reader',
    license='MIT',
    author='Jacob M. Aguirre',
    author_email='your.email@example.com',
    description='Helper functions for analyzing and cleaning .TNTP file data.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
