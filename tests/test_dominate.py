
def test_version():
  import dominix
  version = '1.0.0'
  assert dominix.version == version
  assert dominix.__version__ == version
