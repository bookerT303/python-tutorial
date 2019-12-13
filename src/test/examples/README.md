#Unit testing

## For this to work needed to install `mock`
```
pip3 install mock
```

### mock print()
If you want to check the output you can use another mock:
```python
import io
import unittest.mock 
from mock import patch

...

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            methodUnderTest()
            self.assertEqual(expectedOutput, fake_out.getvalue().strip())
```
