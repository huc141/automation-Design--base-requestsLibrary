import unittest
from jacksonreport import TestRunner

suite = unittest.defaultTestLoader.discover(r'H:\reporttest\demo1')
runner = TestRunner(suite)
runner.run()

wehook = 'https://oapi.dingtalk.com/robot/send?access_token=d34e6b2c64de29ceb51b0b99c888f829fceeef4ef6d6b3a6118eebabd3c71ab2'
res = runner.dingtalk_notice(url=wehook, key=':')

print(res)
