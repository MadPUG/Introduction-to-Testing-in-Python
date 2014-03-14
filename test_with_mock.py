from example_conditions import conditional
from mock import Mock


def test_conditional_with_a():
    fake_obj = Mock()
    conditional(fake_obj, 'a')
    assert fake_obj.foo.called is True

def test_conditional_with_c():
    fake_obj = Mock()
    conditional(fake_obj, 'c')
    fake_obj.baz.assert_called_once_with(True)
