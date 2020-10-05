from storage import Storage

def test_add():
    st = Storage({'a': 1, 'b': 2})
    key = 'b'
    val = 3
    try:
        st.add(key, val)
        assert st.get(key) == 2, "Value for the existing key {} was changed".format(key)
    except Exception:
        pass
    key = 'c'
    val = 3
    st.add(key, val)
    assert st.get(key) == val, "Value for the key {} is not equal to expected or there is no such key".format(key)

def test_remove():
    pass

def test_set():
    pass

def test_get():
    st = Storage({'a': 1, 'b': 2})
    key = 'b'
    val = st.get(key)
    assert val == 2, "Value for the key {} is not equal to expected".format(key)
    key = 'c'
    val = st.get(key)
    assert val is None, "Value for an unexisting key is not None"

def run_tests():
    test_add()
    test_remove()
    test_set()
    test_get()

if __name__ == "__main__":
    run_tests()
