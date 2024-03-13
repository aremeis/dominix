
def test_version():
  import dominix
  version = '1.1.1'
  assert dominix.version == version
  assert dominix.__version__ == version
