import sys
import pytest
from testing.cffi0 import backend_tests
from cffi.backend_ctypes import CTypesBackend


class TestCTypes(backend_tests.BackendTests):
    # for individual tests see
    # ====> backend_tests.py
    
    Backend = CTypesBackend
    TypeRepr = "<class 'ffi.CData<%s>'>"

    def test_array_slicing(self):
        pytest.skip("ctypes backend: not supported: "
                     "slice of array")

    def test_array_of_func_ptr(self):
        pytest.skip("ctypes backend: not supported: "
                     "initializers for function pointers")

    def test_structptr_argument(self):
        pytest.skip("ctypes backend: not supported: passing a list "
                     "for a pointer argument")

    def test_array_argument_as_list(self):
        pytest.skip("ctypes backend: not supported: passing a list "
                     "for a pointer argument")

    def test_cast_to_array_type(self):
        pytest.skip("ctypes backend: not supported: casting to array")

    def test_nested_anonymous_struct(self):
        pytest.skip("ctypes backend: not supported: nested anonymous struct")

    def test_nested_field_offset_align(self):
        pytest.skip("ctypes backend: not supported: nested anonymous struct")

    def test_nested_anonymous_union(self):
        pytest.skip("ctypes backend: not supported: nested anonymous union")

    def test_nested_anonymous_struct_2(self):
        pytest.skip("ctypes backend: not supported: nested anonymous union")

    def test_CData_CType_2(self):
        if sys.version_info >= (3,):
            pytest.skip("ctypes backend: not supported in Python 3: CType")
        backend_tests.BackendTests.test_CData_CType_2(self)
