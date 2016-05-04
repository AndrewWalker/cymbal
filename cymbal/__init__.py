from . import clangext

# As these functions are added to libclang the intention will be to deprecate
# functions here or replace them with appropriate compatibility wrappers

# This module intentionally exports nothing - it has side effects on the
# libclang (ie/ it monkey patches libclang in place to make the necessary
# changes)
__all__ = [  ]
