import sys
import os
from setuptools import setup, Extension
import numpy as np

_VERSION = "2.2.1"

f_compile_args = ['-ffixed-form', '-fdefault-real-8']

def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as _in:
        return _in.read()

if sys.platform == 'darwin':
    GFORTRAN_LIB = np.distutils.sysconfig.get_config_var("LIBDIR")
    QUADMATH_LIB = GFORTRAN_LIB  # Adjust this based on your requirements
    ARGS = ["-Wl,-rpath,{}:{}".format(GFORTRAN_LIB, QUADMATH_LIB)]
    f_compile_args += ARGS
    library_dirs = [GFORTRAN_LIB, QUADMATH_LIB]
else:
    library_dirs = None

glmnet_lib = Extension(
    name='_glmnet',
    sources=['glmnet/_glmnet.pyf', 'glmnet/src/glmnet/glmnet5.f90'],
    extra_f90_compile_args=f_compile_args,
    library_dirs=library_dirs,
)

if __name__ == "__main__":
    setup(
        name="glmnet",
        version=_VERSION,
        description="Python wrapper for glmnet",
        long_description=read('README.rst'),
        long_description_content_type="text/x-rst",
        author="Civis Analytics Inc",
        author_email="opensource@civisanalytics.com",
        url="https://github.com/civisanalytics/python-glmnet",
        install_requires=[
            "numpy>=1.9.2",
            "scikit-learn>=0.18.0",
            "scipy>=0.14.1",
            "joblib>=0.14.1",
        ],
        python_requires=">=3.6.*",
        ext_modules=[glmnet_lib],
        packages=['glmnet'],
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Console',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3 :: Only',
            'Operating System :: OS Independent',
            'Intended Audience :: Developers',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
            'Topic :: Scientific/Engineering'
        ]
    )
