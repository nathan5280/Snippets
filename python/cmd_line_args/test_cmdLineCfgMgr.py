import unittest

from python.cmd_line_args.CmdLineCfgMgr import CmdLineCfgMgr


class TestCmdLineCfgMgr(unittest.TestCase):
    def test_all_parse(self):
        argv = ['-v', 'some-value',
                '-t',
                '-m', 'value-1',
                '-m', 'value-2']

        parser = CmdLineCfgMgr(argv)
        arg_dict = parser.cfg_dict

        self.assertEqual('some-value', arg_dict['arg_v'], 'Value Arg')
        self.assertTrue(arg_dict['arg_t'], 'True flag')
        self.assertFalse(arg_dict['arg_f'], 'False flag')
        self.assertEqual(['value-1', 'value-2'], arg_dict['arg_list'], 'Arg List')


if __name__ == '__main__':
    unittest.main()

