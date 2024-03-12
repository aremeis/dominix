
def test_version():
  import dominix
  version = '2.9.1'
  assert dominix.version == version
  assert dominix.__version__ == version
