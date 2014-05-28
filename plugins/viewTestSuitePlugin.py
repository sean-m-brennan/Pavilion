#!python
""" plug-in to view the test suite configurations 
"""

import os,sys
from yapsy.IPlugin import IPlugin
from testConfig import YamlTestConfig

class ViewTestSuite(IPlugin):
    """ This implements the feature to view the default, user, and 
        effective (combined) test suite configuration files.
    """

    def print_name(self):
        print "viewTestSuite handler loaded!"

    # Every plugin class MUST have a method by the name "add_parser_info
    # and must return the name of the this sub-command

    def add_parser_info(self, subparser): 
        parser_rts = subparser.add_parser("view_test_suite", help="view test suite config files")
        parser_rts.add_argument('testSuite', help='test-suite-config-file')
        parser_rts.add_argument('-d', "--dict", help='show in dictionary format (yaml default)', action="store_true")
        parser_rts.set_defaults(sub_cmds='view_test_suite')
        return ('view_test_suite')

    # Every plug-in class MUST have a method by the name "cmd"
    # so that it can called when its sub-command is selected
        
    def cmd(self, args):
        print "\n"
        if args['verbose']:
            print "\nrunning run_test_suite"
            print "args -> %s" % args
            print "using test suite -> %s\n" % args['testSuite']
        
        if (os.path.isfile(args['testSuite'])):
            with open(args['testSuite']) as file:
                # Build the test configuration
                tc = YamlTestConfig(args['testSuite'])
                
            if args['dict']:
                
                print "\nMy test suite configuration (dict style):"
                print tc.get_user_test_config()
                
                print "\nDefault test suite configuration (dict style):"
                print tc.get_default_test_config()
  
                print "\nEffective test configuration (dict style):"
                print tc.get_effective_config_file()

            else:

                print "\nMy test suite configuration (yaml style):"
                tc.show_user_test_config()
    
                print "\nDefault test suite configuration (yaml style):"
                tc.show_default_config()
    
                print "\nEffective test suite configuration (yaml style):"
                tc.show_effective_config_file()

        else:
            print "  Error: could not find test suite %s" % args['testSuite']
            sys.exit()
        

if __name__=="__main__":
    print ViewTestSuite.__doc__
