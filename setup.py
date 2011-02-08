from distutils.core import setup
from distutils.extension import Extension

ext_files = ["src/mmapbitarray.c",
             "src/bloomfilter.c",
             "src/primetester.c",
             ]

kwargs = {}

try:
    from Cython.Distutils import build_ext
    print "Building from Cython"
    ext_files.append("src/pybloomfilter.pyx")
    kwargs['cmdclass'] = {'build_ext': build_ext}
except ImportError:
    ext_files.append("src/pybloomfilter.c")
    print "Building from C"

ext_modules = [Extension("pybloomfilter",
                         ext_files)]

setup(
  name = 'pybloomfiltermmap',
  version = "0.1.21",
  author = "Rob Stacey, Michael Axiak",
  author_email = "rob@robstacey.com",
  url = "http://github.com/rpstac/pybloomfiltermmap/",
  description = "A Bloom filter for Python built on mmap",
  license = "MIT License",
  ext_modules = ext_modules,
  classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: C',
        'Programming Language :: Cython',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
  **kwargs
)
 
