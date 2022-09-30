Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@zakwarlord7 
Your account has been flagged.
Because of that, your profile is hidden from the public. If you believe this is a mistake, contact support to have your account status reviewed.
zakwarlord7
/
instructions-Enter-CUSIP
Public
generated from zakwarlord7/zakwarlord7
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
Open a pull request
Create a new pull request by comparing changes across two branches. If you need to, you can also .
    Able to merge. These branches can be automatically merged.
@zakwarlord7
Revert "Revert "butt""
 
Add heading textAdd bold text, <Ctrl+b>Add italic text, <Ctrl+i>
Add a quote, <Ctrl+Shift+.>Add code, <Ctrl+e>Add a link, <Ctrl+k>
Add a bulleted list, <Ctrl+Shift+8>Add a numbered list, <Ctrl+Shift+7>Add a task list, <Ctrl+Shift+l>
Directly mention a user or team
Reference an issue, pull request, or discussion
Add saved reply
Reverts zakwarlord7/instructions-Enter-CUSIP#4
No file chosen
Attach files by dragging & dropping, selecting or pasting them.
Styling with Markdown is supported
Remember, contributions to this repository should follow its contributing guidelines.
Reviewers
No reviews
Assignees
No one—
Labels
None yet
Projects
None yet
Milestone
No milestone
Development
Use Closing keywords in the description to automatically close issues

Helpful resources
Contributing
GitHub Community Guidelines
 1 commit
 1 file changed
 1 contributor
Commits on Sep 30, 2022
Revert "Revert "butt""

@zakwarlord7
zakwarlord7 committed 5 minutes ago
  
Showing  with 9,028 additions and 0 deletions.
 9,028  
PAT
@@ -0,0 +1,9028 @@
on:
  push:
    branches:
    - main
    - release/*
Set your workflow to run on pull_request events that target the main branch

on:
  pull_request:
    branches:
    - main
Set your workflow to run every day of the week from Monday to Friday at 2:00 UTC

on:
  schedule:
  - cron: "0 2 * * 1-5"
For more information, see "Events that trigger workflows."

Manually running a workflow
To manually run a workflow, you can configure your workflow to use the workflow_dispatch event. This enables a "Run workflow" button on the Actions tab.

on:
  workflow_dispatch:
For more information, see "Manually running a workflow."

Running your jobs on different operating systems
GitHub Actions provides hosted runners for Linux, Windows, and macOS.

To set the operating system for your job, specify the operating system using runs-on:

jobs:
  my_job:
    name: deploy to staging
    runs-on: ubuntu-18.04
The available virtual machine types are:

ubuntu-latest, ubuntu-18.04, or ubuntu-16.04
windows-latest or windows-2019
macos-latest or macos-10.15
For more information, see "Virtual environments for GitHub Actions."

Using an action
Actions are reusable units of code that can be built and distributed by anyone on GitHub. You can find a variety of actions in GitHub Marketplace, and also in the official Actions repository.

To use an action, you must specify the repository that contains the action. We also recommend that you specify a Git tag to ensure you are using a released version of the action.

- name: Setup Node
  uses: actions/setup-node@v1
  with:
    node-version: '10.x'
For more information, see "Workflow syntax for GitHub Actions."

Running a command
You can run commands on the job's virtual machine.

- name: Install Dependencies
  run: npm install
For more information, see "Workflow syntax for GitHub Actions."

Running a job across a matrix of operating systems and runtime versions
You can automatically run a job across a set of different values, such as different versions of code libraries or operating systems.

For example, this job uses a matrix strategy to run across 3 versions of Node and 3 operating systems:

jobs:
  test:
    name: Test on node ${{ matrix.node_version }} and ${{ matrix.os }}
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        node_version: ['8', '10', '12']
        os: [ubuntu-latest, windows-latest, macOS-latest]

    steps:
    - uses: actions/checkout@v1
    - name: Use Node.js ${{ matrix.node_version }}
      uses: actions/setup-node@v1
      with:
        node-version: ${{ matrix.node_version }}

    - name: npm install, build and test
      run: |
        npm install
        npm run build --if-present
        npm test
For more information, see "Workflow syntax for GitHub Actions."

Running steps or jobs conditionally
GitHub Actions supports conditions on steps and jobs using data present in your workflow context.

For example, to run a step only as part of a push and not in a pull_request, you can specify a condition in the if: property based on the event name:

steps:
- run: npm publish
  if: github.event_name == 'push'
For more information, see "Contexts and expression syntax for GitHub Actions."require'
require 'json'
post '/payload' do
  push = JSON.parse(request.body.read}
# -loader = :rake.i
# -ruby_opts = Automate autoupdate
# -description = "Run tests" + @name == :test ? "" : " for #{@name}")
# -deps = [list]
# -if?=name:(Hash.#:"','")
# -deps = @name.values.first
# -name = @name.keys.first
# -pattern = "test/test*.rb" if @pattern.nil? && @test_files.nil?
# -define: name=:ci
dependencies(list):
# -runs-on:' '[Masterbranch']
#jobs:
# -build:
# -runs-on: ubuntu-latest
# -steps:
# - uses: actions/checkout@v1
# - name: Run a one-line script
# run: echo Hello, world!
# - name: Run a multi-line script
# run=:name: echo: hello.World!
# echo test, and deploy your project'@'#'!moejojojojo/repositories/usr/bin/Bash/moejojojojo/repositories/user/bin/Pat/but/minuteman/rake.i/rust.u/pom.XML/Rakefil.IU/package.json/pkg.yml/package.yam/pkg.js/Runestone.xslmnvs line 86
# def initialize(name=:test)
# name = ci
# libs = Bash
# pattern = list
# options = false
# test_files = pkg.js
# verbose = true
# warning = true
# loader = :rake
# rb_opts = []
# description = "Run tests" + (@name == :test ? "" : " for #{@name}")
# deps = []
# if @name.is_a'?','"':'"'('"'#'"'.Hash':'"')'"''
# deps = @name.values.first
# name=::rake.gems/.specs_keyscutter
# pattern = "test/test*.rb" if @pattern.nil? && @test_files.nil?
# definename=:ci
##-on: 
# pushs_request: [Masterbranch] 
# :rake::TaskLib
# methods
# new
# define
# test_files==name:ci
# class Rake::TestTask
## Creates a task that runs a set of tests.
# require "rake/test.task'@ci@travis.yml.task.new do |-v|
# t.libs << "test"
# t.test_files = FileList['test/test*.rb']
# t.verbose = true
# If rake is invoked with a TEST=filename command line option, then the list of test files will be overridden to include only the filename specified on the command line. This provides an easy way to run just one test.
# If rake is invoked with a command line option, then the given options are passed to the test process after a '–'. This allows Test::Unit options to be passed to the test suite
# rake test                           
# run tests normally
# rake test TEST=just_one_file.rb     
# run just one test file.
# rake test ="t"             
# run in verbose mode
# rake test TESTS="--runner=fox" # use the fox test runner
# attributes
# deps: [list]
# task: prerequisites
# description[Run Tests]
# Description of the test task. (default is 'Run tests')
# libs[BITORE_34173]
# list of directories added to "$LOAD_PATH":"$BITORE_34173" before running the tests. (default is 'lib')
# loader[test]
# style of test loader to use. Options are:
# :rake – rust/rake provided tests loading script (default).
# :test=: name =rb.dist/src.index = Ruby provided test loading script.
direct=: $LOAD_PATH uses test using command-line loader.
name[test]
# name=: testtask.(default is :test)
# options[dist]
# Tests options passed to the test suite. An explicit TESTOPTS=opts on the command line will override this. (default is NONE)
# pattern[list]
# Glob pattern to match test files. (default is 'test/test*.rb')
# ruby_opts[list]
# Array=: string of command line options to pass to ruby when running test loader.
# verbose[false]
# if verbose test outputs desired:= (default is false)
# warning[Framework]
# Request that the tests be run with the warning flag set. E.g. warning=true implies “ruby -w” used to run the tests. (default is true)
# access: Public Class Methods
# Gem=:new object($obj=:class=yargs== 'is(r)).)=={ |BITORE_34173| ... }
# Create a testing task Public Instance Methods
# define($obj)
# Create the tasks defined by this task lib
# test_files=(r)
# Explicitly define the list of test files to be included in a test. list is expected to be an array of file names (a File list is acceptable). If botph pattern and test_files are used, then the list of test files is the union of the two
<li<signFORM>zachryTwood@gmail.com Zachry Tyler Wood DOB 10 15 1994 SSID *******1725<SIGNform/><li/>


ZACHRY WOOD <zachryiixixiiwood@gmail.com>
Sep 29, 2022, 12:37 AM (1 day ago)
to me, JOSEPH


UNAUDITED FUND HOLDINGS (AS OF 10/31/2020)

























Zachry T WooD III	
























JPMorgan 100% U.S. Treasury Securities Money Market Fund - Capital
























INCOME	INCOME	INCOME	INCOME	INCOME	INCOME	INCOME	INCOME	INCOME	INCOME	INCOME	INCOME	INCOME	INCOME	
INCOME	SHAREHOLDER ZACHRY T WOOD III'S SIGNIFINANCE	














issuer	INVESTMENT CATEGORY	CUSIP	EFFECTIVE MATURITY	FINAL LEGAL MATURITY	COUPON OR YIELD (%)	PRINCIPAL AMOUNT ($)	MARKET VALUE ($)	FIXED/VARIABLE	PARENT NAME	% OF TOTAL VALUE	S AND P RATING	MOODYS RATING	FITCH RATING		SPONSOR	








US TREASURY	U.S. Treasury Debt	9127962Q1	04/22/2021	04/22/2021	0.1046	750,000,000.00	749,625,540.90	Fixed	US DEPARTMENT OF THE TREASURY	0.8000	A-1+	P-1	F1+		NA	






US TREASURY	U.S. Treasury Debt	9127963A5	11/19/2020	11/19/2020	0.1129	6,675,000,000.00	6,674,623,438.00	Fixed	US DEPARTMENT OF THE TREASURY	6.9000	A-1+	P-1	F1+		NA	






US TREASURY	U.S. Treasury Debt	9127963B3	11/27/2020	11/27/2020	0.1068	7,100,000,000.00	7,099,452,736.00	Fixed	US DEPARTMENT OF THE TREASURY	7.4000	A-1+	P-1	F1+		NA	






US TREASURY	U.S. Treasury Debt	9127963J6	12/10/2020	12/10/2020	0.1057	5,000,000,000.00	4,999,427,729.00	Fixed	US DEPARTMENT OF THE TREASURY	5.2000	A-1+	P-1	F1+		NA	






US TREASURY	U.S. Treasury Debt	9127963K3	12/17/2020	12/17/2020	0.0825	75,000,000.00	74,992,093.74	Fixed	US DEPARTMENT OF THE TREASURY	0.1000	A-1+	P-1	F1+		NA	






US TREASURY	U.S. Treasury Debt	9127963L1	12/24/2020	12/24/2020	0.1011	1,950,000,000.00	1,949,709,788.00	Fixed	US DEPARTMENT OF THE TREASURY	2.0000	A-1+	P-1	F1+		NA	






US TREASURY	U.S. Treasury Debt	9127963V9	01/21/2021	01/21/2021	0.1010	9,100,000,000.00	9,097,931,687.00	Fixed	US DEPARTMENT OF THE TREASURY	9.5000	A-1+	P-1	F1+		NA	






US TREASURY	U.S. Treasury Debt	9127964D8	02/18/2021	02/18/2021	0.1009	1,500,000,000.00	1,499,542,049.00	Fixed	US DEPARTMENT OF THE TREASURY	1.6000	A-1+	P-1	F1+		NA	






US TREASURY	U.S. Treasury Debt	9127964N6	03/18/2021	03/18/2021	0.1081	250,000,000.00	249,897,250.00	Fixed	US DEPARTMENT OF THE TREASURY	0.3000	A-1+	P-1	F1+		NA	






US TREASURY	U.S. Treasury Debt	9127964R7	11/10/2020	11/10/2020	0.1344	11,300,000,000.00	11,299,620,406.00	Fixed	US DEPARTMENT OF THE TREASURY	11.8000	A-1+	P-1	F1+		NA	






US TREASURY	U.S. Treasury Debt	9127964S5	11/17/2020	11/17/2020	0.1005	1,250,000,000.00	1,249,944,167.00	Fixed	US DEPARTMENT OF THE TREASURY	1.3000	A-1+	P-1	F1+		NA	






US TREASURY	U.S. Treasury Debt	9127964T3	11/24/2020	11/24/2020	0.1198	4,034,950,000.00	4,034,641,199.00	Fixed	US DEPARTMENT OF THE TREASURY	4.2000	A-1+	P-1	F1+		NA	






US TREASURY	U.S. Treasury Debt	9127964U0	12/01/2020	12/01/2020	0.1112	1,500,000,000.00	1,499,861,042.00	Fixed	US DEPARTMENT OF THE TREASURY	1.6000	A-1+	P-1	F1+		NA	






US TREASURY	U.S. Treasury Debt	9127964Y2	04/15/2021	04/15/2021	0.0925	150,000,000.00	149,936,405.70	Fixed	US DEPARTMENT OF THE TREASURY	0.2000	A-1+	P-1	F1+		NA	






US TREASURY	U.S. Treasury Debt	9127965D7	12/22/2020	12/22/2020	0.1451	2,000,000,000.00	1,999,589,167.00	Fixed	US DEPARTMENT OF THE TREASURY	2.1000	A-1+	P-1	F1+		NA	






US TREASURY	U.S. Treasury Debt	9127965F2	12/29/2020	12/29/2020	0.1151	5,055,020,000.00	5,054,082,611.00	Fixed	US DEPARTMENT OF THE TREASURY	5.3000	A-1+	P-1	F1+		NA	






US TREASURY	U.S. Treasury Debt	912796A58	01/05/2021	01/05/2021	0.0850	100,000,000.00	99,984,652.78	Fixed	US DEPARTMENT OF THE TREASURY	0.1000	A-1+	P-1	F1+		NA	






US TREASURY	U.S. Treasury Debt	912796A66	01/12/2021	01/12/2021	0.1101	3,200,000,000.00	3,199,295,400.00	Fixed	US DEPARTMENT OF THE TREASURY	3.3000	A-1+	P-1	F1+		NA	






US TREASURY	U.S. Treasury Debt	912796A82	01/26/2021	01/26/2021	0.1000	150,000,000.00	149,964,166.70	Fixed	US DEPARTMENT OF THE TREASURY	0.2000	A-1+	P-1	F1+		NA	






US TREASURY	U.S. Treasury Debt	912796B65	02/02/2021	02/02/2021	0.1074	1,450,000,000.00	1,449,597,969.00	Fixed	US DEPARTMENT OF THE TREASURY	1.5000	A-1+	P-1	F1+		NA	






US TREASURY	U.S. Treasury Debt	912796B99	02/23/2021	02/23/2021	0.1098	2,050,000,000.00	2,049,287,500.00	Fixed	US DEPARTMENT OF THE TREASURY	2.1000	A-1+	P-1	F1+		NA	






US TREASURY	U.S. Treasury Debt	912796C23	03/02/2021	03/02/2021	0.1006	850,000,000.00	849,712,624.90	Fixed	US DEPARTMENT OF THE TREASURY	0.9000	A-1+	P-1	F1+		NA	






US TREASURY	U.S. Treasury Debt	912796C72	03/09/2021	03/09/2021	0.1051	150,000,000.00	149,944,000.00	Fixed	US DEPARTMENT OF THE TREASURY	0.2000	A-1+	P-1	F1+		NA	






US TREASURY	U.S. Treasury Debt	912796C80	03/16/2021	03/16/2021	0.1005	500,000,000.00	499,811,562.50	Fixed	US DEPARTMENT OF THE TREASURY	0.5000	A-1+	P-1	F1+		NA	






US TREASURY	U.S. Treasury Debt	912796D22	03/30/2021	03/30/2021	0.0950	465,000,000.00	464,817,164.60	Fixed	US DEPARTMENT OF THE TREASURY	0.5000	A-1+	P-1	F1+		NA	






US TREASURY	U.S. Treasury Debt	912796D71	04/06/2021	04/06/2021	0.0000	525,000,000.00	524,764,187.50	Fixed	US DEPARTMENT OF THE TREASURY	0.5000	A-1+	P-1	F1+		NA	






US TREASURY	U.S. Treasury Debt	912796TP4	11/05/2020	11/05/2020	0.1517	1,246,000,000.00	1,245,979,011.00	Fixed	US DEPARTMENT OF THE TREASURY	1.3000	A-1+	P-1	F1+		NA	






US TREASURY	U.S. Treasury Debt	912796TU3	12/03/2020	12/03/2020	0.1007	5,873,658,000.00	5,873,132,400.00	
...

[Message clipped]  View entire message
indexmodules |next |previous |python logo Python » 

English

3.10.7
 3.10.7 Documentation » Python Setup and Usage » 1. Command line and environment
Quick search
  |
1. Command line and environment
The CPython interpreter scans the command line and the environment for various settings.

CPython implementation detail: Other implementations’ command line schemes may differ. See Alternate Implementations for further resources.

1.1. Command line
When invoking Python, you may specify any of these options:

python [-bBdEhiIOqsSuvVWx?] [-c command | -m module-name | script | - ] [args]
The most common use case is, of course, a simple invocation of a script:

python myscript.py
1.1.1. Interface options
The interpreter interface resembles that of the UNIX shell, but provides some additional methods of invocation:

When called with standard input connected to a tty device, it prompts for commands and executes them until an EOF (an end-of-file character, you can produce that with Ctrl-D on UNIX or Ctrl-Z, Enter on Windows) is read.

When called with a file name argument or with a file as standard input, it reads and executes a script from that file.

When called with a directory name argument, it reads and executes an appropriately named script from that directory.

When called with -c command, it executes the Python statement(s) given as command. Here command may contain multiple statements separated by newlines. Leading whitespace is significant in Python statements!

When called with -m module-name, the given module is located on the Python module path and executed as a script.

In non-interactive mode, the entire input is parsed before it is executed.

An interface option terminates the list of options consumed by the interpreter, all consecutive arguments will end up in sys.argv – note that the first element, subscript zero (sys.argv[0]), is a string reflecting the program’s source.

-c <command>
Execute the Python code in command. command can be one or more statements separated by newlines, with significant leading whitespace as in normal module code.

If this option is given, the first element of sys.argv will be "-c" and the current directory will be added to the start of sys.path (allowing modules in that directory to be imported as top level modules).

Raises an auditing event cpython.run_command with argument command.

-m <module-name>
Search sys.path for the named module and execute its contents as the __main__ module.

Since the argument is a module name, you must not give a file extension (.py). The module name should be a valid absolute Python module name, but the implementation may not always enforce this (e.g. it may allow you to use a name that includes a hyphen).

Package names (including namespace packages) are also permitted. When a package name is supplied instead of a normal module, the interpreter will execute <pkg>.__main__ as the main module. This behaviour is deliberately similar to the handling of directories and zipfiles that are passed to the interpreter as the script argument.

Note This option cannot be used with built-in modules and extension modules written in C, since they do not have Python module files. However, it can still be used for precompiled modules, even if the original source file is not available.
If this option is given, the first element of sys.argv will be the full path to the module file (while the module file is being located, the first element will be set to "-m"). As with the -c option, the current directory will be added to the start of sys.path.

-I option can be used to run the script in isolated mode where sys.path contains neither the current directory nor the user’s site-packages directory. All PYTHON* environment variables are ignored, too.

Many standard library modules contain code that is invoked on their execution as a script. An example is the timeit module:

python -m timeit -s 'setup here' 'benchmarked code here'
python -m timeit -h # for details
Raises an auditing event cpython.run_module with argument module-name.

See also
runpy.run_module()
Equivalent functionality directly available to Python code

PEP 338 – Executing modules as scripts

Changed in version 3.1: Supply the package name to run a __main__ submodule.

Changed in version 3.4: namespace packages are also supported

-
Read commands from standard input (sys.stdin). If standard input is a terminal, -i is implied.

If this option is given, the first element of sys.argv will be "-" and the current directory will be added to the start of sys.path.

Raises an auditing event cpython.run_stdin with no arguments.

<script>
Execute the Python code contained in script, which must be a filesystem path (absolute or relative) referring to either a Python file, a directory containing a __main__.py file, or a zipfile containing a __main__.py file.

If this option is given, the first element of sys.argv will be the script name as given on the command line.

If the script name refers directly to a Python file, the directory containing that file is added to the start of sys.path, and the file is executed as the __main__ module.

If the script name refers to a directory or zipfile, the script name is added to the start of sys.path and the __main__.py file in that location is executed as the __main__ module.

-I option can be used to run the script in isolated mode where sys.path contains neither the script’s directory nor the user’s site-packages directory. All PYTHON* environment variables are ignored, too.

Raises an auditing event cpython.run_file with argument filename.

See also
runpy.run_path()
Equivalent functionality directly available to Python code

If no interface option is given, -i is implied, sys.argv[0] is an empty string ("") and the current directory will be added to the start of sys.path. Also, tab-completion and history editing is automatically enabled, if available on your platform (see Readline configuration).

See also Invoking the Interpreter
Changed in version 3.4: Automatic enabling of tab-completion and history editing.

1.1.2. Generic options
-?
-h
--help
Print a short description of all command line options.

-V
--version
Print the Python version number and exit. Example output could be:

Python 3.8.0b2+
When given twice, print more information about the build, like:

Python 3.8.0b2+ (3.8:0c076caaa8, Apr 20 2019, 21:55:00)
[GCC 6.2.0 20161005]
New in version 3.6: The -VV option.

1.1.3. Miscellaneous options
-b
Issue a warning when comparing bytes or bytearray with str or bytes with int. Issue an error when the option is given twice (-bb).

Changed in version 3.5: Affects comparisons of bytes with int.

-B
If given, Python won’t try to write .pyc files on the import of source modules. See also PYTHONDONTWRITEBYTECODE.

--check-hash-based-pycs default|always|never
Control the validation behavior of hash-based .pyc files. See Cached bytecode invalidation. When set to default, checked and unchecked hash-based bytecode cache files are validated according to their default semantics. When set to always, all hash-based .pyc files, whether checked or unchecked, are validated against their corresponding source file. When set to never, hash-based .pyc files are not validated against their corresponding source files.

The semantics of timestamp-based .pyc files are unaffected by this option.

-d
Turn on parser debugging output (for expert only, depending on compilation options). See also PYTHONDEBUG.

-E
Ignore all PYTHON* environment variables, e.g. PYTHONPATH and PYTHONHOME, that might be set.

-i
When a script is passed as first argument or the -c option is used, enter interactive mode after executing the script or the command, even when sys.stdin does not appear to be a terminal. The PYTHONSTARTUP file is not read.

This can be useful to inspect global variables or a stack trace when a script raises an exception. See also PYTHONINSPECT.

-I
Run Python in isolated mode. This also implies -E and -s. In isolated mode sys.path contains neither the script’s directory nor the user’s site-packages directory. All PYTHON* environment variables are ignored, too. Further restrictions may be imposed to prevent the user from injecting malicious code.

New in version 3.4.

-O
Remove assert statements and any code conditional on the value of __debug__. Augment the filename for compiled (bytecode) files by adding .opt-1 before the .pyc extension (see PEP 488). See also PYTHONOPTIMIZE.

Changed in version 3.5: Modify .pyc filenames according to PEP 488.

-OO
Do -O and also discard docstrings. Augment the filename for compiled (bytecode) files by adding .opt-2 before the .pyc extension (see PEP 488).

Changed in version 3.5: Modify .pyc filenames according to PEP 488.

-q
Don’t display the copyright and version messages even in interactive mode.

New in version 3.2.

-R
Turn on hash randomization. This option only has an effect if the PYTHONHASHSEED environment variable is set to 0, since hash randomization is enabled by default.

On previous versions of Python, this option turns on hash randomization, so that the __hash__() values of str and bytes objects are “salted” with an unpredictable random value. Although they remain constant within an individual Python process, they are not predictable between repeated invocations of Python.

Hash randomization is intended to provide protection against a denial-of-service caused by carefully chosen inputs that exploit the worst case performance of a dict construction, O(n2) complexity. See http://www.ocert.org/advisories/ocert-2011-003.html for details.

PYTHONHASHSEED allows you to set a fixed value for the hash seed secret.

Changed in version 3.7: The option is no longer ignored.

New in version 3.2.3.

-s
Don’t add the user site-packages directory to sys.path.

See also PEP 370 – Per user site-packages directory
-S
Disable the import of the module site and the site-dependent manipulations of sys.path that it entails. Also disable these manipulations if site is explicitly imported later (call site.main() if you want them to be triggered).

-u
Force the stdout and stderr streams to be unbuffered. This option has no effect on the stdin stream.

See also PYTHONUNBUFFERED.

Changed in version 3.7: The text layer of the stdout and stderr streams now is unbuffered.

-v
Print a message each time a module is initialized, showing the place (filename or built-in module) from which it is loaded. When given twice (-vv), print a message for each file that is checked for when searching for a module. Also provides information on module cleanup at exit.

Changed in version 3.10: The site module reports the site-specific paths and .pth files being processed.

See also PYTHONVERBOSE.

-W arg
Warning control. Python’s warning machinery by default prints warning messages to sys.stderr.

The simplest settings apply a particular action unconditionally to all warnings emitted by a process (even those that are otherwise ignored by default):

-Wdefault  # Warn once per call location
-Werror    # Convert to exceptions
-Walways   # Warn every time
-Wmodule   # Warn once per calling module
-Wonce     # Warn once per Python process
-Wignore   # Never warn
The action names can be abbreviated as desired and the interpreter will resolve them to the appropriate action name. For example, -Wi is the same as -Wignore.

The full form of argument is:

action:message:category:module:lineno
Empty fields match all values; trailing empty fields may be omitted. For example -W ignore::DeprecationWarning ignores all DeprecationWarning warnings.

The action field is as explained above but only applies to warnings that match the remaining fields.

The message field must match the whole warning message; this match is case-insensitive.

The category field matches the warning category (ex: DeprecationWarning). This must be a class name; the match test whether the actual warning category of the message is a subclass of the specified warning category.

The module field matches the (fully qualified) module name; this match is case-sensitive.

The lineno field matches the line number, where zero matches all line numbers and is thus equivalent to an omitted line number.

Multiple -W options can be given; when a warning matches more than one option, the action for the last matching option is performed. Invalid -W options are ignored (though, a warning message is printed about invalid options when the first warning is issued).

Warnings can also be controlled using the PYTHONWARNINGS environment variable and from within a Python program using the warnings module. For example, the warnings.filterwarnings() function can be used to use a regular expression on the warning message.

See The Warnings Filter and Describing Warning Filters for more details.

-x
Skip the first line of the source, allowing use of non-Unix forms of #!cmd. This is intended for a DOS specific hack only.

-X
Reserved for various implementation-specific options. CPython currently defines the following possible values:

-X faulthandler to enable faulthandler;

-X showrefcount to output the total reference count and number of used memory blocks when the program finishes or after each statement in the interactive interpreter. This only works on debug builds.

-X tracemalloc to start tracing Python memory allocations using the tracemalloc module. By default, only the most recent frame is stored in a traceback of a trace. Use -X tracemalloc=NFRAME to start tracing with a traceback limit of NFRAME frames. See the tracemalloc.start() for more information.

-X int_max_str_digits configures the integer string conversion length limitation. See also PYTHONINTMAXSTRDIGITS.

-X importtime to show how long each import takes. It shows module name, cumulative time (including nested imports) and self time (excluding nested imports). Note that its output may be broken in multi-threaded application. Typical usage is python3 -X importtime -c 'import asyncio'. See also PYTHONPROFILEIMPORTTIME.

-X dev: enable Python Development Mode, introducing additional runtime checks that are too expensive to be enabled by default.

-X utf8 enables the Python UTF-8 Mode. -X utf8=0 explicitly disables Python UTF-8 Mode (even when it would otherwise activate automatically).

-X pycache_prefix=PATH enables writing .pyc files to a parallel tree rooted at the given directory instead of to the code tree. See also PYTHONPYCACHEPREFIX.

-X warn_default_encoding issues a EncodingWarning when the locale-specific default encoding is used for opening files. See also PYTHONWARNDEFAULTENCODING.

It also allows passing arbitrary values and retrieving them through the sys._xoptions dictionary.

Changed in version 3.2: The -X option was added.

New in version 3.3: The -X faulthandler option.

New in version 3.4: The -X showrefcount and -X tracemalloc options.

New in version 3.6: The -X showalloccount option.

New in version 3.7: The -X importtime, -X dev and -X utf8 options.

New in version 3.8: The -X pycache_prefix option. The -X dev option now logs close() exceptions in io.IOBase destructor.

Changed in version 3.9: Using -X dev option, check encoding and errors arguments on string encoding and decoding operations.

The -X showalloccount option has been removed.

New in version 3.10: The -X warn_default_encoding option.

New in version 3.10.7: The -X int_max_str_digits option.

Deprecated since version 3.9, removed in version 3.10: The -X oldparser option.

1.1.4. Options you shouldn’t use
-J
Reserved for use by Jython.

1.2. Environment variables
These environment variables influence Python’s behavior, they are processed before the command-line switches other than -E or -I. It is customary that command-line switches override environmental variables where there is a conflict.

PYTHONHOME
Change the location of the standard Python libraries. By default, the libraries are searched in prefix/lib/pythonversion and exec_prefix/lib/pythonversion, where prefix and exec_prefix are installation-dependent directories, both defaulting to /usr/local.

When PYTHONHOME is set to a single directory, its value replaces both prefix and exec_prefix. To specify different values for these, set PYTHONHOME to prefix:exec_prefix.

PYTHONPATH
Augment the default search path for module files. The format is the same as the shell’s PATH: one or more directory pathnames separated by os.pathsep (e.g. colons on Unix or semicolons on Windows). Non-existent directories are silently ignored.

In addition to normal directories, individual PYTHONPATH entries may refer to zipfiles containing pure Python modules (in either source or compiled form). Extension modules cannot be imported from zipfiles.

The default search path is installation dependent, but generally begins with prefix/lib/pythonversion (see PYTHONHOME above). It is always appended to PYTHONPATH.

An additional directory will be inserted in the search path in front of PYTHONPATH as described above under Interface options. The search path can be manipulated from within a Python program as the variable sys.path.

PYTHONPLATLIBDIR
If this is set to a non-empty string, it overrides the sys.platlibdir value.

New in version 3.9.

PYTHONSTARTUP
If this is the name of a readable file, the Python commands in that file are executed before the first prompt is displayed in interactive mode. The file is executed in the same namespace where interactive commands are executed so that objects defined or imported in it can be used without qualification in the interactive session. You can also change the prompts sys.ps1 and sys.ps2 and the hook sys.__interactivehook__ in this file.

Raises an auditing event cpython.run_startup with the filename as the argument when called on startup.

PYTHONOPTIMIZE
If this is set to a non-empty string it is equivalent to specifying the -O option. If set to an integer, it is equivalent to specifying -O multiple times.

PYTHONBREAKPOINT
If this is set, it names a callable using dotted-path notation. The module containing the callable will be imported and then the callable will be run by the default implementation of sys.breakpointhook() which itself is called by built-in breakpoint(). If not set, or set to the empty string, it is equivalent to the value “pdb.set_trace”. Setting this to the string “0” causes the default implementation of sys.breakpointhook() to do nothing but return immediately.

New in version 3.7.

PYTHONDEBUG
If this is set to a non-empty string it is equivalent to specifying the -d option. If set to an integer, it is equivalent to specifying -d multiple times.

PYTHONINSPECT
If this is set to a non-empty string it is equivalent to specifying the -i option.

This variable can also be modified by Python code using os.environ to force inspect mode on program termination.

PYTHONUNBUFFERED
If this is set to a non-empty string it is equivalent to specifying the -u option.

PYTHONVERBOSE
If this is set to a non-empty string it is equivalent to specifying the -v option. If set to an integer, it is equivalent to specifying -v multiple times.

PYTHONCASEOK
If this is set, Python ignores case in import statements. This only works on Windows and macOS.

PYTHONDONTWRITEBYTECODE
If this is set to a non-empty string, Python won’t try to write .pyc files on the import of source modules. This is equivalent to specifying the -B option.

PYTHONPYCACHEPREFIX
If this is set, Python will write .pyc files in a mirror directory tree at this path, instead of in __pycache__ directories within the source tree. This is equivalent to specifying the -X pycache_prefix=PATH option.

New in version 3.8.

PYTHONHASHSEED
If this variable is not set or set to random, a random value is used to seed the hashes of str and bytes objects.

If PYTHONHASHSEED is set to an integer value, it is used as a fixed seed for generating the hash() of the types covered by the hash randomization.

Its purpose is to allow repeatable hashing, such as for selftests for the interpreter itself, or to allow a cluster of python processes to share hash values.

The integer must be a decimal number in the range [0,4294967295]. Specifying the value 0 will disable hash randomization.

New in version 3.2.3.

PYTHONINTMAXSTRDIGITS
If this variable is set to an integer, it is used to configure the interpreter’s global integer string conversion length limitation.

New in version 3.10.7.

PYTHONIOENCODING
If this is set before running the interpreter, it overrides the encoding used for stdin/stdout/stderr, in the syntax encodingname:errorhandler. Both the encodingname and the :errorhandler parts are optional and have the same meaning as in str.encode().

For stderr, the :errorhandler part is ignored; the handler will always be 'backslashreplace'.

Changed in version 3.4: The encodingname part is now optional.

Changed in version 3.6: On Windows, the encoding specified by this variable is ignored for interactive console buffers unless PYTHONLEGACYWINDOWSSTDIO is also specified. Files and pipes redirected through the standard streams are not affected.

PYTHONNOUSERSITE
If this is set, Python won’t add the user site-packages directory to sys.path.

See also PEP 370 – Per user site-packages directory
PYTHONUSERBASE
Defines the user base directory, which is used to compute the path of the user site-packages directory and Distutils installation paths for python setup.py install --user.

See also PEP 370 – Per user site-packages directory
PYTHONEXECUTABLE
If this environment variable is set, sys.argv[0] will be set to its value instead of the value got through the C runtime. Only works on macOS.

PYTHONWARNINGS
This is equivalent to the -W option. If set to a comma separated string, it is equivalent to specifying -W multiple times, with filters later in the list taking precedence over those earlier in the list.

The simplest settings apply a particular action unconditionally to all warnings emitted by a process (even those that are otherwise ignored by default):

PYTHONWARNINGS=default  # Warn once per call location
PYTHONWARNINGS=error    # Convert to exceptions
PYTHONWARNINGS=always   # Warn every time
PYTHONWARNINGS=module   # Warn once per calling module
PYTHONWARNINGS=once     # Warn once per Python process
PYTHONWARNINGS=ignore   # Never warn
See The Warnings Filter and Describing Warning Filters for more details.

PYTHONFAULTHANDLER
If this environment variable is set to a non-empty string, faulthandler.enable() is called at startup: install a handler for SIGSEGV, SIGFPE, SIGABRT, SIGBUS and SIGILL signals to dump the Python traceback. This is equivalent to -X faulthandler option.

New in version 3.3.

PYTHONTRACEMALLOC
If this environment variable is set to a non-empty string, start tracing Python memory allocations using the tracemalloc module. The value of the variable is the maximum number of frames stored in a traceback of a trace. For example, PYTHONTRACEMALLOC=1 stores only the most recent frame. See the tracemalloc.start() for more information.

New in version 3.4.

PYTHONPROFILEIMPORTTIME
If this environment variable is set to a non-empty string, Python will show how long each import takes. This is exactly equivalent to setting -X importtime on the command line.

New in version 3.7.

PYTHONASYNCIODEBUG
If this environment variable is set to a non-empty string, enable the debug mode of the asyncio module.

New in version 3.4.

PYTHONMALLOC
Set the Python memory allocators and/or install debug hooks.

Set the family of memory allocators used by Python:

default: use the default memory allocators.

malloc: use the malloc() function of the C library for all domains (PYMEM_DOMAIN_RAW, PYMEM_DOMAIN_MEM, PYMEM_DOMAIN_OBJ).

pymalloc: use the pymalloc allocator for PYMEM_DOMAIN_MEM and PYMEM_DOMAIN_OBJ domains and use the malloc() function for the PYMEM_DOMAIN_RAW domain.

Install debug hooks:

debug: install debug hooks on top of the default memory allocators.

malloc_debug: same as malloc but also install debug hooks.

pymalloc_debug: same as pymalloc but also install debug hooks.

Changed in version 3.7: Added the "default" allocator.

New in version 3.6.

PYTHONMALLOCSTATS
If set to a non-empty string, Python will print statistics of the pymalloc memory allocator every time a new pymalloc object arena is created, and on shutdown.

This variable is ignored if the PYTHONMALLOC environment variable is used to force the malloc() allocator of the C library, or if Python is configured without pymalloc support.

Changed in version 3.6: This variable can now also be used on Python compiled in release mode. It now has no effect if set to an empty string.

PYTHONLEGACYWINDOWSFSENCODING
If set to a non-empty string, the default filesystem encoding and error handler mode will revert to their pre-3.6 values of ‘mbcs’ and ‘replace’, respectively. Otherwise, the new defaults ‘utf-8’ and ‘surrogatepass’ are used.

This may also be enabled at runtime with sys._enablelegacywindowsfsencoding().

Availability: Windows.

New in version 3.6: See PEP 529 for more details.

PYTHONLEGACYWINDOWSSTDIO
If set to a non-empty string, does not use the new console reader and writer. This means that Unicode characters will be encoded according to the active console code page, rather than using utf-8.

This variable is ignored if the standard streams are redirected (to files or pipes) rather than referring to console buffers.

Availability: Windows.

New in version 3.6.

PYTHONCOERCECLOCALE
If set to the value 0, causes the main Python command line application to skip coercing the legacy ASCII-based C and POSIX locales to a more capable UTF-8 based alternative.

If this variable is not set (or is set to a value other than 0), the LC_ALL locale override environment variable is also not set, and the current locale reported for the LC_CTYPE category is either the default C locale, or else the explicitly ASCII-based POSIX locale, then the Python CLI will attempt to configure the following locales for the LC_CTYPE category in the order listed before loading the interpreter runtime:

C.UTF-8

C.utf8

UTF-8

If setting one of these locale categories succeeds, then the LC_CTYPE environment variable will also be set accordingly in the current process environment before the Python runtime is initialized. This ensures that in addition to being seen by both the interpreter itself and other locale-aware components running in the same process (such as the GNU readline library), the updated setting is also seen in subprocesses (regardless of whether or not those processes are running a Python interpreter), as well as in operations that query the environment rather than the current C locale (such as Python’s own locale.getdefaultlocale()).

Configuring one of these locales (either explicitly or via the above implicit locale coercion) automatically enables the surrogateescape error handler for sys.stdin and sys.stdout (sys.stderr continues to use backslashreplace as it does in any other locale). This stream handling behavior can be overridden using PYTHONIOENCODING as usual.

For debugging purposes, setting PYTHONCOERCECLOCALE=warn will cause Python to emit warning messages on stderr if either the locale coercion activates, or else if a locale that would have triggered coercion is still active when the Python runtime is initialized.

Also note that even when locale coercion is disabled, or when it fails to find a suitable target locale, PYTHONUTF8 will still activate by default in legacy ASCII-based locales. Both features must be disabled in order to force the interpreter to use ASCII instead of UTF-8 for system interfaces.

Availability: *nix.

New in version 3.7: See PEP 538 for more details.

PYTHONDEVMODE
If this environment variable is set to a non-empty string, enable Python Development Mode, introducing additional runtime checks that are too expensive to be enabled by default.

New in version 3.7.

PYTHONUTF8
If set to 1, enable the Python UTF-8 Mode.

If set to 0, disable the Python UTF-8 Mode.

Setting any other non-empty string causes an error during interpreter initialisation.

New in version 3.7.

PYTHONWARNDEFAULTENCODING
If this environment variable is set to a non-empty string, issue a EncodingWarning when the locale-specific default encoding is used.

See Opt-in EncodingWarning for details.

New in version 3.10.

1.2.1. Debug-mode variables
PYTHONTHREADDEBUG
If set, Python will print threading debug info into stdout.

Need a debug build of Python.

Deprecated since version 3.10, will be removed in version 3.12.

PYTHONDUMPREFS
If set, Python will dump objects and reference counts still alive after shutting down the interpreter.

Need Python configured with the --with-trace-refs build option.

Table of Contents
1. Command line and environment
1.1. Command line
1.1.1. Interface options
1.1.2. Generic options
1.1.3. Miscellaneous options
1.1.4. Options you shouldn’t use
1.2. Environment variables
1.2.1. Debug-mode variables
Previous topic
Python Setup and Usage

Next topic
2. Using Python on Unix platforms

This Page
Report a Bug
Show Source
«
indexmodules |next |previous |python logo Python » 

English

3.10.7
 3.10.7 Documentation » Python Setup and Usage » 1. Command line and environment
Quick search
  |
© Copyright 2001-2022, Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See History and License for more information.

The Python Software Foundation is a non-profit corporation. Please donate.

Last updated on Sep 30, 2022. Found a bug?
Created using Sphinx 3.4.3.# This workflow uses actions that are not certified by GitHub.
# They are provided by a third-party and are governed by
# separate terms of service, privacy policy, and support
# documentation.

# 💁 The OpenShift Starter workflow will:
# - Checkout your repository
# - Perform a container image build
# - Push the built image to the GitHub Container Registry (GHCR)
# - Log in to your OpenShift cluster
# - Create an OpenShift app from the image and expose it to the internet

# ℹ️ Configure your repository and the workflow with the following steps:
# 1. Have access to an OpenShift cluster. Refer to https://www.openshift.com/try
# 2. Create the OPENSHIFT_SERVER and OPENSHIFT_TOKEN repository secrets. Refer to:
#   - https://github.com/redhat-actions/oc-login#readme
#   - https://docs.github.com/en/actions/reference/encrypted-secrets
#   - https://cli.github.com/manual/gh_secret_set
# 3. (Optional) Edit the top-level 'env' section as marked with '🖊️' if the defaults are not suitable for your project.
# 4. (Optional) Edit the build-image step to build your project.
#    The default build type is by using a Dockerfile at the root of the repository,
#    but can be replaced with a different file, a source-to-image build, or a step-by-step buildah build.
# 5. Commit and push the workflow file to your default branch to trigger a workflow run.

# 👋 Visit our GitHub organization at https://github.com/redhat-actions/ to see our actions and provide feedback.

name: OpenShift

env:
  # 🖊️ EDIT your repository secrets to log into your OpenShift cluster and set up the context.
  # See https://github.com/redhat-actions/oc-login#readme for how to retrieve these values.
  # To get a permanent token, refer to https://github.com/redhat-actions/oc-login/wiki/Using-a-Service-Account-for-GitHub-Actions
  OPENSHIFT_SERVER: ${{ secrets.OPENSHIFT_SERVER }}
  OPENSHIFT_TOKEN: ${{ secrets.OPENSHIFT_TOKEN }}
  # 🖊️ EDIT to set the kube context's namespace after login. Leave blank to use your user's default namespace.
  OPENSHIFT_NAMESPACE: ""

  # 🖊️ EDIT to set a name for your OpenShift app, or a default one will be generated below.
  APP_NAME: ""

  # 🖊️ EDIT with the port your application should be accessible on.
  # If the container image exposes *exactly one* port, this can be left blank.
  # Refer to the 'port' input of https://github.com/redhat-actions/oc-new-app
  APP_PORT: ""

  # 🖊️ EDIT to change the image registry settings.
  # Registries such as GHCR, Quay.io, and Docker Hub are supported.
  IMAGE_REGISTRY: ghcr.io/${{ github.repository_owner }}
  IMAGE_REGISTRY_USER: ${{ github.actor }}
  IMAGE_REGISTRY_PASSWORD: ${{ github.token }}

  # 🖊️ EDIT to specify custom tags for the container image, or default tags will be generated below.
  IMAGE_TAGS: ""

on:
  # https://docs.github.com/en/actions/reference/events-that-trigger-workflows
  workflow_dispatch:
  push:
    # Edit to the branch(es) you want to build and deploy on each push.
    branches: [ "paradice" ]

jobs:
  # 🖊️ EDIT if you want to run vulnerability check on your project before deploying
  # the application. Please uncomment the below CRDA scan job and configure to run it in
  # your workflow. For details about CRDA action visit https://github.com/redhat-actions/crda/blob/main/README.md
  #
  # TODO: Make sure to add 'CRDA Scan' starter workflow from the 'Actions' tab.
  # For guide on adding new starter workflow visit https://docs.github.com/en/github-ae@latest/actions/using-workflows/using-starter-workflows

  crda-scan:
    uses: ./.github/workflows/crda.yml
    secrets:
      CRDA_KEY: ${{ secrets.CRDA_KEY }}
      # SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}       # Either use SNYK_TOKEN or CRDA_KEY

  openshift-ci-cd:
    # 🖊️ Uncomment this if you are using CRDA scan step above
    # needs: crda-scan
    name: Build and deploy to OpenShift
    runs-on: ubuntu-20.04
    environment: production

    outputs:
      ROUTE: ${{ steps.deploy-and-expose.outputs.route }}
      SELECTOR: ${{ steps.deploy-and-expose.outputs.selector }}

    steps:
    - name: Check for required secrets
      uses: actions/github-script@v6
      with:
        script: |
          const secrets = {
            OPENSHIFT_SERVER: `${{ secrets.OPENSHIFT_SERVER }}`,
            OPENSHIFT_TOKEN: `${{ secrets.OPENSHIFT_TOKEN }}`,
          };

          const GHCR = "ghcr.io";
          if (`${{ env.IMAGE_REGISTRY }}`.startsWith(GHCR)) {
            core.info(`Image registry is ${GHCR} - no registry password required`);
          }
          else {
            core.info("A registry password is required");
            secrets["IMAGE_REGISTRY_PASSWORD"] = `${{ secrets.IMAGE_REGISTRY_PASSWORD }}`;
          }

          const missingSecrets = Object.entries(secrets).filter(([ name, value ]) => {
            if (value.length === 0) {
              core.error(`Secret "${name}" is not set`);
              return true;
            }
            core.info(`✔️ Secret "${name}" is set`);
            return false;
          });

          if (missingSecrets.length > 0) {
            core.setFailed(`❌ At least one required secret is not set in the repository. \n` +
              "You can add it using:\n" +
              "GitHub UI: https://docs.github.com/en/actions/reference/encrypted-secrets#creating-encrypted-secrets-for-a-repository \n" +
              "GitHub CLI: https://cli.github.com/manual/gh_secret_set \n" +
              "Also, refer to https://github.com/redhat-actions/oc-login#getting-started-with-the-action-or-see-example");
          }
          else {
            core.info(`✅ All the required secrets are set`);
          }

    - name: Check out repository
      uses: actions/checkout@v3

    - name: Determine app name
      if: env.APP_NAME == ''
      run: |
        echo "APP_NAME=$(basename $PWD)" | tee -a $GITHUB_ENV

    - name: Determine image tags
      if: env.IMAGE_TAGS == ''
      run: |
        echo "IMAGE_TAGS=latest ${GITHUB_SHA::12}" | tee -a $GITHUB_ENV

    # https://github.com/redhat-actions/buildah-build#readme
    - name: Build from Dockerfile
      id: build-image
      uses: redhat-actions/buildah-build@v2
      with:
        image: ${{ env.APP_NAME }}
        tags: ${{ env.IMAGE_TAGS }}

        # If you don't have a Dockerfile/Containerfile, refer to https://github.com/redhat-actions/buildah-build#scratch-build-inputs
        # Or, perform a source-to-image build using https://github.com/redhat-actions/s2i-build
        # Otherwise, point this to your Dockerfile/Containerfile relative to the repository root.
        dockerfiles: |
          ./Dockerfile

    # https://github.com/redhat-actions/push-to-registry#readme
    - name: Push to registry
      id: push-image
      uses: redhat-actions/push-to-registry@v2
      with:
        image: ${{ steps.build-image.outputs.image }}
        tags: ${{ steps.build-image.outputs.tags }}
        registry: ${{ env.IMAGE_REGISTRY }}
        username: ${{ env.IMAGE_REGISTRY_USER }}
        password: ${{ env.IMAGE_REGISTRY_PASSWORD }}

    # The path the image was pushed to is now stored in ${{ steps.push-image.outputs.registry-path }}

    - name: Install oc
      uses: redhat-actions/openshift-tools-installer@v1
      with:
        oc: 4

    # https://github.com/redhat-actions/oc-login#readme
    - name: Log in to OpenShift
      uses: redhat-actions/oc-login@v1
      with:
        openshift_server_url: ${{ env.OPENSHIFT_SERVER }}
        openshift_token: ${{ env.OPENSHIFT_TOKEN }}
        insecure_skip_tls_verify: true
        namespace: ${{ env.OPENSHIFT_NAMESPACE }}

    # This step should create a deployment, service, and route to run your app and expose it to the internet.
    # https://github.com/redhat-actions/oc-new-app#readme
    - name: Create and expose app
      id: deploy-and-expose
      uses: redhat-actions/oc-new-app@v1
      with:
        app_name: ${{ env.APP_NAME }}
        image: ${{ steps.push-image.outputs.registry-path }}
        namespace: ${{ env.OPENSHIFT_NAMESPACE }}
        port: ${{ env.APP_PORT }}

    - name: Print application URL
      env:
        ROUTE: ${{ steps.deploy-and-expose.outputs.route }}
        SELECTOR: ${{ steps.deploy-and-expose.outputs.selector }}
      run: |
        [[ -n ${{ env.ROUTE }} ]] || (echo "Determining application route failed in previous step"; exit 1)
        echo
        echo "======================== Your application is available at: ========================"
        echo ${{ env.ROUTE }}
        echo "==================================================================================="
        echo
        echo "Your app can be taken down with: \"oc delete all --selector='${Skip to content

Search…
All gists
Back to GitHub
@zakwarlord7 
Your account has been flagged.
Because of that, your profile is hidden from the public. If you believe this is a mistake, contact support to have your account status reviewed.
@zakwarlord7
zakwarlord7/BITORE_34173 Secret
Last active now
1
Code
Revisions
6
Stars
1
<script src="https://gist.github.com/zakwarlord7/97168e256ecd3ddda090253a901fc349.js"></script>
((c)(r))
BITORE_34173
Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore

@zakwarlord7 
Your account has been flagged.
Because of that, your profile is hidden from the public. If you believe this is a mistake, contact support to have your account status reviewed.
zakwarlord7
/
Patch-5
Public
generated from zakwarlord7/peter-evans-create-pull-request
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
Initialize main
 main
@zakwarlord7
zakwarlord7 committed 9 days ago 
0 parents commit a0e21ef989cd84f37c125a5925bebd2f2724006b
Show file tree Hide file tree
Showing 40 changed files with 32,705 additions and 0 deletions.
 3  
.eslintignore
@@ -0,0 +1,3 @@
dist/
lib/
node_modules/
 23  
.eslintrc.json
@@ -0,0 +1,23 @@
{
  "env": { "node": true, "jest": true },
  "parser": "@typescript-eslint/parser",
  "parserOptions": { "ecmaVersion": 9, "sourceType": "module" },
  "extends": [
    "eslint:recommended",
    "plugin:@typescript-eslint/eslint-recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:import/errors",
    "plugin:import/warnings",
    "plugin:import/typescript",
    "plugin:prettier/recommended"
  ],
  "plugins": ["@typescript-eslint"],
  "rules": {
    "@typescript-eslint/camelcase": "off"
  },
  "settings": {
    "import/resolver": {
      "typescript": {}
    }
  }
}
 1  
.github/FUNDING.yml
@@ -0,0 +1 @@
github: peter-evans
 7  
.github/ISSUE_TEMPLATE.md
@@ -0,0 +1,7 @@
### Subject of the issue

Describe your issue here.

### Steps to reproduce

If this issue is describing a possible bug please provide (or link to) your GitHub Actions workflow.
 8  
.github/dependabot.yml
@@ -0,0 +1,8 @@
version: 2
updates:
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
    labels:
      - "dependencies"
 134  
.github/workflows/ci.yml
@@ -0,0 +1,134 @@
name: CI
on:
  push:
    branches: [main]
    paths-ignore:
      - 'README.md'
      - 'docs/**'
  pull_request:
    branches: [main]
    paths-ignore:
      - 'README.md'
      - 'docs/**'

permissions:
  pull-requests: write
  contents: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: 16.x
          cache: npm
      - run: npm ci
      - run: npm run build
      - run: npm run format-check
      - run: npm run lint
      - run: npm run test
      - uses: actions/upload-artifact@v3
        with:
          name: dist
          path: dist
      - uses: actions/upload-artifact@v3
        with:
          name: action.yml
          path: action.yml

  test:
    if: github.event_name == 'push' || github.event.pull_request.head.repo.full_name == github.repository
    needs: [build]
    runs-on: ubuntu-latest
    strategy:
      matrix:
        target: [built, committed]
    steps:
      - uses: actions/checkout@v3
        with:
          ref: main
      - if: matrix.target == 'built' || github.event_name == 'pull_request'
        uses: actions/download-artifact@v3
        with:
          name: dist
          path: dist
      - if: matrix.target == 'built' || github.event_name == 'pull_request'
        uses: actions/download-artifact@v3
        with:
          name: action.yml
          path: .

      - name: Create change
        run: date +%s > report.txt

      - name: Create Pull Request
        id: cpr
        uses: ./
        with:
          commit-message: '[CI] test ${{ matrix.target }}'
          committer: GitHub <noreply@github.com>
          author: ${{ github.actor }} <${{ github.actor }}@users.noreply.github.com>
          title: '[CI] test ${{ matrix.target }}'
          body: |
            - CI test case for target '${{ matrix.target }}'
            Auto-generated by [create-pull-request][1]
            [1]: https://github.com/peter-evans/create-pull-request
          branch: ci-test-${{ matrix.target }}

      - name: Close Pull
        uses: peter-evans/close-pull@v2
        with:
          pull-request-number: ${{ steps.cpr.outputs.pull-request-number }}
          comment: '[CI] test ${{ matrix.target }}'
          delete-branch: true

  commentTestSuiteHelp:
    if: github.event_name == 'pull_request'
    needs: [test]
    runs-on: ubuntu-latest
    steps:
      - name: Find Comment
        uses: peter-evans/find-comment@v2
        id: fc
        with:
          issue-number: ${{ github.event.number }}
          comment-author: 'github-actions[bot]'
          body-includes: Full test suite slash command

      - if: steps.fc.outputs.comment-id == ''
        name: Create comment
        uses: peter-evans/create-or-update-comment@v2
        with:
          issue-number: ${{ github.event.number }}
          body: |
            Full test suite slash command (repository admin only)
            ```
            /test repository=${{ github.event.pull_request.head.repo.full_name }} ref=${{ github.event.pull_request.head.ref }} build=true
            ```
  package:
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    needs: [test]
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/download-artifact@v3
        with:
          name: dist
          path: dist
      - name: Create Pull Request
        uses: peter-evans/create-pull-request@v4
        with:
          commit-message: 'build: update distribution'
          title: Update distribution
          body: |
            - Updates the distribution for changes on `main`
            Auto-generated by [create-pull-request][1]
            [1]: https://github.com/peter-evans/create-pull-request
          branch: update-distribution
 49  
.github/workflows/cpr-example-command.yml
@@ -0,0 +1,49 @@
name: Create Pull Request Example Command
on:
  repository_dispatch:
    types: [cpr-example-command]
jobs:
  createPullRequest:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Make changes to pull request
        run: date +%s > report.txt

      - name: Create Pull Request
        id: cpr
        uses: ./
        with:
          commit-message: Update report
          committer: GitHub <noreply@github.com>
          author: ${{ github.actor }} <${{ github.actor }}@users.noreply.github.com>
          signoff: false
          title: '[Example] Update report'
          body: |
            Update report
            - Updated with *today's* date
            - Auto-generated by [create-pull-request][1]
            [1]: https://github.com/peter-evans/create-pull-request
          labels: |
            report
            automated pr
          assignees: peter-evans
          reviewers: peter-evans
          milestone: 1
          draft: false
          branch: example-patches
          delete-branch: true

      - name: Check output
        run: |
          echo "Pull Request Number - ${{ steps.cpr.outputs.pull-request-number }}"
          echo "Pull Request URL - ${{ steps.cpr.outputs.pull-request-url }}"
      - name: Add reaction
        uses: peter-evans/create-or-update-comment@v2
        with:
          repository: ${{ github.event.client_payload.github.payload.repository.full_name }}
          comment-id: ${{ github.event.client_payload.github.payload.comment.id }}
          reaction-type: hooray
 37  
.github/workflows/slash-command-dispatch.yml
@@ -0,0 +1,37 @@
name: Slash Command Dispatch
on:
  issue_comment:
    types: [created]
jobs:
  slashCommandDispatch:
    runs-on: ubuntu-latest
    steps:
      - name: Slash Command Dispatch
        uses: peter-evans/slash-command-dispatch@v3
        with:
          token: ${{ secrets.ACTIONS_BOT_TOKEN }}
          config: >
            [
              {
                "command": "test",
                "permission": "admin",
                "repository": "peter-evans/create-pull-request-tests",
                "named_args": true
              },
              {
                "command": "clean",
                "permission": "admin",
                "repository": "peter-evans/create-pull-request-tests"
              },
              {
                "command": "cpr-example",
                "permission": "admin",
                "issue_type": "issue"
              },
              {
                "command": "rebase",
                "permission": "admin",
                "repository": "peter-evans/slash-command-dispatch-processor",
                "issue_type": "pull-request"
              }
            ]
 5  
.gitignore
@@ -0,0 +1,5 @@
lib/
node_modules/

.DS_Store
.idea
 3  
.prettierignore
@@ -0,0 +1,3 @@
dist/
lib/
node_modules/
 11  
.prettierrc.json
@@ -0,0 +1,11 @@
{
  "printWidth": 80,
  "tabWidth": 2,
  "useTabs": false,
  "semi": false,
  "singleQuote": true,
  "trailingComma": "none",
  "bracketSpacing": false,
  "arrowParens": "avoid",
  "parser": "typescript"
}
 21  
LICENSE
@@ -0,0 +1,21 @@
MIT License

Copyright (c) 2019 Peter Evans

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
 267  
README.md
@@ -0,0 +1,267 @@
# <img width="24" height="24" src="docs/assets/logo.svg"> Create Pull Request
[![CI](https://github.com/peter-evans/create-pull-request/workflows/CI/badge.svg)](https://github.com/peter-evans/create-pull-request/actions?query=workflow%3ACI)
[![GitHub Marketplace](https://img.shields.io/badge/Marketplace-Create%20Pull%20Request-blue.svg?colorA=24292e&colorB=0366d6&style=flat&longCache=true&logo=github)](https://github.com/marketplace/actions/create-pull-request)

A GitHub action to create a pull request for changes to your repository in the actions workspace.

Changes to a repository in the Actions workspace persist between steps in a workflow.
This action is designed to be used in conjunction with other steps that modify or add files to your repository.
The changes will be automatically committed to a new branch and a pull request created.

Create Pull Request action will:

1. Check for repository changes in the Actions workspace. This includes:
   - untracked (new) files
   - tracked (modified) files
   - commits made during the workflow that have not been pushed
2. Commit all changes to a new branch, or update an existing pull request branch.
3. Create a pull request to merge the new branch into the base&mdash;the branch checked out in the workflow.

## Documentation

- [Concepts, guidelines and advanced usage](docs/concepts-guidelines.md)
- [Examples](docs/examples.md)
- [Updating to v4](docs/updating.md)

## Usage

```yml
      - uses: actions/checkout@v3
      # Make changes to pull request here
      - name: Create Pull Request
        uses: peter-evans/create-pull-request@v4
```

You can also pin to a [specific release](https://github.com/peter-evans/create-pull-request/releases) version in the format `@v4.x.x`

### Workflow permissions

For this action to work you must explicitly allow GitHub Actions to create pull requests.
This setting can be found in a repository's settings under Actions > General > Workflow permissions.

For repositories belonging to an organization, this setting can be managed by admins in organization settings under Actions > General > Workflow permissions.

### Action inputs

All inputs are **optional**. If not set, sensible defaults will be used.

**Note**: If you want pull requests created by this action to trigger an `on: push` or `on: pull_request` workflow then you cannot use the default `GITHUB_TOKEN`. See the [documentation here](docs/concepts-guidelines.md#triggering-further-workflow-runs) for workarounds.

| Name | Description | Default |
| --- | --- | --- |
| `token` | `GITHUB_TOKEN` (permissions `contents: write` and `pull-requests: write`) or a `repo` scoped [Personal Access Token (PAT)](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token). | `GITHUB_TOKEN` |
| `path` | Relative path under `GITHUB_WORKSPACE` to the repository. | `GITHUB_WORKSPACE` |
| `add-paths` | A comma or newline-separated list of file paths to commit. Paths should follow git's [pathspec](https://git-scm.com/docs/gitglossary#Documentation/gitglossary.txt-aiddefpathspecapathspec) syntax. If no paths are specified, all new and modified files are added. See [Add specific paths](#add-specific-paths). | |
| `commit-message` | The message to use when committing changes. | `[create-pull-request] automated change` |
| `committer` | The committer name and email address in the format `Display Name <email@address.com>`. Defaults to the GitHub Actions bot user. | `GitHub <noreply@github.com>` |
| `author` | The author name and email address in the format `Display Name <email@address.com>`. Defaults to the user who triggered the workflow run. | `${{ github.actor }} <${{ github.actor }}@users.noreply.github.com>` |
| `signoff` | Add [`Signed-off-by`](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---signoff) line by the committer at the end of the commit log message. | `false` |
| `branch` | The pull request branch name. | `create-pull-request/patch` |
| `delete-branch` | Delete the `branch` when closing pull requests, and when undeleted after merging. Recommend `true`. | `false` |
| `branch-suffix` | The branch suffix type when using the alternative branching strategy. Valid values are `random`, `timestamp` and `short-commit-hash`. See [Alternative strategy](#alternative-strategy---always-create-a-new-pull-request-branch) for details. | |
| `base` | Sets the pull request base branch. | Defaults to the branch checked out in the workflow. |
| `push-to-fork` | A fork of the checked-out parent repository to which the pull request branch will be pushed. e.g. `owner/repo-fork`. The pull request will be created to merge the fork's branch into the parent's base. See [push pull request branches to a fork](docs/concepts-guidelines.md#push-pull-request-branches-to-a-fork) for details. | |
| `title` | The title of the pull request. | `Changes by create-pull-request action` |
| `body` | The body of the pull request. | `Automated changes by [create-pull-request](https://github.com/peter-evans/create-pull-request) GitHub action` |
| `labels` | A comma or newline-separated list of labels. | |
| `assignees` | A comma or newline-separated list of assignees (GitHub usernames). | |
| `reviewers` | A comma or newline-separated list of reviewers (GitHub usernames) to request a review from. | |
| `team-reviewers` | A comma or newline-separated list of GitHub teams to request a review from. Note that a `repo` scoped [PAT](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token) may be required. See [this issue](https://github.com/peter-evans/create-pull-request/issues/155). If using a GitHub App, refer to [Authenticating with GitHub App generated tokens](docs/concepts-guidelines.md#authenticating-with-github-app-generated-tokens) for the proper permissions. | |
| `milestone` | The number of the milestone to associate this pull request with. | |
| `draft` | Create a [draft pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests#draft-pull-requests). It is not possible to change draft status after creation except through the web interface. | `false` |

For self-hosted runners behind a corporate proxy set the `https_proxy` environment variable.
```yml
      - name: Create Pull Request
        uses: peter-evans/create-pull-request@v4
        env:
          https_proxy: http://<proxy_address>:<port>
```

### Action outputs

The following outputs can be used by subsequent workflow steps.

- `pull-request-number` - The pull request number.
- `pull-request-url` - The URL of the pull request.
- `pull-request-operation` - The pull request operation performed by the action, `created`, `updated` or `closed`.
- `pull-request-head-sha` - The commit SHA of the pull request branch.

Step outputs can be accessed as in the following example.
Note that in order to read the step outputs the action step must have an id.

```yml
      - name: Create Pull Request
        id: cpr
        uses: peter-evans/create-pull-request@v4
      - name: Check outputs
        if: ${{ steps.cpr.outputs.pull-request-number }}
        run: |
          echo "Pull Request Number - ${{ steps.cpr.outputs.pull-request-number }}"
          echo "Pull Request URL - ${{ steps.cpr.outputs.pull-request-url }}"
```

### Action behaviour

The default behaviour of the action is to create a pull request that will be continually updated with new changes until it is merged or closed.
Changes are committed and pushed to a fixed-name branch, the name of which can be configured with the `branch` input.
Any subsequent changes will be committed to the *same* branch and reflected in the open pull request.

How the action behaves:

- If there are changes (i.e. a diff exists with the checked-out base branch), the changes will be pushed to a new `branch` and a pull request created.
- If there are no changes (i.e. no diff exists with the checked-out base branch), no pull request will be created and the action exits silently.
- If a pull request already exists it will be updated if necessary. Local changes in the Actions workspace, or changes on the base branch, can cause an update. If no update is required the action exits silently.
- If a pull request exists and new changes on the base branch make the pull request unnecessary (i.e. there is no longer a diff between the pull request branch and the base), the pull request is automatically closed. Additionally, if `delete-branch` is set to `true` the `branch` will be deleted.

For further details about how the action works and usage guidelines, see [Concepts, guidelines and advanced usage](docs/concepts-guidelines.md).

#### Alternative strategy - Always create a new pull request branch

For some use cases it may be desirable to always create a new unique branch each time there are changes to be committed.
This strategy is *not recommended* because if not used carefully it could result in multiple pull requests being created unnecessarily. If in doubt, use the [default strategy](#action-behaviour) of creating an updating a fixed-name branch.

To use this strategy, set input `branch-suffix` with one of the following options.

- `random` - Commits will be made to a branch suffixed with a random alpha-numeric string. e.g. `create-pull-request/patch-6qj97jr`, `create-pull-request/patch-5jrjhvd`

- `timestamp` - Commits will be made to a branch suffixed by a timestamp. e.g. `create-pull-request/patch-1569322532`, `create-pull-request/patch-1569322552`

- `short-commit-hash` - Commits will be made to a branch suffixed with the short SHA1 commit hash. e.g. `create-pull-request/patch-fcdfb59`, `create-pull-request/patch-394710b`

### Controlling committed files

The action defaults to adding all new and modified files.
If there are files that should not be included in the pull request, you can use the following methods to control the committed content.

#### Remove files

The most straightforward way to handle unwanted files is simply to remove them in a step before the action runs.

```yml
      - run: |
          rm -rf temp-dir
          rm temp-file.txt
```

#### Ignore files

If there are files or directories you want to ignore you can simply add them to a `.gitignore` file at the root of your repository. The action will respect this file.

#### Add specific paths

You can control which files are committed with the `add-paths` input.
Paths should follow git's [pathspec](https://git-scm.com/docs/gitglossary#Documentation/gitglossary.txt-aiddefpathspecapathspec) syntax.
All file changes that do not match one of the paths will be discarded.

```yml
      - name: Create Pull Request
        uses: peter-evans/create-pull-request@v4
        with:
          add-paths: |
            *.java
            docs/*.md
```

#### Create your own commits

As well as relying on the action to handle uncommitted changes, you can additionally make your own commits before the action runs.
Note that the repository must be checked out on a branch with a remote, it won't work for [events which checkout a commit](docs/concepts-guidelines.md#events-which-checkout-a-commit).

```yml
    steps:
      - uses: actions/checkout@v3
      - name: Create commits
        run: |
          git config user.name 'Peter Evans'
          git config user.email 'peter-evans@users.noreply.github.com'
          date +%s > report.txt
          git commit -am "Modify tracked file during workflow"
          date +%s > new-report.txt
          git add -A
          git commit -m "Add untracked file during workflow"
      - name: Uncommitted change
        run: date +%s > report.txt
      - name: Create Pull Request
        uses: peter-evans/create-pull-request@v4
```

### Create a project card

To create a project card for the pull request, pass the `pull-request-number` step output to [create-or-update-project-card](https://github.com/peter-evans/create-or-update-project-card) action.

```yml
      - name: Create Pull Request
        id: cpr
        uses: peter-evans/create-pull-request@v4
      - name: Create or Update Project Card
        if: ${{ steps.cpr.outputs.pull-request-number }}
        uses: peter-evans/create-or-update-project-card@v2
        with:
          project-name: My project
          column-name: My column
          issue-number: ${{ steps.cpr.outputs.pull-request-number }}
```

### Auto-merge

Auto-merge can be enabled on a pull request allowing it to be automatically merged once requirements have been satisfied.
See [enable-pull-request-automerge](https://github.com/peter-evans/enable-pull-request-automerge) action for usage details.

## Reference Example

The following workflow sets many of the action's inputs for reference purposes.
Check the [defaults](#action-inputs) to avoid setting inputs unnecessarily.

See [examples](docs/examples.md) for more realistic use cases.

```yml
jobs:
  createPullRequest:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Make changes to pull request
        run: date +%s > report.txt
      - name: Create Pull Request
        id: cpr
        uses: peter-evans/create-pull-request@v4
        with:
          token: ${{ secrets.PAT }}
          commit-message: Update report
          committer: GitHub <noreply@github.com>
          author: ${{ github.actor }} <${{ github.actor }}@users.noreply.github.com>
          signoff: false
          branch: example-patches
          delete-branch: true
          title: '[Example] Update report'
          body: |
            Update report
            - Updated with *today's* date
            - Auto-generated by [create-pull-request][1]
            [1]: https://github.com/peter-evans/create-pull-request
          labels: |
            report
            automated pr
          assignees: peter-evans
          reviewers: peter-evans
          team-reviewers: |
            owners
            maintainers
          milestone: 1
          draft: false
```

An example based on the above reference configuration creates pull requests that look like this:

![Pull Request Example](docs/assets/pull-request-example.png)

## License

[MIT](LICENSE)
 1,942  
__test__/create-or-update-branch.int.test.ts
Large diffs are not rendered by default.

 40  
__test__/entrypoint.sh
@@ -0,0 +1,40 @@
#!/bin/sh -l
set -euo pipefail

# Save the working directory
WORKINGDIR=$PWD

# Create and serve a remote repo
mkdir -p /git/remote
git init --bare /git/remote/test-base.git
git daemon --verbose --enable=receive-pack --base-path=/git/remote --export-all /git/remote &>/dev/null &

# Give the daemon time to start
sleep 2

# Create a local clone and make an initial commit
mkdir -p /git/local
git clone git://127.0.0.1/test-base.git /git/local/test-base
cd /git/local/test-base
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
echo "#test-base" > README.md
git add .
git commit -m "initial commit"
git push -u
git log -1 --pretty=oneline
git config --global --unset user.email
git config --global --unset user.name
git config -l

# Clone a server-side fork of the base repo
cd $WORKINGDIR
git clone --mirror git://127.0.0.1/test-base.git /git/remote/test-fork.git
cd /git/remote/test-fork.git
git log -1 --pretty=oneline

# Restore the working directory
cd $WORKINGDIR

# Execute integration tests
jest int --runInBand
 49  
__test__/git-auth-helper.int.test.ts
@@ -0,0 +1,49 @@
import {GitCommandManager} from '../lib/git-command-manager'
import {GitAuthHelper} from '../lib/git-auth-helper'

const REPO_PATH = '/git/local/test-base'

const extraheaderConfigKey = 'http.https://github.com/.extraheader'

describe('git-auth-helper tests', () => {
  let git: GitCommandManager
  let gitAuthHelper: GitAuthHelper

  beforeAll(async () => {
    git = await GitCommandManager.create(REPO_PATH)
    gitAuthHelper = new GitAuthHelper(git)
  })

  it('tests save and restore with no persisted auth', async () => {
    await gitAuthHelper.savePersistedAuth()
    await gitAuthHelper.restorePersistedAuth()
  })

  it('tests configure and removal of auth', async () => {
    await gitAuthHelper.configureToken('github-token')
    expect(await git.configExists(extraheaderConfigKey)).toBeTruthy()
    expect(await git.getConfigValue(extraheaderConfigKey)).toEqual(
      'AUTHORIZATION: basic eC1hY2Nlc3MtdG9rZW46Z2l0aHViLXRva2Vu'
    )

    await gitAuthHelper.removeAuth()
    expect(await git.configExists(extraheaderConfigKey)).toBeFalsy()
  })

  it('tests save and restore of persisted auth', async () => {
    const extraheaderConfigValue = 'AUTHORIZATION: basic ***persisted-auth***'
    await git.config(extraheaderConfigKey, extraheaderConfigValue)

    await gitAuthHelper.savePersistedAuth()

    const exists = await git.configExists(extraheaderConfigKey)
    expect(exists).toBeFalsy()

    await gitAuthHelper.restorePersistedAuth()

    const configValue = await git.getConfigValue(extraheaderConfigKey)
    expect(configValue).toEqual(extraheaderConfigValue)

    await gitAuthHelper.removeAuth()
  })
})
 23  
__test__/integration-tests.sh
@@ -0,0 +1,23 @@
#!/usr/bin/env bash
set -euo pipefail

IMAGE="cpr-integration-tests:latest"
ARG1=${1:-}

if [[ "$(docker images -q $IMAGE 2> /dev/null)" == "" || $ARG1 == "build" ]]; then
    echo "Building Docker image $IMAGE ..."

    cat > Dockerfile << EOF
FROM node:16-alpine
RUN apk --no-cache add git git-daemon
RUN npm install jest jest-environment-jsdom --global
WORKDIR /cpr
COPY __test__/entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
EOF

    docker build --no-cache -t $IMAGE .
    rm Dockerfile
fi

docker run -v $PWD:/cpr $IMAGE
 130  
__test__/utils.unit.test.ts
@@ -0,0 +1,130 @@
import * as path from 'path'
import * as utils from '../lib/utils'

const originalGitHubWorkspace = process.env['GITHUB_WORKSPACE']

describe('utils tests', () => {
  beforeAll(() => {
    // GitHub workspace
    process.env['GITHUB_WORKSPACE'] = __dirname
  })

  afterAll(() => {
    // Restore GitHub workspace
    delete process.env['GITHUB_WORKSPACE']
    if (originalGitHubWorkspace) {
      process.env['GITHUB_WORKSPACE'] = originalGitHubWorkspace
    }
  })

  test('getStringAsArray splits string input by newlines and commas', async () => {
    const array = utils.getStringAsArray('1, 2, 3\n4, 5, 6')
    expect(array.length).toEqual(6)

    const array2 = utils.getStringAsArray('')
    expect(array2.length).toEqual(0)
  })

  test('getRepoPath successfully returns the path to the repository', async () => {
    expect(utils.getRepoPath()).toEqual(process.env['GITHUB_WORKSPACE'])
    expect(utils.getRepoPath('foo')).toEqual(
      path.resolve(process.env['GITHUB_WORKSPACE'] || '', 'foo')
    )
  })

  test('getRemoteDetail successfully parses remote URLs', async () => {
    const remote1 = utils.getRemoteDetail(
      'https://github.com/peter-evans/create-pull-request'
    )
    expect(remote1.protocol).toEqual('HTTPS')
    expect(remote1.repository).toEqual('peter-evans/create-pull-request')

    const remote2 = utils.getRemoteDetail(
      'https://xxx:x-oauth-basic@github.com/peter-evans/create-pull-request'
    )
    expect(remote2.protocol).toEqual('HTTPS')
    expect(remote2.repository).toEqual('peter-evans/create-pull-request')

    const remote3 = utils.getRemoteDetail(
      'git@github.com:peter-evans/create-pull-request.git'
    )
    expect(remote3.protocol).toEqual('SSH')
    expect(remote3.repository).toEqual('peter-evans/create-pull-request')

    const remote4 = utils.getRemoteDetail(
      'https://github.com/peter-evans/create-pull-request.git'
    )
    expect(remote4.protocol).toEqual('HTTPS')
    expect(remote4.repository).toEqual('peter-evans/create-pull-request')
  })

  test('getRemoteDetail fails to parse a remote URL', async () => {
    const remoteUrl = 'https://github.com/peter-evans'
    try {
      utils.getRemoteDetail(remoteUrl)
      // Fail the test if an error wasn't thrown
      expect(true).toEqual(false)
    } catch (e: any) {
      expect(e.message).toEqual(
        `The format of '${remoteUrl}' is not a valid GitHub repository URL`
      )
    }
  })

  test('getRemoteUrl successfully returns remote URLs', async () => {
    const url1 = utils.getRemoteUrl('HTTPS', 'peter-evans/create-pull-request')
    expect(url1).toEqual('https://github.com/peter-evans/create-pull-request')

    const url2 = utils.getRemoteUrl('SSH', 'peter-evans/create-pull-request')
    expect(url2).toEqual('git@github.com:peter-evans/create-pull-request.git')
  })

  test('secondsSinceEpoch returns the number of seconds since the Epoch', async () => {
    const seconds = `${utils.secondsSinceEpoch()}`
    expect(seconds.length).toEqual(10)
  })

  test('randomString returns strings of length 7', async () => {
    for (let i = 0; i < 1000; i++) {
      expect(utils.randomString().length).toEqual(7)
    }
  })

  test('parseDisplayNameEmail successfully parses display name email formats', async () => {
    const parsed1 = utils.parseDisplayNameEmail('abc def <abc@def.com>')
    expect(parsed1.name).toEqual('abc def')
    expect(parsed1.email).toEqual('abc@def.com')

    const parsed2 = utils.parseDisplayNameEmail(
      'github-actions[bot] <41898282+github-actions[bot]@users.noreply.github.com>'
    )
    expect(parsed2.name).toEqual('github-actions[bot]')
    expect(parsed2.email).toEqual(
      '41898282+github-actions[bot]@users.noreply.github.com'
    )
  })

  test('parseDisplayNameEmail fails to parse display name email formats', async () => {
    const displayNameEmail1 = 'abc@def.com'
    try {
      utils.parseDisplayNameEmail(displayNameEmail1)
      // Fail the test if an error wasn't thrown
      expect(true).toEqual(false)
    } catch (e: any) {
      expect(e.message).toEqual(
        `The format of '${displayNameEmail1}' is not a valid email address with display name`
      )
    }

    const displayNameEmail2 = ' < >'
    try {
      utils.parseDisplayNameEmail(displayNameEmail2)
      // Fail the test if an error wasn't thrown
      expect(true).toEqual(false)
    } catch (e: any) {
      expect(e.message).toEqual(
        `The format of '${displayNameEmail2}' is not a valid email address with display name`
      )
    }
  })
})
 86  
action.yml
@@ -0,0 +1,86 @@
name: 'Create Pull Request'
description: 'Creates a pull request for changes to your repository in the actions workspace'
inputs:
  token:
    description: 'GITHUB_TOKEN or a `repo` scoped Personal Access Token (PAT)'
    default: ${{ github.token }}
  path:
    description: >
      Relative path under $GITHUB_WORKSPACE to the repository.
      Defaults to $GITHUB_WORKSPACE.
  add-paths:
    description: >
      A comma or newline-separated list of file paths to commit.
      Paths should follow git's pathspec syntax.
      Defaults to adding all new and modified files.
  commit-message:
    description: 'The message to use when committing changes.'
    default: '[create-pull-request] automated change'
  committer:
    description: >
      The committer name and email address in the format `Display Name <email@address.com>`.
      Defaults to the GitHub Actions bot user.
    default: 'GitHub <noreply@github.com>'
  author:
    description: >
      The author name and email address in the format `Display Name <email@address.com>`.
      Defaults to the user who triggered the workflow run.
    default: '${{ github.actor }} <${{ github.actor }}@users.noreply.github.com>'
  signoff:
    description: 'Add `Signed-off-by` line by the committer at the end of the commit log message.'
    default: false
  branch:
    description: 'The pull request branch name.'
    default: 'create-pull-request/patch'
  delete-branch:
    description: >
      Delete the `branch` when closing pull requests, and when undeleted after merging.
      Recommend `true`.
    default: false
  branch-suffix:
    description: 'The branch suffix type when using the alternative branching strategy.'
  base:
    description: >
      The pull request base branch.
      Defaults to the branch checked out in the workflow.
  push-to-fork:
    description: >
      A fork of the checked out parent repository to which the pull request branch will be pushed.
      e.g. `owner/repo-fork`.
      The pull request will be created to merge the fork's branch into the parent's base.
  title:
    description: 'The title of the pull request.'
    default: 'Changes by create-pull-request action'
  body:
    description: 'The body of the pull request.'
    default: 'Automated changes by [create-pull-request](https://github.com/peter-evans/create-pull-request) GitHub action'
  labels:
    description: 'A comma or newline separated list of labels.'
  assignees:
    description: 'A comma or newline separated list of assignees (GitHub usernames).'
  reviewers:
    description: 'A comma or newline separated list of reviewers (GitHub usernames) to request a review from.'
  team-reviewers:
    description: >
      A comma or newline separated list of GitHub teams to request a review from.
      Note that a `repo` scoped Personal Access Token (PAT) may be required.
  milestone:
    description: 'The number of the milestone to associate the pull request with.'
  draft:
    description: 'Create a draft pull request. It is not possible to change draft status after creation except through the web interface'
    default: false
outputs:
  pull-request-number:
    description: 'The pull request number'
  pull-request-url:
    description: 'The URL of the pull request.'
  pull-request-operation:
    description: 'The pull request operation performed by the action, `created`, `updated` or `closed`.'
  pull-request-head-sha:
    description: 'The commit SHA of the pull request branch.'
runs:
  using: 'node16'
  main: 'dist/index.js'
branding:
  icon: 'git-pull-request'
  color: 'gray-dark'
 13,672  
dist/index.js
Large diffs are not rendered by default.

 68  
docs/assets/cpr-gitgraph.htm
@@ -0,0 +1,68 @@
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>create-pull-request GitHub action</title>
</head>

<body>
    <!-- partial:index.partial.html -->
    <div id="graph-container"></div>
    <!-- partial -->
    <script src='https://cdn.jsdelivr.net/npm/@gitgraph/js'></script>
    <script>
        const graphContainer = document.getElementById("graph-container");

        const customTemplate = GitgraphJS.templateExtend(GitgraphJS.TemplateName.Metro, {
            commit: {
                message: {
                    displayAuthor: false,
                    displayHash: false,
                },
            },
        });

        // Instantiate the graph.
        const gitgraph = GitgraphJS.createGitgraph(graphContainer, {
            template: customTemplate,
            orientation: "vertical-reverse"
        });

        const main = gitgraph.branch("main");
        main.commit("Last commit on base");
        const localMain = gitgraph.branch("<#1> main (local)");
        localMain.commit({
            subject: "<uncommitted changes>",
            body: "Changes to the local base during the workflow",
        })
        const remotePatch = gitgraph.branch("create-pull-request/patch");
        remotePatch.merge({
            branch: localMain,
            commitOptions: {
                subject: "[create-pull-request] automated change",
                body: "Changes pushed to create the remote branch",
            },
        });
        main.commit("New commit on base");

        const localMain2 = gitgraph.branch("<#2> main (local)");
        localMain2.commit({
            subject: "<uncommitted changes>",
            body: "Changes to the updated local base during the workflow",
        })
        remotePatch.merge({
            branch: localMain2,
            commitOptions: {
                subject: "[create-pull-request] automated change",
                body: "Changes force pushed to update the remote branch",
            },
        });

        main.merge(remotePatch);

    </script>

</body>

</html>
 BIN +108 KB 
docs/assets/cpr-gitgraph.png
Unable to render code block

 6  
docs/assets/logo.svg
Unable to render code block

 BIN +327 KB 
docs/assets/pull-request-example.png
Unable to render code block

 370  
docs/concepts-guidelines.md
Large diffs are not rendered by default.

 630  
docs/examples.md
Large diffs are not rendered by default.

 87  
docs/updating.md
@@ -0,0 +1,87 @@
## Updating from `v3` to `v4`

### Breaking changes

- The `add-paths` input no longer accepts `-A` as a valid value. When committing all new and modified files the `add-paths` input should be omitted.

- If using self-hosted runners or GitHub Enterprise Server, there are minimum requirements for `v4` to run. See "What's new" below for details.

### What's new

- Updated runtime to Node.js 16
  - The action now requires a minimum version of v2.285.0 for the [Actions Runner](https://github.com/actions/runner/releases/tag/v2.285.0).
  - If using GitHub Enterprise Server, the action requires [GHES 3.4](https://docs.github.com/en/enterprise-server@3.4/admin/release-notes) or later.

## Updating from `v2` to `v3`

### Breaking changes

- The `author` input now defaults to the user who triggered the workflow run. This default is set via [action.yml](../action.yml) as `${{ github.actor }} <${{ github.actor }}@users.noreply.github.com>`, where `github.actor` is the GitHub user account associated with the run. For example, `peter-evans <peter-evans@users.noreply.github.com>`.

  To continue to use the `v2` default, set the `author` input as follows.
  ```yaml
      - uses: peter-evans/create-pull-request@v3
        with:
          author: github-actions[bot] <41898282+github-actions[bot]@users.noreply.github.com>
  ```

- The `author` and `committer` inputs are no longer cross-used if only one is supplied. Additionally, when neither input is set, the `author` and `committer` are no longer determined from an existing identity set in git config. In both cases, the inputs will fall back to their default set in [action.yml](../action.yml).

- Deprecated inputs `project` and `project-column` have been removed in favour of an additional action step. See [Create a project card](https://github.com/peter-evans/create-pull-request#create-a-project-card) for details.

- Deprecated output `pr_number` has been removed in favour of `pull-request-number`.

- Input `request-to-parent` has been removed in favour of `push-to-fork`. This greatly simplifies pushing the pull request branch to a fork of the parent repository. See [Push pull request branches to a fork](concepts-guidelines.md#push-pull-request-branches-to-a-fork) for details.

  e.g.
  ```yaml
      - uses: actions/checkout@v2
      # Make changes to pull request here
      - uses: peter-evans/create-pull-request@v3
        with:
          token: ${{ secrets.MACHINE_USER_PAT }}
          push-to-fork: machine-user/fork-of-repository
  ```

### What's new

- The action has been converted to Typescript giving it a significant performance improvement.

- If you run this action in a container, or on [self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners), `python` and `pip` are no longer required dependencies. See [Running in a container or on self-hosted runners](concepts-guidelines.md#running-in-a-container-or-on-self-hosted-runners) for details.

- Inputs `labels`, `assignees`, `reviewers` and `team-reviewers` can now be newline separated, or comma separated.
  e.g.
  ```yml
          labels: |
            chore
            dependencies
            automated
  ```

## Updating from `v1` to `v2`

### Breaking changes

- `v2` now expects repositories to be checked out with `actions/checkout@v2`

  To use `actions/checkout@v1` the following step to checkout the branch is necessary.
  ```yml
      - uses: actions/checkout@v1
      - name: Checkout branch
        run: git checkout "${GITHUB_REF:11}"
  ```

- The two branch naming strategies have been swapped. Fixed-branch naming strategy is now the default. i.e. `branch-suffix: none` is now the default and should be removed from configuration if set.

- `author-name`, `author-email`, `committer-name`, `committer-email` have been removed in favour of `author` and `committer`.
  They can both be set in the format `Display Name <email@address.com>`

  If neither `author` or `committer` are set the action will default to making commits as the GitHub Actions bot user.

### What's new

- Unpushed commits made during the workflow before the action runs will now be considered as changes to be raised in the pull request. See [Create your own commits](https://github.com/peter-evans/create-pull-request#create-your-own-commits) for details.
- New commits made to the pull request base will now be taken into account when pull requests are updated.
- If an updated pull request no longer differs from its base it will automatically be closed and the pull request branch deleted.
 276  
gideons.sig
Large diffs are not rendered by default.

 11  
jest.config.js
@@ -0,0 +1,11 @@
module.exports = {
  clearMocks: true,
  moduleFileExtensions: ['js', 'ts'],
  testEnvironment: 'node',
  testMatch: ['**/*.test.ts'],
  testRunner: 'jest-circus/runner',
  transform: {
    '^.+\\.ts$': 'ts-jest'
  },
  verbose: true
}
 13,315  
package-lock.json
Large diffs are not rendered by default.

 58  
package.json
@@ -0,0 +1,58 @@
{
  "name": "create-pull-request",
  "version": "4.0.0",
  "private": true,
  "description": "Creates a pull request for changes to your repository in the actions workspace",
  "main": "lib/main.js",
  "scripts": {
    "build": "tsc && ncc build",
    "format": "prettier --write '**/*.ts'",
    "format-check": "prettier --check '**/*.ts'",
    "lint": "eslint src/**/*.ts",
    "test:unit": "jest unit",
    "test:int": "__test__/integration-tests.sh",
    "test": "npm run test:unit && npm run test:int"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/peter-evans/create-pull-request.git"
  },
  "keywords": [
    "actions",
    "pull",
    "request"
  ],
  "author": "Peter Evans",
  "license": "MIT",
  "bugs": {
    "url": "https://github.com/peter-evans/create-pull-request/issues"
  },
  "homepage": "https://github.com/peter-evans/create-pull-request",
  "dependencies": {
    "@actions/core": "^1.9.1",
    "@actions/exec": "^1.1.0",
    "@octokit/core": "^3.5.1",
    "@octokit/plugin-paginate-rest": "^2.17.0",
    "@octokit/plugin-rest-endpoint-methods": "^5.13.0",
    "https-proxy-agent": "^5.0.0",
    "uuid": "^8.3.2"
  },
  "devDependencies": {
    "@types/jest": "^27.5.0",
    "@types/node": "^16.11.11",
    "@typescript-eslint/parser": "^5.5.0",
    "@vercel/ncc": "^0.32.0",
    "eslint": "^8.3.0",
    "eslint-import-resolver-typescript": "^2.5.0",
    "eslint-plugin-github": "^4.3.5",
    "eslint-plugin-import": "^2.25.3",
    "eslint-plugin-jest": "^26.1.5",
    "jest": "^28.1.0",
    "jest-circus": "^28.1.0",
    "jest-environment-jsdom": "^28.1.0",
    "js-yaml": "^4.1.0",
    "prettier": "^2.5.0",
    "ts-jest": "^28.0.2",
    "typescript": "^4.5.2"
  }
}
 270  
src/create-or-update-branch.ts
@@ -0,0 +1,270 @@
import * as core from '@actions/core'
import {GitCommandManager} from './git-command-manager'
import {v4 as uuidv4} from 'uuid'

const CHERRYPICK_EMPTY =
  'The previous cherry-pick is now empty, possibly due to conflict resolution.'
const NOTHING_TO_COMMIT = 'nothing to commit, working tree clean'

export enum WorkingBaseType {
  Branch = 'branch',
  Commit = 'commit'
}

export async function getWorkingBaseAndType(
  git: GitCommandManager
): Promise<[string, WorkingBaseType]> {
  const symbolicRefResult = await git.exec(
    ['symbolic-ref', 'HEAD', '--short'],
    true
  )
  if (symbolicRefResult.exitCode == 0) {
    // A ref is checked out
    return [symbolicRefResult.stdout.trim(), WorkingBaseType.Branch]
  } else {
    // A commit is checked out (detached HEAD)
    const headSha = await git.revParse('HEAD')
    return [headSha, WorkingBaseType.Commit]
  }
}

export async function tryFetch(
  git: GitCommandManager,
  remote: string,
  branch: string
): Promise<boolean> {
  try {
    await git.fetch([`${branch}:refs/remotes/${remote}/${branch}`], remote, [
      '--force'
    ])
    return true
  } catch {
    return false
  }
}

// Return true if branch2 is ahead of branch1
async function isAhead(
  git: GitCommandManager,
  branch1: string,
  branch2: string
): Promise<boolean> {
  const result = await git.revList(
    [`${branch1}...${branch2}`],
    ['--right-only', '--count']
  )
  return Number(result) > 0
}

// Return true if branch2 is behind branch1
async function isBehind(
  git: GitCommandManager,
  branch1: string,
  branch2: string
): Promise<boolean> {
  const result = await git.revList(
    [`${branch1}...${branch2}`],
    ['--left-only', '--count']
  )
  return Number(result) > 0
}

// Return true if branch2 is even with branch1
async function isEven(
  git: GitCommandManager,
  branch1: string,
  branch2: string
): Promise<boolean> {
  return (
    !(await isAhead(git, branch1, branch2)) &&
    !(await isBehind(git, branch1, branch2))
  )
}

function splitLines(multilineString: string): string[] {
  return multilineString
    .split('\n')
    .map(s => s.trim())
    .filter(x => x !== '')
}

export async function createOrUpdateBranch(
  git: GitCommandManager,
  commitMessage: string,
  base: string,
  branch: string,
  branchRemoteName: string,
  signoff: boolean,
  addPaths: string[]
): Promise<CreateOrUpdateBranchResult> {
  // Get the working base.
  // When a ref, it may or may not be the actual base.
  // When a commit, we must rebase onto the actual base.
  const [workingBase, workingBaseType] = await getWorkingBaseAndType(git)
  core.info(`Working base is ${workingBaseType} '${workingBase}'`)
  if (workingBaseType == WorkingBaseType.Commit && !base) {
    throw new Error(`When in 'detached HEAD' state, 'base' must be supplied.`)
  }

  // If the base is not specified it is assumed to be the working base.
  base = base ? base : workingBase
  const baseRemote = 'origin'

  // Set the default return values
  const result: CreateOrUpdateBranchResult = {
    action: 'none',
    base: base,
    hasDiffWithBase: false,
    headSha: ''
  }

  // Save the working base changes to a temporary branch
  const tempBranch = uuidv4()
  await git.checkout(tempBranch, 'HEAD')
  // Commit any uncommitted changes
  if (await git.isDirty(true, addPaths)) {
    core.info('Uncommitted changes found. Adding a commit.')
    const aopts = ['add']
    if (addPaths.length > 0) {
      aopts.push(...['--', ...addPaths])
    } else {
      aopts.push('-A')
    }
    await git.exec(aopts, true)
    const popts = ['-m', commitMessage]
    if (signoff) {
      popts.push('--signoff')
    }
    const commitResult = await git.commit(popts, true)
    // 'nothing to commit' can occur when core.autocrlf is set to true
    if (
      commitResult.exitCode != 0 &&
      !commitResult.stdout.includes(NOTHING_TO_COMMIT)
    ) {
      throw new Error(`Unexpected error: ${commitResult.stderr}`)
    }
  }

  // Remove uncommitted tracked and untracked changes
  await git.exec(['reset', '--hard'])
  await git.exec(['clean', '-f', '-d'])

  // Perform fetch and reset the working base
  // Commits made during the workflow will be removed
  if (workingBaseType == WorkingBaseType.Branch) {
    core.info(`Resetting working base branch '${workingBase}'`)
    if (branchRemoteName == 'fork') {
      // If pushing to a fork we must fetch with 'unshallow' to avoid the following error on git push
      // ! [remote rejected] HEAD -> tests/push-branch-to-fork (shallow update not allowed)
      await git.fetch([`${workingBase}:${workingBase}`], baseRemote, [
        '--force'
      ])
    } else {
      // If the remote is 'origin' we can git reset
      await git.checkout(workingBase)
      await git.exec(['reset', '--hard', `${baseRemote}/${workingBase}`])
    }
  }

  // If the working base is not the base, rebase the temp branch commits
  // This will also be true if the working base type is a commit
  if (workingBase != base) {
    core.info(
      `Rebasing commits made to ${workingBaseType} '${workingBase}' on to base branch '${base}'`
    )
    // Checkout the actual base
    await git.fetch([`${base}:${base}`], baseRemote, ['--force'])
    await git.checkout(base)
    // Cherrypick commits from the temporary branch starting from the working base
    const commits = await git.revList(
      [`${workingBase}..${tempBranch}`, '.'],
      ['--reverse']
    )
    for (const commit of splitLines(commits)) {
      const result = await git.cherryPick(
        ['--strategy=recursive', '--strategy-option=theirs', commit],
        true
      )
      if (result.exitCode != 0 && !result.stderr.includes(CHERRYPICK_EMPTY)) {
        throw new Error(`Unexpected error: ${result.stderr}`)
      }
    }
    // Reset the temp branch to the working index
    await git.checkout(tempBranch, 'HEAD')
    // Reset the base
    await git.fetch([`${base}:${base}`], baseRemote, ['--force'])
  }

  // Try to fetch the pull request branch
  if (!(await tryFetch(git, branchRemoteName, branch))) {
    // The pull request branch does not exist
    core.info(`Pull request branch '${branch}' does not exist yet.`)
    // Create the pull request branch
    await git.checkout(branch, tempBranch)
    // Check if the pull request branch is ahead of the base
    result.hasDiffWithBase = await isAhead(git, base, branch)
    if (result.hasDiffWithBase) {
      result.action = 'created'
      core.info(`Created branch '${branch}'`)
    } else {
      core.info(
        `Branch '${branch}' is not ahead of base '${base}' and will not be created`
      )
    }
  } else {
    // The pull request branch exists
    core.info(
      `Pull request branch '${branch}' already exists as remote branch '${branchRemoteName}/${branch}'`
    )
    // Checkout the pull request branch
    await git.checkout(branch)

    // Reset the branch if one of the following conditions is true.
    // - If the branch differs from the recreated temp branch.
    // - If the recreated temp branch is not ahead of the base. This means there will be
    //   no pull request diff after the branch is reset. This will reset any undeleted
    //   branches after merging. In particular, it catches a case where the branch was
    //   squash merged but not deleted. We need to reset to make sure it doesn't appear
    //   to have a diff with the base due to different commits for the same changes.
    // For changes on base this reset is equivalent to a rebase of the pull request branch.
    if (
      (await git.hasDiff([`${branch}..${tempBranch}`])) ||
      !(await isAhead(git, base, tempBranch))
    ) {
      core.info(`Resetting '${branch}'`)
      // Alternatively, git switch -C branch tempBranch
      await git.checkout(branch, tempBranch)
    }

    // Check if the pull request branch has been updated
    // If the branch was reset or updated it will be ahead
    // It may be behind if a reset now results in no diff with the base
    if (!(await isEven(git, `${branchRemoteName}/${branch}`, branch))) {
      result.action = 'updated'
      core.info(`Updated branch '${branch}'`)
    } else {
      result.action = 'not-updated'
      core.info(
        `Branch '${branch}' is even with its remote and will not be updated`
      )
    }

    // Check if the pull request branch is ahead of the base
    result.hasDiffWithBase = await isAhead(git, base, branch)
  }

  // Get the pull request branch SHA
  result.headSha = await git.revParse('HEAD')

  // Delete the temporary branch
  await git.exec(['branch', '--delete', '--force', tempBranch])

  return result
}

interface CreateOrUpdateBranchResult {
  action: string
  base: string
  hasDiffWithBase: boolean
  headSha: string
}
 252  
src/create-pull-request.ts
@@ -0,0 +1,252 @@
import * as core from '@actions/core'
import {
  createOrUpdateBranch,
  getWorkingBaseAndType,
  WorkingBaseType
} from './create-or-update-branch'
import {GitHubHelper} from './github-helper'
import {GitCommandManager} from './git-command-manager'
import {GitAuthHelper} from './git-auth-helper'
import * as utils from './utils'

export interface Inputs {
  token: string
  path: string
  addPaths: string[]
  commitMessage: string
  committer: string
  author: string
  signoff: boolean
  branch: string
  deleteBranch: boolean
  branchSuffix: string
  base: string
  pushToFork: string
  title: string
  body: string
  labels: string[]
  assignees: string[]
  reviewers: string[]
  teamReviewers: string[]
  milestone: number
  draft: boolean
}

export async function createPullRequest(inputs: Inputs): Promise<void> {
  let gitAuthHelper
  try {
    // Get the repository path
    const repoPath = utils.getRepoPath(inputs.path)
    // Create a git command manager
    const git = await GitCommandManager.create(repoPath)

    // Save and unset the extraheader auth config if it exists
    core.startGroup('Save persisted git credentials')
    gitAuthHelper = new GitAuthHelper(git)
    await gitAuthHelper.savePersistedAuth()
    core.endGroup()

    // Init the GitHub client
    const githubHelper = new GitHubHelper(inputs.token)

    core.startGroup('Determining the base and head repositories')
    // Determine the base repository from git config
    const remoteUrl = await git.tryGetRemoteUrl()
    const baseRemote = utils.getRemoteDetail(remoteUrl)
    // Determine the head repository; the target for the pull request branch
    const branchRemoteName = inputs.pushToFork ? 'fork' : 'origin'
    const branchRepository = inputs.pushToFork
      ? inputs.pushToFork
      : baseRemote.repository
    if (inputs.pushToFork) {
      // Check if the supplied fork is really a fork of the base
      const parentRepository = await githubHelper.getRepositoryParent(
        branchRepository
      )
      if (parentRepository != baseRemote.repository) {
        throw new Error(
          `Repository '${branchRepository}' is not a fork of '${baseRemote.repository}'. Unable to continue.`
        )
      }
      // Add a remote for the fork
      const remoteUrl = utils.getRemoteUrl(
        baseRemote.protocol,
        branchRepository
      )
      await git.exec(['remote', 'add', 'fork', remoteUrl])
    }
    core.endGroup()
    core.info(
      `Pull request branch target repository set to ${branchRepository}`
    )

    // Configure auth
    if (baseRemote.protocol == 'HTTPS') {
      core.startGroup('Configuring credential for HTTPS authentication')
      await gitAuthHelper.configureToken(inputs.token)
      core.endGroup()
    }

    core.startGroup('Checking the base repository state')
    const [workingBase, workingBaseType] = await getWorkingBaseAndType(git)
    core.info(`Working base is ${workingBaseType} '${workingBase}'`)
    // When in detached HEAD state (checked out on a commit), we need to
    // know the 'base' branch in order to rebase changes.
    if (workingBaseType == WorkingBaseType.Commit && !inputs.base) {
      throw new Error(
        `When the repository is checked out on a commit instead of a branch, the 'base' input must be supplied.`
      )
    }
    // If the base is not specified it is assumed to be the working base.
    const base = inputs.base ? inputs.base : workingBase
    // Throw an error if the base and branch are not different branches
    // of the 'origin' remote. An identically named branch in the `fork`
    // remote is perfectly fine.
    if (branchRemoteName == 'origin' && base == inputs.branch) {
      throw new Error(
        `The 'base' and 'branch' for a pull request must be different branches. Unable to continue.`
      )
    }
    // For self-hosted runners the repository state persists between runs.
    // This command prunes the stale remote ref when the pull request branch was
    // deleted after being merged or closed. Without this the push using
    // '--force-with-lease' fails due to "stale info."
    // https://github.com/peter-evans/create-pull-request/issues/633
    await git.exec(['remote', 'prune', branchRemoteName])
    core.endGroup()

    // Apply the branch suffix if set
    if (inputs.branchSuffix) {
      switch (inputs.branchSuffix) {
        case 'short-commit-hash':
          // Suffix with the short SHA1 hash
          inputs.branch = `${inputs.branch}-${await git.revParse('HEAD', [
            '--short'
          ])}`
          break
        case 'timestamp':
          // Suffix with the current timestamp
          inputs.branch = `${inputs.branch}-${utils.secondsSinceEpoch()}`
          break
        case 'random':
          // Suffix with a 7 character random string
          inputs.branch = `${inputs.branch}-${utils.randomString()}`
          break
        default:
          throw new Error(
            `Branch suffix '${inputs.branchSuffix}' is not a valid value. Unable to continue.`
          )
      }
    }

    // Output head branch
    core.info(
      `Pull request branch to create or update set to '${inputs.branch}'`
    )

    // Configure the committer and author
    core.startGroup('Configuring the committer and author')
    const parsedAuthor = utils.parseDisplayNameEmail(inputs.author)
    const parsedCommitter = utils.parseDisplayNameEmail(inputs.committer)
    git.setIdentityGitOptions([
      '-c',
      `author.name=${parsedAuthor.name}`,
      '-c',
      `author.email=${parsedAuthor.email}`,
      '-c',
      `committer.name=${parsedCommitter.name}`,
      '-c',
      `committer.email=${parsedCommitter.email}`
    ])
    core.info(
      `Configured git committer as '${parsedCommitter.name} <${parsedCommitter.email}>'`
    )
    core.info(
      `Configured git author as '${parsedAuthor.name} <${parsedAuthor.email}>'`
    )
    core.endGroup()

    // Create or update the pull request branch
    core.startGroup('Create or update the pull request branch')
    const result = await createOrUpdateBranch(
      git,
      inputs.commitMessage,
      inputs.base,
      inputs.branch,
      branchRemoteName,
      inputs.signoff,
      inputs.addPaths
    )
    core.endGroup()

    if (['created', 'updated'].includes(result.action)) {
      // The branch was created or updated
      core.startGroup(
        `Pushing pull request branch to '${branchRemoteName}/${inputs.branch}'`
      )
      await git.push([
        '--force-with-lease',
        branchRemoteName,
        `HEAD:refs/heads/${inputs.branch}`
      ])
      core.endGroup()
    }

    // Set the base. It would have been '' if not specified as an input
    inputs.base = result.base

    if (result.hasDiffWithBase) {
      // Create or update the pull request
      core.startGroup('Create or update the pull request')
      const pull = await githubHelper.createOrUpdatePullRequest(
        inputs,
        baseRemote.repository,
        branchRepository
      )
      core.endGroup()

      // Set outputs
      core.startGroup('Setting outputs')
      core.setOutput('pull-request-number', pull.number)
      core.setOutput('pull-request-url', pull.html_url)
      if (pull.created) {
        core.setOutput('pull-request-operation', 'created')
      } else if (result.action == 'updated') {
        core.setOutput('pull-request-operation', 'updated')
      }
      core.setOutput('pull-request-head-sha', result.headSha)
      // Deprecated
      core.exportVariable('PULL_REQUEST_NUMBER', pull.number)
      core.endGroup()
    } else {
      // There is no longer a diff with the base
      // Check we are in a state where a branch exists
      if (['updated', 'not-updated'].includes(result.action)) {
        core.info(
          `Branch '${inputs.branch}' no longer differs from base branch '${inputs.base}'`
        )
        if (inputs.deleteBranch) {
          core.info(`Deleting branch '${inputs.branch}'`)
          await git.push([
            '--delete',
            '--force',
            branchRemoteName,
            `refs/heads/${inputs.branch}`
          ])
          // Set outputs
          core.startGroup('Setting outputs')
          core.setOutput('pull-request-operation', 'closed')
          core.endGroup()
        }
      }
    }
  } catch (error: any) {
    core.setFailed(error.message)
  } finally {
    // Remove auth and restore persisted auth config if it existed
    core.startGroup('Restore persisted git credentials')
    await gitAuthHelper.removeAuth()
    await gitAuthHelper.restorePersistedAuth()
    core.endGroup()
  }
}
 126  
src/git-auth-helper.ts
@@ -0,0 +1,126 @@
import * as core from '@actions/core'
import * as fs from 'fs'
import {GitCommandManager} from './git-command-manager'
import * as path from 'path'
import {URL} from 'url'

export class GitAuthHelper {
  private git: GitCommandManager
  private gitConfigPath: string
  private extraheaderConfigKey: string
  private extraheaderConfigPlaceholderValue = 'AUTHORIZATION: basic ***'
  private extraheaderConfigValueRegex = '^AUTHORIZATION:'
  private persistedExtraheaderConfigValue = ''

  constructor(git: GitCommandManager) {
    this.git = git
    this.gitConfigPath = path.join(
      this.git.getWorkingDirectory(),
      '.git',
      'config'
    )
    const serverUrl = this.getServerUrl()
    this.extraheaderConfigKey = `http.${serverUrl.origin}/.extraheader`
  }

  async savePersistedAuth(): Promise<void> {
    // Save and unset persisted extraheader credential in git config if it exists
    this.persistedExtraheaderConfigValue = await this.getAndUnset()
  }

  async restorePersistedAuth(): Promise<void> {
    if (this.persistedExtraheaderConfigValue) {
      try {
        await this.setExtraheaderConfig(this.persistedExtraheaderConfigValue)
        core.info('Persisted git credentials restored')
      } catch (e: any) {
        core.warning(e)
      }
    }
  }

  async configureToken(token: string): Promise<void> {
    // Encode and configure the basic credential for HTTPS access
    const basicCredential = Buffer.from(
      `x-access-token:${token}`,
      'utf8'
    ).toString('base64')
    core.setSecret(basicCredential)
    const extraheaderConfigValue = `AUTHORIZATION: basic ${basicCredential}`
    await this.setExtraheaderConfig(extraheaderConfigValue)
  }

  async removeAuth(): Promise<void> {
    await this.getAndUnset()
  }

  private async setExtraheaderConfig(
    extraheaderConfigValue: string
  ): Promise<void> {
    // Configure a placeholder value. This approach avoids the credential being captured
    // by process creation audit events, which are commonly logged. For more information,
    // refer to https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/manage/component-updates/command-line-process-auditing
    // See https://github.com/actions/checkout/blob/main/src/git-auth-helper.ts#L267-L274
    await this.git.config(
      this.extraheaderConfigKey,
      this.extraheaderConfigPlaceholderValue
    )
    // Replace the placeholder
    await this.gitConfigStringReplace(
      this.extraheaderConfigPlaceholderValue,
      extraheaderConfigValue
    )
  }

  private async getAndUnset(): Promise<string> {
    let configValue = ''
    // Save and unset persisted extraheader credential in git config if it exists
    if (
      await this.git.configExists(
        this.extraheaderConfigKey,
        this.extraheaderConfigValueRegex
      )
    ) {
      configValue = await this.git.getConfigValue(
        this.extraheaderConfigKey,
        this.extraheaderConfigValueRegex
      )
      if (
        await this.git.tryConfigUnset(
          this.extraheaderConfigKey,
          this.extraheaderConfigValueRegex
        )
      ) {
        core.info(`Unset config key '${this.extraheaderConfigKey}'`)
      } else {
        core.warning(
          `Failed to unset config key '${this.extraheaderConfigKey}'`
        )
      }
    }
    return configValue
  }

  private async gitConfigStringReplace(
    find: string,
    replace: string
  ): Promise<void> {
    let content = (await fs.promises.readFile(this.gitConfigPath)).toString()
    const index = content.indexOf(find)
    if (index < 0 || index != content.lastIndexOf(find)) {
      throw new Error(`Unable to replace '${find}' in ${this.gitConfigPath}`)
    }
    content = content.replace(find, replace)
    await fs.promises.writeFile(this.gitConfigPath, content)
  }

  private getServerUrl(): URL {
    // todo: remove GITHUB_URL after support for GHES Alpha is no longer needed
    // See https://github.com/actions/checkout/blob/main/src/url-helper.ts#L22-L29
    return new URL(
      process.env['GITHUB_SERVER_URL'] ||
        process.env['GITHUB_URL'] ||
        'https://github.com'
    )
  }
}
 303  
src/git-command-manager.ts
@@ -0,0 +1,303 @@
import * as exec from '@actions/exec'
import * as io from '@actions/io'
import * as utils from './utils'
import * as path from 'path'

const tagsRefSpec = '+refs/tags/*:refs/tags/*'

export class GitCommandManager {
  private gitPath: string
  private workingDirectory: string
  // Git options used when commands require an identity
  private identityGitOptions?: string[]

  private constructor(workingDirectory: string, gitPath: string) {
    this.workingDirectory = workingDirectory
    this.gitPath = gitPath
  }

  static async create(workingDirectory: string): Promise<GitCommandManager> {
    const gitPath = await io.which('git', true)
    return new GitCommandManager(workingDirectory, gitPath)
  }

  setIdentityGitOptions(identityGitOptions: string[]): void {
    this.identityGitOptions = identityGitOptions
  }

  async checkout(ref: string, startPoint?: string): Promise<void> {
    const args = ['checkout', '--progress']
    if (startPoint) {
      args.push('-B', ref, startPoint)
    } else {
      args.push(ref)
    }
    // https://github.com/git/git/commit/a047fafc7866cc4087201e284dc1f53e8f9a32d5
    args.push('--')
    await this.exec(args)
  }

  async cherryPick(
    options?: string[],
    allowAllExitCodes = false
  ): Promise<GitOutput> {
    const args = ['cherry-pick']
    if (this.identityGitOptions) {
      args.unshift(...this.identityGitOptions)
    }

    if (options) {
      args.push(...options)
    }

    return await this.exec(args, allowAllExitCodes)
  }

  async commit(
    options?: string[],
    allowAllExitCodes = false
  ): Promise<GitOutput> {
    const args = ['commit']
    if (this.identityGitOptions) {
      args.unshift(...this.identityGitOptions)
    }

    if (options) {
      args.push(...options)
    }

    return await this.exec(args, allowAllExitCodes)
  }

  async config(
    configKey: string,
    configValue: string,
    globalConfig?: boolean
  ): Promise<void> {
    await this.exec([
      'config',
      globalConfig ? '--global' : '--local',
      configKey,
      configValue
    ])
  }

  async configExists(
    configKey: string,
    configValue = '.',
    globalConfig?: boolean
  ): Promise<boolean> {
    const output = await this.exec(
      [
        'config',
        globalConfig ? '--global' : '--local',
        '--name-only',
        '--get-regexp',
        configKey,
        configValue
      ],
      true
    )
    return output.exitCode === 0
  }

  async fetch(
    refSpec: string[],
    remoteName?: string,
    options?: string[]
  ): Promise<void> {
    const args = ['-c', 'protocol.version=2', 'fetch']
    if (!refSpec.some(x => x === tagsRefSpec)) {
      args.push('--no-tags')
    }

    args.push('--progress', '--no-recurse-submodules')
    if (
      utils.fileExistsSync(path.join(this.workingDirectory, '.git', 'shallow'))
    ) {
      args.push('--unshallow')
    }

    if (options) {
      args.push(...options)
    }

    if (remoteName) {
      args.push(remoteName)
    } else {
      args.push('origin')
    }
    for (const arg of refSpec) {
      args.push(arg)
    }

    await this.exec(args)
  }

  async getConfigValue(configKey: string, configValue = '.'): Promise<string> {
    const output = await this.exec([
      'config',
      '--local',
      '--get-regexp',
      configKey,
      configValue
    ])
    return output.stdout.trim().split(`${configKey} `)[1]
  }

  getWorkingDirectory(): string {
    return this.workingDirectory
  }

  async hasDiff(options?: string[]): Promise<boolean> {
    const args = ['diff', '--quiet']
    if (options) {
      args.push(...options)
    }
    const output = await this.exec(args, true)
    return output.exitCode === 1
  }

  async isDirty(untracked: boolean, pathspec?: string[]): Promise<boolean> {
    const pathspecArgs = pathspec ? ['--', ...pathspec] : []
    // Check untracked changes
    const sargs = ['--porcelain', '-unormal']
    sargs.push(...pathspecArgs)
    if (untracked && (await this.status(sargs))) {
      return true
    }
    // Check working index changes
    if (await this.hasDiff(pathspecArgs)) {
      return true
    }
    // Check staged changes
    const dargs = ['--staged']
    dargs.push(...pathspecArgs)
    if (await this.hasDiff(dargs)) {
      return true
    }
    return false
  }

  async push(options?: string[]): Promise<void> {
    const args = ['push']
    if (options) {
      args.push(...options)
    }
    await this.exec(args)
  }

  async revList(
    commitExpression: string[],
    options?: string[]
  ): Promise<string> {
    const args = ['rev-list']
    if (options) {
      args.push(...options)
    }
    args.push(...commitExpression)
    const output = await this.exec(args)
    return output.stdout.trim()
  }

  async revParse(ref: string, options?: string[]): Promise<string> {
    const args = ['rev-parse']
    if (options) {
      args.push(...options)
    }
    args.push(ref)
    const output = await this.exec(args)
    return output.stdout.trim()
  }

  async status(options?: string[]): Promise<string> {
    const args = ['status']
    if (options) {
      args.push(...options)
    }
    const output = await this.exec(args)
    return output.stdout.trim()
  }

  async symbolicRef(ref: string, options?: string[]): Promise<string> {
    const args = ['symbolic-ref', ref]
    if (options) {
      args.push(...options)
    }
    const output = await this.exec(args)
    return output.stdout.trim()
  }

  async tryConfigUnset(
    configKey: string,
    configValue = '.',
    globalConfig?: boolean
  ): Promise<boolean> {
    const output = await this.exec(
      [
        'config',
        globalConfig ? '--global' : '--local',
        '--unset',
        configKey,
        configValue
      ],
      true
    )
    return output.exitCode === 0
  }

  async tryGetRemoteUrl(): Promise<string> {
    const output = await this.exec(
      ['config', '--local', '--get', 'remote.origin.url'],
      true
    )

    if (output.exitCode !== 0) {
      return ''
    }

    const stdout = output.stdout.trim()
    if (stdout.includes('\n')) {
      return ''
    }

    return stdout
  }

  async exec(args: string[], allowAllExitCodes = false): Promise<GitOutput> {
    const result = new GitOutput()

    const env = {}
    for (const key of Object.keys(process.env)) {
      env[key] = process.env[key]
    }

    const stdout: string[] = []
    const stderr: string[] = []

    const options = {
      cwd: this.workingDirectory,
      env,
      ignoreReturnCode: allowAllExitCodes,
      listeners: {
        stdout: (data: Buffer) => {
          stdout.push(data.toString())
        },
        stderr: (data: Buffer) => {
          stderr.push(data.toString())
        }
      }
    }

    result.exitCode = await exec.exec(`"${this.gitPath}"`, args, options)
    result.stdout = stdout.join('')
    result.stderr = stderr.join('')
    return result
  }
}

class GitOutput {
  stdout = ''
  stderr = ''
  exitCode = 0
}
 183  
src/github-helper.ts
@@ -0,0 +1,183 @@
import * as core from '@actions/core'
import {Inputs} from './create-pull-request'
import {Octokit, OctokitOptions} from './octokit-client'

const ERROR_PR_REVIEW_FROM_AUTHOR =
  'Review cannot be requested from pull request author'

interface Repository {
  owner: string
  repo: string
}

interface Pull {
  number: number
  html_url: string
  created: boolean
}

export class GitHubHelper {
  private octokit: InstanceType<typeof Octokit>

  constructor(token: string) {
    const options: OctokitOptions = {}
    if (token) {
      options.auth = `${token}`
    }
    options.baseUrl = process.env['GITHUB_API_URL'] || 'https://api.github.com'
    this.octokit = new Octokit(options)
  }

  private parseRepository(repository: string): Repository {
    const [owner, repo] = repository.split('/')
    return {
      owner: owner,
      repo: repo
    }
  }

  private async createOrUpdate(
    inputs: Inputs,
    baseRepository: string,
    headRepository: string
  ): Promise<Pull> {
    const [headOwner] = headRepository.split('/')
    const headBranch = `${headOwner}:${inputs.branch}`
    const headBranchFull = `${headRepository}:${inputs.branch}`

    // Try to create the pull request
    try {
      core.info(`Attempting creation of pull request`)
      const {data: pull} = await this.octokit.rest.pulls.create({
        ...this.parseRepository(baseRepository),
        title: inputs.title,
        head: headBranch,
        base: inputs.base,
        body: inputs.body,
        draft: inputs.draft
      })
      core.info(
        `Created pull request #${pull.number} (${headBranch} => ${inputs.base})`
      )
      return {
        number: pull.number,
        html_url: pull.html_url,
        created: true
      }
    } catch (e: any) {
      if (
        e.message &&
        e.message.includes(`A pull request already exists for`)
      ) {
        core.info(`A pull request already exists for ${headBranch}`)
      } else {
        throw e
      }
    }

    // Update the pull request that exists for this branch and base
    core.info(`Fetching existing pull request`)
    const {data: pulls} = await this.octokit.rest.pulls.list({
      ...this.parseRepository(baseRepository),
      state: 'open',
      head: headBranchFull,
      base: inputs.base
    })
    core.info(`Attempting update of pull request`)
    const {data: pull} = await this.octokit.rest.pulls.update({
      ...this.parseRepository(baseRepository),
      pull_number: pulls[0].number,
      title: inputs.title,
      body: inputs.body
    })
    core.info(
      `Updated pull request #${pull.number} (${headBranch} => ${inputs.base})`
    )
    return {
      number: pull.number,
      html_url: pull.html_url,
      created: false
    }
  }

  async getRepositoryParent(headRepository: string): Promise<string> {
    const {data: headRepo} = await this.octokit.rest.repos.get({
      ...this.parseRepository(headRepository)
    })
    if (!headRepo.parent) {
      throw new Error(
        `Repository '${headRepository}' is not a fork. Unable to continue.`
      )
    }
    return headRepo.parent.full_name
  }

  async createOrUpdatePullRequest(
    inputs: Inputs,
    baseRepository: string,
    headRepository: string
  ): Promise<Pull> {
    // Create or update the pull request
    const pull = await this.createOrUpdate(
      inputs,
      baseRepository,
      headRepository
    )

    // Apply milestone
    if (inputs.milestone) {
      core.info(`Applying milestone '${inputs.milestone}'`)
      await this.octokit.rest.issues.update({
        ...this.parseRepository(baseRepository),
        issue_number: pull.number,
        milestone: inputs.milestone
      })
    }
    // Apply labels
    if (inputs.labels.length > 0) {
      core.info(`Applying labels '${inputs.labels}'`)
      await this.octokit.rest.issues.addLabels({
        ...this.parseRepository(baseRepository),
        issue_number: pull.number,
        labels: inputs.labels
      })
    }
    // Apply assignees
    if (inputs.assignees.length > 0) {
      core.info(`Applying assignees '${inputs.assignees}'`)
      await this.octokit.rest.issues.addAssignees({
        ...this.parseRepository(baseRepository),
        issue_number: pull.number,
        assignees: inputs.assignees
      })
    }

    // Request reviewers and team reviewers
    const requestReviewersParams = {}
    if (inputs.reviewers.length > 0) {
      requestReviewersParams['reviewers'] = inputs.reviewers
      core.info(`Requesting reviewers '${inputs.reviewers}'`)
    }
    if (inputs.teamReviewers.length > 0) {
      requestReviewersParams['team_reviewers'] = inputs.teamReviewers
      core.info(`Requesting team reviewers '${inputs.teamReviewers}'`)
    }
    if (Object.keys(requestReviewersParams).length > 0) {
      try {
        await this.octokit.rest.pulls.requestReviewers({
          ...this.parseRepository(baseRepository),
          pull_number: pull.number,
          ...requestReviewersParams
        })
      } catch (e: any) {
        if (e.message && e.message.includes(ERROR_PR_REVIEW_FROM_AUTHOR)) {
          core.warning(ERROR_PR_REVIEW_FROM_AUTHOR)
        } else {
          throw e
        }
      }
    }

    return pull
  }
}
 38  
src/main.ts
@@ -0,0 +1,38 @@
import * as core from '@actions/core'
import {Inputs, createPullRequest} from './create-pull-request'
import {inspect} from 'util'
import * as utils from './utils'

async function run(): Promise<void> {
  try {
    const inputs: Inputs = {
      token: core.getInput('token'),
      path: core.getInput('path'),
      addPaths: utils.getInputAsArray('add-paths'),
      commitMessage: core.getInput('commit-message'),
      committer: core.getInput('committer'),
      author: core.getInput('author'),
      signoff: core.getBooleanInput('signoff'),
      branch: core.getInput('branch'),
      deleteBranch: core.getBooleanInput('delete-branch'),
      branchSuffix: core.getInput('branch-suffix'),
      base: core.getInput('base'),
      pushToFork: core.getInput('push-to-fork'),
      title: core.getInput('title'),
      body: core.getInput('body'),
      labels: utils.getInputAsArray('labels'),
      assignees: utils.getInputAsArray('assignees'),
      reviewers: utils.getInputAsArray('reviewers'),
      teamReviewers: utils.getInputAsArray('team-reviewers'),
      milestone: Number(core.getInput('milestone')),
      draft: core.getBooleanInput('draft')
    }
    core.debug(`Inputs: ${inspect(inputs)}`)

    await createPullRequest(inputs)
  } catch (error: any) {
    core.setFailed(error.message)
  }
}

run()
 33  
src/octokit-client.ts
@@ -0,0 +1,33 @@
import {Octokit as Core} from '@octokit/core'
import {paginateRest} from '@octokit/plugin-paginate-rest'
import {restEndpointMethods} from '@octokit/plugin-rest-endpoint-methods'
import {HttpsProxyAgent} from 'https-proxy-agent'
export {RestEndpointMethodTypes} from '@octokit/plugin-rest-endpoint-methods'
export {OctokitOptions} from '@octokit/core/dist-types/types'

export const Octokit = Core.plugin(
  paginateRest,
  restEndpointMethods,
  autoProxyAgent
)

// Octokit plugin to support the https_proxy and no_proxy environment variable
function autoProxyAgent(octokit: Core) {
  const proxy = process.env.https_proxy || process.env.HTTPS_PROXY

  const noProxy = process.env.no_proxy || process.env.NO_PROXY
  let noProxyArray: string[] = []
  if (noProxy) {
    noProxyArray = noProxy.split(',')
  }

  if (!proxy) return

  const agent = new HttpsProxyAgent(proxy)
  octokit.hook.before('request', options => {
    if (noProxyArray.includes(options.request.hostname)) {
      return
    }
    options.request.agent = agent
  })
}
 152  
src/utils.ts
@@ -0,0 +1,152 @@
import * as core from '@actions/core'
import * as fs from 'fs'
import * as path from 'path'

export function getInputAsArray(
  name: string,
  options?: core.InputOptions
): string[] {
  return getStringAsArray(core.getInput(name, options))
}

export function getStringAsArray(str: string): string[] {
  return str
    .split(/[\n,]+/)
    .map(s => s.trim())
    .filter(x => x !== '')
}

export function getRepoPath(relativePath?: string): string {
  let githubWorkspacePath = process.env['GITHUB_WORKSPACE']
  if (!githubWorkspacePath) {
    throw new Error('GITHUB_WORKSPACE not defined')
  }
  githubWorkspacePath = path.resolve(githubWorkspacePath)
  core.debug(`githubWorkspacePath: ${githubWorkspacePath}`)

  let repoPath = githubWorkspacePath
  if (relativePath) repoPath = path.resolve(repoPath, relativePath)

  core.debug(`repoPath: ${repoPath}`)
  return repoPath
}

interface RemoteDetail {
  protocol: string
  repository: string
}

export function getRemoteDetail(remoteUrl: string): RemoteDetail {
  // Parse the protocol and github repository from a URL
  // e.g. HTTPS, peter-evans/create-pull-request
  const githubUrl = process.env['GITHUB_SERVER_URL'] || 'https://github.com'

  const githubServerMatch = githubUrl.match(/^https?:\/\/(.+)$/i)
  if (!githubServerMatch) {
    throw new Error('Could not parse GitHub Server name')
  }

  const httpsUrlPattern = new RegExp(
    '^https?://.*@?' + githubServerMatch[1] + '/(.+/.+?)(.git)?$',
    'i'
  )
  const sshUrlPattern = new RegExp(
    '^git@' + githubServerMatch[1] + ':(.+/.+).git$',
    'i'
  )

  const httpsMatch = remoteUrl.match(httpsUrlPattern)
  if (httpsMatch) {
    return {
      protocol: 'HTTPS',
      repository: httpsMatch[1]
    }
  }

  const sshMatch = remoteUrl.match(sshUrlPattern)
  if (sshMatch) {
    return {
      protocol: 'SSH',
      repository: sshMatch[1]
    }
  }

  throw new Error(
    `The format of '${remoteUrl}' is not a valid GitHub repository URL`
  )
}

export function getRemoteUrl(protocol: string, repository: string): string {
  return protocol == 'HTTPS'
    ? `https://github.com/${repository}`
    : `git@github.com:${repository}.git`
}

export function secondsSinceEpoch(): number {
  const now = new Date()
  return Math.round(now.getTime() / 1000)
}

export function randomString(): string {
  return Math.random().toString(36).substr(2, 7)
}

interface DisplayNameEmail {
  name: string
  email: string
}

export function parseDisplayNameEmail(
  displayNameEmail: string
): DisplayNameEmail {
  // Parse the name and email address from a string in the following format
  // Display Name <email@address.com>
  const pattern = /^([^<]+)\s*<([^>]+)>$/i

  // Check we have a match
  const match = displayNameEmail.match(pattern)
  if (!match) {
    throw new Error(
      `The format of '${displayNameEmail}' is not a valid email address with display name`
    )
  }

  // Check that name and email are not just whitespace
  const name = match[1].trim()
  const email = match[2].trim()
  if (!name || !email) {
    throw new Error(
      `The format of '${displayNameEmail}' is not a valid email address with display name`
    )
  }

  return {
    name: name,
    email: email
  }
}

export function fileExistsSync(path: string): boolean {
  if (!path) {
    throw new Error("Arg 'path' must not be empty")
  }

  let stats: fs.Stats
  try {
    stats = fs.statSync(path)
  } catch (error: any) {
    if (error.code === 'ENOENT') {
      return false
    }

    throw new Error(
      `Encountered an error when checking whether path '${path}' exists: ${error.message}`
    )
  }

  if (!stats.isDirectory()) {
    return true
  }

  return false
}
 16  
tsconfig.json
@@ -0,0 +1,16 @@
{
  "compilerOptions": {
    "target": "es6",
    "module": "commonjs",
    "lib": [
      "es6"
    ],
    "outDir": "./lib",
    "rootDir": "./src",
    "declaration": true,
    "strict": true,
    "noImplicitAny": false,
    "esModuleInterop": true
  },
  "exclude": ["__test__", "lib", "node_modules"]
}
0 comments on commit a0e21ef
@zakwarlord7

Add heading textAdd bold text, <Ctrl+b>Add italic text, <Ctrl+i>
Add a quote, <Ctrl+Shift+.>Add code, <Ctrl+e>Add a link, <Ctrl+k>
Add a bulleted list, <Ctrl+Shift+8>Add a numbered list, <Ctrl+Shift+7>Add a task list, <Ctrl+Shift+l>
Directly mention a user or team
Reference an issue, pull request, or discussion
Add saved reply
Leave a comment
No file chosen
Attach files by dragging & dropping, selecting or pasting them.
Styling with Markdown is supported
 You’re receiving notifications because you’re watching this repository.
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore

@zakwarlord7 
Your account has been flagged.
Because of that, your profile is hidden from the public. If you believe this is a mistake, contact support to have your account status reviewed.
zakwarlord7
/
Patch-5
Public
generated from zakwarlord7/peter-evans-create-pull-request
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
Initialize main
 main
@zakwarlord7
zakwarlord7 committed 9 days ago 
0 parents commit a0e21ef989cd84f37c125a5925bebd2f2724006b
Show file tree Hide file tree
Showing 40 changed files with 32,705 additions and 0 deletions.
 3  
.eslintignore
@@ -0,0 +1,3 @@
dist/
lib/
node_modules/
 23  
.eslintrc.json
@@ -0,0 +1,23 @@
{
  "env": { "node": true, "jest": true },
  "parser": "@typescript-eslint/parser",
  "parserOptions": { "ecmaVersion": 9, "sourceType": "module" },
  "extends": [
    "eslint:recommended",
    "plugin:@typescript-eslint/eslint-recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:import/errors",
    "plugin:import/warnings",
    "plugin:import/typescript",
    "plugin:prettier/recommended"
  ],
  "plugins": ["@typescript-eslint"],
  "rules": {
    "@typescript-eslint/camelcase": "off"
  },
  "settings": {
    "import/resolver": {
      "typescript": {}
    }
  }
}
 1  
.github/FUNDING.yml
@@ -0,0 +1 @@
github: peter-evans
 7  
.github/ISSUE_TEMPLATE.md
@@ -0,0 +1,7 @@
### Subject of the issue

Describe your issue here.

### Steps to reproduce

If this issue is describing a possible bug please provide (or link to) your GitHub Actions workflow.
 8  
.github/dependabot.yml
@@ -0,0 +1,8 @@
version: 2
updates:
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
    labels:
      - "dependencies"
 134  
.github/workflows/ci.yml
@@ -0,0 +1,134 @@
name: CI
on:
  push:
    branches: [main]
    paths-ignore:
      - 'README.md'
      - 'docs/**'
  pull_request:
    branches: [main]
    paths-ignore:
      - 'README.md'
      - 'docs/**'

permissions:
  pull-requests: write
  contents: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: 16.x
          cache: npm
      - run: npm ci
      - run: npm run build
      - run: npm run format-check
      - run: npm run lint
      - run: npm run test
      - uses: actions/upload-artifact@v3
        with:
          name: dist
          path: dist
      - uses: actions/upload-artifact@v3
        with:
          name: action.yml
          path: action.yml

  test:
    if: github.event_name == 'push' || github.event.pull_request.head.repo.full_name == github.repository
    needs: [build]
    runs-on: ubuntu-latest
    strategy:
      matrix:
        target: [built, committed]
    steps:
      - uses: actions/checkout@v3
        with:
          ref: main
      - if: matrix.target == 'built' || github.event_name == 'pull_request'
        uses: actions/download-artifact@v3
        with:
          name: dist
          path: dist
      - if: matrix.target == 'built' || github.event_name == 'pull_request'
        uses: actions/download-artifact@v3
        with:
          name: action.yml
          path: .

      - name: Create change
        run: date +%s > report.txt

      - name: Create Pull Request
        id: cpr
        uses: ./
        with:
          commit-message: '[CI] test ${{ matrix.target }}'
          committer: GitHub <noreply@github.com>
          author: ${{ github.actor }} <${{ github.actor }}@users.noreply.github.com>
          title: '[CI] test ${{ matrix.target }}'
          body: |
            - CI test case for target '${{ matrix.target }}'
            Auto-generated by [create-pull-request][1]
            [1]: https://github.com/peter-evans/create-pull-request
          branch: ci-test-${{ matrix.target }}

      - name: Close Pull
        uses: peter-evans/close-pull@v2
        with:
          pull-request-number: ${{ steps.cpr.outputs.pull-request-number }}
          comment: '[CI] test ${{ matrix.target }}'
          delete-branch: true

  commentTestSuiteHelp:
    if: github.event_name == 'pull_request'
    needs: [test]
    runs-on: ubuntu-latest
    steps:
      - name: Find Comment
        uses: peter-evans/find-comment@v2
        id: fc
        with:
          issue-number: ${{ github.event.number }}
          comment-author: 'github-actions[bot]'
          body-includes: Full test suite slash command

      - if: steps.fc.outputs.comment-id == ''
        name: Create comment
        uses: peter-evans/create-or-update-comment@v2
        with:
          issue-number: ${{ github.event.number }}
          body: |
            Full test suite slash command (repository admin only)
            ```
            /test repository=${{ github.event.pull_request.head.repo.full_name }} ref=${{ github.event.pull_request.head.ref }} build=true
            ```
  package:
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    needs: [test]
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/download-artifact@v3
        with:
          name: dist
          path: dist
      - name: Create Pull Request
        uses: peter-evans/create-pull-request@v4
        with:
          commit-message: 'build: update distribution'
          title: Update distribution
          body: |
            - Updates the distribution for changes on `main`
            Auto-generated by [create-pull-request][1]
            [1]: https://github.com/peter-evans/create-pull-request
          branch: update-distribution
 49  
.github/workflows/cpr-example-command.yml
@@ -0,0 +1,49 @@
name: Create Pull Request Example Command
on:
  repository_dispatch:
    types: [cpr-example-command]
jobs:
  createPullRequest:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Make changes to pull request
        run: date +%s > report.txt

      - name: Create Pull Request
        id: cpr
        uses: ./
        with:
          commit-message: Update report
          committer: GitHub <noreply@github.com>
          author: ${{ github.actor }} <${{ github.actor }}@users.noreply.github.com>
          signoff: false
          title: '[Example] Update report'
          body: |
            Update report
            - Updated with *today's* date
            - Auto-generated by [create-pull-request][1]
            [1]: https://github.com/peter-evans/create-pull-request
          labels: |
            report
            automated pr
          assignees: peter-evans
          reviewers: peter-evans
          milestone: 1
          draft: false
          branch: example-patches
          delete-branch: true

      - name: Check output
        run: |
          echo "Pull Request Number - ${{ steps.cpr.outputs.pull-request-number }}"
          echo "Pull Request URL - ${{ steps.cpr.outputs.pull-request-url }}"
      - name: Add reaction
        uses: peter-evans/create-or-update-comment@v2
        with:
          repository: ${{ github.event.client_payload.github.payload.repository.full_name }}
          comment-id: ${{ github.event.client_payload.github.payload.comment.id }}
          reaction-type: hooray
 37  
.github/workflows/slash-command-dispatch.yml
@@ -0,0 +1,37 @@
name: Slash Command Dispatch
on:
  issue_comment:
    types: [created]
jobs:
  slashCommandDispatch:
    runs-on: ubuntu-latest
    steps:
      - name: Slash Command Dispatch
        uses: peter-evans/slash-command-dispatch@v3
        with:
          token: ${{ secrets.ACTIONS_BOT_TOKEN }}
          config: >
            [
              {
                "command": "test",
                "permission": "admin",
                "repository": "peter-evans/create-pull-request-tests",
                "named_args": true
              },
              {
                "command": "clean",
                "permission": "admin",
                "repository": "peter-evans/create-pull-request-tests"
              },
              {
                "command": "cpr-example",
                "permission": "admin",
                "issue_type": "issue"
              },
              {
                "command": "rebase",
                "permission": "admin",
                "repository": "peter-evans/slash-command-dispatch-processor",
                "issue_type": "pull-request"
              }
            ]
 5  
.gitignore
@@ -0,0 +1,5 @@
lib/
node_modules/

.DS_Store
.idea
 3  
.prettierignore
@@ -0,0 +1,3 @@
dist/
lib/
node_modules/
 11  
.prettierrc.json
@@ -0,0 +1,11 @@
{
  "printWidth": 80,
  "tabWidth": 2,
  "useTabs": false,
  "semi": false,
  "singleQuote": true,
  "trailingComma": "none",
  "bracketSpacing": false,
  "arrowParens": "avoid",
  "parser": "typescript"
}
 21  
LICENSE
@@ -0,0 +1,21 @@
MIT License

Copyright (c) 2019 Peter Evans

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
 267  
README.md
@@ -0,0 +1,267 @@
# <img width="24" height="24" src="docs/assets/logo.svg"> Create Pull Request
[![CI](https://github.com/peter-evans/create-pull-request/workflows/CI/badge.svg)](https://github.com/peter-evans/create-pull-request/actions?query=workflow%3ACI)
[![GitHub Marketplace](https://img.shields.io/badge/Marketplace-Create%20Pull%20Request-blue.svg?colorA=24292e&colorB=0366d6&style=flat&longCache=true&logo=github)](https://github.com/marketplace/actions/create-pull-request)

A GitHub action to create a pull request for changes to your repository in the actions workspace.

Changes to a repository in the Actions workspace persist between steps in a workflow.
This action is designed to be used in conjunction with other steps that modify or add files to your repository.
The changes will be automatically committed to a new branch and a pull request created.

Create Pull Request action will:

1. Check for repository changes in the Actions workspace. This includes:
   - untracked (new) files
   - tracked (modified) files
   - commits made during the workflow that have not been pushed
2. Commit all changes to a new branch, or update an existing pull request branch.
3. Create a pull request to merge the new branch into the base&mdash;the branch checked out in the workflow.

## Documentation

- [Concepts, guidelines and advanced usage](docs/concepts-guidelines.md)
- [Examples](docs/examples.md)
- [Updating to v4](docs/updating.md)

## Usage

```yml
      - uses: actions/checkout@v3
      # Make changes to pull request here
      - name: Create Pull Request
        uses: peter-evans/create-pull-request@v4
```

You can also pin to a [specific release](https://github.com/peter-evans/create-pull-request/releases) version in the format `@v4.x.x`

### Workflow permissions

For this action to work you must explicitly allow GitHub Actions to create pull requests.
This setting can be found in a repository's settings under Actions > General > Workflow permissions.

For repositories belonging to an organization, this setting can be managed by admins in organization settings under Actions > General > Workflow permissions.

### Action inputs

All inputs are **optional**. If not set, sensible defaults will be used.

**Note**: If you want pull requests created by this action to trigger an `on: push` or `on: pull_request` workflow then you cannot use the default `GITHUB_TOKEN`. See the [documentation here](docs/concepts-guidelines.md#triggering-further-workflow-runs) for workarounds.

| Name | Description | Default |
| --- | --- | --- |
| `token` | `GITHUB_TOKEN` (permissions `contents: write` and `pull-requests: write`) or a `repo` scoped [Personal Access Token (PAT)](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token). | `GITHUB_TOKEN` |
| `path` | Relative path under `GITHUB_WORKSPACE` to the repository. | `GITHUB_WORKSPACE` |
| `add-paths` | A comma or newline-separated list of file paths to commit. Paths should follow git's [pathspec](https://git-scm.com/docs/gitglossary#Documentation/gitglossary.txt-aiddefpathspecapathspec) syntax. If no paths are specified, all new and modified files are added. See [Add specific paths](#add-specific-paths). | |
| `commit-message` | The message to use when committing changes. | `[create-pull-request] automated change` |
| `committer` | The committer name and email address in the format `Display Name <email@address.com>`. Defaults to the GitHub Actions bot user. | `GitHub <noreply@github.com>` |
| `author` | The author name and email address in the format `Display Name <email@address.com>`. Defaults to the user who triggered the workflow run. | `${{ github.actor }} <${{ github.actor }}@users.noreply.github.com>` |
| `signoff` | Add [`Signed-off-by`](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---signoff) line by the committer at the end of the commit log message. | `false` |
| `branch` | The pull request branch name. | `create-pull-request/patch` |
| `delete-branch` | Delete the `branch` when closing pull requests, and when undeleted after merging. Recommend `true`. | `false` |
| `branch-suffix` | The branch suffix type when using the alternative branching strategy. Valid values are `random`, `timestamp` and `short-commit-hash`. See [Alternative strategy](#alternative-strategy---always-create-a-new-pull-request-branch) for details. | |
| `base` | Sets the pull request base branch. | Defaults to the branch checked out in the workflow. |
| `push-to-fork` | A fork of the checked-out parent repository to which the pull request branch will be pushed. e.g. `owner/repo-fork`. The pull request will be created to merge the fork's branch into the parent's base. See [push pull request branches to a fork](docs/concepts-guidelines.md#push-pull-request-branches-to-a-fork) for details. | |
| `title` | The title of the pull request. | `Changes by create-pull-request action` |
| `body` | The body of the pull request. | `Automated changes by [create-pull-request](https://github.com/peter-evans/create-pull-request) GitHub action` |
| `labels` | A comma or newline-separated list of labels. | |
| `assignees` | A comma or newline-separated list of assignees (GitHub usernames). | |
| `reviewers` | A comma or newline-separated list of reviewers (GitHub usernames) to request a review from. | |
| `team-reviewers` | A comma or newline-separated list of GitHub teams to request a review from. Note that a `repo` scoped [PAT](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token) may be required. See [this issue](https://github.com/peter-evans/create-pull-request/issues/155). If using a GitHub App, refer to [Authenticating with GitHub App generated tokens](docs/concepts-guidelines.md#authenticating-with-github-app-generated-tokens) for the proper permissions. | |
| `milestone` | The number of the milestone to associate this pull request with. | |
| `draft` | Create a [draft pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests#draft-pull-requests). It is not possible to change draft status after creation except through the web interface. | `false` |

For self-hosted runners behind a corporate proxy set the `https_proxy` environment variable.
```yml
      - name: Create Pull Request
        uses: peter-evans/create-pull-request@v4
        env:
          https_proxy: http://<proxy_address>:<port>
```

### Action outputs

The following outputs can be used by subsequent workflow steps.

- `pull-request-number` - The pull request number.
- `pull-request-url` - The URL of the pull request.
- `pull-request-operation` - The pull request operation performed by the action, `created`, `updated` or `closed`.
- `pull-request-head-sha` - The commit SHA of the pull request branch.

Step outputs can be accessed as in the following example.
Note that in order to read the step outputs the action step must have an id.

```yml
      - name: Create Pull Request
        id: cpr
        uses: peter-evans/create-pull-request@v4
      - name: Check outputs
        if: ${{ steps.cpr.outputs.pull-request-number }}
        run: |
          echo "Pull Request Number - ${{ steps.cpr.outputs.pull-request-number }}"
          echo "Pull Request URL - ${{ steps.cpr.outputs.pull-request-url }}"
```

### Action behaviour

The default behaviour of the action is to create a pull request that will be continually updated with new changes until it is merged or closed.
Changes are committed and pushed to a fixed-name branch, the name of which can be configured with the `branch` input.
Any subsequent changes will be committed to the *same* branch and reflected in the open pull request.

How the action behaves:

- If there are changes (i.e. a diff exists with the checked-out base branch), the changes will be pushed to a new `branch` and a pull request created.
- If there are no changes (i.e. no diff exists with the checked-out base branch), no pull request will be created and the action exits silently.
- If a pull request already exists it will be updated if necessary. Local changes in the Actions workspace, or changes on the base branch, can cause an update. If no update is required the action exits silently.
- If a pull request exists and new changes on the base branch make the pull request unnecessary (i.e. there is no longer a diff between the pull request branch and the base), the pull request is automatically closed. Additionally, if `delete-branch` is set to `true` the `branch` will be deleted.

For further details about how the action works and usage guidelines, see [Concepts, guidelines and advanced usage](docs/concepts-guidelines.md).

#### Alternative strategy - Always create a new pull request branch

For some use cases it may be desirable to always create a new unique branch each time there are changes to be committed.
This strategy is *not recommended* because if not used carefully it could result in multiple pull requests being created unnecessarily. If in doubt, use the [default strategy](#action-behaviour) of creating an updating a fixed-name branch.

To use this strategy, set input `branch-suffix` with one of the following options.

- `random` - Commits will be made to a branch suffixed with a random alpha-numeric string. e.g. `create-pull-request/patch-6qj97jr`, `create-pull-request/patch-5jrjhvd`

- `timestamp` - Commits will be made to a branch suffixed by a timestamp. e.g. `create-pull-request/patch-1569322532`, `create-pull-request/patch-1569322552`

- `short-commit-hash` - Commits will be made to a branch suffixed with the short SHA1 commit hash. e.g. `create-pull-request/patch-fcdfb59`, `create-pull-request/patch-394710b`

### Controlling committed files

The action defaults to adding all new and modified files.
If there are files that should not be included in the pull request, you can use the following methods to control the committed content.

#### Remove files

The most straightforward way to handle unwanted files is simply to remove them in a step before the action runs.

```yml
      - run: |
          rm -rf temp-dir
          rm temp-file.txt
```

#### Ignore files

If there are files or directories you want to ignore you can simply add them to a `.gitignore` file at the root of your repository. The action will respect this file.

#### Add specific paths

You can control which files are committed with the `add-paths` input.
Paths should follow git's [pathspec](https://git-scm.com/docs/gitglossary#Documentation/gitglossary.txt-aiddefpathspecapathspec) syntax.
All file changes that do not match one of the paths will be discarded.

```yml
      - name: Create Pull Request
        uses: peter-evans/create-pull-request@v4
        with:
          add-paths: |
            *.java
            docs/*.md
```

#### Create your own commits

As well as relying on the action to handle uncommitted changes, you can additionally make your own commits before the action runs.
Note that the repository must be checked out on a branch with a remote, it won't work for [events which checkout a commit](docs/concepts-guidelines.md#events-which-checkout-a-commit).

```yml
    steps:
      - uses: actions/checkout@v3
      - name: Create commits
        run: |
          git config user.name 'Peter Evans'
          git config user.email 'peter-evans@users.noreply.github.com'
          date +%s > report.txt
          git commit -am "Modify tracked file during workflow"
          date +%s > new-report.txt
          git add -A
          git commit -m "Add untracked file during workflow"
      - name: Uncommitted change
        run: date +%s > report.txt
      - name: Create Pull Request
        uses: peter-evans/create-pull-request@v4
```

### Create a project card

To create a project card for the pull request, pass the `pull-request-number` step output to [create-or-update-project-card](https://github.com/peter-evans/create-or-update-project-card) action.

```yml
      - name: Create Pull Request
        id: cpr
        uses: peter-evans/create-pull-request@v4
      - name: Create or Update Project Card
        if: ${{ steps.cpr.outputs.pull-request-number }}
        uses: peter-evans/create-or-update-project-card@v2
        with:
          project-name: My project
          column-name: My column
          issue-number: ${{ steps.cpr.outputs.pull-request-number }}
```

### Auto-merge

Auto-merge can be enabled on a pull request allowing it to be automatically merged once requirements have been satisfied.
See [enable-pull-request-automerge](https://github.com/peter-evans/enable-pull-request-automerge) action for usage details.

## Reference Example

The following workflow sets many of the action's inputs for reference purposes.
Check the [defaults](#action-inputs) to avoid setting inputs unnecessarily.

See [examples](docs/examples.md) for more realistic use cases.

```yml
jobs:
  createPullRequest:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Make changes to pull request
        run: date +%s > report.txt
      - name: Create Pull Request
        id: cpr
        uses: peter-evans/create-pull-request@v4
        with:
          token: ${{ secrets.PAT }}
          commit-message: Update report
          committer: GitHub <noreply@github.com>
          author: ${{ github.actor }} <${{ github.actor }}@users.noreply.github.com>
          signoff: false
          branch: example-patches
          delete-branch: true
          title: '[Example] Update report'
          body: |
            Update report
            - Updated with *today's* date
            - Auto-generated by [create-pull-request][1]
            [1]: https://github.com/peter-evans/create-pull-request
          labels: |
            report
            automated pr
          assignees: peter-evans
          reviewers: peter-evans
          team-reviewers: |
            owners
            maintainers
          milestone: 1
          draft: false
```

An example based on the above reference configuration creates pull requests that look like this:

![Pull Request Example](docs/assets/pull-request-example.png)

## License

[MIT](LICENSE)
 1,942  
__test__/create-or-update-branch.int.test.ts
Large diffs are not rendered by default.

 40  
__test__/entrypoint.sh
@@ -0,0 +1,40 @@
#!/bin/sh -l
set -euo pipefail

# Save the working directory
WORKINGDIR=$PWD

# Create and serve a remote repo
mkdir -p /git/remote
git init --bare /git/remote/test-base.git
git daemon --verbose --enable=receive-pack --base-path=/git/remote --export-all /git/remote &>/dev/null &

# Give the daemon time to start
sleep 2

# Create a local clone and make an initial commit
mkdir -p /git/local
git clone git://127.0.0.1/test-base.git /git/local/test-base
cd /git/local/test-base
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
echo "#test-base" > README.md
git add .
git commit -m "initial commit"
git push -u
git log -1 --pretty=oneline
git config --global --unset user.email
git config --global --unset user.name
git config -l

# Clone a server-side fork of the base repo
cd $WORKINGDIR
git clone --mirror git://127.0.0.1/test-base.git /git/remote/test-fork.git
cd /git/remote/test-fork.git
git log -1 --pretty=oneline

# Restore the working directory
cd $WORKINGDIR

# Execute integration tests
jest int --runInBand
 49  
__test__/git-auth-helper.int.test.ts
@@ -0,0 +1,49 @@
import {GitCommandManager} from '../lib/git-command-manager'
import {GitAuthHelper} from '../lib/git-auth-helper'

const REPO_PATH = '/git/local/test-base'

const extraheaderConfigKey = 'http.https://github.com/.extraheader'

describe('git-auth-helper tests', () => {
  let git: GitCommandManager
  let gitAuthHelper: GitAuthHelper

  beforeAll(async () => {
    git = await GitCommandManager.create(REPO_PATH)
    gitAuthHelper = new GitAuthHelper(git)
  })

  it('tests save and restore with no persisted auth', async () => {
    await gitAuthHelper.savePersistedAuth()
    await gitAuthHelper.restorePersistedAuth()
  })

  it('tests configure and removal of auth', async () => {
    await gitAuthHelper.configureToken('github-token')
    expect(await git.configExists(extraheaderConfigKey)).toBeTruthy()
    expect(await git.getConfigValue(extraheaderConfigKey)).toEqual(
      'AUTHORIZATION: basic eC1hY2Nlc3MtdG9rZW46Z2l0aHViLXRva2Vu'
    )

    await gitAuthHelper.removeAuth()
    expect(await git.configExists(extraheaderConfigKey)).toBeFalsy()
  })

  it('tests save and restore of persisted auth', async () => {
    const extraheaderConfigValue = 'AUTHORIZATION: basic ***persisted-auth***'
    await git.config(extraheaderConfigKey, extraheaderConfigValue)

    await gitAuthHelper.savePersistedAuth()

    const exists = await git.configExists(extraheaderConfigKey)
    expect(exists).toBeFalsy()

    await gitAuthHelper.restorePersistedAuth()

    const configValue = await git.getConfigValue(extraheaderConfigKey)
    expect(configValue).toEqual(extraheaderConfigValue)

    await gitAuthHelper.removeAuth()
  })
})
 23  
__test__/integration-tests.sh
@@ -0,0 +1,23 @@
#!/usr/bin/env bash
set -euo pipefail

IMAGE="cpr-integration-tests:latest"
ARG1=${1:-}

if [[ "$(docker images -q $IMAGE 2> /dev/null)" == "" || $ARG1 == "build" ]]; then
    echo "Building Docker image $IMAGE ..."

    cat > Dockerfile << EOF
FROM node:16-alpine
RUN apk --no-cache add git git-daemon
RUN npm install jest jest-environment-jsdom --global
WORKDIR /cpr
COPY __test__/entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
EOF

    docker build --no-cache -t $IMAGE .
    rm Dockerfile
fi

docker run -v $PWD:/cpr $IMAGE
 130  
__test__/utils.unit.test.ts
@@ -0,0 +1,130 @@
import * as path from 'path'
import * as utils from '../lib/utils'

const originalGitHubWorkspace = process.env['GITHUB_WORKSPACE']

describe('utils tests', () => {
  beforeAll(() => {
    // GitHub workspace
    process.env['GITHUB_WORKSPACE'] = __dirname
  })

  afterAll(() => {
    // Restore GitHub workspace
    delete process.env['GITHUB_WORKSPACE']
    if (originalGitHubWorkspace) {
      process.env['GITHUB_WORKSPACE'] = originalGitHubWorkspace
    }
  })

  test('getStringAsArray splits string input by newlines and commas', async () => {
    const array = utils.getStringAsArray('1, 2, 3\n4, 5, 6')
    expect(array.length).toEqual(6)

    const array2 = utils.getStringAsArray('')
    expect(array2.length).toEqual(0)
  })

  test('getRepoPath successfully returns the path to the repository', async () => {
    expect(utils.getRepoPath()).toEqual(process.env['GITHUB_WORKSPACE'])
    expect(utils.getRepoPath('foo')).toEqual(
      path.resolve(process.env['GITHUB_WORKSPACE'] || '', 'foo')
    )
  })

  test('getRemoteDetail successfully parses remote URLs', async () => {
    const remote1 = utils.getRemoteDetail(
      'https://github.com/peter-evans/create-pull-request'
    )
    expect(remote1.protocol).toEqual('HTTPS')
    expect(remote1.repository).toEqual('peter-evans/create-pull-request')

    const remote2 = utils.getRemoteDetail(
      'https://xxx:x-oauth-basic@github.com/peter-evans/create-pull-request'
    )
    expect(remote2.protocol).toEqual('HTTPS')
    expect(remote2.repository).toEqual('peter-evans/create-pull-request')

    const remote3 = utils.getRemoteDetail(
      'git@github.com:peter-evans/create-pull-request.git'
    )
    expect(remote3.protocol).toEqual('SSH')
    expect(remote3.repository).toEqual('peter-evans/create-pull-request')

    const remote4 = utils.getRemoteDetail(
      'https://github.com/peter-evans/create-pull-request.git'
    )
    expect(remote4.protocol).toEqual('HTTPS')
    expect(remote4.repository).toEqual('peter-evans/create-pull-request')
  })

  test('getRemoteDetail fails to parse a remote URL', async () => {
    const remoteUrl = 'https://github.com/peter-evans'
    try {
      utils.getRemoteDetail(remoteUrl)
      // Fail the test if an error wasn't thrown
      expect(true).toEqual(false)
    } catch (e: any) {
      expect(e.message).toEqual(
        `The format of '${remoteUrl}' is not a valid GitHub repository URL`
      )
    }
  })

  test('getRemoteUrl successfully returns remote URLs', async () => {
    const url1 = utils.getRemoteUrl('HTTPS', 'peter-evans/create-pull-request')
    expect(url1).toEqual('https://github.com/peter-evans/create-pull-request')

    const url2 = utils.getRemoteUrl('SSH', 'peter-evans/create-pull-request')
    expect(url2).toEqual('git@github.com:peter-evans/create-pull-request.git')
  })

  test('secondsSinceEpoch returns the number of seconds since the Epoch', async () => {
    const seconds = `${utils.secondsSinceEpoch()}`
    expect(seconds.length).toEqual(10)
  })

  test('randomString returns strings of length 7', async () => {
    for (let i = 0; i < 1000; i++) {
      expect(utils.randomString().length).toEqual(7)
    }
  })

  test('parseDisplayNameEmail successfully parses display name email formats', async () => {
    const parsed1 = utils.parseDisplayNameEmail('abc def <abc@def.com>')
    expect(parsed1.name).toEqual('abc def')
    expect(parsed1.email).toEqual('abc@def.com')

    const parsed2 = utils.parseDisplayNameEmail(
      'github-actions[bot] <41898282+github-actions[bot]@users.noreply.github.com>'
    )
    expect(parsed2.name).toEqual('github-actions[bot]')
    expect(parsed2.email).toEqual(
      '41898282+github-actions[bot]@users.noreply.github.com'
    )
  })

  test('parseDisplayNameEmail fails to parse display name email formats', async () => {
    const displayNameEmail1 = 'abc@def.com'
    try {
      utils.parseDisplayNameEmail(displayNameEmail1)
      // Fail the test if an error wasn't thrown
      expect(true).toEqual(false)
    } catch (e: any) {
      expect(e.message).toEqual(
        `The format of '${displayNameEmail1}' is not a valid email address with display name`
      )
    }

    const displayNameEmail2 = ' < >'
    try {
      utils.parseDisplayNameEmail(displayNameEmail2)
      // Fail the test if an error wasn't thrown
      expect(true).toEqual(false)
    } catch (e: any) {
      expect(e.message).toEqual(
        `The format of '${displayNameEmail2}' is not a valid email address with display name`
      )
    }
  })
})
 86  
action.yml
@@ -0,0 +1,86 @@
name: 'Create Pull Request'
description: 'Creates a pull request for changes to your repository in the actions workspace'
inputs:
  token:
    description: 'GITHUB_TOKEN or a `repo` scoped Personal Access Token (PAT)'
    default: ${{ github.token }}
  path:
    description: >
      Relative path under $GITHUB_WORKSPACE to the repository.
      Defaults to $GITHUB_WORKSPACE.
  add-paths:
    description: >
      A comma or newline-separated list of file paths to commit.
      Paths should follow git's pathspec syntax.
      Defaults to adding all new and modified files.
  commit-message:
    description: 'The message to use when committing changes.'
    default: '[create-pull-request] automated change'
  committer:
    description: >
      The committer name and email address in the format `Display Name <email@address.com>`.
      Defaults to the GitHub Actions bot user.
    default: 'GitHub <noreply@github.com>'
  author:
    description: >
      The author name and email address in the format `Display Name <email@address.com>`.
      Defaults to the user who triggered the workflow run.
    default: '${{ github.actor }} <${{ github.actor }}@users.noreply.github.com>'
  signoff:
    description: 'Add `Signed-off-by` line by the committer at the end of the commit log message.'
    default: false
  branch:
    description: 'The pull request branch name.'
    default: 'create-pull-request/patch'
  delete-branch:
    description: >
      Delete the `branch` when closing pull requests, and when undeleted after merging.
      Recommend `true`.
    default: false
  branch-suffix:
    description: 'The branch suffix type when using the alternative branching strategy.'
  base:
    description: >
      The pull request base branch.
      Defaults to the branch checked out in the workflow.
  push-to-fork:
    description: >
      A fork of the checked out parent repository to which the pull request branch will be pushed.
      e.g. `owner/repo-fork`.
      The pull request will be created to merge the fork's branch into the parent's base.
  title:
    description: 'The title of the pull request.'
    default: 'Changes by create-pull-request action'
  body:
    description: 'The body of the pull request.'
    default: 'Automated changes by [create-pull-request](https://github.com/peter-evans/create-pull-request) GitHub action'
  labels:
    description: 'A comma or newline separated list of labels.'
  assignees:
    description: 'A comma or newline separated list of assignees (GitHub usernames).'
  reviewers:
    description: 'A comma or newline separated list of reviewers (GitHub usernames) to request a review from.'
  team-reviewers:
    description: >
      A comma or newline separated list of GitHub teams to request a review from.
      Note that a `repo` scoped Personal Access Token (PAT) may be required.
  milestone:
    description: 'The number of the milestone to associate the pull request with.'
  draft:
    description: 'Create a draft pull request. It is not possible to change draft status after creation except through the web interface'
    default: false
outputs:
  pull-request-number:
    description: 'The pull request number'
  pull-request-url:
    description: 'The URL of the pull request.'
  pull-request-operation:
    description: 'The pull request operation performed by the action, `created`, `updated` or `closed`.'
  pull-request-head-sha:
    description: 'The commit SHA of the pull request branch.'
runs:
  using: 'node16'
  main: 'dist/index.js'
branding:
  icon: 'git-pull-request'
  color: 'gray-dark'
 13,672  
dist/index.js
Large diffs are not rendered by default.

 68  
docs/assets/cpr-gitgraph.htm
@@ -0,0 +1,68 @@
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>create-pull-request GitHub action</title>
</head>

<body>
    <!-- partial:index.partial.html -->
    <div id="graph-container"></div>
    <!-- partial -->
    <script src='https://cdn.jsdelivr.net/npm/@gitgraph/js'></script>
    <script>
        const graphContainer = document.getElementById("graph-container");

        const customTemplate = GitgraphJS.templateExtend(GitgraphJS.TemplateName.Metro, {
            commit: {
                message: {
                    displayAuthor: false,
                    displayHash: false,
                },
            },
        });

        // Instantiate the graph.
        const gitgraph = GitgraphJS.createGitgraph(graphContainer, {
            template: customTemplate,
            orientation: "vertical-reverse"
        });

        const main = gitgraph.branch("main");
        main.commit("Last commit on base");
        const localMain = gitgraph.branch("<#1> main (local)");
        localMain.commit({
            subject: "<uncommitted changes>",
            body: "Changes to the local base during the workflow",
        })
        const remotePatch = gitgraph.branch("create-pull-request/patch");
        remotePatch.merge({
            branch: localMain,
            commitOptions: {
                subject: "[create-pull-request] automated change",
                body: "Changes pushed to create the remote branch",
            },
        });
        main.commit("New commit on base");

        const localMain2 = gitgraph.branch("<#2> main (local)");
        localMain2.commit({
            subject: "<uncommitted changes>",
            body: "Changes to the updated local base during the workflow",
        })
        remotePatch.merge({
            branch: localMain2,
            commitOptions: {
                subject: "[create-pull-request] automated change",
                body: "Changes force pushed to update the remote branch",
            },
        });

        main.merge(remotePatch);

    </script>

</body>

</html>
 BIN +108 KB 
docs/assets/cpr-gitgraph.png
Unable to render code block

 6  
docs/assets/logo.svg
Unable to render code block

 BIN +327 KB 
docs/assets/pull-request-example.png
Unable to render code block

 370  
docs/concepts-guidelines.md
Large diffs are not rendered by default.

 630  
docs/examples.md
Large diffs are not rendered by default.

 87  
docs/updating.md
@@ -0,0 +1,87 @@
## Updating from `v3` to `v4`

### Breaking changes

- The `add-paths` input no longer accepts `-A` as a valid value. When committing all new and modified files the `add-paths` input should be omitted.

- If using self-hosted runners or GitHub Enterprise Server, there are minimum requirements for `v4` to run. See "What's new" below for details.

### What's new

- Updated runtime to Node.js 16
  - The action now requires a minimum version of v2.285.0 for the [Actions Runner](https://github.com/actions/runner/releases/tag/v2.285.0).
  - If using GitHub Enterprise Server, the action requires [GHES 3.4](https://docs.github.com/en/enterprise-server@3.4/admin/release-notes) or later.

## Updating from `v2` to `v3`

### Breaking changes

- The `author` input now defaults to the user who triggered the workflow run. This default is set via [action.yml](../action.yml) as `${{ github.actor }} <${{ github.actor }}@users.noreply.github.com>`, where `github.actor` is the GitHub user account associated with the run. For example, `peter-evans <peter-evans@users.noreply.github.com>`.

  To continue to use the `v2` default, set the `author` input as follows.
  ```yaml
      - uses: peter-evans/create-pull-request@v3
        with:
          author: github-actions[bot] <41898282+github-actions[bot]@users.noreply.github.com>
  ```

- The `author` and `committer` inputs are no longer cross-used if only one is supplied. Additionally, when neither input is set, the `author` and `committer` are no longer determined from an existing identity set in git config. In both cases, the inputs will fall back to their default set in [action.yml](../action.yml).

- Deprecated inputs `project` and `project-column` have been removed in favour of an additional action step. See [Create a project card](https://github.com/peter-evans/create-pull-request#create-a-project-card) for details.

- Deprecated output `pr_number` has been removed in favour of `pull-request-number`.

- Input `request-to-parent` has been removed in favour of `push-to-fork`. This greatly simplifies pushing the pull request branch to a fork of the parent repository. See [Push pull request branches to a fork](concepts-guidelines.md#push-pull-request-branches-to-a-fork) for details.

  e.g.
  ```yaml
      - uses: actions/checkout@v2
      # Make changes to pull request here
      - uses: peter-evans/create-pull-request@v3
        with:
          token: ${{ secrets.MACHINE_USER_PAT }}
          push-to-fork: machine-user/fork-of-repository
  ```

### What's new

- The action has been converted to Typescript giving it a significant performance improvement.

- If you run this action in a container, or on [self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners), `python` and `pip` are no longer required dependencies. See [Running in a container or on self-hosted runners](concepts-guidelines.md#running-in-a-container-or-on-self-hosted-runners) for details.

- Inputs `labels`, `assignees`, `reviewers` and `team-reviewers` can now be newline separated, or comma separated.
  e.g.
  ```yml
          labels: |
            chore
            dependencies
            automated
  ```

## Updating from `v1` to `v2`

### Breaking changes

- `v2` now expects repositories to be checked out with `actions/checkout@v2`

  To use `actions/checkout@v1` the following step to checkout the branch is necessary.
  ```yml
      - uses: actions/checkout@v1
      - name: Checkout branch
        run: git checkout "${GITHUB_REF:11}"
  ```

- The two branch naming strategies have been swapped. Fixed-branch naming strategy is now the default. i.e. `branch-suffix: none` is now the default and should be removed from configuration if set.

- `author-name`, `author-email`, `committer-name`, `committer-email` have been removed in favour of `author` and `committer`.
  They can both be set in the format `Display Name <email@address.com>`

  If neither `author` or `committer` are set the action will default to making commits as the GitHub Actions bot user.

### What's new

- Unpushed commits made during the workflow before the action runs will now be considered as changes to be raised in the pull request. See [Create your own commits](https://github.com/peter-evans/create-pull-request#create-your-own-commits) for details.
- New commits made to the pull request base will now be taken into account when pull requests are updated.
- If an updated pull request no longer differs from its base it will automatically be closed and the pull request branch deleted.
 276  
gideons.sig
Large diffs are not rendered by default.

 11  
jest.config.js
@@ -0,0 +1,11 @@
module.exports = {
  clearMocks: true,
  moduleFileExtensions: ['js', 'ts'],
  testEnvironment: 'node',
  testMatch: ['**/*.test.ts'],
  testRunner: 'jest-circus/runner',
  transform: {
    '^.+\\.ts$': 'ts-jest'
  },
  verbose: true
}
 13,315  
package-lock.json
Large diffs are not rendered by default.

 58  
package.json
@@ -0,0 +1,58 @@
{
  "name": "create-pull-request",
  "version": "4.0.0",
  "private": true,
  "description": "Creates a pull request for changes to your repository in the actions workspace",
  "main": "lib/main.js",
  "scripts": {
    "build": "tsc && ncc build",
    "format": "prettier --write '**/*.ts'",
    "format-check": "prettier --check '**/*.ts'",
    "lint": "eslint src/**/*.ts",
    "test:unit": "jest unit",
    "test:int": "__test__/integration-tests.sh",
    "test": "npm run test:unit && npm run test:int"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/peter-evans/create-pull-request.git"
  },
  "keywords": [
    "actions",
    "pull",
    "request"
  ],
  "author": "Peter Evans",
  "license": "MIT",
  "bugs": {
    "url": "https://github.com/peter-evans/create-pull-request/issues"
  },
  "homepage": "https://github.com/peter-evans/create-pull-request",
  "dependencies": {
    "@actions/core": "^1.9.1",
    "@actions/exec": "^1.1.0",
    "@octokit/core": "^3.5.1",
    "@octokit/plugin-paginate-rest": "^2.17.0",
    "@octokit/plugin-rest-endpoint-methods": "^5.13.0",
    "https-proxy-agent": "^5.0.0",
    "uuid": "^8.3.2"
  },
  "devDependencies": {
    "@types/jest": "^27.5.0",
    "@types/node": "^16.11.11",
    "@typescript-eslint/parser": "^5.5.0",
    "@vercel/ncc": "^0.32.0",
    "eslint": "^8.3.0",
    "eslint-import-resolver-typescript": "^2.5.0",
    "eslint-plugin-github": "^4.3.5",
    "eslint-plugin-import": "^2.25.3",
    "eslint-plugin-jest": "^26.1.5",
    "jest": "^28.1.0",
    "jest-circus": "^28.1.0",
    "jest-environment-jsdom": "^28.1.0",
    "js-yaml": "^4.1.0",
    "prettier": "^2.5.0",
    "ts-jest": "^28.0.2",
    "typescript": "^4.5.2"
  }
}
 270  
src/create-or-update-branch.ts
@@ -0,0 +1,270 @@
import * as core from '@actions/core'
import {GitCommandManager} from './git-command-manager'
import {v4 as uuidv4} from 'uuid'

const CHERRYPICK_EMPTY =
  'The previous cherry-pick is now empty, possibly due to conflict resolution.'
const NOTHING_TO_COMMIT = 'nothing to commit, working tree clean'

export enum WorkingBaseType {
  Branch = 'branch',
  Commit = 'commit'
}

export async function getWorkingBaseAndType(
  git: GitCommandManager
): Promise<[string, WorkingBaseType]> {
  const symbolicRefResult = await git.exec(
    ['symbolic-ref', 'HEAD', '--short'],
    true
  )
  if (symbolicRefResult.exitCode == 0) {
    // A ref is checked out
    return [symbolicRefResult.stdout.trim(), WorkingBaseType.Branch]
  } else {
    // A commit is checked out (detached HEAD)
    const headSha = await git.revParse('HEAD')
    return [headSha, WorkingBaseType.Commit]
  }
}

export async function tryFetch(
  git: GitCommandManager,
  remote: string,
  branch: string
): Promise<boolean> {
  try {
    await git.fetch([`${branch}:refs/remotes/${remote}/${branch}`], remote, [
      '--force'
    ])
    return true
  } catch {
    return false
  }
}

// Return true if branch2 is ahead of branch1
async function isAhead(
  git: GitCommandManager,
  branch1: string,
  branch2: string
): Promise<boolean> {
  const result = await git.revList(
    [`${branch1}...${branch2}`],
    ['--right-only', '--count']
  )
  return Number(result) > 0
}

// Return true if branch2 is behind branch1
async function isBehind(
  git: GitCommandManager,
  branch1: string,
  branch2: string
): Promise<boolean> {
  const result = await git.revList(
    [`${branch1}...${branch2}`],
    ['--left-only', '--count']
  )
  return Number(result) > 0
}

// Return true if branch2 is even with branch1
async function isEven(
  git: GitCommandManager,
  branch1: string,
  branch2: string
): Promise<boolean> {
  return (
    !(await isAhead(git, branch1, branch2)) &&
    !(await isBehind(git, branch1, branch2))
  )
}

function splitLines(multilineString: string): string[] {
  return multilineString
    .split('\n')
    .map(s => s.trim())
    .filter(x => x !== '')
}

export async function createOrUpdateBranch(
  git: GitCommandManager,
  commitMessage: string,
  base: string,
  branch: string,
  branchRemoteName: string,
  signoff: boolean,
  addPaths: string[]
): Promise<CreateOrUpdateBranchResult> {
  // Get the working base.
  // When a ref, it may or may not be the actual base.
  // When a commit, we must rebase onto the actual base.
  const [workingBase, workingBaseType] = await getWorkingBaseAndType(git)
  core.info(`Working base is ${workingBaseType} '${workingBase}'`)
  if (workingBaseType == WorkingBaseType.Commit && !base) {
    throw new Error(`When in 'detached HEAD' state, 'base' must be supplied.`)
  }

  // If the base is not specified it is assumed to be the working base.
  base = base ? base : workingBase
  const baseRemote = 'origin'

  // Set the default return values
  const result: CreateOrUpdateBranchResult = {
    action: 'none',
    base: base,
    hasDiffWithBase: false,
    headSha: ''
  }

  // Save the working base changes to a temporary branch
  const tempBranch = uuidv4()
  await git.checkout(tempBranch, 'HEAD')
  // Commit any uncommitted changes
  if (await git.isDirty(true, addPaths)) {
    core.info('Uncommitted changes found. Adding a commit.')
    const aopts = ['add']
    if (addPaths.length > 0) {
      aopts.push(...['--', ...addPaths])
    } else {
      aopts.push('-A')
    }
    await git.exec(aopts, true)
    const popts = ['-m', commitMessage]
    if (signoff) {
      popts.push('--signoff')
    }
    const commitResult = await git.commit(popts, true)
    // 'nothing to commit' can occur when core.autocrlf is set to true
    if (
      commitResult.exitCode != 0 &&
      !commitResult.stdout.includes(NOTHING_TO_COMMIT)
    ) {
      throw new Error(`Unexpected error: ${commitResult.stderr}`)
    }
  }

  // Remove uncommitted tracked and untracked changes
  await git.exec(['reset', '--hard'])
  await git.exec(['clean', '-f', '-d'])

  // Perform fetch and reset the working base
  // Commits made during the workflow will be removed
  if (workingBaseType == WorkingBaseType.Branch) {
    core.info(`Resetting working base branch '${workingBase}'`)
    if (branchRemoteName == 'fork') {
      // If pushing to a fork we must fetch with 'unshallow' to avoid the following error on git push
      // ! [remote rejected] HEAD -> tests/push-branch-to-fork (shallow update not allowed)
      await git.fetch([`${workingBase}:${workingBase}`], baseRemote, [
        '--force'
      ])
    } else {
      // If the remote is 'origin' we can git reset
      await git.checkout(workingBase)
      await git.exec(['reset', '--hard', `${baseRemote}/${workingBase}`])
    }
  }

  // If the working base is not the base, rebase the temp branch commits
  // This will also be true if the working base type is a commit
  if (workingBase != base) {
    core.info(
      `Rebasing commits made to ${workingBaseType} '${workingBase}' on to base branch '${base}'`
    )
    // Checkout the actual base
    await git.fetch([`${base}:${base}`], baseRemote, ['--force'])
    await git.checkout(base)
    // Cherrypick commits from the temporary branch starting from the working base
    const commits = await git.revList(
      [`${workingBase}..${tempBranch}`, '.'],
      ['--reverse']
    )
    for (const commit of splitLines(commits)) {
      const result = await git.cherryPick(
        ['--strategy=recursive', '--strategy-option=theirs', commit],
        true
      )
      if (result.exitCode != 0 && !result.stderr.includes(CHERRYPICK_EMPTY)) {
        throw new Error(`Unexpected error: ${result.stderr}`)
      }
    }
    // Reset the temp branch to the working index
    await git.checkout(tempBranch, 'HEAD')
    // Reset the base
    await git.fetch([`${base}:${base}`], baseRemote, ['--force'])
  }

  // Try to fetch the pull request branch
  if (!(await tryFetch(git, branchRemoteName, branch))) {
    // The pull request branch does not exist
    core.info(`Pull request branch '${branch}' does not exist yet.`)
    // Create the pull request branch
    await git.checkout(branch, tempBranch)
    // Check if the pull request branch is ahead of the base
    result.hasDiffWithBase = await isAhead(git, base, branch)
    if (result.hasDiffWithBase) {
      result.action = 'created'
      core.info(`Created branch '${branch}'`)
    } else {
      core.info(
        `Branch '${branch}' is not ahead of base '${base}' and will not be created`
      )
    }
  } else {
    // The pull request branch exists
    core.info(
      `Pull request branch '${branch}' already exists as remote branch '${branchRemoteName}/${branch}'`
    )
    // Checkout the pull request branch
    await git.checkout(branch)

    // Reset the branch if one of the following conditions is true.
    // - If the branch differs from the recreated temp branch.
    // - If the recreated temp branch is not ahead of the base. This means there will be
    //   no pull request diff after the branch is reset. This will reset any undeleted
    //   branches after merging. In particular, it catches a case where the branch was
    //   squash merged but not deleted. We need to reset to make sure it doesn't appear
    //   to have a diff with the base due to different commits for the same changes.
    // For changes on base this reset is equivalent to a rebase of the pull request branch.
    if (
      (await git.hasDiff([`${branch}..${tempBranch}`])) ||
      !(await isAhead(git, base, tempBranch))
    ) {
      core.info(`Resetting '${branch}'`)
      // Alternatively, git switch -C branch tempBranch
      await git.checkout(branch, tempBranch)
    }

    // Check if the pull request branch has been updated
    // If the branch was reset or updated it will be ahead
    // It may be behind if a reset now results in no diff with the base
    if (!(await isEven(git, `${branchRemoteName}/${branch}`, branch))) {
      result.action = 'updated'
      core.info(`Updated branch '${branch}'`)
    } else {
      result.action = 'not-updated'
      core.info(
        `Branch '${branch}' is even with its remote and will not be updated`
      )
    }

    // Check if the pull request branch is ahead of the base
    result.hasDiffWithBase = await isAhead(git, base, branch)
  }

  // Get the pull request branch SHA
  result.headSha = await git.revParse('HEAD')

  // Delete the temporary branch
  await git.exec(['branch', '--delete', '--force', tempBranch])

  return result
}

interface CreateOrUpdateBranchResult {
  action: string
  base: string
  hasDiffWithBase: boolean
  headSha: string
}
 252  
src/create-pull-request.ts
@@ -0,0 +1,252 @@
import * as core from '@actions/core'
import {
  createOrUpdateBranch,
  getWorkingBaseAndType,
  WorkingBaseType
} from './create-or-update-branch'
import {GitHubHelper} from './github-helper'
import {GitCommandManager} from './git-command-manager'
import {GitAuthHelper} from './git-auth-helper'
import * as utils from './utils'

export interface Inputs {
  token: string
  path: string
  addPaths: string[]
  commitMessage: string
  committer: string
  author: string
  signoff: boolean
  branch: string
  deleteBranch: boolean
  branchSuffix: string
  base: string
  pushToFork: string
  title: string
  body: string
  labels: string[]
  assignees: string[]
  reviewers: string[]
  teamReviewers: string[]
  milestone: number
  draft: boolean
}

export async function createPullRequest(inputs: Inputs): Promise<void> {
  let gitAuthHelper
  try {
    // Get the repository path
    const repoPath = utils.getRepoPath(inputs.path)
    // Create a git command manager
    const git = await GitCommandManager.create(repoPath)

    // Save and unset the extraheader auth config if it exists
    core.startGroup('Save persisted git credentials')
    gitAuthHelper = new GitAuthHelper(git)
    await gitAuthHelper.savePersistedAuth()
    core.endGroup()

    // Init the GitHub client
    const githubHelper = new GitHubHelper(inputs.token)

    core.startGroup('Determining the base and head repositories')
    // Determine the base repository from git config
    const remoteUrl = await git.tryGetRemoteUrl()
    const baseRemote = utils.getRemoteDetail(remoteUrl)
    // Determine the head repository; the target for the pull request branch
    const branchRemoteName = inputs.pushToFork ? 'fork' : 'origin'
    const branchRepository = inputs.pushToFork
      ? inputs.pushToFork
      : baseRemote.repository
    if (inputs.pushToFork) {
      // Check if the supplied fork is really a fork of the base
      const parentRepository = await githubHelper.getRepositoryParent(
        branchRepository
      )
      if (parentRepository != baseRemote.repository) {
        throw new Error(
          `Repository '${branchRepository}' is not a fork of '${baseRemote.repository}'. Unable to continue.`
        )
      }
      // Add a remote for the fork
      const remoteUrl = utils.getRemoteUrl(
        baseRemote.protocol,
        branchRepository
      )
      await git.exec(['remote', 'add', 'fork', remoteUrl])
    }
    core.endGroup()
    core.info(
      `Pull request branch target repository set to ${branchRepository}`
    )

    // Configure auth
    if (baseRemote.protocol == 'HTTPS') {
      core.startGroup('Configuring credential for HTTPS authentication')
      await gitAuthHelper.configureToken(inputs.token)
      core.endGroup()
    }

    core.startGroup('Checking the base repository state')
    const [workingBase, workingBaseType] = await getWorkingBaseAndType(git)
    core.info(`Working base is ${workingBaseType} '${workingBase}'`)
    // When in detached HEAD state (checked out on a commit), we need to
    // know the 'base' branch in order to rebase changes.
    if (workingBaseType == WorkingBaseType.Commit && !inputs.base) {
      throw new Error(
        `When the repository is checked out on a commit instead of a branch, the 'base' input must be supplied.`
      )
    }
    // If the base is not specified it is assumed to be the working base.
    const base = inputs.base ? inputs.base : workingBase
    // Throw an error if the base and branch are not different branches
    // of the 'origin' remote. An identically named branch in the `fork`
    // remote is perfectly fine.
    if (branchRemoteName == 'origin' && base == inputs.branch) {
      throw new Error(
        `The 'base' and 'branch' for a pull request must be different branches. Unable to continue.`
      )
    }
    // For self-hosted runners the repository state persists between runs.
    // This command prunes the stale remote ref when the pull request branch was
    // deleted after being merged or closed. Without this the push using
    // '--force-with-lease' fails due to "stale info."
    // https://github.com/peter-evans/create-pull-request/issues/633
    await git.exec(['remote', 'prune', branchRemoteName])
    core.endGroup()

    // Apply the branch suffix if set
    if (inputs.branchSuffix) {
      switch (inputs.branchSuffix) {
        case 'short-commit-hash':
          // Suffix with the short SHA1 hash
          inputs.branch = `${inputs.branch}-${await git.revParse('HEAD', [
            '--short'
          ])}`
          break
        case 'timestamp':
          // Suffix with the current timestamp
          inputs.branch = `${inputs.branch}-${utils.secondsSinceEpoch()}`
          break
        case 'random':
          // Suffix with a 7 character random string
          inputs.branch = `${inputs.branch}-${utils.randomString()}`
          break
        default:
          throw new Error(
            `Branch suffix '${inputs.branchSuffix}' is not a valid value. Unable to continue.`
          )
      }
    }

    // Output head branch
    core.info(
      `Pull request branch to create or update set to '${inputs.branch}'`
    )

    // Configure the committer and author
    core.startGroup('Configuring the committer and author')
    const parsedAuthor = utils.parseDisplayNameEmail(inputs.author)
    const parsedCommitter = utils.parseDisplayNameEmail(inputs.committer)
    git.setIdentityGitOptions([
      '-c',
      `author.name=${parsedAuthor.name}`,
      '-c',
      `author.email=${parsedAuthor.email}`,
      '-c',
      `committer.name=${parsedCommitter.name}`,
      '-c',
      `committer.email=${parsedCommitter.email}`
    ])
    core.info(
      `Configured git committer as '${parsedCommitter.name} <${parsedCommitter.email}>'`
    )
    core.info(
      `Configured git author as '${parsedAuthor.name} <${parsedAuthor.email}>'`
    )
    core.endGroup()

    // Create or update the pull request branch
    core.startGroup('Create or update the pull request branch')
    const result = await createOrUpdateBranch(
      git,
      inputs.commitMessage,
      inputs.base,
      inputs.branch,
      branchRemoteName,
      inputs.signoff,
      inputs.addPaths
    )
    core.endGroup()

    if (['created', 'updated'].includes(result.action)) {
      // The branch was created or updated
      core.startGroup(
        `Pushing pull request branch to '${branchRemoteName}/${inputs.branch}'`
      )
      await git.push([
        '--force-with-lease',
        branchRemoteName,
        `HEAD:refs/heads/${inputs.branch}`
      ])
      core.endGroup()
    }

    // Set the base. It would have been '' if not specified as an input
    inputs.base = result.base

    if (result.hasDiffWithBase) {
      // Create or update the pull request
      core.startGroup('Create or update the pull request')
      const pull = await githubHelper.createOrUpdatePullRequest(
        inputs,
        baseRemote.repository,
        branchRepository
      )
      core.endGroup()

      // Set outputs
      core.startGroup('Setting outputs')
      core.setOutput('pull-request-number', pull.number)
      core.setOutput('pull-request-url', pull.html_url)
      if (pull.created) {
        core.setOutput('pull-request-operation', 'created')
      } else if (result.action == 'updated') {
        core.setOutput('pull-request-operation', 'updated')
      }
      core.setOutput('pull-request-head-sha', result.headSha)
      // Deprecated
      core.exportVariable('PULL_REQUEST_NUMBER', pull.number)
      core.endGroup()
    } else {
      // There is no longer a diff with the base
      // Check we are in a state where a branch exists
      if (['updated', 'not-updated'].includes(result.action)) {
        core.info(
          `Branch '${inputs.branch}' no longer differs from base branch '${inputs.base}'`
        )
        if (inputs.deleteBranch) {
          core.info(`Deleting branch '${inputs.branch}'`)
          await git.push([
            '--delete',
            '--force',
            branchRemoteName,
            `refs/heads/${inputs.branch}`
          ])
          // Set outputs
          core.startGroup('Setting outputs')
          core.setOutput('pull-request-operation', 'closed')
          core.endGroup()
        }
      }
    }
  } catch (error: any) {
    core.setFailed(error.message)
  } finally {
    // Remove auth and restore persisted auth config if it existed
    core.startGroup('Restore persisted git credentials')
    await gitAuthHelper.removeAuth()
    await gitAuthHelper.restorePersistedAuth()
    core.endGroup()
  }
}
 126  
src/git-auth-helper.ts
@@ -0,0 +1,126 @@
import * as core from '@actions/core'
import * as fs from 'fs'
import {GitCommandManager} from './git-command-manager'
import * as path from 'path'
import {URL} from 'url'

export class GitAuthHelper {
  private git: GitCommandManager
  private gitConfigPath: string
  private extraheaderConfigKey: string
  private extraheaderConfigPlaceholderValue = 'AUTHORIZATION: basic ***'
  private extraheaderConfigValueRegex = '^AUTHORIZATION:'
  private persistedExtraheaderConfigValue = ''

  constructor(git: GitCommandManager) {
    this.git = git
    this.gitConfigPath = path.join(
      this.git.getWorkingDirectory(),
      '.git',
      'config'
    )
    const serverUrl = this.getServerUrl()
    this.extraheaderConfigKey = `http.${serverUrl.origin}/.extraheader`
  }

  async savePersistedAuth(): Promise<void> {
    // Save and unset persisted extraheader credential in git config if it exists
    this.persistedExtraheaderConfigValue = await this.getAndUnset()
  }

  async restorePersistedAuth(): Promise<void> {
    if (this.persistedExtraheaderConfigValue) {
      try {
        await this.setExtraheaderConfig(this.persistedExtraheaderConfigValue)
        core.info('Persisted git credentials restored')
      } catch (e: any) {
        core.warning(e)
      }
    }
  }

  async configureToken(token: string): Promise<void> {
    // Encode and configure the basic credential for HTTPS access
    const basicCredential = Buffer.from(
      `x-access-token:${token}`,
      'utf8'
    ).toString('base64')
    core.setSecret(basicCredential)
    const extraheaderConfigValue = `AUTHORIZATION: basic ${basicCredential}`
    await this.setExtraheaderConfig(extraheaderConfigValue)
  }

  async removeAuth(): Promise<void> {
    await this.getAndUnset()
  }

  private async setExtraheaderConfig(
    extraheaderConfigValue: string
  ): Promise<void> {
    // Configure a placeholder value. This approach avoids the credential being captured
    // by process creation audit events, which are commonly logged. For more information,
    // refer to https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/manage/component-updates/command-line-process-auditing
    // See https://github.com/actions/checkout/blob/main/src/git-auth-helper.ts#L267-L274
    await this.git.config(
      this.extraheaderConfigKey,
      this.extraheaderConfigPlaceholderValue
    )
    // Replace the placeholder
    await this.gitConfigStringReplace(
      this.extraheaderConfigPlaceholderValue,
      extraheaderConfigValue
    )
  }

  private async getAndUnset(): Promise<string> {
    let configValue = ''
    // Save and unset persisted extraheader credential in git config if it exists
    if (
      await this.git.configExists(
        this.extraheaderConfigKey,
        this.extraheaderConfigValueRegex
      )
    ) {
      configValue = await this.git.getConfigValue(
        this.extraheaderConfigKey,
        this.extraheaderConfigValueRegex
      )
      if (
        await this.git.tryConfigUnset(
          this.extraheaderConfigKey,
          this.extraheaderConfigValueRegex
        )
      ) {
        core.info(`Unset config key '${this.extraheaderConfigKey}'`)
      } else {
        core.warning(
          `Failed to unset config key '${this.extraheaderConfigKey}'`
        )
      }
    }
    return configValue
  }

  private async gitConfigStringReplace(
    find: string,
    replace: string
  ): Promise<void> {
    let content = (await fs.promises.readFile(this.gitConfigPath)).toString()
    const index = content.indexOf(find)
    if (index < 0 || index != content.lastIndexOf(find)) {
      throw new Error(`Unable to replace '${find}' in ${this.gitConfigPath}`)
    }
    content = content.replace(find, replace)
    await fs.promises.writeFile(this.gitConfigPath, content)
  }

  private getServerUrl(): URL {
    // todo: remove GITHUB_URL after support for GHES Alpha is no longer needed
    // See https://github.com/actions/checkout/blob/main/src/url-helper.ts#L22-L29
    return new URL(
      process.env['GITHUB_SERVER_URL'] ||
        process.env['GITHUB_URL'] ||
        'https://github.com'
    )
  }
}
 303  
src/git-command-manager.ts
@@ -0,0 +1,303 @@
import * as exec from '@actions/exec'
import * as io from '@actions/io'
import * as utils from './utils'
import * as path from 'path'

const tagsRefSpec = '+refs/tags/*:refs/tags/*'

export class GitCommandManager {
  private gitPath: string
  private workingDirectory: string
  // Git options used when commands require an identity
  private identityGitOptions?: string[]

  private constructor(workingDirectory: string, gitPath: string) {
    this.workingDirectory = workingDirectory
    this.gitPath = gitPath
  }

  static async create(workingDirectory: string): Promise<GitCommandManager> {
    const gitPath = await io.which('git', true)
    return new GitCommandManager(workingDirectory, gitPath)
  }

  setIdentityGitOptions(identityGitOptions: string[]): void {
    this.identityGitOptions = identityGitOptions
  }

  async checkout(ref: string, startPoint?: string): Promise<void> {
    const args = ['checkout', '--progress']
    if (startPoint) {
      args.push('-B', ref, startPoint)
    } else {
      args.push(ref)
    }
    // https://github.com/git/git/commit/a047fafc7866cc4087201e284dc1f53e8f9a32d5
    args.push('--')
    await this.exec(args)
  }

  async cherryPick(
    options?: string[],
    allowAllExitCodes = false
  ): Promise<GitOutput> {
    const args = ['cherry-pick']
    if (this.identityGitOptions) {
      args.unshift(...this.identityGitOptions)
    }

    if (options) {
      args.push(...options)
    }

    return await this.exec(args, allowAllExitCodes)
  }

  async commit(
    options?: string[],
    allowAllExitCodes = false
  ): Promise<GitOutput> {
    const args = ['commit']
    if (this.identityGitOptions) {
      args.unshift(...this.identityGitOptions)
    }

    if (options) {
      args.push(...options)
    }

    return await this.exec(args, allowAllExitCodes)
  }

  async config(
    configKey: string,
    configValue: string,
    globalConfig?: boolean
  ): Promise<void> {
    await this.exec([
      'config',
      globalConfig ? '--global' : '--local',
      configKey,
      configValue
    ])
  }

  async configExists(
    configKey: string,
    configValue = '.',
    globalConfig?: boolean
  ): Promise<boolean> {
    const output = await this.exec(
      [
        'config',
        globalConfig ? '--global' : '--local',
        '--name-only',
        '--get-regexp',
        configKey,
        configValue
      ],
      true
    )
    return output.exitCode === 0
  }

  async fetch(
    refSpec: string[],
    remoteName?: string,
    options?: string[]
  ): Promise<void> {
    const args = ['-c', 'protocol.version=2', 'fetch']
    if (!refSpec.some(x => x === tagsRefSpec)) {
      args.push('--no-tags')
    }

    args.push('--progress', '--no-recurse-submodules')
    if (
      utils.fileExistsSync(path.join(this.workingDirectory, '.git', 'shallow'))
    ) {
      args.push('--unshallow')
    }

    if (options) {
      args.push(...options)
    }

    if (remoteName) {
      args.push(remoteName)
    } else {
      args.push('origin')
    }
    for (const arg of refSpec) {
      args.push(arg)
    }

    await this.exec(args)
  }

  async getConfigValue(configKey: string, configValue = '.'): Promise<string> {
    const output = await this.exec([
      'config',
      '--local',
      '--get-regexp',
      configKey,
      configValue
    ])
    return output.stdout.trim().split(`${configKey} `)[1]
  }

  getWorkingDirectory(): string {
    return this.workingDirectory
  }

  async hasDiff(options?: string[]): Promise<boolean> {
    const args = ['diff', '--quiet']
    if (options) {
      args.push(...options)
    }
    const output = await this.exec(args, true)
    return output.exitCode === 1
  }

  async isDirty(untracked: boolean, pathspec?: string[]): Promise<boolean> {
    const pathspecArgs = pathspec ? ['--', ...pathspec] : []
    // Check untracked changes
    const sargs = ['--porcelain', '-unormal']
    sargs.push(...pathspecArgs)
    if (untracked && (await this.status(sargs))) {
      return true
    }
    // Check working index changes
    if (await this.hasDiff(pathspecArgs)) {
      return true
    }
    // Check staged changes
    const dargs = ['--staged']
    dargs.push(...pathspecArgs)
    if (await this.hasDiff(dargs)) {
      return true
    }
    return false
  }

  async push(options?: string[]): Promise<void> {
    const args = ['push']
    if (options) {
      args.push(...options)
    }
    await this.exec(args)
  }

  async revList(
    commitExpression: string[],
    options?: string[]
  ): Promise<string> {
    const args = ['rev-list']
    if (options) {
      args.push(...options)
    }
    args.push(...commitExpression)
    const output = await this.exec(args)
    return output.stdout.trim()
  }

  async revParse(ref: string, options?: string[]): Promise<string> {
    const args = ['rev-parse']
    if (options) {
      args.push(...options)
    }
    args.push(ref)
    const output = await this.exec(args)
    return output.stdout.trim()
  }

  async status(options?: string[]): Promise<string> {
    const args = ['status']
    if (options) {
      args.push(...options)
    }
    const output = await this.exec(args)
    return output.stdout.trim()
  }

  async symbolicRef(ref: string, options?: string[]): Promise<string> {
    const args = ['symbolic-ref', ref]
    if (options) {
      args.push(...options)
    }
    const output = await this.exec(args)
    return output.stdout.trim()
  }

  async tryConfigUnset(
    configKey: string,
    configValue = '.',
    globalConfig?: boolean
  ): Promise<boolean> {
    const output = await this.exec(
      [
        'config',
        globalConfig ? '--global' : '--local',
        '--unset',
        configKey,
        configValue
      ],
      true
    )
    return output.exitCode === 0
  }

  async tryGetRemoteUrl(): Promise<string> {
    const output = await this.exec(
      ['config', '--local', '--get', 'remote.origin.url'],
      true
    )

    if (output.exitCode !== 0) {
      return ''
    }

    const stdout = output.stdout.trim()
    if (stdout.includes('\n')) {
      return ''
    }

    return stdout
  }

  async exec(args: string[], allowAllExitCodes = false): Promise<GitOutput> {
    const result = new GitOutput()

    const env = {}
    for (const key of Object.keys(process.env)) {
      env[key] = process.env[key]
    }

    const stdout: string[] = []
    const stderr: string[] = []

    const options = {
      cwd: this.workingDirectory,
      env,
      ignoreReturnCode: allowAllExitCodes,
      listeners: {
        stdout: (data: Buffer) => {
          stdout.push(data.toString())
        },
        stderr: (data: Buffer) => {
          stderr.push(data.toString())
        }
      }
    }

    result.exitCode = await exec.exec(`"${this.gitPath}"`, args, options)
    result.stdout = stdout.join('')
    result.stderr = stderr.join('')
    return result
  }
}

class GitOutput {
  stdout = ''
  stderr = ''
  exitCode = 0
}
 183  
src/github-helper.ts
@@ -0,0 +1,183 @@
import * as core from '@actions/core'
import {Inputs} from './create-pull-request'
import {Octokit, OctokitOptions} from './octokit-client'

const ERROR_PR_REVIEW_FROM_AUTHOR =
  'Review cannot be requested from pull request author'

interface Repository {
  owner: string
  repo: string
}

interface Pull {
  number: number
  html_url: string
  created: boolean
}

export class GitHubHelper {
  private octokit: InstanceType<typeof Octokit>

  constructor(token: string) {
    const options: OctokitOptions = {}
    if (token) {
      options.auth = `${token}`
    }
    options.baseUrl = process.env['GITHUB_API_URL'] || 'https://api.github.com'
    this.octokit = new Octokit(options)
  }

  private parseRepository(repository: string): Repository {
    const [owner, repo] = repository.split('/')
    return {
      owner: owner,
      repo: repo
    }
  }

  private async createOrUpdate(
    inputs: Inputs,
    baseRepository: string,
    headRepository: string
  ): Promise<Pull> {
    const [headOwner] = headRepository.split('/')
    const headBranch = `${headOwner}:${inputs.branch}`
    const headBranchFull = `${headRepository}:${inputs.branch}`

    // Try to create the pull request
    try {
      core.info(`Attempting creation of pull request`)
      const {data: pull} = await this.octokit.rest.pulls.create({
        ...this.parseRepository(baseRepository),
        title: inputs.title,
        head: headBranch,
        base: inputs.base,
        body: inputs.body,
        draft: inputs.draft
      })
      core.info(
        `Created pull request #${pull.number} (${headBranch} => ${inputs.base})`
      )
      return {
        number: pull.number,
        html_url: pull.html_url,
        created: true
      }
    } catch (e: any) {
      if (
        e.message &&
        e.message.includes(`A pull request already exists for`)
      ) {
        core.info(`A pull request already exists for ${headBranch}`)
      } else {
        throw e
      }
    }

    // Update the pull request that exists for this branch and base
    core.info(`Fetching existing pull request`)
    const {data: pulls} = await this.octokit.rest.pulls.list({
      ...this.parseRepository(baseRepository),
      state: 'open',
      head: headBranchFull,
      base: inputs.base
    })
    core.info(`Attempting update of pull request`)
    const {data: pull} = await this.octokit.rest.pulls.update({
      ...this.parseRepository(baseRepository),
      pull_number: pulls[0].number,
      title: inputs.title,
      body: inputs.body
    })
    core.info(
      `Updated pull request #${pull.number} (${headBranch} => ${inputs.base})`
    )
    return {
      number: pull.number,
      html_url: pull.html_url,
      created: false
    }
  }

  async getRepositoryParent(headRepository: string): Promise<string> {
    const {data: headRepo} = await this.octokit.rest.repos.get({
      ...this.parseRepository(headRepository)
    })
    if (!headRepo.parent) {
      throw new Error(
        `Repository '${headRepository}' is not a fork. Unable to continue.`
      )
    }
    return headRepo.parent.full_name
  }

  async createOrUpdatePullRequest(
    inputs: Inputs,
    baseRepository: string,
    headRepository: string
  ): Promise<Pull> {
    // Create or update the pull request
    const pull = await this.createOrUpdate(
      inputs,
      baseRepository,
      headRepository
    )

    // Apply milestone
    if (inputs.milestone) {
      core.info(`Applying milestone '${inputs.milestone}'`)
      await this.octokit.rest.issues.update({
        ...this.parseRepository(baseRepository),
        issue_number: pull.number,
        milestone: inputs.milestone
      })
    }
    // Apply labels
    if (inputs.labels.length > 0) {
      core.info(`Applying labels '${inputs.labels}'`)
      await this.octokit.rest.issues.addLabels({
        ...this.parseRepository(baseRepository),
        issue_number: pull.number,
        labels: inputs.labels
      })
    }
    // Apply assignees
    if (inputs.assignees.length > 0) {
      core.info(`Applying assignees '${inputs.assignees}'`)
      await this.octokit.rest.issues.addAssignees({
        ...this.parseRepository(baseRepository),
        issue_number: pull.number,
        assignees: inputs.assignees
      })
    }

    // Request reviewers and team reviewers
    const requestReviewersParams = {}
    if (inputs.reviewers.length > 0) {
      requestReviewersParams['reviewers'] = inputs.reviewers
      core.info(`Requesting reviewers '${inputs.reviewers}'`)
    }
    if (inputs.teamReviewers.length > 0) {
      requestReviewersParams['team_reviewers'] = inputs.teamReviewers
      core.info(`Requesting team reviewers '${inputs.teamReviewers}'`)
    }
    if (Object.keys(requestReviewersParams).length > 0) {
      try {
        await this.octokit.rest.pulls.requestReviewers({
          ...this.parseRepository(baseRepository),
          pull_number: pull.number,
          ...requestReviewersParams
        })
      } catch (e: any) {
        if (e.message && e.message.includes(ERROR_PR_REVIEW_FROM_AUTHOR)) {
          core.warning(ERROR_PR_REVIEW_FROM_AUTHOR)
        } else {
          throw e
        }
      }
    }

    return pull
  }
}
 38  
src/main.ts
@@ -0,0 +1,38 @@
import * as core from '@actions/core'
import {Inputs, createPullRequest} from './create-pull-request'
import {inspect} from 'util'
import * as utils from './utils'

async function run(): Promise<void> {
  try {
    const inputs: Inputs = {
      token: core.getInput('token'),
      path: core.getInput('path'),
      addPaths: utils.getInputAsArray('add-paths'),
      commitMessage: core.getInput('commit-message'),
      committer: core.getInput('committer'),
      author: core.getInput('author'),
      signoff: core.getBooleanInput('signoff'),
      branch: core.getInput('branch'),
      deleteBranch: core.getBooleanInput('delete-branch'),
      branchSuffix: core.getInput('branch-suffix'),
      base: core.getInput('base'),
      pushToFork: core.getInput('push-to-fork'),
      title: core.getInput('title'),
      body: core.getInput('body'),
      labels: utils.getInputAsArray('labels'),
      assignees: utils.getInputAsArray('assignees'),
      reviewers: utils.getInputAsArray('reviewers'),
      teamReviewers: utils.getInputAsArray('team-reviewers'),
      milestone: Number(core.getInput('milestone')),
      draft: core.getBooleanInput('draft')
    }
    core.debug(`Inputs: ${inspect(inputs)}`)

    await createPullRequest(inputs)
  } catch (error: any) {
    core.setFailed(error.message)
  }
}

run()
 33  
src/octokit-client.ts
@@ -0,0 +1,33 @@
import {Octokit as Core} from '@octokit/core'
import {paginateRest} from '@octokit/plugin-paginate-rest'
import {restEndpointMethods} from '@octokit/plugin-rest-endpoint-methods'
import {HttpsProxyAgent} from 'https-proxy-agent'
export {RestEndpointMethodTypes} from '@octokit/plugin-rest-endpoint-methods'
export {OctokitOptions} from '@octokit/core/dist-types/types'

export const Octokit = Core.plugin(
  paginateRest,
  restEndpointMethods,
  autoProxyAgent
)

// Octokit plugin to support the https_proxy and no_proxy environment variable
function autoProxyAgent(octokit: Core) {
  const proxy = process.env.https_proxy || process.env.HTTPS_PROXY

  const noProxy = process.env.no_proxy || process.env.NO_PROXY
  let noProxyArray: string[] = []
  if (noProxy) {
    noProxyArray = noProxy.split(',')
  }

  if (!proxy) return

  const agent = new HttpsProxyAgent(proxy)
  octokit.hook.before('request', options => {
    if (noProxyArray.includes(options.request.hostname)) {
      return
    }
    options.request.agent = agent
  })
}
 152  
src/utils.ts
@@ -0,0 +1,152 @@
import * as core from '@actions/core'
import * as fs from 'fs'
import * as path from 'path'

export function getInputAsArray(
  name: string,
  options?: core.InputOptions
): string[] {
  return getStringAsArray(core.getInput(name, options))
}

export function getStringAsArray(str: string): string[] {
  return str
    .split(/[\n,]+/)
    .map(s => s.trim())
    .filter(x => x !== '')
}

export function getRepoPath(relativePath?: string): string {
  let githubWorkspacePath = process.env['GITHUB_WORKSPACE']
  if (!githubWorkspacePath) {
    throw new Error('GITHUB_WORKSPACE not defined')
  }
  githubWorkspacePath = path.resolve(githubWorkspacePath)
  core.debug(`githubWorkspacePath: ${githubWorkspacePath}`)

  let repoPath = githubWorkspacePath
  if (relativePath) repoPath = path.resolve(repoPath, relativePath)

  core.debug(`repoPath: ${repoPath}`)
  return repoPath
}

interface RemoteDetail {
  protocol: string
  repository: string
}

export function getRemoteDetail(remoteUrl: string): RemoteDetail {
  // Parse the protocol and github repository from a URL
  // e.g. HTTPS, peter-evans/create-pull-request
  const githubUrl = process.env['GITHUB_SERVER_URL'] || 'https://github.com'

  const githubServerMatch = githubUrl.match(/^https?:\/\/(.+)$/i)
  if (!githubServerMatch) {
    throw new Error('Could not parse GitHub Server name')
  }

  const httpsUrlPattern = new RegExp(
    '^https?://.*@?' + githubServerMatch[1] + '/(.+/.+?)(.git)?$',
    'i'
  )
  const sshUrlPattern = new RegExp(
    '^git@' + githubServerMatch[1] + ':(.+/.+).git$',
    'i'
  )

  const httpsMatch = remoteUrl.match(httpsUrlPattern)
  if (httpsMatch) {
    return {
      protocol: 'HTTPS',
      repository: httpsMatch[1]
    }
  }

  const sshMatch = remoteUrl.match(sshUrlPattern)
  if (sshMatch) {
    return {
      protocol: 'SSH',
      repository: sshMatch[1]
    }
  }

  throw new Error(
    `The format of '${remoteUrl}' is not a valid GitHub repository URL`
  )
}

export function getRemoteUrl(protocol: string, repository: string): string {
  return protocol == 'HTTPS'
    ? `https://github.com/${repository}`
    : `git@github.com:${repository}.git`
}

export function secondsSinceEpoch(): number {
  const now = new Date()
  return Math.round(now.getTime() / 1000)
}

export function randomString(): string {
  return Math.random().toString(36).substr(2, 7)
}

interface DisplayNameEmail {
  name: string
  email: string
}

export function parseDisplayNameEmail(
  displayNameEmail: string
): DisplayNameEmail {
  // Parse the name and email address from a string in the following format
  // Display Name <email@address.com>
  const pattern = /^([^<]+)\s*<([^>]+)>$/i

  // Check we have a match
  const match = displayNameEmail.match(pattern)
  if (!match) {
    throw new Error(
      `The format of '${displayNameEmail}' is not a valid email address with display name`
    )
  }

  // Check that name and email are not just whitespace
  const name = match[1].trim()
  const email = match[2].trim()
  if (!name || !email) {
    throw new Error(
      `The format of '${displayNameEmail}' is not a valid email address with display name`
    )
  }

  return {
    name: name,
    email: email
  }
}

export function fileExistsSync(path: string): boolean {
  if (!path) {
    throw new Error("Arg 'path' must not be empty")
  }

  let stats: fs.Stats
  try {
    stats = fs.statSync(path)
  } catch (error: any) {
    if (error.code === 'ENOENT') {
      return false
    }

    throw new Error(
      `Encountered an error when checking whether path '${path}' exists: ${error.message}`
    )
  }

  if (!stats.isDirectory()) {
    return true
  }

  return false
}
 16  
tsconfig.json
@@ -0,0 +1,16 @@
{
  "compilerOptions": {
    "target": "es6",
    "module": "commonjs",
    "lib": [
      "es6"
    ],
    "outDir": "./lib",
    "rootDir": "./src",
    "declaration": true,
    "strict": true,
    "noImplicitAny": false,
    "esModuleInterop": true
  },
  "exclude": ["NODEMON-and-.gitignore", ".lib", "node_modules"]
}

'"'('"((c)(r))"')©)[2001-09-17]((c)(r))[Trademark](CopyRight)[Mozilla2.0](Apache4.0)[LICENSE](2003-01-19) GitHub, Inc. :
navigate :discussion :To :Help-Wanted'!"' : :
Terms :
Privacy :
Security :
Status :
dockerfile/RAKEFILE.U.I :
Contact :SEC :
Price :
API :
Train :
Blog :
About :
Based on facts as set forth in.															Based on facts as set forth in.			6551							6550The U.S. Internal Revenue Code of 1986, as amended, the Treasury Regulations promulgated thereunder, published pronouncements of the Internal Revenue Service, which may be cited or used as precedents, and case law, any of which may be changed at any time with retroactive effect. No opinion is expressed on any matters other than those specifically referred to above.															The U.S. Internal Revenue Code of 1986, as amended, the Treasury Regulations promulgated thereunder, published pronouncements of the Internal Revenue Service, which may be cited or used as precedents, and case law, any of which may be changed at any time with retroactive effect. No opinion is expressed on any matters other than those specifically referred to above.										
EMPLOYER IDENTIFICATION NUMBER: 61-1767919															EMPLOYER IDENTIFICATION NUMBER: 61-1767920										

[DRAFT FORM OF TAX OPINION]															[DRAFT FORM OF TAX OPINION]										

											1														
															ALPHABET																									ZACHRY T WOOD																									5324 BRADFORD DR																									DALLAS TX 75235-8315										ORIGINAL REPORT															ORIGINAL REPORT										Income, Rents, & Royalty															Income, Rents, & Royalty										INCOME STATEMENT 	61-1767919														INCOME STATEMENT 	61-1767920										88-1303491															88-1303492									GOOGL_income-statement_Quarterly_As_Originally_Reported	TTM	Q4 2021	Q2 2021	Q1 2021	Q4 2020	Q3 2020	Q2 2020	Q1 2020	Q4 2019	Q3 2019					GOOGL_income-statement_Quarterly_As_Originally_Reported	TTM	Q4 2022	Q3 2022	Q2 2022	Q1 2022	Q4 2021	Q3 2021		Q2 2021	Q3 2021
Gross Profit	$146,698,000,000.00	$42,337,000,000.00	$35,653,000,000.00	$31,211,000,000.00	30818000000	$25,056,000,000.00	1974400000000.0%	22177000000	25055000000	22931000000					Gross Profit	-2178236364	-9195472727	-16212709091	-23229945455	-30247181818	-37264418182	-44281654545		-51298890909	37497000000Total Revenue as Reported, Supplemental	$257,637,000,000.00	$75,325,000,000.00	$61,880,000,000.00	$55,314,000,000.00	56898000000	$46,173,000,000.00	3829700000000.0%	41159000000	46075000000	40499000000					Total Revenue as Reported, Supplemental	-1286309091	-13385163636	-25484018182	-37582872727	-49681727273	-61780581818	-73879436364		-85978290909	65118000000	$257,637,000,000.00	$75,325,000,000.00	$61,880,000,000.00	$55,314,000,000.00	56898000000	$46,173,000,000.00	3829700000000.0%	41159000000	64133000000	34071000000						1957800000	-9776581818	-21510963636	-33245345455	-44979727273	-56714109091	-68448490909		-80182872727	65118000000Other Revenue										6428000000					Other Revenue										Cost of Revenue	-110939000000	-32988000000	-26227000000	-$24,103,000,000.00	-26080000000	-$21,117,000,000.00	-1855300000000.0%	-18982000000	-21020000000	-17568000000					Cost of Revenue	-891927272.7	4189690909	9271309091	14352927273	19434545455	24516163636	29597781818		34679400000	-27621000000Cost of Goods and Services	-110939000000	-32988000000	-26227000000	-24103000000	-26080000000	-21117000000	-18553000000	-18982000000	-21020000000	-17568000000					Cost of Goods and Services	-891927272.7	4189690909	9271309091	14352927273	19434545455	24516163636	29597781818		34679400000	-27621000000Operating Income/Expenses	-67984000000	-20452000000	-16292000000	-$14,774,000,000.00	-$15,167,000,000.00	-1384300000000.0%	-$13,361,000,000.00	-14200000000	-15789000000	-13754000000					Operating Income/Expenses	-3640563636	-882445454.5	1875672727	4633790909	7391909091	10150027273	12908145455		15666263636	-16466000000Selling, General and Administrative Expenses	-36422000000	-11744000000	-8617000000	-7289000000	-8145000000	-6987000000	-6486000000	-7380000000	-8567000000	-7200000000					Selling, General and Administrative Expenses	-1552200000	-28945454.55	1494309091	3017563636	4540818182	6064072727	7587327273		9110581818	-8772000000General and Administrative Expenses	-13510000000	-4140000000	-3341000000	-2773000000	-2831000000	-2756000000	-2585000000	-2880000000	-2829000000	-2591000000					General and Administrative Expenses	-544945454.5	23200000	591345454.5	1159490909	1727636364	2295781818	2863927273		3432072727	-3256000000Selling and Marketing Expenses	-22912000000	-7604000000	-5276000000	-4516000000	-5314000000	-4231000000	-3901000000	-4500000000	-5738000000	-4609000000					Selling and Marketing Expenses	-1007254545	-52145454.55	902963636.4	1858072727	2813181818	3768290909	4723400000		5678509091	-5516000000Research and Development Expenses	-31562000000	-8708000000	-7675000000	-7485000000	-7022000000	-6856000000	-6875000000	-6820000000	-7222000000	-6554000000					Research and Development Expenses	-2088363636	-853500000	381363636.4	1616227273	2851090909	4085954545	5320818182		6555681818	-7694000000Total Operating Profit/Loss	78714000000	21885000000	19361000000	16437000000	15651000000	11213000000	6383000000	7977000000	9266000000	9177000000					Total Operating Profit/Loss	-5818800000	-10077918182	-14337036364	-18596154545	-22855272727	-27114390909	-31373509091		-35632627273	21031000000Non-Operating Income/Expenses, Total	12020000000	2517000000	2624000000	4846000000	3038000000	2146000000	1894000000	-220000000	1438000000	-549000000					Non-Operating Income/Expenses, Total	-1369181818	-2079000000	-2788818182	-3498636364	-4208454545	-4918272727	-5628090909		-6337909091	2033000000Total Net Finance Income/Expense	1153000000	261000000	313000000	269000000	333000000	412000000	420000000	565000000	604000000	608000000					Total Net Finance Income/Expense	464490909.1	462390909.1	460290909.1	458190909.1	456090909.1	453990909.1	451890909.1		449790909.1	310000000Net Interest Income/Expense	1153000000	261000000	313000000	269000000	333000000	412000000	420000000	565000000	604000000	608000000					Net Interest Income/Expense	464490909.1	462390909.1	460290909.1	458190909.1	456090909.1	453990909.1	451890909.1		449790909.1	310000000
Interest Expense Net of Capitalized Interest	-346000000	-117000000	-76000000	-76000000	-53000000	-48000000	-13000000	-21000000	-17000000	-23000000					Interest Expense Net of Capitalized Interest	48654545.45	69900000	91145454.55	112390909.1	133636363.6	154881818.2	176127272.7		197372727.3	-77000000Interest Income	1499000000	378000000	389000000	345000000	386000000	460000000	433000000	586000000	621000000	631000000					Interest Income	415836363.6	392490909.1	369145454.5	345800000	322454545.5	299109090.9	275763636.4		252418181.8	387000000Net Investment Income	12364000000	2364000000	2924000000	4869000000	3530000000	1957000000	1696000000	-809000000	899000000	-1452000000					Net Investment Income	-2096781818	-2909109091	-3721436364	-4533763636	-5346090909	-6158418182	-6970745455		-7783072727	2207000000Gain/Loss on Investments and Other Financial Instruments	12270000000	2478000000	2883000000	4751000000	3262000000	2015000000	1842000000	-802000000	399000000	-1479000000					Gain/Loss on Investments and Other Financial Instruments	-2243490909	-3068572727	-3893654545	-4718736364	-5543818182	-6368900000	-7193981818		-8019063636	2158000000Income from Associates, Joint Ventures and Other Participating Interests	334000000	49000000	92000000	5000000	355000000	26000000	-54000000	74000000	460000000	-14000000					Income from Associates, Joint Ventures and Other Participating Interests	99054545.45	92609090.91	86163636.36	79718181.82	73272727.27	66827272.73	60381818.18		53936363.64	188000000Gain/Loss on Foreign Exchange	-240000000	-163000000	-51000000	113000000	-87000000	-84000000	-92000000	-81000000	40000000	41000000					Gain/Loss on Foreign Exchange	47654545.45	66854545.45	86054545.45	105254545.5	124454545.5	143654545.5	162854545.5		182054545.5	-139000000Irregular Income/Expenses	0	0			0	0	0	0	0	0					Irregular Income/Expenses	0	0				0	0		0	Other Irregular Income/Expenses	0	0			0	0	0	0	0	0					Other Irregular Income/Expenses	0	0				0	0		0	Other Income/Expense, Non-Operating	-1497000000	-108000000	-613000000	-292000000	-825000000	-223000000	-222000000	24000000	-65000000	295000000					Other Income/Expense, Non-Operating	263109090.9	367718181.8	472327272.7	576936363.6	681545454.5	786154545.5	890763636.4		995372727.3	-484000000Pretax Income	90734000000	24402000000	21985000000	21283000000	18689000000	13359000000	8277000000	7757000000	10704000000	8628000000					Pretax Income	-7187981818	-12156918182	-17125854545	-22094790909	-27063727273	-32032663636	-37001600000		-41970536364	23064000000Provision for Income Tax	-14701000000	-3760000000	-3460000000	-3353000000	-3462000000	-2112000000	-1318000000	-921000000	-33000000	-1560000000					Provision for Income Tax	1695218182	2565754545	3436290909	4306827273	5177363636	6047900000	6918436364		7788972727	-4128000000Net Income from Continuing Operations	76033000000	20642000000	18525000000	17930000000	15227000000	11247000000	6959000000	6836000000	10671000000	7068000000					Net Income from Continuing Operations	-5492763636	-9591163636	-13689563636	-17787963636	-21886363636	-25984763636	-30083163636		-34181563636	18936000000Net Income after Extraordinary Items and Discontinued Operations	76033000000	20642000000	18525000000	17930000000	15227000000	11247000000	6959000000	6836000000	10671000000	7068000000					Net Income after Extraordinary Items and Discontinued Operations	-5492763636	-9591163636	-13689563636	-17787963636	-21886363636	-25984763636	-30083163636		-34181563636	18936000000Net Income after Non-Controlling/Minority Interests	76033000000	20642000000	18525000000	17930000000	15227000000	11247000000	6959000000	6836000000	10671000000	7068000000					Net Income after Non-Controlling/Minority Interests	-5492763636	-9591163636	-13689563636	-17787963636	-21886363636	-25984763636	-30083163636		-34181563636	18936000000Net Income Available to Common Stockholders	76033000000	20642000000	18525000000	17930000000	15227000000	11247000000	6959000000	6836000000	10671000000	7068000000					Net Income Available to Common Stockholders	-5492763636	-9591163636	-13689563636	-17787963636	-21886363636	-25984763636	-30083163636		-34181563636	18936000000Diluted Net Income Available to Common Stockholders	76033000000	20642000000	18525000000	17930000000	15227000000	11247000000	6959000000	6836000000	10671000000	7068000000					Diluted Net Income Available to Common Stockholders	-5492763636	-9591163636	-13689563636	-17787963636	-21886363636	-25984763636	-30083163636		-34181563636	18936000000Income Statement Supplemental Section															Income Statement Supplemental Section										Reported Normalized and Operating Income/Expense Supplemental Section															Reported Normalized and Operating Income/Expense Supplemental Section										Total Revenue as Reported, Supplemental	257637000000	75325000000	61880000000	55314000000	56898000000	46173000000	38297000000	41159000000	46075000000	40499000000					Total Revenue as Reported, Supplemental	-1286309091	-13385163636	-25484018182	-37582872727	-49681727273	-61780581818	-73879436364		-85978290909	65118000000Total Operating Profit/Loss as Reported, Supplemental	78714000000	21885000000	19361000000	16437000000	15651000000	11213000000	6383000000	7977000000	9266000000	9177000000					Total Operating Profit/Loss as Reported, Supplemental	-5818800000	-10077918182	-14337036364	-18596154545	-22855272727	-27114390909	-31373509091		-35632627273	21031000000Reported Effective Tax Rate	0.162		0.157	0.158		0.158	0.159	0.119		0.181					Reported Effective Tax Rate	1.162		0.1436666667	0.1331666667	0.1226666667		0.1063333333		0.08683333333	0.179Reported Normalized Income								6836000000							Reported Normalized Income										Reported Normalized Operating Profit								7977000000							Reported Normalized Operating Profit										Other Adjustments to Net Income Available to Common Stockholders															Other Adjustments to Net Income Available to Common Stockholders										Discontinued Operations															Discontinued Operations										Basic EPS	113.88	31.15	27.69	26.63	22.54	16.55	10.21	9.96	15.49	10.2					Basic EPS	-8.742909091	-14.93854545	-21.13418182	-27.32981818	-33.52545455	-39.72109091	-45.91672727		-52.11236364	28.44Basic EPS from Continuing Operations	113.88	31.12	27.69	26.63	22.46	16.55	10.21	9.96	15.47	10.2					Basic EPS from Continuing Operations	-8.752545455	-14.94781818	-21.14309091	-27.33836364	-33.53363636	-39.72890909	-45.92418182		-52.11945455	28.44Basic EPS from Discontinued Operations															Basic EPS from Discontinued Operations										Diluted EPS	112.2	30.69	27.26	26.29	22.3	16.4	10.13	9.87	15.35	10.12					Diluted EPS	-8.505636364	-14.599	-20.69236364	-26.78572727	-32.87909091	-38.97245455	-45.06581818		-51.15918182	27.99Diluted EPS from Continuing Operations	112.2	30.67	27.26	26.29	22.23	16.4	10.13	9.87	15.33	10.12					Diluted EPS from Continuing Operations	-8.515636364	-14.609	-20.70236364	-26.79572727	-32.88909091	-38.98245455	-45.07581818		-51.16918182	27.99Diluted EPS from Discontinued Operations															Diluted EPS from Discontinued Operations										Basic Weighted Average Shares Outstanding	667650000	662664000	668958000	673220000	675581000	679449000	681768000	686465000	688804000	692741000					Basic Weighted Average Shares Outstanding	694313545.5	697258863.6	700204181.8	703149500	706094818.2	709040136.4	711985454.5		714930772.7	665758000Diluted Weighted Average Shares Outstanding	677674000	672493000	679612000	682071000	682969000	685851000	687024000	692267000	695193000	698199000					Diluted Weighted Average Shares Outstanding	698675981.8	701033009.1	703390036.4	705747063.6	708104090.9	710461118.2	712818145.5		715175172.7	676519000Reported Normalized Diluted EPS								9.87							Reported Normalized Diluted EPS										Basic EPS	113.88	31.15	27.69	26.63	22.54	16.55	10.21	9.96	15.49	10.2					Basic EPS	-8.742909091	-14.93854545	-21.13418182	-27.32981818	-33.52545455	-39.72109091	-45.91672727		-52.11236364	28.44Diluted EPS	112.2	30.69	27.26	26.29	22.3	16.4	10.13	9.87	15.35	10.12					Diluted EPS	-8.505636364	-14.599	-20.69236364	-26.78572727	-32.87909091	-38.97245455	-45.06581818		-51.15918182	27.99Basic WASO	667650000	662664000	668958000	673220000	675581000	679449000	681768000	686465000	688804000	692741000					Basic WASO	694313545.5	697258863.6	700204181.8	703149500	706094818.2	709040136.4	711985454.5		714930772.7	665758000Diluted WASO	677674000	672493000	679612000	682071000	682969000	685851000	687024000	692267000	695193000	698199000					Diluted WASO	698675981.8	701033009.1	703390036.4	705747063.6	708104090.9	710461118.2	712818145.5		715175172.7	676519000Fiscal year end September 28th., 2022. | USD															Fiscal year end September 28th., 2022. | USD										
31622,6:39 PM															31622,6:39 PM										Morningstar.com Intraday Fundamental Portfolio View Print Report							Print								Morningstar.com Intraday Fundamental Portfolio View Print Report									Print	
3/6/2022 at 6:37 PM										Current Value					3/6/2022 at 6:37 PM																				15335150186014															
GOOGL_income-statement_Quarterly_As_Originally_Reported		Q4 2021													GOOGL_income-statement_Quarterly_As_Originally_Reported		Q4 2022								Cash Flow from Operating Activities, Indirect		24934000000	Q2 2021	Q1 2021	Q4 2020										Cash Flow from Operating Activities, Indirect		24934000001	Q3 2022	Q2 2022	Q1 2022	Q4 2021				Q3 2021Net Cash Flow from Continuing Operating Activities, Indirect		24934000000	37497000000	31211000000	30818000000										Net Cash Flow from Continuing Operating Activities, Indirect		35231800000	36975800000	38719800000	40463800000	42207800000				25539000000Cash Generated from Operating Activities		24934000000	21890000000	19289000000	22677000000										Cash Generated from Operating Activities		19636600000	18560200000	17483800000	16407400000	15331000000				25539000000Income/Loss before Non-Cash Adjustment		20642000000	21890000000	19289000000	22677000000										Income/Loss before Non-Cash Adjustment		21353400000	21135400000	20917400000	20699400000	20481400000				25539000000Total Adjustments for Non-Cash Items		6517000000	18525000000	17930000000	15227000000										Total Adjustments for Non-Cash Items		20351200000	21992600000	23634000000	25275400000	26916800000				18936000000Depreciation, Amortization and Depletion, Non-Cash Adjustment		3439000000	4236000000	2592000000	5748000000										Depreciation, Amortization and Depletion, Non-Cash Adjustment		4986300000	5327600000	5668900000	6010200000	6351500000				3797000000Depreciation and Amortization, Non-Cash Adjustment		3439000000	2945000000	2753000000	3725000000										Depreciation and Amortization, Non-Cash Adjustment		3239500000	3241600000	3243700000	3245800000	3247900000				3304000000Depreciation, Non-Cash Adjustment		3215000000	2945000000	2753000000	3725000000										Depreciation, Non-Cash Adjustment		3329100000	3376000000	3422900000	3469800000	3516700000				3304000000Amortization, Non-Cash Adjustment		224000000	2730000000	2525000000	3539000000										Amortization, Non-Cash Adjustment		4241600000	4848600000	5455600000	6062600000	6669600000				3085000000Stock-Based Compensation, Non-Cash Adjustment		3954000000	215000000	228000000	186000000										Stock-Based Compensation, Non-Cash Adjustment		-1297700000	-2050400000	-2803100000	-3555800000	-4308500000				219000000Taxes, Non-Cash Adjustment		1616000000	3803000000	3745000000	3223000000										Taxes, Non-Cash Adjustment		4177700000	4486200000	4794700000	5103200000	5411700000				3874000000Investment Income/Loss, Non-Cash Adjustment		-2478000000	379000000	1100000000	1670000000										Investment Income/Loss, Non-Cash Adjustment		3081700000	4150000000	5218300000	6286600000	7354900000				-1287000000Gain/Loss on Financial Instruments, Non-Cash Adjustment		-2478000000	-2883000000	-4751000000	-3262000000										Gain/Loss on Financial Instruments, Non-Cash Adjustment		-4354700000	-4770800000	-5186900000	-5603000000	-6019100000				-2158000000Other Non-Cash Items		-14000000	-2883000000	-4751000000	-3262000000										Other Non-Cash Items		-5340300000	-6249200000	-7158100000	-8067000000	-8975900000				-2158000000Changes in Operating Capital		-2225000000	-8000000	-255000000	392000000										Changes in Operating Capital		1068100000	1559600000	2051100000	2542600000	3034100000				64000000Change in Trade and Other Receivables		-5819000000	-871000000	-1233000000	1702000000										Change in Trade and Other Receivables		2617900000	3718200000	4818500000	5918800000	7019100000				2806000000Change in Trade/Accounts Receivable		-5819000000	-3661000000	2794000000	-5445000000										Change in Trade/Accounts Receivable		-1122700000	-527600000	67500000	662600000	1257700000				-2409000000Change in Other Current Assets		-399000000	-3661000000	2794000000	-5445000000										Change in Other Current Assets		-3290700000	-3779600000	-4268500000	-4757400000	-5246300000				-2409000000Change in Payables and Accrued Expenses		6994000000	-199000000	7000000	-738000000										Change in Payables and Accrued Expenses		-3298800000	-4719000000	-6139200000	-7559400000	-8979600000				-1255000000Change in Trade and Other Payables		1157000000	4074000000	-4956000000	6938000000										Change in Trade and Other Payables		3108700000	3453600000	3798500000	4143400000	4488300000				3157000000Change in Trade/Accounts Payable		1157000000	-130000000	-982000000	963000000										Change in Trade/Accounts Payable		-233200000	-394000000	-554800000	-715600000	-876400000				238000000Change in Accrued Expenses		5837000000	-130000000	-982000000	963000000										Change in Accrued Expenses		-2105200000	-3202000000	-4298800000	-5395600000	-6492400000				238000000Change in Deferred Assets/Liabilities		368000000	4204000000	-3974000000	5975000000										Change in Deferred Assets/Liabilities		3194700000	3626800000	4058900000	4491000000	4923100000				2919000000Change in Other Operating Capital		-3369000000	-3000000	137000000	207000000										Change in Other Operating Capital		1553900000	2255600000	2957300000	3659000000	4360700000				272000000Change in Prepayments and Deposits			-1082000000	785000000	740000000										Change in Prepayments and Deposits			-388000000	-891600000	-1395200000	-1898800000				3041000000Cash Flow from Investing Activities		-11016000000													Cash Flow from Investing Activities		-11015999999								Cash Flow from Continuing Investing Activities		-11016000000	-9074000000	-5383000000	-7281000000										Cash Flow from Continuing Investing Activities		-4919700000	-3706000000	-2492300000	-1278600000	-64900000				-10050000000Purchase/Sale and Disposal of Property, Plant and Equipment, Net		-6383000000	-9074000000	-5383000000	-7281000000										Purchase/Sale and Disposal of Property, Plant and Equipment, Net		-6772900000	-6485800000	-6198700000	-5911600000	-5624500000				-10050000000Purchase of Property, Plant and Equipment		-6383000000	-5496000000	-5942000000	-5479000000										Purchase of Property, Plant and Equipment		-5218300000	-4949800000	-4681300000	-4412800000	-4144300000				-6819000000Sale and Disposal of Property, Plant and Equipment			-5496000000	-5942000000	-5479000000										Sale and Disposal of Property, Plant and Equipment			-5040500000	-4683100000	-4325700000	-3968300000				-6819000000Purchase/Sale of Business, Net		-385000000													Purchase/Sale of Business, Net		-384999999								Purchase/Acquisition of Business		-385000000	-308000000	-1666000000	-370000000										Purchase/Acquisition of Business		-1010700000	-1148400000	-1286100000	-1423800000	-1561500000				-259000000Purchase/Sale of Investments, Net		-4348000000	-308000000	-1666000000	-370000000										Purchase/Sale of Investments, Net		574500000	1229400000	1884300000	2539200000	3194100000				-259000000Purchase of Investments		-40860000000	-3293000000	2195000000	-1375000000										Purchase of Investments		16018900000	24471400000	32923900000	41376400000	49828900000				-3360000000Sale of Investments		36512000000	-24949000000	-37072000000	-36955000000										Sale of Investments		-64179300000	-79064600000	-93949900000	-108835200000	-123720500000				-35153000000Other Investing Cash Flow		100000000	21656000000	39267000000	35580000000										Other Investing Cash Flow		49209400000	57052800000	64896200000	72739600000	80583000000				31793000000Purchase/Sale of Other Non-Current Assets, Net			23000000	30000000	-57000000										Purchase/Sale of Other Non-Current Assets, Net			-236000000	-368800000	-501600000	-634400000				388000000Sales of Other Non-Current Assets															Sales of Other Non-Current Assets										Cash Flow from Financing Activities		-16511000000													Cash Flow from Financing Activities		-13997000000	-12740000000							-15254000000Cash Flow from Continuing Financing Activities		-16511000000	-15991000000	-13606000000	-9270000000										Cash Flow from Continuing Financing Activities		-9287400000	-7674400000	-6061400000	-4448400000	-2835400000				-15254000000Issuance of/Payments for Common Stock, Net		-13473000000	-15991000000	-13606000000	-9270000000										Issuance of/Payments for Common Stock, Net		-10767000000	-10026000000	-9285000000	-8544000000	-7803000000				-12610000000Payments for Common Stock		13473000000	-12796000000	-11395000000	-7904000000										Payments for Common Stock		-18708100000	-22862000000	-27015900000	-31169800000	-35323700000				-12610000000Proceeds from Issuance of Common Stock			-12796000000	-11395000000	-7904000000										Proceeds from Issuance of Common Stock				-5806333333	-3360333333	-914333333.3				Issuance of/Repayments for Debt, Net		115000000													Issuance of/Repayments for Debt, Net		-199000000	-356000000							-42000000Issuance of/Repayments for Long Term Debt, Net		115000000	-1042000000	-37000000	-57000000										Issuance of/Repayments for Long Term Debt, Net		-314300000	-348200000	-382100000	-416000000	-449900000				-42000000Proceeds from Issuance of Long Term Debt		6250000000	-1042000000	-37000000	-57000000										Proceeds from Issuance of Long Term Debt		-3407500000	-5307600000	-7207700000	-9107800000	-11007900000				6350000000Repayments for Long Term Debt		6365000000	6699000000	900000000	0										Repayments for Long Term Debt		-117000000	-660800000	-1204600000	-1748400000	-2292200000				-6392000000Proceeds from Issuance/Exercising of Stock Options/Warrants		2923000000	-7741000000	-937000000	-57000000										Proceeds from Issuance/Exercising of Stock Options/Warrants		-2971300000	-3400800000	-3830300000	-4259800000	-4689300000				-2602000000			-2453000000	-2184000000	-1647000000														-1288666667	-885666666.7	-482666666.7				
Other Financing Cash Flow															Other Financing Cash Flow										Cash and Cash Equivalents, End of Period															Cash and Cash Equivalents, End of Period										Change in Cash		0	300000000	10000000	338000000000)										Change in Cash		1		-280000000	-570000000	338000000000)				Effect of Exchange Rate Changes		20945000000	23630000000	26622000000	26465000000										Effect of Exchange Rate Changes		28459100000	29853400000	31247700000	32642000000	34036300000				23719000000Cash and Cash Equivalents, Beginning of Period		25930000000	-3175000000	300000000	6126000000										Cash and Cash Equivalents, Beginning of Period		25930000001	235000000000)	10384666667	15035166667	19685666667				235000000000)Cash Flow Supplemental Section		181000000000)	183000000	-143000000	210000000										Cash Flow Supplemental Section		181000000000)	-146000000000)	110333333.3	123833333.3	137333333.3				-146000000000)Change in Cash as Reported, Supplemental		23719000000000	26622000000000	26465000000000	20129000000000										Change in Cash as Reported, Supplemental		22809500000000	22375000000000	21940500000000	21506000000000	21071500000000				23630000000000Income Tax Paid, Supplemental		2774000000	-2992000000		6336000000										Income Tax Paid, Supplemental		-5809000000	-8692000000	-11575000000		6336000001				89000000Cash and Cash Equivalents, Beginning of Period		13412000000			-4990000000										Cash and Cash Equivalents, Beginning of Period		-13098000000	-26353000000			-4989999999				157000000
12 Months Ended															13 Months Ended										_________________________________________________________															_________________________________________________________															Q4 2019													Q4 2021			Q4 2020				Q4 2020Income Statement 															Income Statement 										USD in "000'"s															USD in "000'"s										Repayments for Long Term Debt					Dec. 31, 2019										Repayments for Long Term Debt			Dec. 31, 2021			Dec. 31, 2020				Dec. 31, 2020Costs and expenses:															Costs and expenses:										Cost of revenues					161857										Cost of revenues			182528			161858				182527Research and development															Research and development										Sales and marketing					71896										Sales and marketing			84733			71897				84732General and administrative					26018										General and administrative			27574			26019				27573European Commission fines					18464										European Commission fines			17947			18465				17946Total costs and expenses					9551										Total costs and expenses			11053			9552				11052Income from operations					1697										Income from operations			1			1698				0Other income (expense), net					127626										Other income (expense), net			141304			127627				141303Income before income taxes					34231										Income before income taxes			41225			34232				41224Provision for income taxes					5394										Provision for income taxes			6858000001			5395				6858000000Net income					19289000000										Net income			22677000001			19289000001				22677000000*include interest paid, capital obligation, and underweighting					19289000000										*include interest paid, capital obligation, and underweighting			22677000001			19289000001				22677000000					19289000000													22677000001			19289000001				22677000000Basic net income per share of Class A and B common stock and Class C capital stock (in dollars par share)															Basic net income per share of Class A and B common stock and Class C capital stock (in dollars par share)										Diluted net income per share of Class A and Class B common stock and Class C capital stock (in dollars par share)															Diluted net income per share of Class A and Class B common stock and Class C capital stock (in dollars par share)										

For Paperwork Reduction Act Notice, see the seperate Instructions.															For Paperwork Reduction Act Notice, see the seperate Instructions.										

















































































					Name	Tax Period 	Total	Social Security	Medicare	Withholding											Name	Tax Period 		Total						Fed 941 Corporate	39355	66986.66	28841.48	6745.18	31400											Fed 941 Corporate	11820.22		4205.072						Fed 941 West Subsidiary	39355	17115.41	7369.14	1723.42	8022.85											Fed 941 West Subsidiary	-8699.723		-16505.352						Fed 941 South Subsidiary	39355	23906.09	10292.9	2407.21	11205.98											Fed 941 South Subsidiary	-5905.64		-13685.332						Fed 941 East Subsidiary	39355	11247.64	4842.74	1132.57	5272.33											Fed 941 East Subsidiary	-11114.067		-18942.108						Fed 941 Corp - Penalty	39355	27198.5	11710.47	2738.73	12749.3											Fed 941 Corp - Penalty	-4550.951		-12318.068						Fed 940 Annual Unemp - Corp	39355	17028.05														Fed 940 Annual Unemp - Corp	-5298.9		-27625.85	

				ID:	TxDL: 00037305581	Ssn:	633-44-1725	DoB: 1994-10-15												ID:	TxDL: 00037305582	Ssn:		633-44-1726	


























































































































































































































































































































































































































































































































































































































































Alphabet Inc. GOOGL, GOOG on Nasdaq															Alphabet Inc. GOOGL, GOOG on Nasdaq										[-] Company Information															[-] Company Information										CIK:															CIK:										1652044															1652045										EIN:															EIN:										61-1767919															61-1767920										SIC:															SIC:										7370 - Services-Computer Programming, Data Processing, Etc.															7371 - Services-Computer Programming, Data Processing, Etc.										(CF Office: Office of Technology)															(CF Office: Office of Technology)										State location:															State location:										CA															CA										State of incorporation:															State of incorporation:										DE															DE										Fiscal year end:															Fiscal year end:										44926															44927										Business address:															Business address:										1600 AMPHITHEATRE PARKWAY, MOUNTAIN VIEW, CA, 94043															1601 AMPHITHEATRE PARKWAY, MOUNTAIN VIEW, CA, 94043										Phone: 650-253-0000															Phone: 650-253-0001										Mailing address:															Mailing address:										1600 AMPHIITHEATRE PARKWAY, MOINTAIN VIEW, CA, 94043															1601 AMPHIITHEATRE PARKWAY, MOINTAIN VIEW, CA, 94043										Category:															Category:										Large accelerated filer															Large accelerated filer										Filings:															Filings:										1,388 EDGAR filings since October 2, 2015															1,388 EDGAR filings since October 2, 2016										Get insider transactions for this issuer															Get insider transactions for this issuer										Get insider transactions for this reporting owner															Get insider transactions for this reporting owner										Latest Filings (excluding insider transactions)															Latest Filings (excluding insider transactions)										March 11, 2022 - SC 13G/A: Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing															March 11, 2022 - SC 13G/A: Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing										February 14, 2022 - SC 13G/A: Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing															February 14, 2022 - SC 13G/A: Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing										February 11, 2022 - SC 13G/A: Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing															February 11, 2022 - SC 13G/A: Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing										February 11, 2022 - SC 13G/A: Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing															February 11, 2022 - SC 13G/A: Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing										February 9, 2022 - SC 13G/A: Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing															February 9, 2022 - SC 13G/A: Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing										Selected Filings															Selected Filings										[+] 8-K (current reports)															[+] 8-K (current reports)										[+] 10-K (annual reports) and 10-Q (quarterly reports)															[+] 10-K (annual reports) and 10-Q (quarterly reports)										[+] Proxy (annual meeting) and information statements															[+] Proxy (annual meeting) and information statements										[+] Ownership disclosures															[+] Ownership disclosures										Filings															Filings										Search table From Date (yyyy-mm-dd) To Date (yyyy-mm-dd)															Search table From Date (yyyy-mm-dd) To Date (yyyy-mm-dd)										
Keywords:															Keywords:										Show columns:															Show columns:										Form type															Form type										Form description															Form description										Filing date															Filing date										Reporting date															Reporting date										Act															Act										Film number															Film number										File number															File number										Accession number															Accession number										Size															Size										Form type		Form description	Reporting date												Form type		Form description	Filing date	Reporting date						Filing dateForm type		Form description	Filing date	Reporting date											Form type		Form description		Filing date	Reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44643	2022-03-22View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44644	2022-03-22View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing Amendments	44642	2022-03-18View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing Amendments		44643	2022-03-18View all with same reporting date					4/A		Statement of changes in beneficial ownership of securities - amendmentOpen document FilingOpen filing	44642	2022-03-18View all with same reporting date											4/A		Statement of changes in beneficial ownership of securities - amendmentOpen document FilingOpen filing		44643	2022-03-18View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing Amendments	44641	2022-03-18View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing Amendments		44642	2022-03-18View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing Amendments	44641	2022-03-18View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing Amendments		44642	2022-03-18View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing Amendments	44641	2022-03-18View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing Amendments		44642	2022-03-18View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44638	2022-03-17View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44639	2022-03-17View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44638	2022-03-17View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44639	2022-03-17View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44638	2022-03-17View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44639	2022-03-17View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44637	2022-03-16View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44638	2022-03-16View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44637	2022-03-16View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44638	2022-03-16View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44637	2022-03-16View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44638	2022-03-16View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44637	2022-03-16View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44638	2022-03-16View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44631	2022-03-09View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44632	2022-03-09View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44631	2022-03-09View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44632	2022-03-09View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44631	2022-03-09View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44632	2022-03-09View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44631	2022-03-09View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44632	2022-03-09View all with same reporting date					SC 13G/A		Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing	44631												SC 13G/A		Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing		44632						4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44630	2022-03-08View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44631	2022-03-08View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44630	2022-03-08View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44631	2022-03-08View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44630	2022-03-08View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44631	2022-03-08View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44630	2022-03-08View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44631	2022-03-08View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44630	2022-03-09View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44631	2022-03-09View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44630	2022-03-09View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44631	2022-03-09View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44629	2022-03-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44630	2022-03-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44629	2022-03-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44630	2022-03-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44629	2022-03-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44630	2022-03-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44629	2022-03-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44630	2022-03-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44622	2022-03-01View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44623	2022-03-01View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44620	2022-02-25View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44621	2022-02-25View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44614	2022-02-22View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44615	2022-02-22View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44609	2022-02-16View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44610	2022-02-16View all with same reporting date					5		Annual statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44606	2021-12-31View all with same reporting date											6		Annual statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44607	2021-12-31View all with same reporting date					SC 13G/A		Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing	44606												SC 13G/A		Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing		44607						5		Annual statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44603	2021-12-31View all with same reporting date											6		Annual statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44604	2021-12-31View all with same reporting date					5		Annual statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44603	2021-12-31View all with same reporting date											6		Annual statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44604	2021-12-31View all with same reporting date					5		Annual statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44603	2021-12-31View all with same reporting date											6		Annual statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44604	2021-12-31View all with same reporting date					5		Annual statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44603	2021-12-31View all with same reporting date											6		Annual statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44604	2021-12-31View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44603	2022-02-09View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44604	2022-02-09View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44603	2022-02-09View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44604	2022-02-09View all with same reporting date					SC 13G/A		Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing	44603												SC 13G/A		Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing		44604						SC 13G/A		Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing	44603												SC 13G/A		Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing		44604						5		Annual statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44603	2021-12-31View all with same reporting date											6		Annual statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44604	2021-12-31View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44603	2022-02-09View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44604	2022-02-09View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44603	2022-02-09View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44604	2022-02-09View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44602	2022-02-08View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44603	2022-02-08View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44602	2022-02-08View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44603	2022-02-08View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44602	2022-02-08View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44603	2022-02-08View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44602	2021-11-26View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44603	2021-11-26View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44602	2021-11-24View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44603	2021-11-24View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44602	2021-11-23View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44603	2021-11-23View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44602	2021-11-19View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44603	2021-11-19View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44602	2021-11-17View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44603	2021-11-17View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44602	2021-11-16View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44603	2021-11-16View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44602	2021-11-04View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44603	2021-11-04View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44601	2022-02-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44602	2022-02-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44601	2022-02-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44602	2022-02-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44601	2022-02-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44602	2022-02-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44601	2022-02-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44602	2022-02-07View all with same reporting date					SC 13G/A		Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing	44601												SC 13G/A		Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing		44602						SC 13G/A		Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing	44601												SC 13G/A		Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing		44602						4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44600	2022-02-08View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44601	2022-02-08View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44600	2022-02-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44601	2022-02-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44600	2022-02-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44601	2022-02-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44600	2022-02-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44601	2022-02-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44600	2022-02-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44601	2022-02-07View all with same reporting date					SC 13G		Statement of acquisition of beneficial ownership by individualsOpen document FilingOpen filing	44600												SC 13G		Statement of acquisition of beneficial ownership by individualsOpen document FilingOpen filing		44601						4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44600	2022-02-04View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44601	2022-02-04View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44599	2022-02-04View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44600	2022-02-04View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44599	2022-02-04View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44600	2022-02-04View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44599	2022-02-04View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44600	2022-02-04View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44599	2022-02-04View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44600	2022-02-04View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44596	2022-02-03View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44597	2022-02-03View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44596	2022-02-03View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44597	2022-02-03View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44596	2022-02-03View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44597	2022-02-03View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44596	2022-02-03View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44597	2022-02-03View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44596	2022-02-03View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44597	2022-02-03View all with same reporting date					SC 13G/A		Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing	44595												SC 13G/A		Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing		44596						4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44594	2022-02-02View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44595	2022-02-02View all with same reporting date					S-3ASR		Automatic shelf registration statement of securities of well-known seasoned issuersOpen document FilingOpen filing	44594												S-3ASR		Automatic shelf registration statement of securities of well-known seasoned issuersOpen document FilingOpen filing		44595						10-K		Annual report [Section 13 and 15(d), not S-K Item 405]Open document FilingOpen filing	44594	2021-12-31View all with same reporting date											10-K		Annual report [Section 13 and 15(d), not S-K Item 405]Open document FilingOpen filing		44595	2021-12-31View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44593	2022-02-01View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44594	2022-02-01View all with same reporting date					8-K		Current reportOpen document FilingOpen filing	44593	2022-02-01View all with same reporting date											8-K		Current reportOpen document FilingOpen filing		44594	2022-02-01View all with same reporting date																							2.02 - Results of Operations and Financial Condition							2.02 - Results of Operations and Financial Condition																		8.01 - Other Events (The registrant can use this Item to report events that are not specifically called for by Form 8-K, that the registrant considers to be of importance to security holders.)							8.01 - Other Events (The registrant can use this Item to report events that are not specifically called for by Form 8-K, that the registrant considers to be of importance to security holders.)																		9.01 - Financial Statements and Exhibits							9.01 - Financial Statements and Exhibits4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44588	2022-01-25View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44589	2022-01-25View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44582	2022-01-20View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44583	2022-01-20View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44582	2022-01-20View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44583	2022-01-20View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44582	2022-01-20View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44583	2022-01-20View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44582	2022-01-20View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44583	2022-01-20View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44581	2022-01-19View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44582	2022-01-19View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44581	2022-01-19View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44582	2022-01-19View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44581	2022-01-19View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44582	2022-01-19View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44581	2022-01-19View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44582	2022-01-19View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44580	2022-01-18View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44581	2022-01-18View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44580	2022-01-18View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44581	2022-01-18View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44575	2022-01-12View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44576	2022-01-12View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44574	2022-01-12View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44575	2022-01-12View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44574	2022-01-12View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44575	2022-01-12View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44574	2022-01-11View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44575	2022-01-11View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44574	2022-01-11View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44575	2022-01-11View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44574	2022-01-11View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44575	2022-01-11View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44572	2022-01-10View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44573	2022-01-10View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44572	2022-01-10View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44573	2022-01-10View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44572	2022-01-10View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44573	2022-01-10View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44572	2022-01-10View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44573	2022-01-10View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44572	2022-01-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44573	2022-01-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44568	2022-01-05View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44569	2022-01-05View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44568	2022-01-05View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44569	2022-01-05View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44568	2022-01-05View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44569	2022-01-05View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44568	2022-01-05View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44569	2022-01-05View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44567	2022-01-05View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44568	2022-01-05View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44566	2022-01-05View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44567	2022-01-05View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44566	2022-01-05View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44567	2022-01-05View all with same reporting date					8-K		Current reportOpen document FilingOpen filing	44565	2021-12-28View all with same reporting date											8-K		Current reportOpen document FilingOpen filing		44566	2021-12-28View all with same reporting date																							5.02 - Departure of Directors or Certain Officers; Election of Directors; Appointment of Certain Officers; Compensatory Arrangements of Certain Officers							5.02 - Departure of Directors or Certain Officers; Election of Directors; Appointment of Certain Officers; Compensatory Arrangements of Certain Officers4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44564	2022-01-03View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44565	2022-01-03View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44564	2022-01-03View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44565	2022-01-03View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44559	2021-12-27View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44560	2021-12-27View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44559	2021-12-27View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44560	2021-12-27View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44559	2021-12-27View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44560	2021-12-27View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44559	2021-12-27View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44560	2021-12-27View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44559	2021-12-27View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44560	2021-12-27View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44559	2021-12-27View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44560	2021-12-27View all with same reporting date					3		Initial statement of beneficial ownership of securitiesOpen document FilingOpen filing	44547	2021-12-07View all with same reporting date											4		Initial statement of beneficial ownership of securitiesOpen document FilingOpen filing		44548	2021-12-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44545	2021-12-15View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44546	2021-12-15View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44540	2021-12-09View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44541	2021-12-09View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44540	2021-12-09View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44541	2021-12-09View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44539	2021-12-08View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44540	2021-12-08View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44539	2021-12-08View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44540	2021-12-08View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44539	2021-12-08View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44540	2021-12-08View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44539	2021-12-08View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44540	2021-12-08View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44538	2021-12-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44539	2021-12-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44538	2021-12-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44539	2021-12-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44538	2021-12-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44539	2021-12-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44538	2021-12-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44539	2021-12-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44538	2021-12-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44539	2021-12-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44538	2021-12-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44539	2021-12-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44537	2021-12-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44538	2021-12-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44537	2021-12-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44538	2021-12-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44537	2021-12-06View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44538	2021-12-06View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44537	2021-12-06View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44538	2021-12-06View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44537	2021-12-06View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44538	2021-12-06View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44531	2021-12-01View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44532	2021-12-01View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44531	2021-12-01View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44532	2021-12-01View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44531	2021-12-01View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44532	2021-12-01View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44529	2021-11-25View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44530	2021-11-25View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44523	2021-11-19View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44524	2021-11-19View all with same reporting date					4/A		Statement of changes in beneficial ownership of securities - amendmentOpen document FilingOpen filing	44523	2021-11-11View all with same reporting date											4/A		Statement of changes in beneficial ownership of securities - amendmentOpen document FilingOpen filing		44524	2021-11-11View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44523	2021-11-21View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44524	2021-11-21View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44518	2021-11-16View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44519	2021-11-16View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44517	2021-11-17View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44518	2021-11-17View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44517	2021-11-16View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44518	2021-11-16View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44517	2021-11-16View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44518	2021-11-16View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44516	2021-11-15View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44517	2021-11-15View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44516	2021-11-15View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44517	2021-11-15View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44515	2021-11-12View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44516	2021-11-12View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44515	2021-11-12View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44516	2021-11-12View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44515	2021-11-12View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44516	2021-11-12View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44512	2021-11-10View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44513	2021-11-10View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44512	2021-11-10View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44513	2021-11-10View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44512	2021-11-10View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44513	2021-11-10View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44512	2021-11-09View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44513	2021-11-09View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44510	2021-11-09View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44511	2021-11-09View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44509	2021-11-08View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44510	2021-11-08View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44509	2021-11-08View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44510	2021-11-08View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44509	2021-11-08View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44510	2021-11-08View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44508	2021-11-05View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44509	2021-11-05View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44508	2021-11-05View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44509	2021-11-05View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44508	2021-11-05View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44509	2021-11-05View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44503	2021-11-03View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44504	2021-11-03View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44502	2021-11-02View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44503	2021-11-02View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44501	2021-11-01View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44502	2021-11-01View all with same reporting date					10-Q		Quarterly report [Sections 13 or 15(d)]Open document FilingOpen filing	44496	2021-09-30View all with same reporting date											10-Q		Quarterly report [Sections 13 or 15(d)]Open document FilingOpen filing		44497	2021-09-30View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44495	2021-10-25View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44496	2021-10-25View all with same reporting date					8-K		Current reportOpen document FilingOpen filing	44495	2021-10-26View all with same reporting date											8-K		Current reportOpen document FilingOpen filing		44496	2021-10-26View all with same reporting date																							2.02 - Results of Operations and Financial Condition							2.02 - Results of Operations and Financial Condition																		9.01 - Financial Statements and Exhibits							9.01 - Financial Statements and Exhibits4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44490	2021-10-20View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44491	2021-10-20View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44490	2021-10-20View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44491	2021-10-20View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44490	2021-10-20View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44491	2021-10-20View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44489	2021-10-19View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44490	2021-10-19View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44489	2021-10-19View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44490	2021-10-19View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44487	2021-10-18View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44488	2021-10-18View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44487	2021-10-18View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44488	2021-10-18View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44484	2021-10-13View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44485	2021-10-13View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44484	2021-10-13View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44485	2021-10-13View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44483	2021-10-12View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44484	2021-10-12View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44483	2021-10-12View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44484	2021-10-12View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44481	2021-10-11View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44482	2021-10-11View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44481	2021-10-11View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44482	2021-10-11View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44477	2021-10-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44478	2021-10-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44475	2021-10-06View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44476	2021-10-06View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44475	2021-10-04View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44476	2021-10-04View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44470	2021-10-01View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44471	2021-10-01View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44470	2021-09-29View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44471	2021-09-29View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44467	2021-09-25View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44468	2021-09-25View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44467	2021-09-25View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44468	2021-09-25View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44467	2021-09-25View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44468	2021-09-25View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44467	2021-09-25View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44468	2021-09-25View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44467	2021-09-25View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44468	2021-09-25View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44467	2021-09-25View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44468	2021-09-25View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44466	2021-09-23View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44467	2021-09-23View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44466	2021-09-23View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44467	2021-09-23View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44463	2021-09-24View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44464	2021-09-24View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44463	2021-09-22View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44464	2021-09-22View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44463	2021-09-22View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44464	2021-09-22View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44463	2021-09-22View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44464	2021-09-22View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44461	2021-09-21View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44462	2021-09-21View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44461	2021-09-21View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44462	2021-09-21View all with same reporting date					3		Initial statement of beneficial ownership of securitiesOpen document FilingOpen filing	44460	2021-09-21View all with same reporting date											4		Initial statement of beneficial ownership of securitiesOpen document FilingOpen filing		44461	2021-09-21View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44454	2021-09-15View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44455	2021-09-15View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44452	2021-09-09View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44453	2021-09-09View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44452	2021-09-09View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44453	2021-09-09View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44449	2021-09-08View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44450	2021-09-08View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44449	2021-09-08View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44450	2021-09-08View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44447	2021-09-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44448	2021-09-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44447	2021-09-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44448	2021-09-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44447	2021-09-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44448	2021-09-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44441	2021-09-01View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44442	2021-09-01View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44441	2021-09-01View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44442	2021-09-01View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44441	2021-09-02View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44442	2021-09-02View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44438	2021-08-29View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44439	2021-08-29View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44435	2021-08-25View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44436	2021-08-25View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44431	2021-08-20View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44432	2021-08-20View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44431	2021-08-20View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44432	2021-08-20View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44431	2021-08-19View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44432	2021-08-19View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44431	2021-08-19View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44432	2021-08-19View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44427	2021-08-18View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44428	2021-08-18View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44427	2021-08-18View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44428	2021-08-18View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44427	2021-08-18View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44428	2021-08-18View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44419	2021-08-11View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44420	2021-08-11View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44419	2021-08-11View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44420	2021-08-11View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44419	2021-08-10View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44420	2021-08-10View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44419	2021-08-10View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44420	2021-08-10View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44418	2021-08-09View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44419	2021-08-09View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44418	2021-08-09View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44419	2021-08-09View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44418	2021-08-09View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44419	2021-08-09View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44412	2021-08-04View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44413	2021-08-04View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44411	2021-08-03View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44412	2021-08-03View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44410	2021-07-30View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44411	2021-07-30View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44410	2021-08-02View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44411	2021-08-02View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44410	2021-07-29View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44411	2021-07-29View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44410	2021-07-29View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44411	2021-07-29View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44407	2021-07-28View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44408	2021-07-28View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44407	2021-07-28View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44408	2021-07-28View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44407	2021-07-28View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44408	2021-07-28View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44406	2021-07-27View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44407	2021-07-27View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44406	2021-07-27View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44407	2021-07-27View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44406	2021-07-27View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44407	2021-07-27View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44406	2021-07-27View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44407	2021-07-27View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44405	2021-07-26View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44406	2021-07-26View all with same reporting date					10-Q		Quarterly report [Sections 13 or 15(d)]Open document FilingOpen filing	44405	2021-06-30View all with same reporting date											10-Q		Quarterly report [Sections 13 or 15(d)]Open document FilingOpen filing		44406	2021-06-30View all with same reporting date					3		Initial statement of beneficial ownership of securitiesOpen document FilingOpen filing	44404	2021-07-27View all with same reporting date											4		Initial statement of beneficial ownership of securitiesOpen document FilingOpen filing		44405	2021-07-27View all with same reporting date					8-K		Current reportOpen document FilingOpen filing	44404	2021-07-27View all with same reporting date											8-K		Current reportOpen document FilingOpen filing		44405	2021-07-27View all with same reporting date																							2.02 - Results of Operations and Financial Condition							2.02 - Results of Operations and Financial Condition																		9.01 - Financial Statements and Exhibits							9.01 - Financial Statements and Exhibits4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44398	2021-07-21View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44399	2021-07-21View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44389	2021-07-08View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44390	2021-07-08View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44389	2021-07-08View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44390	2021-07-08View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44386	2021-07-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44387	2021-07-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44386	2021-07-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44387	2021-07-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44386	2021-07-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44387	2021-07-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44386	2021-07-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44387	2021-07-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44386	2021-07-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44387	2021-07-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44386	2021-07-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44387	2021-07-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44386	2021-07-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44387	2021-07-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44386	2021-07-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44387	2021-07-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44386	2021-07-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44387	2021-07-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44386	2021-07-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44387	2021-07-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44385	2021-07-06View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44386	2021-07-06View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44385	2021-07-06View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44386	2021-07-06View all with same reporting date					8-K		Current reportOpen document FilingOpen filing	44385	2021-07-07View all with same reporting date											8-K		Current reportOpen document FilingOpen filing		44386	2021-07-07View all with same reporting date																							8.01 - Other Events (The registrant can use this Item to report events that are not specifically called for by Form 8-K, that the registrant considers to be of importance to security holders.)							8.01 - Other Events (The registrant can use this Item to report events that are not specifically called for by Form 8-K, that the registrant considers to be of importance to security holders.)4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44385	2021-07-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44386	2021-07-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44385	2021-07-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44386	2021-07-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44383	2021-07-02View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44384	2021-07-02View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44378	2021-07-01View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44379	2021-07-01View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44378	2021-07-01View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44379	2021-07-01View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44378	2021-06-30View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44379	2021-06-30View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44378	2021-06-29View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44379	2021-06-29View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44376	2021-06-25View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44377	2021-06-25View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44375	2021-06-25View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44376	2021-06-25View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44375	2021-06-25View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44376	2021-06-25View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44375	2021-06-25View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44376	2021-06-25View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44375	2021-06-25View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44376	2021-06-25View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44375	2021-06-25View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44376	2021-06-25View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44364	2021-06-16View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44365	2021-06-16View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44358	2021-06-09View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44359	2021-06-09View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44358	2021-06-09View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44359	2021-06-09View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44357	2021-06-08View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44358	2021-06-08View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44357	2021-06-08View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44358	2021-06-08View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44356	2021-06-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44357	2021-06-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44356	2021-06-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44357	2021-06-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44356	2021-06-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44357	2021-06-07View all with same reporting date					4		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing	44356	2021-06-07View all with same reporting date											5		Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing		44357	2021-06-07View all with same reporting date					Showing 1 to 32 of 1,000 entries															Showing 1 to 32 of 1,000 entries										Data source: CIK0001652044.json															Data source: CIK0001652044.json										Investor Resources															Investor Resources										How to Use EDGAR															How to Use EDGAR										Learn how to use EDGAR to research public filings by public companies, mutual funds, ETFs, some annuities, and more.															Learn how to use EDGAR to research public filings by public companies, mutual funds, ETFs, some annuities, and more.										Before you Invest, Investor.gov															Before you Invest, Investor.gov										Get answers to your investing questions from the SEC's website dedicated to retail investors															Get answers to your investing questions from the SEC's website dedicated to retail investors										

0 comments on commit f1081d5

 Lock conversation

￼

Write Preview

Add heading textAdd bold text, <Ctrl+b>Add italic text, <Ctrl+i>

Add a quote, <Ctrl+Shift+.>Add code, <Ctrl+e>Add a link, <Ctrl+k>

Add a bulleted list, <Ctrl+Shift+8>Add a numbered list, <Ctrl+Shift+7>Add a task list, <Ctrl+Shift+l>

Directly mention a user or teamReference an issue, pull request, or discussionAdd saved reply

Attach files by dragging & dropping, selecting or pasting them.Styling with Markdown is supported

Comment on this commit

Unsubscribe 

You’re receiving notifications because you’re watching this repository.

Footer

© 2022 GitHub, Inc.

Footer navigation

Terms

Privacy

Security

Status

Docs

Contact GitHub

Pricing

API

Training

Blog

About

instructions · zakwarlord7/zakwarlord7@f1081d5



Web search

Copy


Copyright 2005-09-17,17:00:00:00 :;-17:00:00:00CSMT](All rights reserved. MIT license).
use serde::Deserialize;
table 	{mso-displayed-decimal-separator:"\."; 	mso-displayed-thousand-separator:"\,";} tr 	{mso-height-source:auto;} col 	{mso-width-source:auto;} td 	{padding-top:1px; 	padding-right:1px; 	padding-left:1px; 	mso-ignore:padding; 	color:black; 	font-size:11.0pt; 	font-weight:400; 	font-style:normal; 	text-decoration:none; 	font-family:Calibri, sans-serif; 	mso-font-charset:0; 	text-align:general; 	vertical-align:bottom; 	border:none; 	white-space:nowrap; 	mso-rotate:0;} .xl48 	{font-size:13.5pt; 	font-weight:700; 	font-family:"Courier New"; 	mso-generic-font-family:auto; 	mso-font-charset:0;} .xl49 	{font-size:13.5pt;} .xl50 	{font-size:13.5pt; 	font-weight:700; 	font-family:"Courier New"; 	mso-generic-font-family:auto; 	mso-font-charset:0; 	text-align:left;} .xl51 	{font-size:13.5pt; 	font-weight:700; 	font-family:"Courier New"; 	mso-generic-font-family:auto; 	mso-font-charset:0; 	text-align:right;} .xl52 	{font-family:Arial; 	mso-generic-font-family:auto; 	mso-font-charset:1; 	border-top:.5pt solid #CCCCCC; 	border-right:.5pt solid #CCCCCC; 	border-bottom:.5pt solid #CCCCCC; 	border-left:.5pt solid black;} .xl53 	{font-family:Arial; 	mso-generic-font-family:auto; 	mso-font-charset:1; 	border:.5pt solid #CCCCCC;} .xl54 	{font-size:9.0pt; 	font-family:Arial; 	mso-generic-font-family:auto; 	mso-font-charset:1; 	border-top:.5pt solid #CCCCCC; 	border-right:.5pt solid #CCCCCC; 	border-bottom:.5pt solid #CCCCCC; 	border-left:.5pt solid black;} .xl55 	{font-family:Arial; 	mso-generic-font-family:auto; 	mso-font-charset:1; 	border-top:.5pt solid #CCCCCC; 	border-right:.5pt solid #CCCCCC; 	border-bottom:.5pt solid black; 	border-left:.5pt solid black;} .xl56 	{font-family:Arial; 	mso-generic-font-family:auto; 	mso-font-charset:1; 	border-top:.5pt solid #CCCCCC; 	border-right:.5pt solid #CCCCCC; 	border-bottom:.5pt solid black; 	border-left:.5pt solid #CCCCCC;} .xl58 	{font-family:Arial; 	mso-generic-font-family:auto; 	mso-font-charset:1; 	border-top:.5pt solid #CCCCCC; 	border-right:.5pt solid #CCCCCC; 	border-bottom:2.0pt double black; 	border-left:.5pt solid black;} .xl59 	{font-family:Arial; 	mso-generic-font-family:auto; 	mso-font-charset:1; 	border-top:.5pt solid #CCCCCC; 	border-right:.5pt solid #CCCCCC; 	border-bottom:2.0pt double black; 	border-left:.5pt solid #CCCCCC;} .xl60 	{font-size:9.0pt; 	font-weight:700; 	font-family:Arial; 	mso-generic-font-family:auto; 	mso-font-charset:1; 	border-top:.5pt solid #CCCCCC; 	border-right:.5pt solid #CCCCCC; 	border-bottom:.5pt solid #CCCCCC; 	border-left:.5pt solid black;} .xl66 	{font-size:13.5pt; 	font-weight:700; 	font-family:"Courier New"; 	mso-generic-font-family:auto; 	mso-font-charset:0; 	white-space:normal;} .xl67 	{font-family:Arial; 	mso-generic-font-family:auto; 	mso-font-charset:1; 	text-align:right; 	border-top:.5pt solid #CCCCCC; 	border-right:.5pt solid black; 	border-bottom:.5pt solid #CCCCCC; 	border-left:.5pt solid #CCCCCC;} .xl68 	{font-family:Arial; 	mso-generic-font-family:auto; 	mso-font-charset:1; 	text-align:right; 	border-top:.5pt solid #CCCCCC; 	border-right:.5pt solid black; 	border-bottom:.5pt solid black; 	border-left:.5pt solid #CCCCCC;} .xl69 	{font-family:Arial; 	mso-generic-font-family:auto; 	mso-font-charset:1; 	text-align:right; 	border-top:.5pt solid #CCCCCC; 	border-right:.5pt solid black; 	border-bottom:2.0pt double black; 	border-left:.5pt solid #CCCCCC;} .xl79 	{color:#0563C1; 	text-decoration:underline; 	text-underline-style:single; 	white-space:normal;} .xl80 	{color:#24292F; 	font-family:-Apple-System; 	mso-generic-font-family:auto; 	mso-font-charset:1;} .xl88 	{font-family:Arial; 	mso-generic-font-family:auto; 	mso-font-charset:1; 	text-align:left; 	border-top:.5pt solid #CCCCCC; 	border-right:.5pt solid black; 	border-bottom:2.0pt double black; 	border-left:.5pt solid #CCCCCC;} .xl91 	{font-family:Arial; 	mso-generic-font-family:auto; 	mso-font-charset:1; 	text-align:right; 	vertical-align:middle; 	border-top:2.0pt double black; 	border-right:.5pt solid #CCCCCC; 	border-bottom:none; 	border-left:none; 	white-space:normal;} .xl92 	{font-family:Arial; 	mso-generic-font-family:auto; 	mso-font-charset:1; 	text-align:right; 	vertical-align:middle; 	border-top:none; 	border-right:.5pt solid #CCCCCC; 	border-bottom:none; 	border-left:none; 	white-space:normal;} .xl93 	{font-family:Arial; 	mso-generic-font-family:auto; 	mso-font-charset:1; 	text-align:right; 	vertical-align:middle; 	border-top:none; 	border-right:.5pt solid #CCCCCC; 	border-bottom:.5pt solid #CCCCCC; 	border-left:none; 	white-space:normal;} .xl94 	{font-family:Arial; 	mso-generic-font-family:auto; 	mso-font-charset:1; 	text-align:right; 	vertical-align:middle; 	border-top:2.0pt double black; 	border-right:none; 	border-bottom:.5pt solid #CCCCCC; 	border-left:.5pt solid black; 	white-space:normal;} .xl95 	{font-family:Arial; 	mso-generic-font-family:auto; 	mso-font-charset:1; 	text-align:right; 	vertical-align:middle; 	border-top:2.0pt double black; 	border-right:none; 	border-bottom:.5pt solid #CCCCCC; 	border-left:none; 	white-space:normal;} .xl96 	{font-family:Arial; 	mso-generic-font-family:auto; 	mso-font-charset:1; 	text-align:right; 	vertical-align:middle; 	border-top:2.0pt double black; 	border-right:.5pt solid #CCCCCC; 	border-bottom:.5pt solid #CCCCCC; 	border-left:none; 	white-space:normal;} .xl97 	{font-family:Arial; 	mso-generic-font-family:auto; 	mso-font-charset:1; 	text-align:left; 	vertical-align:top; 	border-top:2.0pt double black; 	border-right:none; 	border-bottom:.5pt solid #CCCCCC; 	border-left:.5pt solid black; 	white-space:normal;} .xl98 	{font-family:Arial; 	mso-generic-font-family:auto; 	mso-font-charset:1; 	text-align:left; 	vertical-align:top; 	border-top:2.0pt double black; 	border-right:none; 	border-bottom:.5pt solid #CCCCCC; 	border-left:none; 	white-space:normal;} $70,842,743,866.00 Taxable Marital Status:
Exemptions/AllowancesFederal:TX:Gross PayStatutoryFederal Income TaxSocial Security TaxMedicare TaxNet PayCHECKINGNet CheckYour federal taxable wages this period are $ALPHABET INCOME1600 AMPIHTHEATRE PARKWAY MOUNTAIN VIEW CA 94043Deposited to the account OfPLEASE READ THE IMPORTANT DISCLOSURES BELOWBased on facts as set forth in.The U.S. Internal Revenue Code of 1986, as amended, the Treasury Regulations promulgated thereunder, published pronouncements of the Internal Revenue Service, which may be cited or used as precedents, and case law, any of which may be changed at any time with retroactive effect. No opinion is expressed on any matters other than those specifically referred to above.EMPLOYER IDENTIFICATION NUMBER: 61-1767919[DRAFT FORM OF TAX OPINION]ORIGINAL REPORTIncome, Rents, & RoyaltyINCOME STATEMENTGOOGL_income-statement_Quarterly_As_Originally_ReportedGross ProfitTotal Revenue as Reported, SupplementalOther RevenueCost of RevenueCost of Goods and ServicesOperating Income/ExpensesSelling, General and Administrative ExpensesGeneral and Administrative ExpensesSelling and Marketing ExpensesResearch and Development ExpensesTotal Operating Profit/LossNon-Operating Income/Expenses, TotalTotal Net Finance Income/ExpenseNet Interest Income/ExpenseInterest Expense Net of Capitalized InterestInterest IncomeNet Investment IncomeGain/Loss on Investments and Other Financial InstrumentsIncome from Associates, Joint Ventures and Other Participating InterestsGain/Loss on Foreign ExchangeIrregular Income/ExpensesOther Irregular Income/ExpensesOther Income/Expense, Non-OperatingPretax IncomeProvision for Income TaxNet Income from Continuing OperationsNet Income after Extraordinary Items and Discontinued OperationsNet Income after Non-Controlling/Minority InterestsNet Income Available to Common StockholdersDiluted Net Income Available to Common StockholdersIncome Statement Supplemental SectionReported Normalized and Operating Income/Expense Supplemental SectionTotal Revenue as Reported, SupplementalTotal Operating Profit/Loss as Reported, SupplementalReported Effective Tax RateReported Normalized IncomeReported Normalized Operating ProfitOther Adjustments to Net Income Available to Common StockholdersDiscontinued OperationsBasic EPSBasic EPS from Continuing OperationsBasic EPS from Discontinued OperationsDiluted EPSDiluted EPS from Continuing OperationsDiluted EPS from Discontinued OperationsBasic Weighted Average Shares OutstandingDiluted Weighted Average Shares OutstandingReported Normalized Diluted EPSBasic EPSDiluted EPSBasic WASODiluted WASOFiscal year end September 28th., 2022. | USD31622,6:39 PMMorningstar.com Intraday Fundamental Portfolio View Print Report3/6/2022 at 6:37 PMGOOGL_income-statement_Quarterly_As_Originally_ReportedCash Flow from Operating Activities, IndirectNet Cash Flow from Continuing Operating Activities, IndirectCash Generated from Operating ActivitiesIncome/Loss before Non-Cash AdjustmentTotal Adjustments for Non-Cash ItemsDepreciation, Amortization and Depletion, Non-Cash AdjustmentDepreciation and Amortization, Non-Cash AdjustmentDepreciation, Non-Cash AdjustmentAmortization, Non-Cash AdjustmentStock-Based Compensation, Non-Cash AdjustmentTaxes, Non-Cash AdjustmentInvestment Income/Loss, Non-Cash AdjustmentGain/Loss on Financial Instruments, Non-Cash AdjustmentOther Non-Cash ItemsChanges in Operating CapitalChange in Trade and Other ReceivablesChange in Trade/Accounts ReceivableChange in Other Current AssetsChange in Payables and Accrued ExpensesChange in Trade and Other PayablesChange in Trade/Accounts PayableChange in Accrued ExpensesChange in Deferred Assets/LiabilitiesChange in Other Operating CapitalChange in Prepayments and DepositsCash Flow from Investing ActivitiesCash Flow from Continuing Investing ActivitiesPurchase/Sale and Disposal of Property, Plant and Equipment, NetPurchase of Property, Plant and EquipmentSale and Disposal of Property, Plant and EquipmentPurchase/Sale of Business, NetPurchase/Acquisition of BusinessPurchase/Sale of Investments, NetPurchase of InvestmentsSale of InvestmentsOther Investing Cash FlowPurchase/Sale of Other Non-Current Assets, NetSales of Other Non-Current AssetsCash Flow from Financing ActivitiesCash Flow from Continuing Financing ActivitiesIssuance of/Payments for Common Stock, NetPayments for Common StockProceeds from Issuance of Common StockIssuance of/Repayments for Debt, NetIssuance of/Repayments for Long Term Debt, NetProceeds from Issuance of Long Term DebtRepayments for Long Term DebtProceeds from Issuance/Exercising of Stock Options/WarrantsOther Financing Cash FlowCash and Cash Equivalents, End of PeriodChange in CashEffect of Exchange Rate ChangesCash and Cash Equivalents, Beginning of PeriodCash Flow Supplemental SectionChange in Cash as Reported, SupplementalIncome Tax Paid, SupplementalCash and Cash Equivalents, Beginning of Period12 Months Ended_________________________________________________________Income StatementUSD in "000'"sRepayments for Long Term DebtCosts and expenses:Cost of revenuesResearch and developmentSales and marketingGeneral and administrativeEuropean Commission finesTotal costs and expensesIncome from operationsOther income (expense), netIncome before income taxesProvision for income taxesNet income*include interest paid, capital obligation, and underweightingBasic net income per share of Class A and B common stock and Class C capital stock (in dollars par share)Diluted net income per share of Class A and Class B common stock and Class C capital stock (in dollars par share)For Paperwork Reduction Act Notice, see the seperate Instructions.rate112.27569887160061-176791988-1303491TTM$146,698,000,000.00 $257,637,000,000.00 $257,637,000,000.00 -1.10939E+11-1.10939E+11-67984000000-36422000000-13510000000-22912000000-31562000000787140000001202000000011530000001153000000-34600000014990000001236400000012270000000334000000-24000000000-149700000090734000000-1470100000076033000000760330000007603300000076033000000760330000002.57637E+11787140000000.162113.88113.88112.2112.2667650000677674000113.88112.2667650000677674000Advice number:NO State Incorne Taxunits67467800070842743866$70,842,743,866.00 Q4 2021$42,337,000,000.00 $75,325,000,000.00 $75,325,000,000.00 -32988000000-32988000000-20452000000-11744000000-4140000000-7604000000-8708000000218850000002517000000261000000261000000-1170000003780000002364000000247800000049000000-16300000000-10800000024402000000-37600000002064200000020642000000206420000002064200000020642000000753250000002188500000031.1531.1230.6930.6766266400067249300031.1530.69662664000672493000Q4 202124934000000249340000002493400000020642000000651700000034390000003439000000321500000022400000039540000001616000000-2478000000-2478000000-14000000-2225000000-5819000000-5819000000-3990000006994000000115700000011570000005837000000368000000-3369000000-11016000000-11016000000-6383000000-6383000000-385000000-385000000-4348000000-4086000000036512000000100000000-16511000000-16511000000-134730000001347300000011500000011500000062500000006365000000292300000002094500000025930000000181000000000)2.3719E+13277400000013412000000Pay date:_70842743866Q2 2021$35,653,000,000.00 $61,880,000,000.00 $61,880,000,000.00 -26227000000-26227000000-16292000000-8617000000-3341000000-5276000000-7675000000193610000002624000000313000000313000000-760000003890000002924000000288300000092000000-51000000-61300000021985000000-3460000000185250000001852500000018525000000185250000001852500000061880000000193610000000.15727.6927.6927.2627.2666895800067961200027.6927.26668958000679612000Q2 20213749700000021890000000218900000001852500000042360000002945000000294500000027300000002150000003803000000379000000-2883000000-2883000000-8000000-871000000-3661000000-3661000000-1990000004074000000-130000000-1300000004204000000-3000000-1082000000-9074000000-9074000000-5496000000-5496000000-308000000-308000000-3293000000-249490000002165600000023000000-15991000000-15991000000-12796000000-12796000000-1042000000-10420000006699000000-7741000000-245300000030000000023630000000-31750000001830000002.6622E+13-2992000000PLEASE READ THE IMPORTANT DISCLOSURES BELOW

FEDERAL RESERVE MASTER SUPPLIER ACCOUNT 31000053-052101023 COD
633-44-1725 Zachryiixixiiiwood@gmail.com 47-2041-6547 111000614 31000053
PNC Bank PNC Bank Business Tax I.D. Number: 633441725
CIF Department (Online Banking) Checking Account: 47-2041-6547
P7-PFSC-04-F Business Type: Sole Proprietorship/Partnership Corporation
500 First Avenue ALPHABET
Pittsburgh, PA 15219-3128 5323 BRADFORD DR
NON-NEGOTIABLE DALLAS TX 75235 8313
ZACHRY, TYLER, WOOD
4/18/2022 650-2530-000 469-697-4300
SIGNATURE Time Zone: Eastern Central Mountain Pacific
Investment Products  • Not FDIC Insured  • No Bank Guarantee  • May Lose ValueQ1 2021$31,211,000,000.00 $55,314,000,000.00 $55,314,000,000.00 ($24,103,000,000.00)-24103000000($14,774,000,000.00)-7289000000-2773000000-4516000000-7485000000164370000004846000000269000000269000000-76000000345000000486900000047510000005000000113000000-29200000021283000000-3353000000179300000001793000000017930000000179300000001793000000055314000000164370000000.15826.6326.6326.2926.2967322000068207100026.6326.29673220000682071000Q1 202131211000000192890000001928900000017930000000259200000027530000002753000000252500000022800000037450000001100000000-4751000000-4751000000-255000000-1233000000279400000027940000007000000-4956000000-982000000-982000000-3974000000137000000785000000-5383000000-5383000000-5942000000-5942000000-1666000000-16660000002195000000-370720000003926700000030000000-13606000000-13606000000-11395000000-11395000000-37000000-37000000900000000-937000000-21840000001000000026622000000300000000-1430000002.6465E+13xxxxxxxx6547Q4 2020308180000005689800000056898000000-26080000000-26080000000($15,167,000,000.00)-8145000000-2831000000-5314000000-7022000000156510000003038000000333000000333000000-5300000038600000035300000003262000000355000000-8700000000-82500000018689000000-34620000001522700000015227000000152270000001522700000015227000000568980000001565100000022.5422.4622.322.2367558100068296900022.5422.3675581000682969000Q4 202030818000000226770000002267700000015227000000574800000037250000003725000000353900000018600000032230000001670000000-3262000000-32620000003920000001702000000-5445000000-5445000000-73800000069380000009630000009630000005975000000207000000740000000-7281000000-7281000000-5479000000-5479000000-370000000-370000000-1375000000-3695500000035580000000-57000000-9270000000-9270000000-7904000000-7904000000-57000000-570000000-57000000-1647000000338000000000)2646500000061260000002100000002.0129E+136336000000-4990000000Q4 2019Dec. 31, 201916185771896260181846495511697127626342315394192890000001928900000019289000000PLEASE READ THE IMPORTANT DISCLOSURES BELOW

FEDERAL RESERVE MASTER SUPPLIER ACCOUNT 31000053-052101023 COD
633-44-1725 Zachryiixixiiiwood@gmail.com 47-2041-6547 111000614 31000053
PNC Bank PNC Bank Business Tax I.D. Number: 633441725
CIF Department (Online Banking) Checking Account: 47-2041-6547
P7-PFSC-04-F Business Type: Sole Proprietorship/Partnership Corporation
500 First Avenue ALPHABET
Pittsburgh, PA 15219-3128 5323 BRADFORD DR
NON-NEGOTIABLE DALLAS TX 75235 8313
ZACHRY, TYLER, WOOD
4/18/2022 650-2530-000 469-697-4300
SIGNATURE Time Zone: Eastern Central Mountain Pacific
Investment Products  • Not FDIC Insured  • No Bank Guarantee  • May Lose Valueyear to date7569887160000.00%Q3 2020$25,056,000,000.00 $46,173,000,000.00 $46,173,000,000.00 ($21,117,000,000.00)-21117000000-1384300000000.00%-6987000000-2756000000-4231000000-6856000000112130000002146000000412000000412000000-480000004600000001957000000201500000026000000-8400000000-22300000013359000000-2112000000112470000001124700000011247000000112470000001124700000046173000000112130000000.15816.5516.5516.416.467944900068585100016.5516.4679449000685851000NON-NEGOTIABLEZACHRY T.5323DALLASOther Benefits andInformationPto BalanceTotal Work HrsImportant NotesCOMPANY PH Y: 650-253-0000BASIS OF PAY: BASIC/DILUTED EPSYOUR BASIC/DILUTED EPS RATE HAS BEEN CHANGED FROM 0.001 TO 112.20 PAR SHARE VALUEAdvice number:Pay date:_xxxxxxxx6547NON-NEGOTIABLEQ2 20201974400000000.00%3829700000000.00%3829700000000.00%-1855300000000.00%-18553000000($13,361,000,000.00)-6486000000-2585000000-3901000000-687500000063830000001894000000420000000420000000-1300000043300000016960000001842000000-54000000-9200000000-2220000008277000000-1318000000695900000069590000006959000000695900000069590000003829700000063830000000.15910.2110.2110.1310.1368176800068702400010.2110.13681768000687024000Print|______________________________________________________________________________________________________________________DOLLARS [OBJ]FeaturesTaxable Marital Status:
Exemptions/AllowancesZACHRY T.|ESTATE OFDetaile on5323|BackFederal:|FOR_____________________________________DALLASTX:NO State Incorne Tax|PLEASE READ THE IMPORTANT DISCLOSURES BELOWrateunitsyear to dateOther Benefits and||AUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATURE.EXECUTOR/112.26746780007569887160000.00%Information|FEDERAL RESERVE MASTER SUPPLIER ACCOUNT 31000053-052101023 COD|{}.ADMINISTRATORPto Balance||AUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATURE.PERSONAL/Total Work Hrs|633-44-1725 Zachryiixixiiiwood@gmail.com 47-2041-6547 111000614 31000053|{}.REPRESENTATIVEGross Pay75698871600Important Notes|PNC Bank PNC Bank Business Tax I.D. Number: 633441725|AUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATURE.TRUSTEE||COMPANY PH Y: 650-253-0000|CIF Department (Online Banking) Checking Account: 47-2041-6547|Deposited to the account Of xxxxxxxx6547StatutoryBASIS OF PAY: BASIC/DILUTED EPS|P7-PFSC-04-F Business Type: Sole Proprietorship/Partnership CorporationFederal Income Tax|500 First Avenue ALPHABETSocial Security Tax|Pittsburgh, PA 15219-3128 5323 BRADFORD DRYOUR BASIC/DILUTED EPS RATE HAS BEEN CHANGED FROM 0.001 TO 112.20 PAR SHARE VALUE|Medicare Tax|NON-NEGOTIABLENet Pay7084274386670842743866CHECKINGNet Check$70,842,743,866.00 Your federal taxable wages this period are $Skip to contentALPHABET INCOMEAdvice number:Search or jump to…1600 AMPIHTHEATRE PARKWAY MOUNTAIN VIEW CA 94043Pay date:_Pull requestsIssuesDeposited to the account Ofxxxxxxxx6547MarketplacePLEASE READ THE IMPORTANT DISCLOSURES BELOW

FEDERAL RESERVE MASTER SUPPLIER ACCOUNT 31000053-052101023 COD
633-44-1725 Zachryiixixiiiwood@gmail.com 47-2041-6547 111000614 31000053
PNC Bank PNC Bank Business Tax I.D. Number: 633441725
CIF Department (Online Banking) Checking Account: 47-2041-6547
P7-PFSC-04-F Business Type: Sole Proprietorship/Partnership Corporation
500 First Avenue ALPHABET
Pittsburgh, PA 15219-3128 5323 BRADFORD DR
NON-NEGOTIABLE DALLAS TX 75235 8313
ZACHRY, TYLER, WOOD
4/18/2022 650-2530-000 469-697-4300
SIGNATURE Time Zone: Eastern Central Mountain Pacific
Investment Products  • Not FDIC Insured  • No Bank Guarantee  • May Lose ValueExploreNON-NEGOTIABLE PLEASE READ THE IMPORTANT DISCLOSURES BELOW#NAME?Your account has been flagged.Because of that, your profile is hidden from the public. If you believe this is a mistake, contact support to have your account status reviewed.zakwarlord7/Supremer-GalaxyPublicCodeIssuesPull requestsActionsProjectsWikiSecurityInsightsSettingsSupremer-Galaxy/Build and Deploy#NAME?zakwarlord7 Update Build and DeployLatest commit 761ec08 now History 1 contributor215 lines (205 sloc)  14.4 KBBased on facts as set forth in.The U.S. Internal Revenue Code of 1986, as amended, the Treasury Regulations promulgated thereunder, published pronouncements of the Internal Revenue Service, which may be cited or used as precedents, and case law, any of which may be changed at any time with retroactive effect. No opinion is expressed on any matters other than those specifically referred to above.Get answers to your investing questions from the SEC's website dedicated to retail investors :941EMPLOYER IDENTIFICATION NUMBER: 61-1767919ALPHABET1600 AMPITHEATRE PARKWAYPeriod Ending:MOUNTAIN VIEW, C.A., 94043Pay Date:[DRAFT FORM OF TAX OPINION]Taxable Marital Status:
Exemptions/AllowancesZACHRY T.5323Federal:DALLASTX:NO State Income Taxrateunitsyear to dateOther Benefits and112.26746780007569887160000.00%InformationPto BalanceTotal Work HrsGross Pay75698871600Important NotesCOMPANY PH Y: 650-253-0000StatutoryBASIS OF PAY: BASIC/DILUTED EPSFederal Income TaxSocial Security TaxYOUR BASIC/DILUTED EPS RATE HAS BEEN CHANGED FROM 0.001 TO 112.20 PAR SHARE VALUEORIGINAL REPORTMedicare TaxIncome, Rents, & RoyaltyNet Pay7084274386670842743866INCOME STATEMENT61-1767919CHECKING88-1303491Net Check$70,842,743,866.00 GOOGL_income-statement_Quarterly_As_Originally_ReportedTTMQ4 2021Q2 2021Q1 2021Q4 2020Q3 2020Q2 2020Your federal taxable wages this period are $ALPHABET INCOMEAdvice number:Gross Profit$146,698,000,000.00 $42,337,000,000.00 $35,653,000,000.00 $31,211,000,000.00 30818000000$25,056,000,000.00 1974400000000.00%1600 AMPIHTHEATRE PARKWAY MOUNTAIN VIEW CA 94043Pay date:_Total Revenue as Reported, Supplemental$257,637,000,000.00 $75,325,000,000.00 $61,880,000,000.00 $55,314,000,000.00 56898000000$46,173,000,000.00 3829700000000.00%Deposited to the account Ofxxxxxxxx6547$257,637,000,000.00 $75,325,000,000.00 $61,880,000,000.00 $55,314,000,000.00 56898000000$46,173,000,000.00 3829700000000.00%PLEASE READ THE IMPORTANT DISCLOSURES BELOWOther RevenueFEDERAL RESERVE MASTER SUPPLIER ACCOUNT 31000053-052101023 CODCost of Revenue-1.10939E+11-32988000000-26227000000($24,103,000,000.00)-26080000000($21,117,000,000.00)-1855300000000.00%633-44-1725 Zachryiixixiiiwood@gmail.com 47-2041-6547 111000614 31000053Cost of Goods and Services-1.10939E+11-32988000000-26227000000-24103000000-26080000000-21117000000-18553000000PNC Bank PNC Bank Business Tax I.D. Number: 633441725Operating Income/Expenses-67984000000-20452000000-16292000000($14,774,000,000.00)($15,167,000,000.00)-1384300000000.00%($13,361,000,000.00)CIF Department (Online Banking) Checking Account: 47-2041-6547Selling, General and Administrative Expenses-36422000000-11744000000-8617000000-7289000000-8145000000-6987000000-6486000000P7-PFSC-04-F Business Type: Sole Proprietorship/Partnership CorporationGeneral and Administrative Expenses-13510000000-4140000000-3341000000-2773000000-2831000000-2756000000-2585000000500 First Avenue ALPHABETSelling and Marketing Expenses-22912000000-7604000000-5276000000-4516000000-5314000000-4231000000-3901000000Pittsburgh, PA 15219-3128 5323 BRADFORD DRResearch and Development Expenses-31562000000-8708000000-7675000000-7485000000-7022000000-6856000000-6875000000NON-NEGOTIABLE DALLAS TX 75235 8313Total Operating Profit/Loss7871400000021885000000193610000001643700000015651000000112130000006383000000ZACHRY, TYLER, WOODNon-Operating Income/Expenses, Total120200000002517000000262400000048460000003038000000214600000018940000004/18/2022 650-2530-000 469-697-4300Total Net Finance Income/Expense1153000000261000000313000000269000000333000000412000000420000000SIGNATURE Time Zone: Eastern Central Mountain PacificNet Interest Income/Expense1153000000261000000313000000269000000333000000412000000420000000Investment Products  • Not FDIC Insured  • No Bank Guarantee  • May Lose Value"NON-NEGOTIABLEPLEASE READ THE IMPORTANT DISCLOSURES BELOWInterest Expense Net of Capitalized Interest-346000000-117000000-76000000-76000000-53000000-48000000-13000000|Security enhanced document.  See back for detailsNO.Interest Income1499000000378000000389000000345000000386000000460000000433000000|[OBJ][OBJ]PNCBANKNet Investment Income12364000000236400000029240000004869000000353000000019570000001696000000|PNC Bank N.A.7170-2188/719Gain/Loss on Investments and Other Financial Instruments12270000000247800000028830000004751000000326200000020150000001842000000|    DATE____________________________________7364Income from Associates, Joint Ventures and Other Participating Interests3340000004900000092000000500000035500000026000000-54000000|Gain/Loss on Foreign Exchange-240000000-163000000-51000000113000000-87000000-84000000-92000000|PAY TO THEIrregular Income/Expenses00000|ORDER OF_______________________________________________________________________________________________________________|***$**22677000000000&00/100cents||Other Irregular Income/Expenses00000|    Security||Other Income/Expense, Non-Operating-1497000000-108000000-613000000-292000000-825000000-223000000-222000000|______________________________________________________________________________________________________________________DOLLARS [OBJ] Features Pretax Income9073400000024402000000219850000002128300000018689000000133590000008277000000|ESTATE OF                                                                                             DetaileProvision for Income Tax-14701000000-3760000000-3460000000-3353000000-3462000000-2112000000-1318000000|                                                                                                     on Back.Net Income from Continuing Operations7603300000020642000000185250000001793000000015227000000112470000006959000000|FOR_____________________________________Net Income after Extraordinary Items and Discontinued Operations7603300000020642000000185250000001793000000015227000000112470000006959000000|AUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATURE.EXECUTOR/Net Income after Non-Controlling/Minority Interests7603300000020642000000185250000001793000000015227000000112470000006959000000|{}.ADMINISTRATORNet Income Available to Common Stockholders7603300000020642000000185250000001793000000015227000000112470000006959000000|AUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATURE.PERSONAL/Diluted Net Income Available to Common Stockholders7603300000020642000000185250000001793000000015227000000112470000006959000000|{}.REPRESENTATIVEIncome Statement Supplemental Section|AUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATURE.TRUSTEE||Reported Normalized and Operating Income/Expense Supplemental Section|Deposited to the account Of xxxxxxxx6547Total Revenue as Reported, Supplemental2.57637E+11753250000006188000000055314000000568980000004617300000038297000000|PLEASE READ THE IMPORTANT DISCLOSURES BELOWTotal Operating Profit/Loss as Reported, Supplemental7871400000021885000000193610000001643700000015651000000112130000006383000000|Reported Effective Tax Rate0.1620.1570.1580.1580.159|FEDERAL RESERVE MASTER SUPPLIER ACCOUNT 31000053-052101023 CODReported Normalized Income|Reported Normalized Operating Profit|633-44-1725 Zachryiixixiiiwood@gmail.com 47-2041-6547 111000614 31000053Other Adjustments to Net Income Available to Common Stockholders|PNC Bank PNC Bank Business Tax I.D. Number: 633441725Discontinued Operations|CIF Department (Online Banking) Checking Account: 47-2041-6547Basic EPS113.8831.1527.6926.6322.5416.5510.21|P7-PFSC-04-F Business Type: Sole Proprietorship/Partnership CorporationBasic EPS from Continuing Operations113.8831.1227.6926.6322.4616.5510.21|500 First Avenue ALPHABETBasic EPS from Discontinued Operations|Pittsburgh, PA 15219-3128 5323 BRADFORD DRDiluted EPS112.230.6927.2626.2922.316.410.13GOOGL_income-statement_Quarterly_As_Originally_ReportedTTMQ4 2021Q2 2021Q1 2021Q4 2020Q3 2020Q2 2020Diluted EPS from Continuing Operations112.230.6727.2626.2922.2316.410.13Gross Profit$146,698,000,000.00 $42,337,000,000.00 $35,653,000,000.00 $31,211,000,000.00 30818000000$25,056,000,000.00 1974400000000.00%Diluted EPS from Discontinued OperationsTotal Revenue as Reported, Supplemental$257,637,000,000.00 $75,325,000,000.00 $61,880,000,000.00 $55,314,000,000.00 56898000000$46,173,000,000.00 3829700000000.00%Basic Weighted Average Shares Outstanding667650000662664000668958000673220000675581000679449000681768000$257,637,000,000.00 $75,325,000,000.00 $61,880,000,000.00 $55,314,000,000.00 56898000000$46,173,000,000.00 3829700000000.00%Diluted Weighted Average Shares Outstanding677674000672493000679612000682071000682969000685851000687024000Other RevenueReported Normalized Diluted EPSCost of Revenue-1.11E+11-32988000000-26227000000($24,103,000,000.00)-26080000000($21,117,000,000.00)-1855300000000.00%Basic EPS113.8831.1527.6926.6322.5416.5510.21Cost of Goods and Services-1.11E+11-32988000000-26227000000-24103000000-26080000000-21117000000-18553000000Diluted EPS112.230.6927.2626.2922.316.410.13Operating Income/Expenses-67984000000-20452000000-16292000000($14,774,000,000.00)($15,167,000,000.00)-1384300000000.00%($13,361,000,000.00)Basic WASO667650000662664000668958000673220000675581000679449000681768000Selling, General and Administrative Expenses-36422000000-11744000000-8617000000-7289000000-8145000000-6987000000-6486000000Diluted WASO677674000672493000679612000682071000682969000685851000687024000General and Administrative Expenses-13510000000-4140000000-3341000000-2773000000-2831000000-2756000000-2585000000Fiscal year end September 28th., 2022. | USDSelling and Marketing Expenses-22912000000-7604000000-5276000000-4516000000-5314000000-4231000000-3901000000Research and Development Expenses-31562000000-8708000000-7675000000-7485000000-7022000000-6856000000-687500000031622,6:39 PMTotal Operating Profit/Loss7871400000021885000000193610000001643700000015651000000112130000006383000000Morningstar.com Intraday Fundamental Portfolio View Print ReportPrintNon-Operating Income/Expenses, Total12020000000251700000026240000004846000000303800000021460000001894000000Total Net Finance Income/Expense11530000002610000003130000002690000003330000004120000004200000003/6/2022 at 6:37 PMNet Interest Income/Expense1153000000261000000313000000269000000333000000412000000420000000Interest Expense Net of Capitalized Interest-346000000-117000000-76000000-76000000-53000000-48000000-13000000Interest Income1499000000378000000389000000345000000386000000460000000433000000GOOGL_income-statement_Quarterly_As_Originally_ReportedQ4 2021Net Investment Income12364000000236400000029240000004869000000353000000019570000001696000000Cash Flow from Operating Activities, Indirect24934000000Q2 2021Q1 2021Q4 2020Gain/Loss on Investments and Other Financial Instruments12270000000247800000028830000004751000000326200000020150000001842000000Net Cash Flow from Continuing Operating Activities, Indirect24934000000374970000003121100000030818000000Income from Associates, Joint Ventures and Other Participating Interests3340000004900000092000000500000035500000026000000-54000000Cash Generated from Operating Activities24934000000218900000001928900000022677000000Gain/Loss on Foreign Exchange-240000000-163000000-51000000113000000-87000000-84000000-92000000Income/Loss before Non-Cash Adjustment20642000000218900000001928900000022677000000Irregular Income/Expenses00000Total Adjustments for Non-Cash Items6517000000185250000001793000000015227000000Other Irregular Income/Expenses00000Depreciation, Amortization and Depletion, Non-Cash Adjustment3439000000423600000025920000005748000000Other Income/Expense, Non-Operating-1497000000-108000000-613000000-292000000-825000000-223000000-222000000Depreciation and Amortization, Non-Cash Adjustment3439000000294500000027530000003725000000Pretax Income9073400000024402000000219850000002128300000018689000000133590000008277000000Depreciation, Non-Cash Adjustment3215000000294500000027530000003725000000Provision for Income Tax-14701000000-3760000000-3460000000-3353000000-3462000000-2112000000-1318000000Amortization, Non-Cash Adjustment224000000273000000025250000003539000000Net Income from Continuing Operations7603300000020642000000185250000001793000000015227000000112470000006959000000Stock-Based Compensation, Non-Cash Adjustment3954000000215000000228000000186000000Net Income after Extraordinary Items and Discontinued Operations7603300000020642000000185250000001793000000015227000000112470000006959000000Taxes, Non-Cash Adjustment1616000000380300000037450000003223000000Net Income after Non-Controlling/Minority Interests7603300000020642000000185250000001793000000015227000000112470000006959000000Investment Income/Loss, Non-Cash Adjustment-247800000037900000011000000001670000000Net Income Available to Common Stockholders7603300000020642000000185250000001793000000015227000000112470000006959000000Gain/Loss on Financial Instruments, Non-Cash Adjustment-2478000000-2883000000-4751000000-3262000000Diluted Net Income Available to Common Stockholders7603300000020642000000185250000001793000000015227000000112470000006959000000Other Non-Cash Items-14000000-2883000000-4751000000-3262000000Income Statement Supplemental SectionChanges in Operating Capital-2225000000-8000000-255000000392000000Reported Normalized and Operating Income/Expense Supplemental SectionChange in Trade and Other Receivables-5819000000-871000000-12330000001702000000Total Revenue as Reported, Supplemental2.58E+11753250000006188000000055314000000568980000004617300000038297000000Change in Trade/Accounts Receivable-5819000000-36610000002794000000-5445000000Total Operating Profit/Loss as Reported, Supplemental7871400000021885000000193610000001643700000015651000000112130000006383000000Change in Other Current Assets-399000000-36610000002794000000-5445000000Reported Effective Tax Rate0.1620.1570.1580.1580.159Change in Payables and Accrued Expenses6994000000-1990000007000000-738000000Reported Normalized IncomeChange in Trade and Other Payables11570000004074000000-49560000006938000000Reported Normalized Operating ProfitChange in Trade/Accounts Payable1157000000-130000000-982000000963000000Other Adjustments to Net Income Available to Common StockholdersChange in Accrued Expenses5837000000-130000000-982000000963000000Discontinued OperationsChange in Deferred Assets/Liabilities3680000004204000000-39740000005975000000Basic EPS113.8831.1527.6926.6322.5416.5510.21Change in Other Operating Capital-3369000000-3000000137000000207000000Basic EPS from Continuing Operations113.8831.1227.6926.6322.4616.5510.21Change in Prepayments and Deposits-1082000000785000000740000000Basic EPS from Discontinued OperationsCash Flow from Investing Activities-11016000000Diluted EPS112.230.6927.2626.2922.316.410.13Cash Flow from Continuing Investing Activities-11016000000-9074000000-5383000000-7281000000Diluted EPS from Continuing Operations112.230.6727.2626.2922.2316.410.13Purchase/Sale and Disposal of Property, Plant and Equipment, Net-6383000000-9074000000-5383000000-7281000000Diluted EPS from Discontinued OperationsPurchase of Property, Plant and Equipment-6383000000-5496000000-5942000000-5479000000Basic Weighted Average Shares Outstanding667650000662664000668958000673220000675581000679449000681768000Sale and Disposal of Property, Plant and Equipment-5496000000-5942000000-5479000000Diluted Weighted Average Shares Outstanding677674000672493000679612000682071000682969000685851000687024000Purchase/Sale of Business, Net-385000000Reported Normalized Diluted EPSPurchase/Acquisition of Business-385000000-308000000-1666000000-370000000Basic EPS113.8831.1527.6926.6322.5416.5510.21Purchase/Sale of Investments, Net-4348000000-308000000-1666000000-370000000Diluted EPS112.230.6927.2626.2922.316.410.13Purchase of Investments-40860000000-32930000002195000000-1375000000Basic WASO667650000662664000668958000673220000675581000679449000681768000Sale of Investments36512000000-24949000000-37072000000-36955000000Diluted WASO677674000672493000679612000682071000682969000685851000687024000Other Investing Cash Flow100000000216560000003926700000035580000000Fiscal year end September 28th., 2022. | USDPurchase/Sale of Other Non-Current Assets, Net2300000030000000-57000000Sales of Other Non-Current Assets31622,6:39 PMCash Flow from Financing Activities-16511000000Morningstar.com Intraday Fundamental Portfolio View Print ReportPrintCash Flow from Continuing Financing Activities-16511000000-15991000000-13606000000-9270000000Issuance of/Payments for Common Stock, Net-13473000000-15991000000-13606000000-92700000003/6/2022 at 6:37 PMPayments for Common Stock13473000000-12796000000-11395000000-7904000000Proceeds from Issuance of Common Stock-12796000000-11395000000-7904000000Issuance of/Repayments for Debt, Net115000000GOOGL_income-statement_Quarterly_As_Originally_ReportedIssuance of/Repayments for Long Term Debt, Net115000000-1042000000-37000000-57000000Cash Flow from Operating Activities, IndirectQ4 2021Q2 2021Q1 2021Q4 2020Proceeds from Issuance of Long Term Debt6250000000-1042000000-37000000-57000000Net Cash Flow from Continuing Operating Activities, Indirect24934000000374970000003121100000030818000000Repayments for Long Term Debt636500000066990000009000000000Cash Generated from Operating Activities24934000000218900000001928900000022677000000Proceeds from Issuance/Exercising of Stock Options/Warrants2923000000-7741000000-937000000-57000000Income/Loss before Non-Cash Adjustment24934000000218900000001928900000022677000000-2453000000-2184000000-1647000000Total Adjustments for Non-Cash Items20642000000185250000001793000000015227000000Depreciation, Amortization and Depletion, Non-Cash Adjustment6517000000423600000025920000005748000000Other Financing Cash FlowDepreciation and Amortization, Non-Cash Adjustment3439000000294500000027530000003725000000Cash and Cash Equivalents, End of PeriodDepreciation, Non-Cash Adjustment3439000000294500000027530000003725000000Change in Cash030000000010000000338000000000)Amortization, Non-Cash Adjustment3215000000273000000025250000003539000000Effect of Exchange Rate Changes20945000000236300000002662200000026465000000Stock-Based Compensation, Non-Cash Adjustment224000000215000000228000000186000000Cash and Cash Equivalents, Beginning of Period25930000000-31750000003000000006126000000Taxes, Non-Cash Adjustment3954000000380300000037450000003223000000Cash Flow Supplemental Section181000000000)183000000-143000000210000000Investment Income/Loss, Non-Cash Adjustment161600000037900000011000000001670000000Change in Cash as Reported, Supplemental2.3719E+132.6622E+132.6465E+132.0129E+13Gain/Loss on Financial Instruments, Non-Cash Adjustment-2478000000-2883000000-4751000000-3262000000Income Tax Paid, Supplemental2774000000-29920000006336000000Other Non-Cash Items-2478000000-2883000000-4751000000-3262000000Cash and Cash Equivalents, Beginning of Period13412000000-4990000000Changes in Operating Capital-14000000-8000000-255000000392000000Change in Trade and Other Receivables-2225000000-871000000-1233000000170200000012 Months EndedChange in Trade/Accounts Receivable-5819000000-36610000002794000000-5445000000_________________________________________________________Change in Other Current Assets-5819000000-36610000002794000000-5445000000Q4 2019Change in Payables and Accrued Expenses-399000000-1990000007000000-738000000Income StatementChange in Trade and Other Payables69940000004074000000-49560000006938000000USD in "000'"sChange in Trade/Accounts Payable1157000000-130000000-982000000963000000Repayments for Long Term DebtDec. 31, 2019Change in Accrued Expenses1157000000-130000000-982000000963000000Costs and expenses:Change in Deferred Assets/Liabilities58370000004204000000-39740000005975000000Cost of revenues161857Change in Other Operating Capital368000000-3000000137000000207000000Research and developmentChange in Prepayments and Deposits-3369000000-1082000000785000000740000000Sales and marketing71896Cash Flow from Investing ActivitiesGeneral and administrative26018Cash Flow from Continuing Investing Activities-11016000000-9074000000-5383000000-7281000000European Commission fines18464Purchase/Sale and Disposal of Property, Plant and Equipment, Net-11016000000-9074000000-5383000000-7281000000Total costs and expenses9551Purchase of Property, Plant and Equipment-6383000000-5496000000-5942000000-5479000000Income from operations1697Sale and Disposal of Property, Plant and Equipment-6383000000-5496000000-5942000000-5479000000Other income (expense), net127626Purchase/Sale of Business, NetIncome before income taxes34231Purchase/Acquisition of Business-385000000-308000000-1666000000-370000000Provision for income taxes5394Purchase/Sale of Investments, Net-385000000-308000000-1666000000-370000000Net income19289000000Purchase of Investments-4348000000-32930000002195000000-1375000000*include interest paid, capital obligation, and underweighting19289000000Sale of Investments-40860000000-24949000000-37072000000-3695500000019289000000Other Investing Cash Flow36512000000216560000003926700000035580000000Basic net income per share of Class A and B common stock and Class C capital stock (in dollars par share)Purchase/Sale of Other Non-Current Assets, Net1000000002300000030000000-57000000Diluted net income per share of Class A and Class B common stock and Class C capital stock (in dollars par share)Sales of Other Non-Current AssetsCash Flow from Financing ActivitiesCash Flow from Continuing Financing Activities-16511000000-15991000000-13606000000-9270000000For Paperwork Reduction Act Notice, see the seperate Instructions.Issuance of/Payments for Common Stock, Net-16511000000-15991000000-13606000000-9270000000Payments for Common Stock-13473000000-12796000000-11395000000-7904000000Proceeds from Issuance of Common Stock13473000000-12796000000-11395000000-7904000000Issuance of/Repayments for Debt, NetIssuance of/Repayments for Long Term Debt, Net115000000-1042000000-37000000-57000000Proceeds from Issuance of Long Term Debt115000000-1042000000-37000000-57000000Repayments for Long Term Debt625000000066990000009000000000Proceeds from Issuance/Exercising of Stock Options/Warrants6365000000-7741000000-937000000-570000002923000000-2453000000-2184000000-1647000000Other Financing Cash FlowCash and Cash Equivalents, End of PeriodChange in Cash030000000010000000338000000000)Effect of Exchange Rate Changes20945000000236300000002662200000026465000000Cash and Cash Equivalents, Beginning of Period25930000000-31750000003000000006126000000Cash Flow Supplemental Section181000000000)183000000-143000000210000000Change in Cash as Reported, Supplemental2.37E+132.66E+132.65E+132.01E+13Income Tax Paid, Supplemental2774000000-29920000006336000000Cash and Cash Equivalents, Beginning of Period13412000000-499000000012 Months Ended_________________________________________________________Q4 2019Income StatementUSD in "000'"sRepayments for Long Term DebtDec. 31, 2019Costs and expenses:Cost of revenues161857Research and developmentSales and marketing71896General and administrative26018European Commission fines18464Total costs and expenses9551Income from operations1697Other income (expense), net127626Income before income taxes34231Provision for income taxes5394Net income19289000000*include interest paid, capital obligation, and underweighting1928900000019289000000Basic net income per share of Class A and B common stock and Class C capital stock (in dollars par share)Diluted net income per share of Class A and Class B common stock and Class C capital stock (in dollars par share)For Paperwork Reduction Act Notice, see the seperate Instructions.
table 	{mso-displayed-decimal-separator:"\."; 	mso-displayed-thousand-separator:"\,";} tr 	{mso-height-source:auto;} col 	{mso-width-source:auto;} td 	{padding-top:1px; 	padding-right:1px; 	padding-left:1px; 	mso-ignore:padding; 	color:black; 	font-size:11.0pt; 	font-weight:400; 	font-style:normal; 	text-decoration:none; 	font-family:Calibri, sans-serif; 	mso-font-charset:0; 	text-align:general; 	vertical-align:bottom; 	border:none; 	white-space:nowrap; 	mso-rotate:0;} .xl18 	{color:#3A3838; 	font-size:9.0pt; 	font-family:"Courier New"; 	mso-generic-font-family:auto; 	mso-font-charset:0; 	background:white; 	mso-pattern:black none;} .xl19 	{color:#3A3838; 	font-size:9.0pt; 	font-family:"Courier New"; 	mso-generic-font-family:auto; 	mso-font-charset:0; 	text-align:right; 	background:white; 	mso-pattern:black none;} .xl20 	{color:#3A3838; 	font-size:9.0pt; 	font-family:"Courier New"; 	mso-generic-font-family:auto; 	mso-font-charset:0; 	background:white; 	mso-pattern:black none; 	white-space:normal;} .xl21 	{color:#3A3838; 	font-size:9.0pt; 	font-family:"Courier New"; 	mso-generic-font-family:auto; 	mso-font-charset:0; 	text-align:right; 	background:white; 	mso-pattern:black none; 	white-space:normal;} .xl24 	{color:#3A3838; 	font-size:9.0pt; 	font-family:"Courier New"; 	mso-generic-font-family:auto; 	mso-font-charset:0; 	text-align:left; 	vertical-align:top; 	background:white; 	mso-pattern:black none; 	white-space:normal;} .xl27 	{color:#3A3838; 	font-size:9.0pt; 	font-family:"Courier New"; 	mso-generic-font-family:auto; 	mso-font-charset:0; 	text-align:center; 	background:white; 	mso-pattern:black none;} .xl34 	{color:#3A3838; 	font-size:9.0pt; 	font-family:"Courier New"; 	mso-generic-font-family:auto; 	mso-font-charset:0; 	vertical-align:top; 	background:white; 	mso-pattern:black none; 	white-space:normal;} Federal 941 Deposit Report
ADP
Report Range5/4/2022 - 6/4/2022Local ID:EIN:63-3441725State ID: 633441725Employee Number: 3
DescriptionAmount5/4/2022 - 6/4/2022Payment Amount (Total)9.24675E+12Display All1. Social Security (Employee + Employer)26661.82. Medicare (Employee + Employer)8.61193E+11Hourly3. Federal Income Tax8.38556E+122.2663E+15Note: This report is generated based on the payroll data for your reference only. Please contact IRS office for special cases such as late payment, previous overpayment, penalty and others.
Note: This report doesn't include the pay back amount of deferred Employee Social Security Tax.CommissionEmployer Customized Report
ADP
Report Range5/4/2022 - 6/4/202288-1656496state ID: 633441725State: AllLocal ID: 000373055812267700EIN:Customized ReportAmountEmployee Payment Report
ADPEmployee Number: 3
DescriptionWages, Tips and Other Compensation2.2663E+13Report Range:TipsTaxable SS Wages215014.49Name:
SSN:0Taxable SS Tips0Payment SummaryTaxable Medicare Wages2.2663E+13SalaryVacation hourlyOTAdvanced EIC Payment03361013.7Federal Income Tax Withheld8.38556E+12Bonus00Employee SS Tax Withheld13330.90Other Wages 1Other Wages 2Employee Medicare Tax Withheld5.3258E+11Total00State Income Tax Withheld02.2663E+13Local Income Tax Withheld
Customized Employer Tax Report0Deduction SummaryDescriptionAmountHealth InsuranceEmployer SS Tax
Employer Medicare Tax13330.90Federal Unemployment Tax3.28613E+11Tax SummaryState Unemployment Tax441.7Federal Tax7Total TaxCustomized Deduction Report840$8,385,561,229,657@3,330.90Local TaxHealth Insurance0401K0Advanced EIC Payment8.91814E+1200Total401K00Social Security Tax Medicare TaxState Tax$532,580,113,050)SHAREHOLDERS ARE URGED TO READ THE DEFINITIVE PROXY STATEMENT AND ANY OTHER RELEVANT MATERIALS THAT THE COMPANY WILL FILE WITH THE SEC CAREFULLY IN THEIR ENTIRETY WHEN THEY BECOME AVAILABLE. SUCH DOCUMENTS WILL CONTAIN IMPORTANT INFORMATION ABOUT THE COMPANY AND ITS DIRECTORS, OFFICERS AND AFFILIATES. INFORMATION REGARDING THE INTERESTS OF CERTAIN OF THE COMPANY’S DIRECTORS, OFFICERS AND AFFILIATES WILL BE AVAILABLE IN THE DEFINITIVE PROXY STATEMENT.The Definitive Proxy Statement and any other relevant materials that will be filed with the SEC will be available free of charge at the SEC’s website at www.sec.gov. In addition, the Definitive Proxy Statement (when available) and other relevant documents will also be available, without charge, by directing a request by mail to Attn: Investor Relations, Alphabet Inc., 1600 Amphitheatre Parkway, Mountain View, California, 94043 or by contacting investor-relations@abc.xyz. The Definitive Proxy Statement and other relevant documents will also be available on the Company’s Investor Relations website at https://abc.xyz/investor/other/annual-meeting/.The Company and its directors and certain of its executive officers may be consideredno participants in the solicitation of proxies with respect to the proposals under the Definitive Proxy Statement under the rules of the SEC. Additional information regarding the participants in the proxy solicitations and a description of their direct and indirect interests, by security holdings or otherwise, also will be included in the Definitive Proxy Statement and other relevant materials to be filed with the SEC when they become available.9.24675E+123/6/2022 at 6:37 PMQ4 2021Q3 2021Q2 2021Q1 2021Q4 2020GOOGL_income-statement_Quarterly_As_Originally_Reported24934000000255390000003749700000031211000000308180000002493400000025539000000218900000001928900000022677000000Cash Flow from Operating Activities, Indirect2493400000025539000000218900000001928900000022677000000Net Cash Flow from Continuing Operating Activities, Indirect2064200000018936000000185250000001793000000015227000000Cash Generated from Operating Activities65170000003797000000423600000025920000005748000000Income/Loss before Non-Cash Adjustment34390000003304000000294500000027530000003725000000Total Adjustments for Non-Cash Items34390000003304000000294500000027530000003725000000Depreciation, Amortization and Depletion, Non-Cash Adjustment32150000003085000000273000000025250000003539000000Depreciation and Amortization, Non-Cash Adjustment224000000219000000215000000228000000186000000Depreciation, Non-Cash Adjustment39540000003874000000380300000037450000003223000000Amortization, Non-Cash Adjustment1616000000-128700000037900000011000000001670000000Stock-Based Compensation, Non-Cash Adjustment-2478000000-2158000000-2883000000-4751000000-3262000000Taxes, Non-Cash Adjustment-2478000000-2158000000-2883000000-4751000000-3262000000Investment Income/Loss, Non-Cash Adjustment-1400000064000000-8000000-255000000392000000Gain/Loss on Financial Instruments, Non-Cash Adjustment-22250000002806000000-871000000-12330000001702000000Other Non-Cash Items-5819000000-2409000000-36610000002794000000-5445000000Changes in Operating Capital-5819000000-2409000000-36610000002794000000-5445000000Change in Trade and Other Receivables-399000000-1255000000-1990000007000000-738000000Change in Trade/Accounts Receivable699400000031570000004074000000-49560000006938000000Change in Other Current Assets1157000000238000000-130000000-982000000963000000Change in Payables and Accrued Expenses1157000000238000000-130000000-982000000963000000Change in Trade and Other Payables583700000029190000004204000000-39740000005975000000Change in Trade/Accounts Payable368000000272000000-3000000137000000207000000Change in Accrued Expenses-33690000003041000000-1082000000785000000740000000Change in Deferred Assets/LiabilitiesChange in Other Operating Capital-11016000000-10050000000-9074000000-5383000000-7281000000Change in Prepayments and Deposits-11016000000-10050000000-9074000000-5383000000-7281000000Cash Flow from Investing ActivitiesCash Flow from Continuing Investing Activities-6383000000-6819000000-5496000000-5942000000-5479000000-6383000000-6819000000-5496000000-5942000000-5479000000Purchase/Sale and Disposal of Property, Plant and Equipment, NetPurchase of Property, Plant and Equipment-385000000-259000000-308000000-1666000000-370000000Sale and Disposal of Property, Plant and Equipment-385000000-259000000-308000000-1666000000-3700000000Purchase/Sale of Business, Net-4348000000-3360000000-32930000002195000000-1375000000Purchase/Acquisition of Business-40860000000-35153000000-24949000000-37072000000-36955000000Purchase/Sale of Investments, NetPurchase of Investments36512000000317930000002165600000039267000000355800000001000000003880000002300000030000000-57000000Sale of InvestmentsOther Investing Cash Flow-15254000000Purchase/Sale of Other Non-Current Assets, Net-16511000000-15254000000-15991000000-13606000000-9270000000Sales of Other Non-Current Assets-16511000000-12610000000-15991000000-13606000000-9270000000Cash Flow from Financing Activities-13473000000-12610000000-12796000000-11395000000-7904000000Cash Flow from Continuing Financing Activities13473000000-12796000000-11395000000-7904000000Issuance of/Payments for Common 343 sec cvxvxvcclpddf wearsStock, Net-42000000Payments for Common Stock115000000-42000000-1042000000-37000000-57000000Proceeds from Issuance of Common Stock1150000006350000000-1042000000-37000000-57000000Issuance of/Repayments for Debt, Net6250000000-639200000066990000009000000000Issuance of/Repayments for Long Term Debt, Net6365000000-2602000000-7741000000-937000000-57000000Proceeds from Issuance of Long Term DebtRepayments for Long Term Debt2923000000-2453000000-2184000000-1647000000Proceeds from Issuance/Exercising of Stock Options/Warrants0300000000100000003.38E+11Other Financing Cash FlowCash and Cash Equivalents, End of PeriodChange in Cash2094500000023719000000236300000002662200000026465000000Effect of Exchange Rate Changes25930000000)235000000000)-31750000003000000006126000000Cash and Cash Equivalents, Beginning of PeriodPAGE="$USD(181000000000)".XLSBRIN="$USD(146000000000)".XLS183000000-143000000210000000Cash Flow Supplemental Section2.3719E+132.6622E+132.6465E+132.0129E+13Change in Cash as Reported, Supplemental277400000089000000-29920000006336000000Income Tax Paid, Supplemental13412000000157000000ZACHRY T WOOD-4990000000Cash and Cash Equivalents, Beginning of PeriodDepartment of the TreasuryInternal Revenue ServiceQ4 2020Q4  2019Calendar YearDue: 04/18/2022Dec. 31, 2020Dec. 31, 2019USD in "000'"sRepayments for Long Term Debt182527161857Costs and expenses:Cost of revenues8473271896Research and development2757326018Sales and marketing1794618464General and administrative110529551European Commission fines01697Total costs and expenses141303127626Income from operations4122434231Other income (expense), net68580000005394Income before income taxes2267700000019289000000Provision for income taxes2267700000019289000000Net income2267700000019289000000*include interest paid, capital obligation, and underweightingBasic net income per share of Class A and B common stock and Class C capital stock (in dollars par share)Diluted net income per share of Class A and Class B common stock and Class C capital stock (in dollars par share)*include interest paid, capital obligation, and underweightingBasic net income per share of Class A and B common stock and Class C capital stock (in dollars par share)Diluted net income per share of Class A and Class B common stock and Class C capital stock (in dollars par share)20210418RateUnitsTotalYTDTaxes / DeductionsCurrentYTD--7084274500070842745000Federal Withholding00FICA - Social Security08853.6FICA - Medicare00Employer TaxesFUTA00SUTA00EIN: 61-1767919ID : 00037305581 SSN: 633441725Gross70842745000Earnings StatementTaxes / DeductionsStub Number: 10Net PaySSNPay SchedulePay PeriodSep 28, 2022 to Sep 29, 2023Pay Date4/18/202270842745000XXX-XX-1725AnnuallyCHECK NUMBERINTERNAL REVENUE SERVICE,PO BOX 1214,CHARLOTTE, NC 28201-1214ZACHRY WOOD157603300000020642000000189360000001852500000017930000000152270000001124700000069590000006836000000106710000007068000000For Disclosure, Privacy Act, and Paperwork Reduction Act Notice, see separate instructions.7603300000020642000000189360000001852500000017930000000152270000001124700000069590000006836000000106710000007068000000Cat. No. 11320B7603300000020642000000189360000001852500000017930000000152270000001124700000069590000006836000000106710000007068000000Form 1040 (2021)760330000002064200000018936000000Reported Normalized and Operating Income/Expense Supplemental SectionTotal Revenue as Reported, Supplemental2.57637E+1175325000000651180000006188000000055314000000568980000004617300000038297000000411590000004607500000040499000000Total Operating Profit/Loss as Reported, Supplemental787140000002188500000021031000000193610000001643700000015651000000112130000006383000000797700000092660000009177000000Reported Effective Tax Rate0.160.1790.1570.1580.1580.1590.1190.181Reported Normalized Income6836000000Reported Normalized Operating Profit7977000000Other Adjustments to Net Income Available to Common StockholdersDiscontinued OperationsBasic EPS113.8831.1528.4427.6926.6322.5416.5510.219.9615.4910.2Basic EPS from Continuing Operations113.8831.1228.4427.6926.6322.4616.5510.219.9615.4710.2Basic EPS from Discontinued OperationsDiluted EPS112.230.6927.9927.2626.2922.316.410.139.8715.3510.12Diluted EPS from Continuing Operations112.230.6727.9927.2626.2922.2316.410.139.8715.3310.12Diluted EPS from Discontinued OperationsBasic Weighted Average Shares Outstanding667650000662664000665758000668958000673220000675581000679449000681768000686465000688804000692741000Diluted Weighted Average Shares Outstanding677674000672493000676519000679612000682071000682969000685851000687024000692267000695193000698199000Reported Normalized Diluted EPS9.87Basic EPS113.8831.1528.4427.6926.6322.5416.5510.219.9615.4910.21Diluted EPS112.230.6927.9927.2626.2922.316.410.139.8715.3510.12Basic WASO667650000662664000665758000668958000673220000675581000679449000681768000686465000688804000692741000Diluted WASO677674000672493000676519000679612000682071000682969000685851000687024000692267000695193000698199000Fiscal year end September 28th., 2022. | USDFor Paperwork Reduction Act Notice, see the seperate Instructions.important informationDescriptionRestated Certificate of Incorporation of PayPal Holdings, Inc.(incorporated by reference to Exhibit  3.01 to PayPal Holdings, Inc.'sQuarterly Report on Form 10-Q, as filed with the Commission onJuly 27, 2017).Amended and Restated Bylaws of PayPal Holdings, Inc. (incorporatedby reference to Exhibit  3.1 to PayPal Holdings, Inc.'s Current Reporton Form 8-K, as filed with the Commission on January 18, 2019).Opinion of Faegre Drinker Biddle & Reath LLP.Consent of PricewaterhouseCoopers LLP, Independent Registered PublicAccounting Firm.Consent of Faegre Drinker Biddle & Reath LLP (included inExhibit 5.1 to this Registration Statement).Power of Attorney (included on the signature page of thisRegistration Statement).All of Us Financial Inc. 2021 Equity Incentive Plan.Filing Fee Table.Business Checking
For 24-hour account information, sign on topnc.com/mybusiness/
Business Checking Account number: 47-2041-6547 - continuedActivity DetailDeposits and Other AdditionsACH AdditionsDate postedAmount Transaction descriptionFor the period 04/13/2022 to 04/29/2022
ZACHRY TYLER WOOD
Primary account number: 47-2041-6547 Page 2 of 34467862.5Reverse Corporate ACH Debit
Effective 04-26-22Reference numberChecks and Other Deductions2.21169E+13DeductionsReference numberDate postedAmount Transaction description2.21169E+134467762.5Corporate ACH Quickbooks 180041ntuit 1940868Reference numberService Charges and Fees2.21169E+13Date postedAmount Transaction descriptionon your next statement as a single line item entitled Service
Waived - New Customer Period4467836Returned Item Fee (nsf)Detail of Services Used During Current PeriodNote: The total charge for the following services will be posted to your account on 05/02/2022 and will appear on your next statement a Charge Period Ending 04/29/2022,DescriptionVolumeAmountAccount Maintenance Charge708467438660        Total For Services Used This Peiiod00Total Service (harge00
0Reviewing Your Statement('PNCBANKPlease review this statement carefully and reconcile it with your records. Call the telephone number on the upper right side of the first page of this statement if:
you have any questions regarding your account(s); your name or address is incorrect;
• you have any questions regarding interest paid to an interest-bearing account.ÉBalancing Your Account
Update Your Account RegisterCertified Copy of Resolutionsl
Authorizations For Accounts And Loans@PNCBANK(Corporations, Partnerships, Unincorporated Associations, Sole Proprietorships & Other Organizations)step 2: Add together checks and other deductions listed in your account register but not on your statement.PNC Bank, National Association ("Bank")Taxpayer I.D. Number (TIN)C'eck
Deduction Descretio•Anount(iv)
(v)account or benefit, or in payment of the individual obligations of, any individual obligations of any such persons to the Bank without regard to the disposition or purpose of same as allowed by applicable law.D pNCBANKIn addition but not by way of limitation, the Bank may take checks, drafts or other items payable to "cash", the Bank or the Customer, and pay the sums represented by such Items in cash to any person presenting such items or credit such Items to the account or obligations of any person presenting such items or any other person or entity as directed by any such person.Products and Services. Resolved that any of the persons listed in Section 3 above are authorized to enter into contracts and agreements, written or verbal, for any products or services now or in the future offered by the Bank, including but not limited to (i) cash management services, (ii) purchases or sales of foreign exchange, securities or other financial products, (iii) computer/internet-based products and services, (iv) wire transfer of funds from or to the accounts of the Customer at the Bank, and (v) ACH transactions, and the Bank may charge any accounts of the Customer at the Bank for such products or services.5Taxpayer I.D. Number (TIN)OWNER("Customer")633-44-1725are hereby authorized (i) to effect loans, advances and renewals at any time for the Customer from the Bank; (ii) to sign and deliver any notes (with or without warrant of attorney to confess judgment) and evidences of indebtedness of the Customer; (iii) to request the Bank to issue letters of credit and to sign and deliver to the bank any agreements on behalf of the Customer to reimburse the Bank for all payments made and expenses incurred by it under such letters of credit and drafts drawn pursuant thereto; (iv) to sign and deliver any instruments or documents on behalf of the Customer guaranteeing, endorsing or securing the payment of any debts or obligations of any person, form or corporation to the Bank; (v) to pledge, assign, transfer, mortgage, grant a security interest in or otherwise hypothecate to the Bank any stock, securities, commercial paper, warehouse receipts and other documents of title, bills, accounts receivable, contract rights, inventory, equipment, real property, and any other investments or property of the Customer, real or personal, tangible or intangible as security for the payment of any and all loans, advances, indebtedness and other liabilities of the Customer to the Bank of every kind and description, direct or indirect, absolute and contingent, joint or several, whether as drawer, maker, endorsee, guarantor, surety or otherwise, and to execute on behalf of the Customer mortgages, pledges, security agreements, financing statements and other instruments or documents in connection therewith; and (vi) to sell or discount with the Bank any commercial paper, bills and other instruments and evidence of indebtedness, warehouse receipts and other documents of title, accounts, accounts receivable, contract rights, and other assets, tangible and intangible, at any time held by the Customer and for such purpose to endorse, assign, transfer and deliver the same to the Bank.6Revolving Credits. Resolved that in connection with any extension of credit obtained by any of the persons authorized in Section 5 above, that permit the Customer to effect multiple advances or draws under such credit, any of the persons listed in Sections 5 (Loans and Extensions of Credit) and 3 (Withdrawals and Endorsements)Resolution for ALPHABET7Telephonic and Facsimile Requests. Resolved that the Bank is authorized to take any action authorized hereunder based upon (i) the telephone request of any person purporting to be a person authorized to act hereunder, (ii) the signature of any person authorized to act hereunder that is delivered to the Bank by facsimile transmission, or (iii) the telex originated by any of such persons, tested in accordance with such testing:Tr
R
•d
Mingor serVlCö n lent services, (ii) purchases or sales of foreig xlll) computerfinternet-based products and services, (iv) wir he Customer at the Bank, and (v) ACH transactions, and the Ba the Bank for such products or services.
It. Resolved that any one of the following:procedures as may be established between the Customer and the Bank from time to time.
General. Resolved that a certified copy of these resolutions be delivered to the Bank; that the persons specified herein are vested with authority to act and may designate successor persons to act on behalf of Customer8without further authority from the Customer or governing body; and that Bank may rely on the authority given by this resolution until actual receipt by the Bank of a certified copy of a new resolution modifying or revoking the/Customer Copy, page 2 of 49Withdrawals and Transfers. Resolved that the Bank is authorized to make payments from the account(s) ofCustomer according to any check, draft, bill of exchange, acceptance or other written instrument or direction signed by any one of the following individuals, officers or designated agents, and that such designated individuals may also otherwise transfer, or enter into agreements with Bank concerning the transfer, of funds from Customer's account(s), whether by telephone, telegraph, computer or any other manner:Column1Column2Loans and Extensions of Credit. Resolved that any one of the following:45999-0023Date of this notice: 44658Employer Identification Number: 88-1656496Form: SS-4Number of this notice: CP 575 AFor assistance you may call us at:1-800-829-493375235IF YOU WRITE, ATTACH THE
STUB AT THE BD OF THIS NOTICE.We assigned youThis EIN will identify you, your business accounts, tax returns, andWE ASSIGNED YOU AN EMPLOYER IDENTIFICATION NUMBER
Thank you for applying for an Employer Identification Number (EIN) . EIN 88-1656496. If the information isPleaseb6.35-for the tax period(s) in question, please file the return (s) showing you have no liabilities .
If you have questions about at the the forms address or the shown due at dates the top shown, of you this can notice. call us If atyou the phone number or write to us Publication 538,
need help in determining your annual accounting period (tax year) , see Accounting Periods and Methods.8Total Year to Date3,Total for this PeriodOverdraft and Returned Item Fee Summary363618Total Returned Item Fees (NSF)t ly ofItemsAmountChecks and Other Deductions
DescriptionItemsAmount162.5ACH Deductions162.5heDeposits and Other Additions
DescriptionService Charges and Fees136ACH Additions162.5Total298.5DateLedger balanceDateLedger balanceTotalDaily Balance(27962.50-4467836DateLedger balance*You'202Alphabet Inc Class C GOOGotm corresti2814TM 27.8414.76%6350053.:202Fair Value Estimate2160gro550ovrConsider Buying PriceConsider Selling PriceFair Value Uncertainty
Economic Moat
Stewardship Grade02-01-2022 1 by Ali MogharabiBusiness Strategy & Outlook 02-01-2022Analyst Digest 1 633-44-1725 10-15-94 Portfolio April 04,2022 - April 03,2022Berkshire Hathaway Inc Class A BRK.A525000527760$0.001 0.00%367500Fair Value EstimateConsider Buying Price$708,750.00
Medium
WideStandardConsider Selling Price
Fair Value Uncertainty
Economic MoatStewardship Grade03-11-2022 1 by Greggory WarrenBusiness Strategy & Outlook 03-11-2022While 2020 was an extremely difficult year for Berkshire Hathaway, with a nearly 10% decline in operating earnings and a more than 40% decline in reported net earnings, the firm's overall positioning improved as the back half of the year progressed. The firm saw an even more marked improvement in its insurance investment portfolio, as well as the operating results of its various subsidiaries, last year. As such, we expect 2022 and 2023 to be a return to more normalized levels of revenue growth and profitability (albeit with inflation impacting results in the first half of this year).We continue to view Berkshire's decentralized business model, broad business diversification, high cash-generation capabilities, and unmatched balance sheet strength as true differentiators. While these advantages have been overshadowed by an ever-expanding cash balance-ANhich is earning next to nothing in a near-zero interest-rate environment--we believe the company has finally hit a nexus where it is far more focused on reducing its cash hoard through stock and bond investments and share repurchases. During the past eight calendar quarters, theWhen filing tax documents,ING  payments, or replying to any related correspondence,it is very important that you use your EIN and complete name and address exactly as shown above. Any variation may cause a delay in processing, result in incorrect information inyour account, or even cause you to be assigned more than one EIN. If the information isnot correct as shown above, please make the correction using the attached tear-off stub and return it to us .
Based on the information received from you or your representative, you must file the following forms by the dates shown.We assigned you44658Form 94044658Form 94344658If the information isForm 106544658Form 72044658Your Form 2290 becomes due the month after your vehicle is put into use .
Your Form 1 IC and/or 730 becomes due the month after your wagering starts .
After our review of your information, we have determined that you have not filedtax returns for the above-mentioned tax period (s) dating as far back as 2007.Plea Sfile your return(s) by 04/22/2022.If there is a balance due on the return (s)penalties and interest will continue to accumulate from the due date of the return (s)until it is filed and paid. If you were not in business or did not hire any employeesfor the tax period(s) in question, please file the return (s) showing you have no liabilities .
If you have questions about the forms or the due dates shown, you can call us atPIthe phone number or write to us at the address shown at the top of this notice. If youneed help in determining your annual accounting period (tax year) , see Publication 538, Accounting Periods and Methods.Business Checking
PNCBANK@PNCBANKFor the period 04/13/2022Primary account number: 47-2041-6547 Page 1 of 35/19/23021022462Q 304Number of enclosures: 0ZACHRY TYLER WOOD ALPHABET
5323 BRADFORD DR
DALLAS TX 75235-8314For 24-hour banking sign on to
PNC Bank Online Banking on pnc.com
FREE Online Bill Pay
For customer service call 1-877-BUS-BNKG
PNC accepts Telecommunications Relay Service (TRS) calls.91.11E+62Para servicio en espalol, 1877.BUS-BNKC,
Moving? Please contact your local branch.
@ Write to: Customer Service PO Box 609
Pittsburgh , PA 15230-9738
Visit us at PNC.com/smaIIbusinessIMPORTANT INFORMATION FOR BUSINESS DEPOSIT CUSTOMERSDate of this notice: Effective February 18,2022, PNC will be temporarily waiving fees for statement, check image, deposit ticket and deposited item copy requests until further notice. Statement, check image, deposit ticket and deposited Item requests will continue to be displayed in the Details of Services Used section of your monthly statement. We will notify you via statement message prior to reinstating these fees.
If vou have any questions, you may reach out to your business banker branch or call us at 1-877-BUS-BNKG (1-877-287-2654).44658Business Checking Summary
Account number; 47-2041-6547
Overdraft Protection has not been established for this account. Please contact us if you would like to set up this service.Zachry Tyler Wood AlphabetEmployer Identification Number: 88-1656496Balance SummaryChecks and other deductionsEnding balanceForm: SS-4Beginning balanceDeposits and other additionsNumber of this notice: CP 575 A0=98.50 Average ledger balance36.00-
Average collected balanceFor assistance you may call ug at:6.35-6.35-1-800-829-4933Overdraft and Returned Item Fee SummaryTotal Year to DateTotal for this PeriodTotal Returned Item Fees (NSF)3636IF YOU WRITE, ATTATCHA TYE
STUB AT OYE END OF THIS NOTICE.Deposits and Other Additions
DescriptionItemsAmountChecks and Other Deductions
DescriptionItemsAmountACH Additions162.5ACH Deductions162.5We assigned youService Charges and Fees136Total162.5Total298.5Daily BalanceDateDateLedger balanceIf the information isDateLedger balanceLedger balance4466404467762.50-4467836Form 94044658Berkshire Hatha,a,n..Business CheckingFor the period 04/13/2022  to 04/29/202244680For 24-hour account information, sign on to pnc.com/mybusiness/ZACHRY TYLER WOODPrimary account number: 47-2041-6547 Page 2 of 3PleaseBusiness Checking Account number: 47-2041-6547 - continuedPage 2 of 3Acüvity DetailDeposits and Other Additionsdid not hire any employeeACH AdditionsReferenc numbDate posted 04/27Transaction 
Amount description
62.50  Reverse Corporate ACH Debit
Effective 04-26-22the due dates shown, you can call us at2.21169E+13If youChecks and Other DeductionsACH DeductionsReferencDate postedTransaction
Amount descriptionnumber4/26/202270842743866Corporate ACH Quickbooks 180041ntuit 19408682.21169E+13ervice Charges and FeesReferencDate postedTransaction
Amount descripton27-Apr2.21169E+13numbDetail of Services Used During Current Period2.21169E+13 ::NOTE:: The total charge for the following services will be posted to your account on 05/02/2022 and will appear on your next statement as a single line item entitled Service Charge Period Ending 04/29/2022.e: The total charge for the following Penod Ending 04/29/2022.Service Charge descriptionAmountAccount Maintenance Charge$62.50Total For Services Used This Period$36.00Total Service Charge$98.50Waived - Waived - New Customer PeriodReviewing Your Statement
of this statement if:
you have any questions regarding your account(s); your name or address is incorrect; you have any questions regarding interest paid to an interest-bearing account.PNCBANKBalancing Your Account
Update Your Account RegisterVolumeCompare:The activity detail section of your statement to your account register.Check Off: 
Add to Your Account Register: Balance:
Subtract From Your Account Register  Balance:All items in your account register that also appear on your statement. Remember to begin with the ending date of your last statement. (An asterisk { * } will appear in the Checks section if there is a gap in the listing of consecutive check numbers.)
Any deposits or additions including interest payments and ATM or electronic deposits listed on the statement that are not already entered in your register.
Any account deductions including fees and ATM or electronic deductions listed on the statement that are not already entered in your register.Your Statement Information : step 2: Add together checks and other deductions listed in your account register but not on your statement.AmountCheck
Deduction DescrptionAmountBalancing Your Account
Update Your Account Register-on :deposit=$B=+A: 22934637118600.00](usd)'"'4720416547Reviewing Your Statement
of this statement if:
you have any questions regarding your account(s); your name or address is incorrect; you have any questions regarding interest paid to an interest-bearing account.Total A=$22934637118600Step 3:$22,934,637,118,600 Enter the ending balance recorded on your statementAdd deposits and other additions not recordedTotal A + $22934637118600Subtotal=$22934637118600Subtract checks and other deductions not recorded Total B$2.29346E+13The result should equal your account register balance$2.29346E+13Total B22934637118600Verification of Direct DepositsTo verify whether a direct deposit or other transfer to your account has occurred, call us Monday - Friday: 7 AM - 10 PM ET and Saturday & Sunday: 8 AM - 5 PM ET at the customer service number listed on the upper right side of the first page of this statement.In Case of Errors or Questions About Your Electronic Transfers
Telephone us at the customer service number listed on the upper right side of the first page of this statement or write us at PNC Bank Debit Card Services, 500 First Avenue, 4th Floor, Mailstop P7-PFSC-04-M, Pittsburgh, PA 15219 as soon as you can, if you think your statement or receipt is wrong or if you need more information about a transfer on the statement or receipt. We must hear from you no later than 60 days after we sent you the FIRST statement on which the error or problem appeared.
Tell us your name and account number (if any).
Describe the error or the transfer you are unsure about, and explain as clearly as you can why you believe it is an error or why you need more information.
Tell us the dollar amount of the suspected error.
We will investigate your complaint and will correct any error promptly. If we take longer than 10 business days, we will provisionally credit your account for the amount you think is in error, so that you will have use of the money during the time it Cakes us to complete our investigation.
EquaLHousing LenderMember FDIC

	Security enhanced document. See back for details				NO.																					Interest Income	1499000000	378000000	389000000	345000000	386000000	460000000	433000000	#NAME?	1499000000	378000000	389000000	345000000	386000000	460000000	433000000																																																																																																																																																																																										|	[OBJ][OBJ]PNCBANK																									Net Investment Income	12364000000	2364000000	2924000000	4869000000	3530000000	1957000000	1696000000	#NAME?	12364000000	2364000000	2924000000	4869000000	3530000000	1957000000	1696000000																																																																																																																																																																																										|		PNC Bank N.A.	71													70-2188/719										Gain/Loss on Investments and Other Financial Instruments	12270000000	2478000000	2883000000	4751000000	3262000000	2015000000	1842000000	#NAME?	12270000000	2478000000	2883000000	4751000000	3262000000	2015000000	1842000000																																																																																																																																																																																										|										 			DATE____________________________________7364													Income from Associates, Joint Ventures and Other Participating Interests	334000000	49000000	92000000	5000000	355000000	26000000	-54000000	#NAME?	334000000	49000000	92000000	5000000	355000000	26000000	-54000000																																																																																																																																																																																										|																										Gain/Loss on Foreign Exchange	-240000000	-163000000	-51000000	113000000	-87000000	-84000000	-92000000	#NAME?	-240000000	-163000000	-51000000	113000000	-87000000	-84000000	-92000000																																																																																																																																																																																										|PAY TO THE																										Irregular Income/Expenses	0	0			0	0	0	#NAME?	0	0			0	0	0																																																																																																																																																																																										|ORDER OF_______________________________________________________________________________________________________________|***$**22677000000000&00/100cents||																										Other Irregular Income/Expenses	0	0			0	0	0	#NAME?	0	0			0	0	0																																																																																																																																																																																										|																 Security||										Other Income/Expense, Non-Operating	-1497000000	-108000000	-613000000	-292000000	-825000000	-223000000	-222000000	#NAME?	-1497000000	-108000000	-613000000	-292000000	-825000000	-223000000	-222000000																																																																																																																																																																																										|______________________________________________________________________________________________________________________DOLLARS [OBJ] Features 																										Pretax Income	90734000000	24402000000	21985000000	21283000000	18689000000	13359000000	8277000000	#NAME?	90734000000	24402000000	21985000000	21283000000	18689000000	13359000000	8277000000																																																																																																																																																																																										|ESTATE OF															 Detaile											Provision for Income Tax	-14701000000	-3760000000	-3460000000	-3353000000	-3462000000	-2112000000	-1318000000	#NAME?	-14701000000	-3760000000	-3460000000	-3353000000	-3462000000	-2112000000	-1318000000																																																																																																																																																																																										|																 on Back.										Net Income from Continuing Operations	76033000000	20642000000	18525000000	17930000000	15227000000	11247000000	6959000000	#NAME?	76033000000	20642000000	18525000000	17930000000	15227000000	11247000000	6959000000																																																																																																																																																																																										|FOR_____________________________________																										Net Income after Extraordinary Items and Discontinued Operations	76033000000	20642000000	18525000000	17930000000	15227000000	11247000000	6959000000	#NAME?	76033000000	20642000000	18525000000	17930000000	15227000000	11247000000	6959000000																																																																																																																																																																																										|AUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATURE.EXECUTOR/																										Net Income after Non-Controlling/Minority Interests	76033000000	20642000000	18525000000	17930000000	15227000000	11247000000	6959000000	#NAME?	76033000000	20642000000	18525000000	17930000000	15227000000	11247000000	6959000000																																																																																																																																																																																										|{														}.ADMINISTRATOR												Net Income Available to Common Stockholders	76033000000	20642000000	18525000000	17930000000	15227000000	11247000000	6959000000	#NAME?	76033000000	20642000000	18525000000	17930000000	15227000000	11247000000	6959000000																																																																																																																																																																																										|AUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATURE.PERSONAL/																										Diluted Net Income Available to Common Stockholders	76033000000	20642000000	18525000000	17930000000	15227000000	11247000000	6959000000	#NAME?	76033000000	20642000000	18525000000	17930000000	15227000000	11247000000	6959000000																																																																																																																																																																																										|{														}.REPRESENTATIVE												Income Statement Supplemental Section								#NAME?																																																																																																																																																																																																	|AUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATURE.TRUSTEE||																										Reported Normalized and Operating Income/Expense Supplemental Section								#NAME?																																																																																																																																																																																																	|Deposited to the account Of xxxxxxxx6547																										Total Revenue as Reported, Supplemental	2.57637E+11	75325000000	61880000000	55314000000	56898000000	46173000000	38297000000	#NAME?	2.58E+11	75325000000	61880000000	55314000000	56898000000	46173000000	38297000000																																																																																																																																																																																										|PLEASE READ THE IMPORTANT DISCLOSURES BELOW																										Total Operating Profit/Loss as Reported, Supplemental	78714000000	21885000000	19361000000	16437000000	15651000000	11213000000	6383000000	#NAME?	78714000000	21885000000	19361000000	16437000000	15651000000	11213000000	6383000000																																																																																																																																																																																										|																										Reported Effective Tax Rate	0.162		0.157	0.158		0.158	0.159	#NAME?	0.162		0.157	0.158		0.158	0.159																																																																																																																																																																																										|FEDERAL RESERVE MASTER SUPPLIER ACCOUNT 31000053-052101023 COD																										Reported Normalized Income								#NAME?																																																																																																																																																																																																	|																										Reported Normalized Operating Profit								#NAME?																																																																																																																																																																																																	|633-44-1725 Zachryiixixiiiwood@gmail.com 47-2041-6547 111000614 31000053																										Other Adjustments to Net Income Available to Common Stockholders								#NAME?																																																																																																																																																																																																	|PNC Bank PNC Bank Business Tax I.D. Number: 633441725																										Discontinued Operations								#NAME?																																																																																																																																																																																																	|CIF Department (Online Banking) Checking Account: 47-2041-6547																										Basic EPS	113.88	31.15	27.69	26.63	22.54	16.55	10.21	WOOD.,	113.88	31.15	27.69	26.63	22.54	16.55	10.21																																																																																																																																																																																										|P7-PFSC-04-F Business Type: Sole Proprietorship/Partnership Corporation																										Basic EPS from Continuing Operations	113.88	31.12	27.69	26.63	22.46	16.55	10.21	S.R.	113.88	31.12	27.69	26.63	22.46	16.55	10.21																																																																																																																																																																																										|500 First Avenue ALPHABET																										Basic EPS from Discontinued Operations								ZACHRY																																																																																																																																																																																																	|Pittsburgh, PA 15219-3128 5323 BRADFORD DR																										Diluted EPS	112.2	30.69	27.26	26.29	22.3	16.4	10.13  112.2	30.69	27.26	26.29	22.3	16.4	10.13																																																																																																																																																																																										GOOGL_income-statement_Quarterly_As_Originally_Reported	TTM	Q4 2021	Q2 2021	Q1 2021	Q4 2020	Q3 2020	Q2 2020																			Diluted EPS from Continuing Operations	112.2	30.67	27.26	26.29	22.23	16.4	10.13	#NAME?	112.2	30.67	27.26	26.29	22.23	16.4	10.13																																																																																																																																																																																										Gross Profit	$146,698,000,000.00 	$42,337,000,000.00 	$35,653,000,000.00 	$31,211,000,000.00 	30818000000	$25,056,000,000.0				Your federal taxable wages this period are $									Your federal taxable wages this period are $								
Purchase/Acquisition of Business			-385000000	-259000000	-308000000	-1666000000	-370000000											USD in "000'"s									Purchase/Acquisition of Business		-1010700000	-1148400000	-1286100000	-1423800000	-1561500000		
TX:			NO State Income Tax				ZACHRY T. WOOD											TX:							Earnings Statement		TX:		NO State Incorne Tax						
																		Total Revenue as Reported, Supplemental	-13385163636	-25484018182	-37582872727	-49681727273	-61780581818	-73879436364	-85978290909										
Gain/Loss on Investments and Other Financial Instruments		12270000000	2478000000	2158000000	2883000000	4751000000	3262000000	2015000000	1842000000	-802000000	399000000	-1479000000	-2243490909					Total Revenue as Reported, Supplemental	-13385163636	-25484018182	-37582872727	-49681727273	-61780581818	-73879436364	-85978290909		Gain/Loss on Investments and Other Financial Instruments	-2243490909	-3068572727	-3893654545	-4718736364	-5543818182	-6368900000	-7193981818	-8019063636
Income from Associates, Joint Ventures and Other Participating Interests		334000000	49000000	188000000	92000000	5000000	355000000	26000000	-54000000	74000000	460000000	-14000000	99054545					Total Operating Profit/Loss as Reported, Supplemental	-10077918182	-14337036364	-18596154545	-22855272727	-27114390909	-31373509091	-35632627273		Income from Associates, Joint Ventures and Other Participating Interests	99054545	92609091	86163636	79718182	73272727	66827273	60381818	53936364
Employee Identification Number: 	61-1767919																	Total Operating Profit/Loss	-10077918182	-14337036364	-18596154545	-22855272727	-27114390909	-31373509091	-35632627273		INCOME STATEMENT 	61-1767920							
		TTM	Q4 2021	Q3 2021	Q2 2021	Q1 2021	Q4 2020	Q3 2020	Q2 2020	Q1 2020	Q4 2019	Q3 2019	TTM					Total Net Finance Income/Expense	462390909	460290909	458190909	456090909	453990909	451890909	449790909		GOOGL_income-statement_Quarterly_As_Originally_Reported	TTM	Q4 2022	Q3 2022	Q2 2022	Q1 2022	Q4 2021	Q3 2021	Q2 2021
Cash Flow from Continuing Financing Activities			-16511000000	-15254000000	-15991000000	-13606000000	-9270000000											Total costs and expenses		11053			09552				Cash Flow from Continuing Financing Activities		-9287400000	-7674400000	-6061400000	-4448400000	-2835400000		
Diluted EPS from Discontinued Operations																		Total Adjustments for Non-Negotiable Cash Items	21353400000	21992600000	23634000000	25275400000	26916800000				Diluted EPS from Discontinued Operations								
The U.S. Internal Revenue Code of 1986, as amended, the Treasury Regulations promulgated thereunder, published pronouncements of the Internal Revenue Service, which may be cited or used as precedents, and case law, any of which may be changed at any time with retroactive effect.  No opinion is expressed on any matters other than those specifically referred to above.																		The U.S. Internal Revenue Code of 1986, as amended, the Treasury Regulations promulgated thereunder, published pronouncements of the Internal Revenue Service, which may be cited or used as precedents, and case law, any of which may be changed at any time with retroactive effect.  No opinion is expressed on any matters other than those specifically referred to above.									The U.S. Internal Revenue Code of 1986, as amended, the Treasury Regulations promulgated thereunder, published pronouncements of the Internal Revenue Service, which may be cited or used as precedents, and case law, any of which may be changed at any time with retroactive effect.  No opinion is expressed on any matters other than those specifically referred to above.								
Basic WASO		667650000	662664000	665758000	668958000	673220000	675581000	679449000	681768000	686465000	688804000	692741000	694313546					Taxes, Non-Cash Adjustment	-1297700000	4486200000	4794700000	5103200000	5411700000				Basic WASO	694313546	697258864	700204182	703149500	706094818	709040136	711985455	714930773
"Taxable Marital Status: 
Exemptions/Allowances"				00001								WOOD						"Taxable Marital Status: 
Exemptions/Allowances"		Married							"Taxable Marital Status: 
Exemptions/Allowances"			Single					ZACHRY T. 
Diluted EPS		00112	00031	00028	00027	00026	00022	00016	00010	00010	00015	00010	-00009					Stock-Based Compensation, Non-Cash Adjustment	4241600000	-2050400000	-2803100000	-3555800000	-4308500000				Diluted EPS	-00009	-00015	-00021	-00027	-00033	-00039	-00045	-00051
DALLAs, TX 75235-8313	"Bonus
Training"							        	and Other Benefits 					00000	75698871600		"Bonus
Training"	Statutory						        	Total Work Hrs	"Bonus
Training"								        	Total Work Hrs
"PLEASE READ THE IMPORTANT DISCLOSURES BELOW

FEDERAL RESERVE MASTER SUPPLIER ACCOUNT31000053-052101023COD
633-44-1725Zachryiixixiiiwood@gmail.com47-2041-654711100061431000053
PNC BankPNC Bank Business Tax I.D. Number: 633441725
CIF Department (Online Banking)Checking Account: 47-2041-6547
P7-PFSC-04-FBusiness Type: Sole Proprietorship/Partnership Corporation
500 First AvenueALPHABET
Pittsburgh, PA 15219-31285323 BRADFORD DR
NON-NEGOTIABLEDALLAS TX 75235 8313
ZACHRY, TYLER, WOOD
4/18/2022650-2530-000 469-697-4300
SIGNATURETime Zone: Eastern Central Mountain Pacific
Investment Products  • Not FDIC Insured  • No Bank Guarantee  • May Lose Value"									Information									Social Security Tax							COMPANY PH Y: 650-253-0001										COMPANY PH Y: 650-253-0001
5323 BRADFORD DR																		Selling, General and Administrative Expenses	-28945455	1494309091	3017563636	4540818182	6064072727	7587327273	9110581818		5324 BRADFORD DR								
ORIGINAL REPORT																		Selling and Marketing Expenses	-52145455	902963636	1858072727	2813181818	3768290909	4723400000	5678509091		ORIGINAL REPORT								
Change in Trade/Accounts Receivable			-5819000000	-2409000000	-3661000000	2794000000	-5445000000											Sales of Other Non-Current Assets	-13997000000	-12740000000	-1288666667	-885666667	-482666667				Change in Trade/Accounts Receivable		-1122700000	-527600000	67500000	662600000	1257700000		
Purchase/Sale of Other Non-Current Assets, Net				388000000	23000000	30000000	-57000000											Sales and marketing		84733			71897				Purchase/Sale of Other Non-Current Assets, Net			-236000000	-368800000	-501600000	-634400000		
Other Non-Cash Items			-14000000	-2158000000	-2883000000	-4751000000	-3262000000											Sale of Investments	49209400000	-79064600000	-93949900000	-108835200000	-123720500000				Other Non-Cash Items		-5340300000	-6249200000	-7158100000	-8067000000	-8975900000		
Amortization, Non-Cash Adjustment			224000000	3085000000	2730000000	2525000000	3539000000											Sale and Disposal of Property, Plant and Equipment	-5218300000	-5040500000	-4683100000	-4325700000	-3968300000				Amortization, Non-Cash Adjustment		4241600000	4848600000	5455600000	6062600000	6669600000		
																		Research and Development Expenses	-853500000	381363636	1616227273	2851090909	4085954545	5320818182	6555681818		Income, Rents, & Royalty								
Other Investing Cash Flow			100000000	31793000000	21656000000	39267000000	35580000000											Research and development									Other Investing Cash Flow		49209400000	57052800000	64896200000	72739600000	80583000000		
Other Irregular Income/Expenses		00000	00000				00000	00000	00000	00000	00000	00000	00000					Reported Normalized Operating Profit									Other Irregular Income/Expenses	00000	00000				00000	00000	00000
Irregular Income/Expenses		00000	00000				00000	00000	00000	00000	00000	00000	00000					Reported Normalized Income									Irregular Income/Expenses	00000	00000				00000	00000	00000
Total Revenue as Reported, Supplemental		257637000000	75325000000	65118000000	61880000000	55314000000	56898000000	46173000000	38297000000	41159000000	46075000000	40499000000	-1286309091					Reported Normalized Diluted EPS									Total Revenue as Reported, Supplemental	-1286309091	-13385163636	-25484018182	-37582872727	-49681727273	-61780581818	-73879436364	-85978290909
Net Investment Income		12364000000	2364000000	2207000000	2924000000	4869000000	3530000000	1957000000	1696000000	-809000000	899000000	-1452000000	-2096781818					Reported Normalized and Operating Income/Expense Supplemental Section									Net Investment Income	-2096781818	-2909109091	-3721436364	-4533763636	-5346090909	-6158418182	-6970745455	-7783072727
Gain/Loss on Foreign Exchange		-240000000	-163000000	-139000000	-51000000	113000000	-87000000	-84000000	-92000000	-81000000	40000000	41000000	47654545					Reported Effective Tax Rate		00000	00000	00000		00000	00000		Gain/Loss on Foreign Exchange	47654545	66854545	86054545	105254546	124454546	143654546	162854546	182054546
Cash Flow from Investing Activities			-11016000000															Repayments for Long Term Debt									Cash Flow from Investing Activities		-11015999999						
Purchase/Sale of Investments, Net			-4348000000	-259000000	-308000000	-1666000000	-370000000											Repayments for Long Term Debt		Dec. 31, 2021			Dec. 31, 2020				Purchase/Sale of Investments, Net		574500000	1229400000	1884300000	2539200000	3194100000		
Purchase/Sale of Business, Net			-385000000															rents', recirpt', and Royalty'									Purchase/Sale of Business, Net		-384999999						
Basic EPS from Continuing Operations		00114	00031	00028	00028	00027	00022	00017	00010	00010	00015	00010	-00009					realized gain/cost as reported supplemental	22809500000000	22375000000000	21940500000000	21506000000000	22677000000000		Print		Basic EPS from Continuing Operations	-00009	-00015	-00021	-00027	-00034	-00040	-00046	-00052
Change in Trade and Other Receivables			-5819000000	2806000000	-871000000	-1233000000	1702000000											Purchase/Sale of Other Non-Current Assets, Net	-384999999	-236000000	-368800000	-501600000	-634400000				Change in Trade and Other Receivables		2617900000	3718200000	4818500000	5918800000	7019100000		
Investment Income/Loss, Non-Cash Adjustment			-2478000000	-1287000000	379000000	1100000000	1670000000											Purchase/Sale of Investments, Net	16018900000	1229400000	1884300000	2539200000	3194100000				Investment Income/Loss, Non-Cash Adjustment		3081700000	4150000000	5218300000	6286600000	7354900000		
Stock-Based Compensation, Non-Cash Adjustment			3954000000	219000000	215000000	228000000	186000000											Purchase/Sale of Business, Net									Stock-Based Compensation, Non-Cash Adjustment		-1297700000	-2050400000	-2803100000	-3555800000	-4308500000		
Depreciation and Amortization, Non-Cash Adjustment			3439000000	3304000000	2945000000	2753000000	3725000000											Purchase/Sale and Disposal of Property, Plant and Equipment, Net	-4919700000	-6485800000	-6198700000	-5911600000	-5624500000				Depreciation and Amortization, Non-Cash Adjustment		3239500000	3241600000	3243700000	3245800000	3247900000		
Taxes, Non-Cash Adjustment			1616000000	3874000000	3803000000	3745000000	3223000000											Purchase/Acquisition of Business	-1010700000	-1148400000	-1286100000	-1423800000	-1561500000				Taxes, Non-Cash Adjustment		4177700000	4486200000	4794700000	5103200000	5411700000		
Depreciation, Non-Cash Adjustment			3215000000	3304000000	2945000000	2753000000	3725000000											Purchase of Property, Plant and Equipment	-6772900000	-4949800000	-4681300000	-4412800000	-4144300000				Depreciation, Non-Cash Adjustment		3329100000	3376000000	3422900000	3469800000	3516700000		
Gain/Loss on Financial Instruments, Non-Cash Adjustment			-2478000000	-2158000000	-2883000000	-4751000000	-3262000000											Purchase of Investments	574500000	24471400000	32923900000	41376400000	49828900000				Gain/Loss on Financial Instruments, Non-Cash Adjustment		-4354700000	-4770800000	-5186900000	-5603000000	-6019100000		
Issuance of/Repayments for Debt, Net			115000000	-42000000														Provision for income taxes		6858000001			05395				Issuance of/Repayments for Debt, Net		-199000000	-356000000					
Total Operating Profit/Loss		78714000000	21885000000	21031000000	19361000000	16437000000	15651000000	11213000000	6383000000	7977000000	9266000000	9177000000	-5818800000					Provision for Income Tax	2565754545	3436290909	4306827273	5177363636	6047900000	6918436364	7788972727		Total Operating Profit/Loss	-5818800000	-10077918182	-14337036364	-18596154545	-22855272727	-27114390909	-31373509091	-35632627273
Cash Flow from Continuing Investing Activities			-11016000000	-10050000000	-9074000000	-5383000000	-7281000000											Proceeds from Issuance/Exercising of Stock Options/Warrants									Cash Flow from Continuing Investing Activities		-4919700000	-3706000000	-2492300000	-1278600000	-64900000		
Change in Prepayments and Deposits				3041000000	-1082000000	785000000	740000000											Proceeds from Issuance of Long Term Debt	-4689300000		-1204600000	-1748400000	-2292200000				Change in Prepayments and Deposits			-388000000	-891600000	-1395200000	-1898800000		
Change in Accrued Expenses			5837000000	238000000	-130000000	-982000000	963000000											Proceeds from Issuance of Common Stock	-3407500000	-348200000	-5806333333	-3360333333	-914333333				Change in Accrued Expenses		-2105200000	-3202000000	-4298800000	-5395600000	-6492400000		
Research and Development Expenses		-31562000000	-8708000000	-7694000000	-7675000000	-7485000000	-7022000000	-6856000000	-6875000000	-6820000000	-7222000000	-6554000000	-2088363636					Pretax Income	-12156918182	-17125854545	-22094790909	-27063727273	-32032663636	-37001600000	-41970536364		Research and Development Expenses	-2088363636	-853500000	381363636	1616227273	2851090909	4085954545	5320818182	6555681818
																70842743866		"PLEASE READ THE IMPORTANT DISCLOSURES BELOW

FEDERAL RESERVE MASTER SUPPLIER ACCOUNT31000053-052101023COD
633-44-1725Zachryiixixiiiwood@gmail.com47-2041-654711100061431000053
PNC BankPNC Bank Business Tax I.D. Number: 633441725
CIF Department (Online Banking)Checking Account: 47-2041-6547
P7-PFSC-04-FBusiness Type: Sole Proprietorship/Partnership Corporation
500 First AvenueALPHABET
Pittsburgh, PA 15219-31285323 BRADFORD DR
NON-NEGOTIABLEDALLAS TX 75235 8313
ZACHRY, TYLER, WOOD
4/18/2022650-2530-000 469-697-4300
SIGNATURETime Zone: Eastern Central Mountain Pacific
Investment Products  • Not FDIC Insured  • No Bank Guarantee  • May Lose Value"									"PLEASE READ THE IMPORTANT DISCLOSURES BELOW

FEDERAL RESERVE MASTER SUPPLIER ACCOUNT31000053-052101023COD
633-44-1725Zachryiixixiiiwood@gmail.com47-2041-654711100061431000053
PNC BankPNC Bank Business Tax I.D. Number: 633441725
CIF Department (Online Banking)Checking Account: 47-2041-6547
P7-PFSC-04-FBusiness Type: Sole Proprietorship/Partnership Corporation
500 First AvenueALPHABET
Pittsburgh, PA 15219-31285323 BRADFORD DR
NON-NEGOTIABLEDALLAS TX 75235 8313
ZACHRY, TYLER, WOOD
4/18/2022650-2530-000 469-697-4300
SIGNATURETime Zone: Eastern Central Mountain Pacific
Investment Products  • Not FDIC Insured  • No Bank Guarantee  • May Lose Value"								
PLEASE READ THE IMPORTANT DISCLOSURES BELOW																		PLEASE READ THE IMPORTANT DISCLOSURES BELOW									PLEASE READ THE IMPORTANT DISCLOSURES BELOW								
Change in Trade/Accounts Payable			1157000000	238000000	-130000000	-982000000	963000000											Payments for Common Stock	-314300000	-356000000	-27015900000	-31169800000	-35323700000				Change in Trade/Accounts Payable		-233200000	-394000000	-554800000	-715600000	-876400000		
														00001				Other Revenue																	
																		Other Non-Cash Items	-4354700000	-6249200000	-7158100000	-8067000000	-8975900000												
General and Administrative Expenses		-13510000000	-4140000000	-3256000000	-3341000000	-2773000000	-2831000000	-2756000000	-2585000000	-2880000000	-2829000000	-2591000000	-544945455					Other Irregular Income/Expenses	00000				00000	00000	00000		General and Administrative Expenses	-544945455	23200000	591345455	1159490909	1727636364	2295781818	2863927273	3432072727
Changes in Operating Capital			-2225000000	64000000	-8000000	-255000000	392000000											Other Investing Cash Flow	-64179300000	57052800000	64896200000	72739600000	80583000000				Changes in Operating Capital		1068100000	1559600000	2051100000	2542600000	3034100000		
Selling and Marketing Expenses		-22912000000	-7604000000	-5516000000	-5276000000	-4516000000	-5314000000	-4231000000	-3901000000	-4500000000	-5738000000	-4609000000	-1007254545					Other Income/Expense, Non-Operating	367718182	472327273	576936364	681545455	786154546	890763636	995372727		Selling and Marketing Expenses	-1007254545	-52145455	902963636	1858072727	2813181818	3768290909	4723400000	5678509091
Payments for Common Stock			13473000000	-12610000000	-12796000000	-11395000000	-7904000000											Other income (expense), net		141304			127627				Payments for Common Stock		-18708100000	-22862000000	-27015900000	-31169800000	-35323700000		
Proceeds from Issuance of Long Term Debt			6250000000	6350000000	-1042000000	-37000000	-57000000											Other Financing Cash Flow		22677000001			19289000001				Proceeds from Issuance of Long Term Debt		-3407500000	-5307600000	-7207700000	-9107800000	-11007900000		
Other Income/Expense, Non-Operating		-1497000000	-108000000	-484000000	-613000000	-292000000	-825000000	-223000000	-222000000	24000000	-65000000	295000000	263109091					Other Adjustments to Net Income Available to Common Stockholders									Other Income/Expense, Non-Operating	263109091	367718182	472327273	576936364	681545455	786154546	890763636	995372727
ZACHRY T WOOD																		Operating Income/Expenses	-882445455	1875672727	4633790909	7391909091	10150027273	12908145455	15666263636		ZACHRY T WOOD								
Federal Employer Identification Number:	88-1303491												9999999999					Non-Operating Income/Expenses, Total	-2079000000	-2788818182	-3498636364	-4208454545	-4918272727	-5628090909	-6337909091			88-1303492							
Statutory	Deductions								_________________								Deductions	NO State Income Tax							BASIS OF PAY: BASIC/DILUTED EPS	Deductions	Statutory								BASIS OF PAY: BASIC/DILUTED EPS
net, pay.			70842743866		70842743866													Net Pay	70842743867		70842743867						Net Pay		70842743867		70842743867				
Other Revenue												6428000000						Net Investment Income	-2909109091	-3721436364	-4533763636	-5346090909	-6158418182	-6970745455	-7783072727		Other Revenue								
																		Net Interest Income/Expense	462390909	460290909	458190909	456090909	453990909	451890909	449790909										
Non-Operating Income/Expenses, Total		12020000000	2517000000	2033000000	2624000000	4846000000	3038000000	2146000000	1894000000	-220000000	1438000000	-549000000	-1369181818					Net Income from Continuing Operations	-9591163636	-13689563636	-17787963636	-21886363636	-25984763636	-30083163636	-34181563636		Non-Operating Income/Expenses, Total	-1369181818	-2079000000	-2788818182	-3498636364	-4208454545	-4918272727	-5628090909	-6337909091
																		Net Income Available to Common Stockholders	-9591163636	-13689563636	-17787963636	-21886363636	-25984763636	-30083163636	-34181563636										
Net Interest Income/Expense		1153000000	261000000	310000000	313000000	269000000	333000000	412000000	420000000	565000000	604000000	608000000	464490909					Net Income after Non-Controlling/Minority Interests	-9591163636	-13689563636	-17787963636	-21886363636	-25984763636	-30083163636	-34181563636		Net Interest Income/Expense	464490909	462390909	460290909	458190909	456090909	453990909	451890909	449790909
Total Net Finance Income/Expense		1153000000	261000000	310000000	313000000	269000000	333000000	412000000	420000000	565000000	604000000	608000000	464490909					Net Income after Extraordinary Items and Discontinued Operations	-9591163636	-13689563636	-17787963636	-21886363636	-25984763636	-30083163636	-34181563636		Total Net Finance Income/Expense	464490909	462390909	460290909	458190909	456090909	453990909	451890909	449790909
Issuance of/Repayments for Long Term Debt, Net			115000000	-42000000	-1042000000	-37000000	-57000000											Net income		22677000001			19289000001				Issuance of/Repayments for Long Term Debt, Net		-314300000	-348200000	-382100000	-416000000	-449900000		
Net Check			70842743866		        													Net Check	70842743867		        						Net Check		70842743867		        				
Basic EPS from Discontinued Operations																		Net Cash Flow from Continuing Operating Activities, Indirect	24934000001	36975800000	38719800000	40463800000	42207800000				Basic EPS from Discontinued Operations								
MOUNTAIN VIEW, C.A., 94043							Earnings Statement					1/30/2022						MOUNTAIN VIEW, C.A., 94044							Pay Date:		MOUNTAIN VIEW, C.A., 94044								Pay Date:
Medicare Tax					        			        										Medicare Tax			        			        			Medicare Tax				        			        	
Change in Other Operating Capital			-3369000000	272000000	-3000000	137000000	207000000											Issuance of/Repayments for Long Term Debt, Net	-2971300000	-660800000	-7207700000	-9107800000	-11007900000				Change in Other Operating Capital		1553900000	2255600000	2957300000	3659000000	4360700000		
Change in Deferred Assets/Liabilities			368000000	2919000000	4204000000	-3974000000	5975000000											Issuance of/Repayments for Debt, Net	-117000000	-5307600000	-382100000	-416000000	-449900000				Change in Deferred Assets/Liabilities		3194700000	3626800000	4058900000	4491000000	4923100000		
Change in Trade and Other Payables			1157000000	3157000000	4074000000	-4956000000	6938000000											Issuance of/Payments for Common Stock, Net	-199000000	-22862000000	-9285000000	-8544000000	-7803000000				Change in Trade and Other Payables		3108700000	3453600000	3798500000	4143400000	4488300000		
Selling, General and Administrative Expenses		-36422000000	-11744000000	-8772000000	-8617000000	-7289000000	-8145000000	-6987000000	-6486000000	-7380000000	-8567000000	-7200000000	-1552200000					Irregular Income/Expenses	00000				00000	00000	00000		Selling, General and Administrative Expenses	-1552200000	-28945455	1494309091	3017563636	4540818182	6064072727	7587327273	9110581818
Diluted WASO		677674000	672493000	676519000	679612000	682071000	682969000	685851000	687024000	692267000	695193000	698199000	698675982					Investment Income/Loss, Non-Cash Adjustment	4177700000	4150000000	5218300000	6286600000	7354900000				Diluted WASO	698675982	701033009	703390036	705747064	708104091	710461118	712818146	715175173
		257637000000	75325000000	65118000000	61880000000	55314000000	56898000000	46173000000	38297000000	41159000000	64133000000	34071000000	1957800000					Interest Income	392490909	369145455	345800000	322454546	299109091	275763636	252418182			1957800000	-9776581818	-21510963636	-33245345455	-44979727273	-56714109091	-68448490909	-80182872727
Total Revenue as Reported, Supplemental		257637000000	75325000000	65118000000	61880000000	55314000000	56898000000	46173000000	38297000000	41159000000	46075000000	40499000000	-1286309091					Interest Expense Net of Capitalized Interest	69900000	91145455	112390909	133636364	154881818	176127273	197372727		Total Revenue as Reported, Supplemental	-1286309091	-13385163636	-25484018182	-37582872727	-49681727273	-61780581818	-73879436364	-85978290909
Diluted EPS from Continuing Operations		00112	00031	00028	00027	00026	00022	00016	00010	00010	00015	00010	-00009					Income/Loss before Non-Negotiable Cash Adjustment	19636600000	21135400000	20917400000	20699400000	20481400000				Diluted EPS from Continuing Operations	-00009	-00015	-00021	-00027	-00033	-00039	-00045	-00051
Change in Cash			00000		300000000	10000000	338000000000)											Income Tax Paid, Supplemental	-13098000000	-26353000000	-280000000	338000000000	-4989999999				Change in Cash		00001		-280000000	-570000000	338000000000)		
Sale and Disposal of Property, Plant and Equipment				-6819000000	-5496000000	-5942000000	-5479000000											INCOME STATMENT		Q4 2021			Q4  2020				Sale and Disposal of Property, Plant and Equipment			-5040500000	-4683100000	-4325700000	-3968300000		
Interest Income		1499000000	378000000	387000000	389000000	345000000	386000000	460000000	433000000	586000000	621000000	631000000	415836364					Income Statement Supplemental Section									Interest Income	415836364	392490909	369145455	345800000	322454546	299109091	275763636	252418182
Issuance of/Payments for Common Stock, Net			-13473000000	-12610000000	-15991000000	-13606000000	-9270000000											Income from operations		00001			01698				Issuance of/Payments for Common Stock, Net		-10767000000	-10026000000	-9285000000	-8544000000	-7803000000		
Cost of Goods and Services		-110939000000	-32988000000	-27621000000	-26227000000	-24103000000	-26080000000	-21117000000	-18553000000	-18982000000	-21020000000	-17568000000	-891927273					Income from Associates, Joint Ventures and Other Participating Interests	92609091	86163636	79718182	73272727	66827273	60381818	53936364		Cost of Goods and Services	-891927273	4189690909	9271309091	14352927273	19434545455	24516163636	29597781818	34679400000
Proceeds from Issuance of Common Stock					-12796000000	-11395000000	-7904000000											Income before income taxes		41225			34232				Proceeds from Issuance of Common Stock				-5806333333	-3360333333	-914333333		
ZACH T  WOO	Regular	$112.20	674678000					75698871600					1349355888	this period	total to date		Regular	Gross Pay	2024033776					75698871601	Information	Regular		1349355888	2024033776					75698871601	Information
																		GOOGL_income-statement_Quarterly_As_Originally_Reported	Q4 2022	Q3 2022	Q2 2022	Q1 2022	Q4 2021	Q3 2021	Q2 2021										
DALLAS TX 75235-8314																		General and Administrative Expenses	23200000	591345455	1159490909	1727636364	2295781818	2863927273	3432072727		DALLAS TX 75235-8315								
Sales of Other Non-Current Assets																		General and administrative		27574			26019				Sales of Other Non-Current Assets								
Cost of Revenue		-110939000000	-32988000000	-27621000000	-26227000000	-24103000000	-26080000000	-21117000000	-18553000000	-18982000000	-21020000000	-17568000000	-891927273					Gain/Loss on Investments and Other Financial Instruments	-3068572727	-3893654545	-4718736364	-5543818182	-6368900000	-7193981818	-8019063636		Cost of Revenue	-891927273	4189690909	9271309091	14352927273	19434545455	24516163636	29597781818	34679400000
Operating Income/Expenses		-67984000000	-20452000000	-16466000000	-16292000000	-14774000000	-15167000000	-13843000000	-13361000000	-14200000000	-15789000000	-13754000000	-3640563636					Gain/Loss on Foreign Exchange	66854545	86054545	105254546	124454546	143654546	162854546	182054546		Operating Income/Expenses	-3640563636	-882445455	1875672727	4633790909	7391909091	10150027273	12908145455	15666263636
Fiscal year end September 28th., 2022. | USD																		Gain/Loss on Financial Instruments, Non-Cash Adjustment	3081700000	-4770800000	-5186900000	-5603000000	-6019100000				Fiscal year end September 28th., 2022. | USD								
Cash and Cash Equivalents, Beginning of Period			13412000000	157000000			-4990000000											For Paperwork Reduction Act Notice, see the seperate Instructions.									Cash and Cash Equivalents, Beginning of Period		-13098000000	-26353000000			-4989999999		
Other Adjustments to Net Income Available to Common Stockholders																		Fiscal years' ending's in September 29th., 2021. | USD									Other Adjustments to Net Income Available to Common Stockholders								
Federal:							Period Ending:											Federal:									Federal:								
Gross Pay		75698871600						        	Important Notes				75698871601					Federal Income Tax						        	Important Notes		Gross Pay	75698871601						        	Important Notes
Cash Flow from Financing Activities			-16511000000	-15254000000														European Commission fines		17947			18465				Cash Flow from Financing Activities		-13997000000	-12740000000					
EMPLOYER IDENTIFICATION NUMBER:       61-1767919																		EMPLOYER IDENTIFICATION NUMBER:       61-1767920									EMPLOYER IDENTIFICATION NUMBER:       61-1767920								
					-2453000000	-2184000000	-1647000000											Effect of Exchange Rate Changes	25930000001	235000000000	10384666667	15035166667	19685666667								-1288666667	-885666667	-482666667		
Pretax Income		90734000000	24402000000	23064000000	21985000000	21283000000	18689000000	13359000000	8277000000	7757000000	10704000000	8628000000	-7187981818					Discontinued Operations									Pretax Income	-7187981818	-12156918182	-17125854545	-22094790909	-27063727273	-32032663636	-37001600000	-41970536364
Reported Normalized and Operating Income/Expense Supplemental Section																		Diluted Weighted Average Shares Outstanding	701033009	703390036	705747064	708104091	710461118	712818146	715175173		Reported Normalized and Operating Income/Expense Supplemental Section								
Reported Normalized Operating Profit										7977000000								Diluted WASO	701033009	703390036	705747064	708104091	710461118	712818146	715175173		Reported Normalized Operating Profit								
Cash Flow Supplemental Section			181000000000)	-146000000000)	183000000	-143000000	210000000											Diluted net income per share of Class A and Class B common stock and Class C capital stock (in dollars par share)									Cash Flow Supplemental Section		181000000000)	-146000000000)	110333333	123833333	137333333		
Interest Expense Net of Capitalized Interest		-346000000	-117000000	-77000000	-76000000	-76000000	-53000000	-48000000	-13000000	-21000000	-17000000	-23000000	48654545					Diluted Net Income Available to Common Stockholders	-9591163636	-13689563636	-17787963636	-21886363636	-25984763636	-30083163636	-34181563636		Interest Expense Net of Capitalized Interest	48654545	69900000	91145455	112390909	133636364	154881818	176127273	197372727
Diluted Net Income Available to Common Stockholders		76033000000	20642000000	18936000000	18525000000	17930000000	15227000000	11247000000	6959000000	6836000000	10671000000	7068000000	-5492763636					Diluted EPS from Discontinued Operations									Diluted Net Income Available to Common Stockholders	-5492763636	-9591163636	-13689563636	-17787963636	-21886363636	-25984763636	-30083163636	-34181563636
Net Income Available to Common Stockholders		76033000000	20642000000	18936000000	18525000000	17930000000	15227000000	11247000000	6959000000	6836000000	10671000000	7068000000	-5492763636					Diluted EPS from Continuing Operations	-00015	-00021	-00027	-00033	-00039	-00045	-00051		Net Income Available to Common Stockholders	-5492763636	-9591163636	-13689563636	-17787963636	-21886363636	-25984763636	-30083163636	-34181563636
Net Income after Non-Controlling/Minority Interests		76033000000	20642000000	18936000000	18525000000	17930000000	15227000000	11247000000	6959000000	6836000000	10671000000	7068000000	-5492763636					Diluted EPS	-00015	-00021	-00027	-00033	-00039	-00045	-00051		Net Income after Non-Controlling/Minority Interests	-5492763636	-9591163636	-13689563636	-17787963636	-21886363636	-25984763636	-30083163636	-34181563636
Reported Effective Tax Rate		00000		00000	00000	00000		00000	00000	00000		00000	00001					Diluted EPS	-00015	-00021	-00027	-00033	-00039	-00045	-00051		Reported Effective Tax Rate	00001		00000	00000	00000		00000	00000
Reported Normalized Diluted EPS										00010								Depreciation, Non-Cash Adjustment	3239500000	3376000000	3422900000	3469800000	3516700000				Reported Normalized Diluted EPS								
Basic Weighted Average Shares Outstanding		667650000	662664000	665758000	668958000	673220000	675581000	679449000	681768000	686465000	688804000	692741000	694313546					Depreciation, Amortization and Depletion, Non-Cash Adjustment	20351200000	5327600000	5668900000	6010200000	6351500000				Basic Weighted Average Shares Outstanding	694313546	697258864	700204182	703149500	706094818	709040136	711985455	714930773
Diluted Weighted Average Shares Outstanding		677674000	672493000	676519000	679612000	682071000	682969000	685851000	687024000	692267000	695193000	698199000	698675982					Depreciation and Amortization, Non-Cash Adjustment	4986300000	3241600000	3243700000	3245800000	3247900000				Diluted Weighted Average Shares Outstanding	698675982	701033009	703390036	705747064	708104091	710461118	712818146	715175173
Deposited to the account Of: 071921891-47204165507									xxxxxxxx6547			transit ABA				amount		Deposited to the account Of									Deposited to the account Of								xxxxxxxx6548
Purchase of Investments			-40860000000	-3360000000	-3293000000	2195000000	-1375000000											Costs and expenses:									Purchase of Investments		16018900000	24471400000	32923900000	41376400000	49828900000		
Sale of Investments			36512000000	-35153000000	-24949000000	-37072000000	-36955000000											Cost of revenues		182528			161858				Sale of Investments		-64179300000	-79064600000	-93949900000	-108835200000	-123720500000		
																		Cost of Revenue	4189690909	9271309091	14352927273	19434545455	24516163636	29597781818	34679400000										
ALPHABET																		Cost of Goods and Services	4189690909	9271309091	14352927273	19434545455	24516163636	29597781818	34679400000		ALPHABET								
					        													CHECKING			        						CHECKING				        				
31622,6:39 PM																		Changes in Operating Capital	-5340300000	1559600000	2051100000	2542600000	3034100000				31622,6:39 PM								
																		Change in Trade/Accounts Receivable	2617900000	-527600000	67500000	662600000	1257700000												
GOOGL_income-statement_Quarterly_As_Originally_Reported			Q4 2021															Change in Trade/Accounts Payable	3108700000	-394000000	-554800000	-715600000	-876400000				GOOGL_income-statement_Quarterly_As_Originally_Reported		Q4 2022						
Morningstar.com Intraday Fundamental Portfolio View Print Report									Press									Change in Trade and Other Receivables	1068100000	3718200000	4818500000	5918800000	7019100000				Morningstar.com Intraday Fundamental Portfolio View Print Report								Print
																		Change in Trade and Other Payables	-3298800000	3453600000	3798500000	4143400000	4488300000												
Income/Loss before Non-Cash Adjustment			20642000000	25539000000	21890000000	19289000000	22677000000											Change in Prepayments and Deposits	1553900000	-388000000	-891600000	-1395200000	-1898800000				Income/Loss before Non-Cash Adjustment		21353400000	21135400000	20917400000	20699400000	20481400000		
																		Change in Payables and Accrued Expenses	-3290700000	-4719000000	-6139200000	-7559400000	-8979600000												
Cash Generated from Operating Activities			24934000000	25539000000	21890000000	19289000000	22677000000											Change in Other Operating Capital	3194700000	2255600000	2957300000	3659000000	4360700000				Cash Generated from Operating Activities		19636600000	18560200000	17483800000	16407400000	15331000000		
3/6/2022 at 6:37 PM													Print					Change in Other Current Assets	-1122700000	-3779600000	-4268500000	-4757400000	-5246300000				3/6/2022 at 6:37 PM								
Net Cash Flow from Continuing Operating Activities, Indirect			24934000000	25539000000	37497000000	31211000000	30818000000											Change in Deferred Assets/Liabilities	-2105200000	3626800000	4058900000	4491000000	4923100000				Net Cash Flow from Continuing Operating Activities, Indirect		35231800000	36975800000	38719800000	40463800000	42207800000		
Cash and Cash Equivalents, End of Period																		Change in Cash as Reported, Supplemental	-5809000000	-8692000000	-11575000000	-570000000	6336000001				Cash and Cash Equivalents, End of Period								
Proceeds from Issuance/Exercising of Stock Options/Warrants			2923000000	-2602000000	-7741000000	-937000000	-57000000											Change in Cash	28459100000	29853400000	31247700000	32642000000	34036300000				Proceeds from Issuance/Exercising of Stock Options/Warrants		-2971300000	-3400800000	-3830300000	-4259800000	-4689300000		
Cash Flow from Operating Activities, Indirect			24934000000	Q3 2021	Q2 2021	Q1 2021	Q4 2020											Change in Accrued Expenses	-233200000	-3202000000	-4298800000	-5395600000	-6492400000				Cash Flow from Operating Activities, Indirect		24934000001	Q3 2022	Q2 2022	Q1 2022	Q4 2021		
Diluted EPS		00112	00031	00028	00027	00026	00022	00016	00010	00010	00015	00010	-00009					Cash Generated from Operating Activities	35231800000	18560200000	17483800000	16407400000	15331000000				Diluted EPS	-00009	-00015	-00021	-00027	-00033	-00039	-00045	-00051
Other Financing Cash Flow																		Cash Flow Supplemental Section	22809500000000	22375000000000	21940500000000	21506000000000	21071500000000				Other Financing Cash Flow								
Total Adjustments for Non-Cash Items			6517000000	18936000000	18525000000	17930000000	15227000000											Cash Flow from Investing Activities									Total Adjustments for Non-Cash Items		20351200000	21992600000	23634000000	25275400000	26916800000		
Change in Other Current Assets			-399000000	-2409000000	-3661000000	2794000000	-5445000000											Cash Flow from Financing Activities	-9287400000	-7674400000	-3400800000	-3830300000	-4259800000				Change in Other Current Assets		-3290700000	-3779600000	-4268500000	-4757400000	-5246300000		
Depreciation, Amortization and Depletion, Non-Cash Adjustment			3439000000	3797000000	4236000000	2592000000	5748000000											Cash Flow from Continuing Investing Activities	-11015999999	-3706000000	-2492300000	-1278600000	-64900000				Depreciation, Amortization and Depletion, Non-Cash Adjustment		4986300000	5327600000	5668900000	6010200000	6351500000		
Change in Payables and Accrued Expenses			6994000000	-1255000000	-199000000	7000000	-738000000											Cash Flow from Continuing Financing Activities	-10767000000	-10026000000	-6061400000	-4448400000	-2835400000				Change in Payables and Accrued Expenses		-3298800000	-4719000000	-6139200000	-7559400000	-8979600000		
Repayments for Long Term Debt			6365000000	-6392000000	6699000000	900000000	00000											Cash and Cash Equivalents, End of Period	00001	22677000001			19289000001				Repayments for Long Term Debt		-117000000	-660800000	-1204600000	-1748400000	-2292200000		
																		Cash and Cash Equivalents, Beginning of Period	181000000000	-146000000000	110333333	123833333	137333333												
Income Statement Supplemental Section																		Basic Weighted Average Shares Outstanding	697258864	700204182	703149500	706094818	709040136	711985455	714930773		Income Statement Supplemental Section								
Reported Normalized Income										6836000000								Basic WASO	697258864	700204182	703149500	706094818	709040136	711985455	714930773		Reported Normalized Income								
Cash and Cash Equivalents, Beginning of Period			25930000000	235000000000)	-3175000000	300000000	6126000000											Basic net income per share of Class A and B common stock and Class C capital stock (in dollars par share)									Cash and Cash Equivalents, Beginning of Period		25930000001	235000000000)	10384666667	15035166667	19685666667		
Net Income after Extraordinary Items and Discontinued Operations		76033000000	20642000000	18936000000	18525000000	17930000000	15227000000	11247000000	6959000000	6836000000	10671000000	7068000000	-5492763636					Basic EPS from Discontinued Operations									Net Income after Extraordinary Items and Discontinued Operations	-5492763636	-9591163636	-13689563636	-17787963636	-21886363636	-25984763636	-30083163636	-34181563636
Net Income from Continuing Operations		76033000000	20642000000	18936000000	18525000000	17930000000	15227000000	11247000000	6959000000	6836000000	10671000000	7068000000	-5492763636					Basic EPS from Continuing Operations	-00015	-00021	-00027	-00034	-00040	-00046	-00052		Net Income from Continuing Operations	-5492763636	-9591163636	-13689563636	-17787963636	-21886363636	-25984763636	-30083163636	-34181563636
Provision for Income Tax		-14701000000	-3760000000	-4128000000	-3460000000	-3353000000	-3462000000	-2112000000	-1318000000	-921000000	-33000000	-1560000000	1695218182					Basic EPS	-00015	-00021	-00027	-00034	-00040	-00046	-00052		Provision for Income Tax	1695218182	2565754545	3436290909	4306827273	5177363636	6047900000	6918436364	7788972727
Total Operating Profit/Loss as Reported, Supplemental		78714000000	21885000000	21031000000	19361000000	16437000000	15651000000	11213000000	6383000000	7977000000	9266000000	9177000000	-5818800000					Basic EPS	-00015	-00021	-00027	-00034	-00040	-00046	-00052		Total Operating Profit/Loss as Reported, Supplemental	-5818800000	-10077918182	-14337036364	-18596154545	-22855272727	-27114390909	-31373509091	-35632627273
Based on facts as set forth in.				06551														Based on facts as set forth in.		06551							Based on facts as set forth in.			06551					
Basic EPS		00114	00031	00028	00028	00027	00023	00017	00010	00010	00015	00010	-00009					Amortization, Non-Cash Adjustment	3329100000	4848600000	5455600000	6062600000	6669600000				Basic EPS	-00009	-00015	-00021	-00027	-00034	-00040	-00046	-00052
ALPHABET INCOME									Advice number:			650001						ALPHABET INCOME							Advice number:	65001	ALPHABET INCOME								Advice number: 000101
ALPHABET INCOME			UNITED STATES 									9/17/2001						ALPHABET	        						Period Beginning:		ALPHABET		        						
Basic EPS		00114	00031	00028	00028	00027	00023	00017	00010	00010	00015	00010	-00009					31622,6:39 PM									Basic EPS	-00009	-00015	-00021	-00027	-00034	-00040	-00046	-00052
1600 AMPITHEATRE PARKWAY 			SECURITIES AND EXCHANGE COMMISSION				Earnings' Statement					9/29/2022						1601 AMPITHEATRE PARKWAY		DR					Period Ending:		1601 AMPITHEATRE PARKWAY			DR					Period Ending:
1600 AMPIHTHEATRE  PARKWAY MOUNTAIN VIEW CA 94043									Calendar Year---			44669						1601 AMPIHTHEATRE  PARKWAY MOUNTAIN VIEW CA 94043									1601 AMPIHTHEATRE  PARKWAY MOUNTAIN VIEW CA 94043								Calendar Year---
Purchase/Sale and Disposal of Property, Plant and Equipment, Net			-6383000000	-10050000000	-9074000000	-5383000000	-7281000000											13 Months Ended									Purchase/Sale and Disposal of Property, Plant and Equipment, Net		-6772900000	-6485800000	-6198700000	-5911600000	-5624500000		
Purchase of Property, Plant and Equipment			-6383000000	-6819000000	-5496000000	-5942000000	-5479000000											_________________________________________________________									Purchase of Property, Plant and Equipment		-5218300000	-4949800000	-4681300000	-4412800000	-4144300000		
Effect of Exchange Rate Changes			20945000000	23719000000	23630000000	26622000000	26465000000											*include interest paid, capital obligation, and underweighting									Effect of Exchange Rate Changes		28459100000	29853400000	31247700000	32642000000	34036300000		
00000	00000	216079000340	194159000093	122778006636	136082000083	138327000080	130704000067	31595000050	18983000031	27564000030	30575000046	21753776685	-15109109116	00000	00000	00000	00000	00000	23021768717684	22275142014852	21971123132251	21550517722869	21145102313489	1423970771	1429861389	65001	00000	-15109109116	111165509049	50433933761	50951012042	45733930204	40516848368	-84621400136	-96206781973
United States Department of the Treasury				Get answers to your investing questions from the SEC's website dedicated to retail investors			00001								A								00002		Earnings Statement								00002		Earnings Statement

							Period Beginning:																		05324										05324
							Pay Date:																												DALLAS
	Earnings	rate	units		05323		5222 BRADFORD DR	YTD	Z				rate						units					year to date	Other Benefits and	Earnings		rate	units					year to date	Other Benefits and
5323 BRADFORD DR	Overtime				DALLAS		TX 75235-8314	        						        			Overtime							        	Pto Balance	Overtime								        	Pto Balance
Federal Income Tax		$22,677,000,000,000.00			        			        	BASIS OF PAY: BASIC/DILUTED EPS												        			        			Federal Income Tax				        			        	
Social Security Tax					        			        													        			        			Social Security Tax				        			        	
									YOUR BASIC/DILUTED EPS RATE HAS BEEN CHANGED FROM 0.001 TO 112.20 PAR SHARE VALUE																YOUR BASIC/DILUTED EPS RATE HAS BEEN CHANGED FROM 0.001 TO 112.20 PAR SHARE VALUE										YOUR BASIC/DILUTED EPS RATE HAS BEEN CHANGED FROM 0.001 TO 112.20 PAR SHARE VALUE

									Due 09/15/2022																										Due 09/15/2022



																			-9776581818	-21510963636	-33245345455	-44979727273	-56714109091	-68448490909	-80182872727										
Gross Profit		146698000000	42337000000	37497000000	35653000000	31211000000	30818000000	25056000000	19744000000	22177000000	25055000000	22931000000	-2178236364																						
Discontinued Operations																																			
Change in Cash as Reported, Supplemental			23719000000000	23630000000000	26622000000000	26465000000000	20129000000000																												
Income Tax Paid, Supplemental			2774000000	89000000	-2992000000		6336000000																				Discontinued Operations						-51298890909		
																											Change in Cash as Reported, Supplemental								
12 Months Ended																											Income Tax Paid, Supplemental		-5809000000	-8692000000	-11575000000	-44281654545	-2178236364		
_________________________________________________________																																			
				Q4 2020			Q4  2019																				13 Months Ended						6336000001		
Income Statement 																											Gross Profit		-9195472727	-16212709091	-23229945455	-30247181818	-37264418182		
USD in "000'"s																											USD in "000'"s		22809500000000	22375000000000	21940500000000	21506000000000	21071500000000		
Repayments for Long Term Debt				Dec. 31, 2020			Dec. 31, 2019																				Repayments for Long Term Debt			Dec. 31, 2021			Dec. 31, 2020		
Costs and expenses:																											Costs and expenses:		22809500000000	22375000000000	21940500000000	21506000000000	21071500000000		
Cost of revenues				182527			161857																				Cost of revenues			182528			161858		
Research and development																											Research and development		22809500000000	22375000000000	21940500000000	21506000000000	21071500000000		
Sales and marketing				84732			71896																				Sales and marketing			84733			71897		
General and administrative				27573			26018																				General and administrative			27574			26019		
European Commission fines				17946			18464																				European Commission fines			17947			18465		
Total costs and expenses				11052			09551																				Total costs and expenses			11053			09552		
Income from operations				00000			01697																				Income from operations			00001			01698		
Other income (expense), net				141303			127626																				Other income (expense), net			141304			127627		
Income before income taxes				41224			34231																				Income before income taxes		00000	22375000000000	21940500000000	21506000000000	21071500000000	00000	00000
Provision for income taxes				6858000000			05394																				Provision for income taxes			257637118600			257637118600		
Net income				22677000000			19289000000																				Net income			22677000001			19289000001		
*include interest paid, capital obligation, and underweighting				22677000000			19289000000																				*include interest paid, capital obligation, and underweighting			22677000001			19289000001		
				22677000000			19289000000																							22677000001			19289000001		
Basic net income per share of Class A and B common stock and Class C capital stock (in dollars par share)																											Basic net income per share of Class A and B common stock and Class C capital stock (in dollars par share)								
Diluted net income per share of Class A and Class B common stock and Class C capital stock (in dollars par share)																											Diluted net income per share of Class A and Class B common stock and Class C capital stock (in dollars par share)								


For Paperwork Reduction Act Notice, see the seperate Instructions.																											For Paperwork Reduction Act Notice, see the seperate Instructions.								





HC2 Holdings INC																									
Zachry Tyler WooD																									
Form:	S-3																								
"CIK:
0001006837


Company Name:
HC2 HOLDINGS, INC.


File Number:
333-248695"		CIK:	1,006,837	Company Name:	HC2 HOLDINGS, INC.	File Number:	333-248695																		
CIK:	1,006,837																								
Company Name:	HC2 HOLDINGS, INC.																								
File Number:	333-248695																								
CIK:	1,006,837																								
Company Name:	HC2 HOLDINGS, INC.																								
File Number:	333-248695		Zachry Tyler Wood																						
			65,000,000.00																						




























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































@zakwarlord7
Author
zakwarlord7 commented 10 minutes ago
Get answers to your investing questions from the SEC's website dedicated to retail investors 1 A 2 Earnings Statement
ALPHABET 37151 ALPHABET Period Beginning: 1600 AMPITHEATRE PARKWAY Period Ending: 44833 1601 AMPITHEATRE PARKWAY DR Period Ending: DRMOUNTAIN VIEW, C.A., 94043 Pay Date: 44591 MOUNTAIN VIEW, C.A., 94044 Pay Date: "Taxable Marital Status: Exemptions/Allowances" ZACHRY T. WOOD "Taxable Marital Status: Exemptions/Allowances" Married ZACHRY T. Married 5323 BRADFORD DR 5324 Federal: Federal: DALLAS TX 75235-8314 DALLAS TX: NO State Incorne Tax TX: NO State Incorne Tax rate units year to date Other Benefits and Earnings rate units year to date Earnings Other Benefits and 112.2 674678000 7569887160000.0% Information this period total to date Regular 1349355888 2024033776 75698871601 Regular Information Pto Balance Overtime Overtime Pto Balance Total Work Hrs 0 75698871600 "BonusTraining" "BonusTraining" Total Work Hrs Gross Pay 75698871600 Important Notes Gross Pay 75698871601 Important Notes COMPANY PH Y: 650-253-0000 COMPANY PH Y: 650-253-0001 Statutory BASIS OF PAY: BASIC/DILUTED EPS Deductions Statutory Deductions BASIS OF PAY: BASIC/DILUTED EPS Federal Income Tax Federal Income Tax Social Security Tax Social Security Tax YOUR BASIC/DILUTED EPS RATE HAS BEEN CHANGED FROM 0.001 TO 112.20 PAR SHARE VALUE YOUR BASIC/DILUTED EPS RATE HAS BEEN CHANGED FROM 0.001 TO 112.20 PAR SHARE VALUE Medicare Tax Medicare Tax
Net Pay 70842743866 70842743866 Net Pay 70842743867 70842743867 CHECKING CHECKING Net Check  Your federal taxable wages this period are $ ALPHABET INCOME Advice number: 650001 ALPHABET INCOME Advice number: 1600 AMPIHTHEATRE PARKWAY MOUNTAIN VIEW CA 94043 Pay date:_ 44669 1601 AMPIHTHEATRE PARKWAY MOUNTAIN VIEW CA 94043 Pay date:_
Deposited to the account Of xxxxxxxx6547 transit ABA amount Deposited to the account Of xxxxxxxx6548 "PLEASE READ THE IMPORTANT DISCLOSURES BELOW
FEDERAL RESERVE MASTER SUPPLIER ACCOUNT 31000053-052101023 COD 633-44-1725 Zachryiixixiiiwood@gmail.com 47-2041-6547 111000614 31000053PNC Bank PNC Bank Business Tax I.D. Number: 633441725 CIF Department (Online Banking) Checking Account: 47-2041-6547 P7-PFSC-04-F Business Type: Sole Proprietorship/Partnership Corporation 500 First Avenue ALPHABET Pittsburgh, PA 15219-3128 5323 BRADFORD DR NON-NEGOTIABLE DALLAS TX 75235 8313 ZACHRY, TYLER, WOOD 4/18/2022 650-2530-000 469-697-4300 SIGNATURE Time Zone: Eastern Central Mountain Pacific Investment Products  • Not FDIC Insured  • No Bank Guarantee  • May Lose Value" 5264-5331 70842743866 "PLEASE READ THE IMPORTANT DISCLOSURES BELOW
FEDERAL RESERVE MASTER SUPPLIER ACCOUNT 31000053-052101023 COD 633-44-1725 Zachryiixixiiiwood@gmail.com 47-2041-6547 111000614 31000053PNC Bank PNC Bank Business Tax I.D. Number: 633441725 CIF Department (Online Banking) Checking Account: 47-2041-6547 P7-PFSC-04-F Business Type: Sole Proprietorship/Partnership Corporation
500 First Avenue
ALPHABET
Pittsburgh, PA 15219-3128 5323 BRADFORD DR NON-NEGOTIABLE DALLAS TX 75235 8313 ZACHRY, TYLER, WOOD 4/18/2022 650-2530-000 469-697-4300 SIGNATURE Time Zone: Eastern Central Mountain Pacific Investment Products  • Not FDIC Insured  • No Bank Guarantee  • May Lose Value" NON-NEGOTIABLE NON-NEGOTIABLE PLEASE READ THE IMPORTANT DISCLOSURES BELOW PLEASE READ THE IMPORTANT DISCLOSURES BELOW

Based on facts as set forth in. Based on facts as set forth in. 6551 6550The U.S. Internal Revenue Code of 1986, as amended, the Treasury Regulations promulgated thereunder, published pronouncements of the Internal Revenue Service, which may be cited or used as precedents, and case law, any of which may be changed at any time with retroactive effect. No opinion is expressed on any matters other than those specifically referred to above. The U.S. Internal Revenue Code of 1986, as amended, the Treasury Regulations promulgated thereunder, published pronouncements of the Internal Revenue Service, which may be cited or used as precedents, and case law, any of which may be changed at any time with retroactive effect. No opinion is expressed on any matters other than those specifically referred to above.
EMPLOYER IDENTIFICATION NUMBER: 61-1767919 EMPLOYER IDENTIFICATION NUMBER: 61-1767920

[DRAFT FORM OF TAX OPINION] [DRAFT FORM OF TAX OPINION]

										1														
														ALPHABET																									ZACHRY T WOOD																									5324 BRADFORD DR																									DALLAS TX 75235-8315										ORIGINAL REPORT															ORIGINAL REPORT										Income, Rents, & Royalty															Income, Rents, & Royalty										INCOME STATEMENT 	61-1767919														INCOME STATEMENT 	61-1767920										88-1303491															88-1303492									GOOGL_income-statement_Quarterly_As_Originally_Reported	TTM	Q4 2021	Q2 2021	Q1 2021	Q4 2020	Q3 2020	Q2 2020	Q1 2020	Q4 2019	Q3 2019					GOOGL_income-statement_Quarterly_As_Originally_Reported	TTM	Q4 2022	Q3 2022	Q2 2022	Q1 2022	Q4 2021	Q3 2021		Q2 2021	Q3 2021
Gross Profit $146,698,000,000.00 $42,337,000,000.00 $35,653,000,000.00 $31,211,000,000.00 30818000000 $25,056,000,000.00 1974400000000.0% 22177000000 25055000000 22931000000 Gross Profit -2178236364 -9195472727 -16212709091 -23229945455 -30247181818 -37264418182 -44281654545 -51298890909 37497000000Total Revenue as Reported, Supplemental $257,637,000,000.00 $75,325,000,000.00 $61,880,000,000.00 $55,314,000,000.00 56898000000 $46,173,000,000.00 3829700000000.0% 41159000000 46075000000 40499000000 Total Revenue as Reported, Supplemental -1286309091 -13385163636 -25484018182 -37582872727 -49681727273 -61780581818 -73879436364 -85978290909 65118000000 $257,637,000,000.00 $75,325,000,000.00 $61,880,000,000.00 $55,314,000,000.00 56898000000 $46,173,000,000.00 3829700000000.0% 41159000000 64133000000 34071000000 1957800000 -9776581818 -21510963636 -33245345455 -44979727273 -56714109091 -68448490909 -80182872727 65118000000Other Revenue 6428000000 Other Revenue Cost of Revenue -110939000000 -32988000000 -26227000000 -$24,103,000,000.00 -26080000000 -$21,117,000,000.00 -1855300000000.0% -18982000000 -21020000000 -17568000000 Cost of Revenue -891927272.7 4189690909 9271309091 14352927273 19434545455 24516163636 29597781818 34679400000 -27621000000Cost of Goods and Services -110939000000 -32988000000 -26227000000 -24103000000 -26080000000 -21117000000 -18553000000 -18982000000 -21020000000 -17568000000 Cost of Goods and Services -891927272.7 4189690909 9271309091 14352927273 19434545455 24516163636 29597781818 34679400000 -27621000000Operating Income/Expenses -67984000000 -20452000000 -16292000000 -$14,774,000,000.00 -$15,167,000,000.00 -1384300000000.0% -$13,361,000,000.00 -14200000000 -15789000000 -13754000000 Operating Income/Expenses -3640563636 -882445454.5 1875672727 4633790909 7391909091 10150027273 12908145455 15666263636 -16466000000Selling, General and Administrative Expenses -36422000000 -11744000000 -8617000000 -7289000000 -8145000000 -6987000000 -6486000000 -7380000000 -8567000000 -7200000000 Selling, General and Administrative Expenses -1552200000 -28945454.55 1494309091 3017563636 4540818182 6064072727 7587327273 9110581818 -8772000000General and Administrative Expenses -13510000000 -4140000000 -3341000000 -2773000000 -2831000000 -2756000000 -2585000000 -2880000000 -2829000000 -2591000000 General and Administrative Expenses -544945454.5 23200000 591345454.5 1159490909 1727636364 2295781818 2863927273 3432072727 -3256000000Selling and Marketing Expenses -22912000000 -7604000000 -5276000000 -4516000000 -5314000000 -4231000000 -3901000000 -4500000000 -5738000000 -4609000000 Selling and Marketing Expenses -1007254545 -52145454.55 902963636.4 1858072727 2813181818 3768290909 4723400000 5678509091 -5516000000Research and Development Expenses -31562000000 -8708000000 -7675000000 -7485000000 -7022000000 -6856000000 -6875000000 -6820000000 -7222000000 -6554000000 Research and Development Expenses -2088363636 -853500000 381363636.4 1616227273 2851090909 4085954545 5320818182 6555681818 -7694000000Total Operating Profit/Loss 78714000000 21885000000 19361000000 16437000000 15651000000 11213000000 6383000000 7977000000 9266000000 9177000000 Total Operating Profit/Loss -5818800000 -10077918182 -14337036364 -18596154545 -22855272727 -27114390909 -31373509091 -35632627273 21031000000Non-Operating Income/Expenses, Total 12020000000 2517000000 2624000000 4846000000 3038000000 2146000000 1894000000 -220000000 1438000000 -549000000 Non-Operating Income/Expenses, Total -1369181818 -2079000000 -2788818182 -3498636364 -4208454545 -4918272727 -5628090909 -6337909091 2033000000Total Net Finance Income/Expense 1153000000 261000000 313000000 269000000 333000000 412000000 420000000 565000000 604000000 608000000 Total Net Finance Income/Expense 464490909.1 462390909.1 460290909.1 458190909.1 456090909.1 453990909.1 451890909.1 449790909.1 310000000Net Interest Income/Expense 1153000000 261000000 313000000 269000000 333000000 412000000 420000000 565000000 604000000 608000000 Net Interest Income/Expense 464490909.1 462390909.1 460290909.1 458190909.1 456090909.1 453990909.1 451890909.1 449790909.1 310000000
Interest Expense Net of Capitalized Interest -346000000 -117000000 -76000000 -76000000 -53000000 -48000000 -13000000 -21000000 -17000000 -23000000 Interest Expense Net of Capitalized Interest 48654545.45 69900000 91145454.55 112390909.1 133636363.6 154881818.2 176127272.7 197372727.3 -77000000Interest Income 1499000000 378000000 389000000 345000000 386000000 460000000 433000000 586000000 621000000 631000000 Interest Income 415836363.6 392490909.1 369145454.5 345800000 322454545.5 299109090.9 275763636.4 252418181.8 387000000Net Investment Income 12364000000 2364000000 2924000000 4869000000 3530000000 1957000000 1696000000 -809000000 899000000 -1452000000 Net Investment Income -2096781818 -2909109091 -3721436364 -4533763636 -5346090909 -6158418182 -6970745455 -7783072727 2207000000Gain/Loss on Investments and Other Financial Instruments 12270000000 2478000000 2883000000 4751000000 3262000000 2015000000 1842000000 -802000000 399000000 -1479000000 Gain/Loss on Investments and Other Financial Instruments -2243490909 -3068572727 -3893654545 -4718736364 -5543818182 -6368900000 -7193981818 -8019063636 2158000000Income from Associates, Joint Ventures and Other Participating Interests 334000000 49000000 92000000 5000000 355000000 26000000 -54000000 74000000 460000000 -14000000 Income from Associates, Joint Ventures and Other Participating Interests 99054545.45 92609090.91 86163636.36 79718181.82 73272727.27 66827272.73 60381818.18 53936363.64 188000000Gain/Loss on Foreign Exchange -240000000 -163000000 -51000000 113000000 -87000000 -84000000 -92000000 -81000000 40000000 41000000 Gain/Loss on Foreign Exchange 47654545.45 66854545.45 86054545.45 105254545.5 124454545.5 143654545.5 162854545.5 182054545.5 -139000000Irregular Income/Expenses 0 0 0 0 0 0 0 0 Irregular Income/Expenses 0 0 0 0 0 Other Irregular Income/Expenses 0 0 0 0 0 0 0 0 Other Irregular Income/Expenses 0 0 0 0 0 Other Income/Expense, Non-Operating -1497000000 -108000000 -613000000 -292000000 -825000000 -223000000 -222000000 24000000 -65000000 295000000 Other Income/Expense, Non-Operating 263109090.9 367718181.8 472327272.7 576936363.6 681545454.5 786154545.5 890763636.4 995372727.3 -484000000Pretax Income 90734000000 24402000000 21985000000 21283000000 18689000000 13359000000 8277000000 7757000000 10704000000 8628000000 Pretax Income -7187981818 -12156918182 -17125854545 -22094790909 -27063727273 -32032663636 -37001600000 -41970536364 23064000000Provision for Income Tax -14701000000 -3760000000 -3460000000 -3353000000 -3462000000 -2112000000 -1318000000 -921000000 -33000000 -1560000000 Provision for Income Tax 1695218182 2565754545 3436290909 4306827273 5177363636 6047900000 6918436364 7788972727 -4128000000Net Income from Continuing Operations 76033000000 20642000000 18525000000 17930000000 15227000000 11247000000 6959000000 6836000000 10671000000 7068000000 Net Income from Continuing Operations -5492763636 -9591163636 -13689563636 -17787963636 -21886363636 -25984763636 -30083163636 -34181563636 18936000000Net Income after Extraordinary Items and Discontinued Operations 76033000000 20642000000 18525000000 17930000000 15227000000 11247000000 6959000000 6836000000 10671000000 7068000000 Net Income after Extraordinary Items and Discontinued Operations -5492763636 -9591163636 -13689563636 -17787963636 -21886363636 -25984763636 -30083163636 -34181563636 18936000000Net Income after Non-Controlling/Minority Interests 76033000000 20642000000 18525000000 17930000000 15227000000 11247000000 6959000000 6836000000 10671000000 7068000000 Net Income after Non-Controlling/Minority Interests -5492763636 -9591163636 -13689563636 -17787963636 -21886363636 -25984763636 -30083163636 -34181563636 18936000000Net Income Available to Common Stockholders 76033000000 20642000000 18525000000 17930000000 15227000000 11247000000 6959000000 6836000000 10671000000 7068000000 Net Income Available to Common Stockholders -5492763636 -9591163636 -13689563636 -17787963636 -21886363636 -25984763636 -30083163636 -34181563636 18936000000Diluted Net Income Available to Common Stockholders 76033000000 20642000000 18525000000 17930000000 15227000000 11247000000 6959000000 6836000000 10671000000 7068000000 Diluted Net Income Available to Common Stockholders -5492763636 -9591163636 -13689563636 -17787963636 -21886363636 -25984763636 -30083163636 -34181563636 18936000000Income Statement Supplemental Section Income Statement Supplemental Section Reported Normalized and Operating Income/Expense Supplemental Section Reported Normalized and Operating Income/Expense Supplemental Section Total Revenue as Reported, Supplemental 257637000000 75325000000 61880000000 55314000000 56898000000 46173000000 38297000000 41159000000 46075000000 40499000000 Total Revenue as Reported, Supplemental -1286309091 -13385163636 -25484018182 -37582872727 -49681727273 -61780581818 -73879436364 -85978290909 65118000000Total Operating Profit/Loss as Reported, Supplemental 78714000000 21885000000 19361000000 16437000000 15651000000 11213000000 6383000000 7977000000 9266000000 9177000000 Total Operating Profit/Loss as Reported, Supplemental -5818800000 -10077918182 -14337036364 -18596154545 -22855272727 -27114390909 -31373509091 -35632627273 21031000000Reported Effective Tax Rate 0.162 0.157 0.158 0.158 0.159 0.119 0.181 Reported Effective Tax Rate 1.162 0.1436666667 0.1331666667 0.1226666667 0.1063333333 0.08683333333 0.179Reported Normalized Income 6836000000 Reported Normalized Income Reported Normalized Operating Profit 7977000000 Reported Normalized Operating Profit Other Adjustments to Net Income Available to Common Stockholders Other Adjustments to Net Income Available to Common Stockholders Discontinued Operations Discontinued Operations Basic EPS 113.88 31.15 27.69 26.63 22.54 16.55 10.21 9.96 15.49 10.2 Basic EPS -8.742909091 -14.93854545 -21.13418182 -27.32981818 -33.52545455 -39.72109091 -45.91672727 -52.11236364 28.44Basic EPS from Continuing Operations 113.88 31.12 27.69 26.63 22.46 16.55 10.21 9.96 15.47 10.2 Basic EPS from Continuing Operations -8.752545455 -14.94781818 -21.14309091 -27.33836364 -33.53363636 -39.72890909 -45.92418182 -52.11945455 28.44Basic EPS from Discontinued Operations Basic EPS from Discontinued Operations Diluted EPS 112.2 30.69 27.26 26.29 22.3 16.4 10.13 9.87 15.35 10.12 Diluted EPS -8.505636364 -14.599 -20.69236364 -26.78572727 -32.87909091 -38.97245455 -45.06581818 -51.15918182 27.99Diluted EPS from Continuing Operations 112.2 30.67 27.26 26.29 22.23 16.4 10.13 9.87 15.33 10.12 Diluted EPS from Continuing Operations -8.515636364 -14.609 -20.70236364 -26.79572727 -32.88909091 -38.98245455 -45.07581818 -51.16918182 27.99Diluted EPS from Discontinued Operations Diluted EPS from Discontinued Operations Basic Weighted Average Shares Outstanding 667650000 662664000 668958000 673220000 675581000 679449000 681768000 686465000 688804000 692741000 Basic Weighted Average Shares Outstanding 694313545.5 697258863.6 700204181.8 703149500 706094818.2 709040136.4 711985454.5 714930772.7 665758000Diluted Weighted Average Shares Outstanding 677674000 672493000 679612000 682071000 682969000 685851000 687024000 692267000 695193000 698199000 Diluted Weighted Average Shares Outstanding 698675981.8 701033009.1 703390036.4 705747063.6 708104090.9 710461118.2 712818145.5 715175172.7 676519000Reported Normalized Diluted EPS 9.87 Reported Normalized Diluted EPS Basic EPS 113.88 31.15 27.69 26.63 22.54 16.55 10.21 9.96 15.49 10.2 Basic EPS -8.742909091 -14.93854545 -21.13418182 -27.32981818 -33.52545455 -39.72109091 -45.91672727 -52.11236364 28.44Diluted EPS 112.2 30.69 27.26 26.29 22.3 16.4 10.13 9.87 15.35 10.12 Diluted EPS -8.505636364 -14.599 -20.69236364 -26.78572727 -32.87909091 -38.97245455 -45.06581818 -51.15918182 27.99Basic WASO 667650000 662664000 668958000 673220000 675581000 679449000 681768000 686465000 688804000 692741000 Basic WASO 694313545.5 697258863.6 700204181.8 703149500 706094818.2 709040136.4 711985454.5 714930772.7 665758000Diluted WASO 677674000 672493000 679612000 682071000 682969000 685851000 687024000 692267000 695193000 698199000 Diluted WASO 698675981.8 701033009.1 703390036.4 705747063.6 708104090.9 710461118.2 712818145.5 715175172.7 676519000Fiscal year end September 28th., 2022. | USD Fiscal year end September 28th., 2022. | USD
31622,6:39 PM 31622,6:39 PM Morningstar.com Intraday Fundamental Portfolio View Print Report Print Morningstar.com Intraday Fundamental Portfolio View Print Report Print
3/6/2022 at 6:37 PM Current Value 3/6/2022 at 6:37 PM 15335150186014
GOOGL_income-statement_Quarterly_As_Originally_Reported Q4 2021 GOOGL_income-statement_Quarterly_As_Originally_Reported Q4 2022 Cash Flow from Operating Activities, Indirect 24934000000 Q2 2021 Q1 2021 Q4 2020 Cash Flow from Operating Activities, Indirect 24934000001 Q3 2022 Q2 2022 Q1 2022 Q4 2021 Q3 2021Net Cash Flow from Continuing Operating Activities, Indirect 24934000000 37497000000 31211000000 30818000000 Net Cash Flow from Continuing Operating Activities, Indirect 35231800000 36975800000 38719800000 40463800000 42207800000 25539000000Cash Generated from Operating Activities 24934000000 21890000000 19289000000 22677000000 Cash Generated from Operating Activities 19636600000 18560200000 17483800000 16407400000 15331000000 25539000000Income/Loss before Non-Cash Adjustment 20642000000 21890000000 19289000000 22677000000 Income/Loss before Non-Cash Adjustment 21353400000 21135400000 20917400000 20699400000 20481400000 25539000000Total Adjustments for Non-Cash Items 6517000000 18525000000 17930000000 15227000000 Total Adjustments for Non-Cash Items 20351200000 21992600000 23634000000 25275400000 26916800000 18936000000Depreciation, Amortization and Depletion, Non-Cash Adjustment 3439000000 4236000000 2592000000 5748000000 Depreciation, Amortization and Depletion, Non-Cash Adjustment 4986300000 5327600000 5668900000 6010200000 6351500000 3797000000Depreciation and Amortization, Non-Cash Adjustment 3439000000 2945000000 2753000000 3725000000 Depreciation and Amortization, Non-Cash Adjustment 3239500000 3241600000 3243700000 3245800000 3247900000 3304000000Depreciation, Non-Cash Adjustment 3215000000 2945000000 2753000000 3725000000 Depreciation, Non-Cash Adjustment 3329100000 3376000000 3422900000 3469800000 3516700000 3304000000Amortization, Non-Cash Adjustment 224000000 2730000000 2525000000 3539000000 Amortization, Non-Cash Adjustment 4241600000 4848600000 5455600000 6062600000 6669600000 3085000000Stock-Based Compensation, Non-Cash Adjustment 3954000000 215000000 228000000 186000000 Stock-Based Compensation, Non-Cash Adjustment -1297700000 -2050400000 -2803100000 -3555800000 -4308500000 219000000Taxes, Non-Cash Adjustment 1616000000 3803000000 3745000000 3223000000 Taxes, Non-Cash Adjustment 4177700000 4486200000 4794700000 5103200000 5411700000 3874000000Investment Income/Loss, Non-Cash Adjustment -2478000000 379000000 1100000000 1670000000 Investment Income/Loss, Non-Cash Adjustment 3081700000 4150000000 5218300000 6286600000 7354900000 -1287000000Gain/Loss on Financial Instruments, Non-Cash Adjustment -2478000000 -2883000000 -4751000000 -3262000000 Gain/Loss on Financial Instruments, Non-Cash Adjustment -4354700000 -4770800000 -5186900000 -5603000000 -6019100000 -2158000000Other Non-Cash Items -14000000 -2883000000 -4751000000 -3262000000 Other Non-Cash Items -5340300000 -6249200000 -7158100000 -8067000000 -8975900000 -2158000000Changes in Operating Capital -2225000000 -8000000 -255000000 392000000 Changes in Operating Capital 1068100000 1559600000 2051100000 2542600000 3034100000 64000000Change in Trade and Other Receivables -5819000000 -871000000 -1233000000 1702000000 Change in Trade and Other Receivables 2617900000 3718200000 4818500000 5918800000 7019100000 2806000000Change in Trade/Accounts Receivable -5819000000 -3661000000 2794000000 -5445000000 Change in Trade/Accounts Receivable -1122700000 -527600000 67500000 662600000 1257700000 -2409000000Change in Other Current Assets -399000000 -3661000000 2794000000 -5445000000 Change in Other Current Assets -3290700000 -3779600000 -4268500000 -4757400000 -5246300000 -2409000000Change in Payables and Accrued Expenses 6994000000 -199000000 7000000 -738000000 Change in Payables and Accrued Expenses -3298800000 -4719000000 -6139200000 -7559400000 -8979600000 -1255000000Change in Trade and Other Payables 1157000000 4074000000 -4956000000 6938000000 Change in Trade and Other Payables 3108700000 3453600000 3798500000 4143400000 4488300000 3157000000Change in Trade/Accounts Payable 1157000000 -130000000 -982000000 963000000 Change in Trade/Accounts Payable -233200000 -394000000 -554800000 -715600000 -876400000 238000000Change in Accrued Expenses 5837000000 -130000000 -982000000 963000000 Change in Accrued Expenses -2105200000 -3202000000 -4298800000 -5395600000 -6492400000 238000000Change in Deferred Assets/Liabilities 368000000 4204000000 -3974000000 5975000000 Change in Deferred Assets/Liabilities 3194700000 3626800000 4058900000 4491000000 4923100000 2919000000Change in Other Operating Capital -3369000000 -3000000 137000000 207000000 Change in Other Operating Capital 1553900000 2255600000 2957300000 3659000000 4360700000 272000000Change in Prepayments and Deposits -1082000000 785000000 740000000 Change in Prepayments and Deposits -388000000 -891600000 -1395200000 -1898800000 3041000000Cash Flow from Investing Activities -11016000000 Cash Flow from Investing Activities -11015999999 Cash Flow from Continuing Investing Activities -11016000000 -9074000000 -5383000000 -7281000000 Cash Flow from Continuing Investing Activities -4919700000 -3706000000 -2492300000 -1278600000 -64900000 -10050000000Purchase/Sale and Disposal of Property, Plant and Equipment, Net -6383000000 -9074000000 -5383000000 -7281000000 Purchase/Sale and Disposal of Property, Plant and Equipment, Net -6772900000 -6485800000 -6198700000 -5911600000 -5624500000 -10050000000Purchase of Property, Plant and Equipment -6383000000 -5496000000 -5942000000 -5479000000 Purchase of Property, Plant and Equipment -5218300000 -4949800000 -4681300000 -4412800000 -4144300000 -6819000000Sale and Disposal of Property, Plant and Equipment -5496000000 -5942000000 -5479000000 Sale and Disposal of Property, Plant and Equipment -5040500000 -4683100000 -4325700000 -3968300000 -6819000000Purchase/Sale of Business, Net -385000000 Purchase/Sale of Business, Net -384999999 Purchase/Acquisition of Business -385000000 -308000000 -1666000000 -370000000 Purchase/Acquisition of Business -1010700000 -1148400000 -1286100000 -1423800000 -1561500000 -259000000Purchase/Sale of Investments, Net -4348000000 -308000000 -1666000000 -370000000 Purchase/Sale of Investments, Net 574500000 1229400000 1884300000 2539200000 3194100000 -259000000Purchase of Investments -40860000000 -3293000000 2195000000 -1375000000 Purchase of Investments 16018900000 24471400000 32923900000 41376400000 49828900000 -3360000000Sale of Investments 36512000000 -24949000000 -37072000000 -36955000000 Sale of Investments -64179300000 -79064600000 -93949900000 -108835200000 -123720500000 -35153000000Other Investing Cash Flow 100000000 21656000000 39267000000 35580000000 Other Investing Cash Flow 49209400000 57052800000 64896200000 72739600000 80583000000 31793000000Purchase/Sale of Other Non-Current Assets, Net 23000000 30000000 -57000000 Purchase/Sale of Other Non-Current Assets, Net -236000000 -368800000 -501600000 -634400000 388000000Sales of Other Non-Current Assets Sales of Other Non-Current Assets Cash Flow from Financing Activities -16511000000 Cash Flow from Financing Activities -13997000000 -12740000000 -15254000000Cash Flow from Continuing Financing Activities -16511000000 -15991000000 -13606000000 -9270000000 Cash Flow from Continuing Financing Activities -9287400000 -7674400000 -6061400000 -4448400000 -2835400000 -15254000000Issuance of/Payments for Common Stock, Net -13473000000 -15991000000 -13606000000 -9270000000 Issuance of/Payments for Common Stock, Net -10767000000 -10026000000 -9285000000 -8544000000 -7803000000 -12610000000Payments for Common Stock 13473000000 -12796000000 -11395000000 -7904000000 Payments for Common Stock -18708100000 -22862000000 -27015900000 -31169800000 -35323700000 -12610000000Proceeds from Issuance of Common Stock -12796000000 -11395000000 -7904000000 Proceeds from Issuance of Common Stock -5806333333 -3360333333 -914333333.3 Issuance of/Repayments for Debt, Net 115000000 Issuance of/Repayments for Debt, Net -199000000 -356000000 -42000000Issuance of/Repayments for Long Term Debt, Net 115000000 -1042000000 -37000000 -57000000 Issuance of/Repayments for Long Term Debt, Net -314300000 -348200000 -382100000 -416000000 -449900000 -42000000Proceeds from Issuance of Long Term Debt 6250000000 -1042000000 -37000000 -57000000 Proceeds from Issuance of Long Term Debt -3407500000 -5307600000 -7207700000 -9107800000 -11007900000 6350000000Repayments for Long Term Debt 6365000000 6699000000 900000000 0 Repayments for Long Term Debt -117000000 -660800000 -1204600000 -1748400000 -2292200000 -6392000000Proceeds from Issuance/Exercising of Stock Options/Warrants 2923000000 -7741000000 -937000000 -57000000 Proceeds from Issuance/Exercising of Stock Options/Warrants -2971300000 -3400800000 -3830300000 -4259800000 -4689300000 -2602000000 -2453000000 -2184000000 -1647000000 -1288666667 -885666666.7 -482666666.7
Other Financing Cash Flow Other Financing Cash Flow Cash and Cash Equivalents, End of Period Cash and Cash Equivalents, End of Period Change in Cash 0 300000000 10000000 338000000000) Change in Cash 1 -280000000 -570000000 338000000000) Effect of Exchange Rate Changes 20945000000 23630000000 26622000000 26465000000 Effect of Exchange Rate Changes 28459100000 29853400000 31247700000 32642000000 34036300000 23719000000Cash and Cash Equivalents, Beginning of Period 25930000000 -3175000000 300000000 6126000000 Cash and Cash Equivalents, Beginning of Period 25930000001 235000000000) 10384666667 15035166667 19685666667 235000000000)Cash Flow Supplemental Section 181000000000) 183000000 -143000000 210000000 Cash Flow Supplemental Section 181000000000) -146000000000) 110333333.3 123833333.3 137333333.3 -146000000000)Change in Cash as Reported, Supplemental 23719000000000 26622000000000 26465000000000 20129000000000 Change in Cash as Reported, Supplemental 22809500000000 22375000000000 21940500000000 21506000000000 21071500000000 23630000000000Income Tax Paid, Supplemental 2774000000 -2992000000 6336000000 Income Tax Paid, Supplemental -5809000000 -8692000000 -11575000000 6336000001 89000000Cash and Cash Equivalents, Beginning of Period 13412000000 -4990000000 Cash and Cash Equivalents, Beginning of Period -13098000000 -26353000000 -4989999999 157000000
12 Months Ended 13 Months Ended _________________________________________________________ _________________________________________________________ Q4 2019 Q4 2021 Q4 2020 Q4 2020Income Statement Income Statement USD in "000'"s USD in "000'"s Repayments for Long Term Debt Dec. 31, 2019 Repayments for Long Term Debt Dec. 31, 2021 Dec. 31, 2020 Dec. 31, 2020Costs and expenses: Costs and expenses: Cost of revenues 161857 Cost of revenues 182528 161858 182527Research and development Research and development Sales and marketing 71896 Sales and marketing 84733 71897 84732General and administrative 26018 General and administrative 27574 26019 27573European Commission fines 18464 European Commission fines 17947 18465 17946Total costs and expenses 9551 Total costs and expenses 11053 9552 11052Income from operations 1697 Income from operations 1 1698 0Other income (expense), net 127626 Other income (expense), net 141304 127627 141303Income before income taxes 34231 Income before income taxes 41225 34232 41224Provision for income taxes 5394 Provision for income taxes 6858000001 5395 6858000000Net income 19289000000 Net income 22677000001 19289000001 22677000000*include interest paid, capital obligation, and underweighting 19289000000 *include interest paid, capital obligation, and underweighting 22677000001 19289000001 22677000000 19289000000 22677000001 19289000001 22677000000Basic net income per share of Class A and B common stock and Class C capital stock (in dollars par share) Basic net income per share of Class A and B common stock and Class C capital stock (in dollars par share) Diluted net income per share of Class A and Class B common stock and Class C capital stock (in dollars par share) Diluted net income per share of Class A and Class B common stock and Class C capital stock (in dollars par share)

For Paperwork Reduction Act Notice, see the seperate Instructions. For Paperwork Reduction Act Notice, see the seperate Instructions.

				Name	Tax Period 	Total	Social Security	Medicare	Withholding											Name	Tax Period 		Total						Fed 941 Corporate	39355	66986.66	28841.48	6745.18	31400											Fed 941 Corporate	11820.22		4205.072						Fed 941 West Subsidiary	39355	17115.41	7369.14	1723.42	8022.85											Fed 941 West Subsidiary	-8699.723		-16505.352						Fed 941 South Subsidiary	39355	23906.09	10292.9	2407.21	11205.98											Fed 941 South Subsidiary	-5905.64		-13685.332						Fed 941 East Subsidiary	39355	11247.64	4842.74	1132.57	5272.33											Fed 941 East Subsidiary	-11114.067		-18942.108						Fed 941 Corp - Penalty	39355	27198.5	11710.47	2738.73	12749.3											Fed 941 Corp - Penalty	-4550.951		-12318.068						Fed 940 Annual Unemp - Corp	39355	17028.05														Fed 940 Annual Unemp - Corp	-5298.9		-27625.85	

			ID:	TxDL: 00037305581	Ssn:	633-44-1725	DoB: 1994-10-15												ID:	TxDL: 00037305582	Ssn:		633-44-1726	
Alphabet Inc. GOOGL, GOOG on Nasdaq Alphabet Inc. GOOGL, GOOG on Nasdaq [-] Company Information [-] Company Information CIK: CIK: 1652044 1652045 EIN: EIN: 61-1767919 61-1767920 SIC: SIC: 7370 - Services-Computer Programming, Data Processing, Etc. 7371 - Services-Computer Programming, Data Processing, Etc. (CF Office: Office of Technology) (CF Office: Office of Technology) State location: State location: CA CA State of incorporation: State of incorporation: DE DE Fiscal year end: Fiscal year end: 44926 44927 Business address: Business address: 1600 AMPHITHEATRE PARKWAY, MOUNTAIN VIEW, CA, 94043 1601 AMPHITHEATRE PARKWAY, MOUNTAIN VIEW, CA, 94043 Phone: 650-253-0000 Phone: 650-253-0001 Mailing address: Mailing address: 1600 AMPHIITHEATRE PARKWAY, MOINTAIN VIEW, CA, 94043 1601 AMPHIITHEATRE PARKWAY, MOINTAIN VIEW, CA, 94043 Category: Category: Large accelerated filer Large accelerated filer Filings: Filings: 1,388 EDGAR filings since October 2, 2015 1,388 EDGAR filings since October 2, 2016 Get insider transactions for this issuer Get insider transactions for this issuer Get insider transactions for this reporting owner Get insider transactions for this reporting owner Latest Filings (excluding insider transactions) Latest Filings (excluding insider transactions) March 11, 2022 - SC 13G/A: Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing March 11, 2022 - SC 13G/A: Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing February 14, 2022 - SC 13G/A: Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing February 14, 2022 - SC 13G/A: Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing February 11, 2022 - SC 13G/A: Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing February 11, 2022 - SC 13G/A: Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing February 11, 2022 - SC 13G/A: Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing February 11, 2022 - SC 13G/A: Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing February 9, 2022 - SC 13G/A: Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing February 9, 2022 - SC 13G/A: Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing Selected Filings Selected Filings [+] 8-K (current reports) [+] 8-K (current reports) [+] 10-K (annual reports) and 10-Q (quarterly reports) [+] 10-K (annual reports) and 10-Q (quarterly reports) [+] Proxy (annual meeting) and information statements [+] Proxy (annual meeting) and information statements [+] Ownership disclosures [+] Ownership disclosures Filings Filings Search table From Date (yyyy-mm-dd) To Date (yyyy-mm-dd) Search table From Date (yyyy-mm-dd) To Date (yyyy-mm-dd)
Keywords: Keywords: Show columns: Show columns: Form type Form type Form description Form description Filing date Filing date Reporting date Reporting date Act Act Film number Film number File number File number Accession number Accession number Size Size Form type Form description Reporting date Form type Form description Filing date Reporting date Filing dateForm type Form description Filing date Reporting date Form type Form description Filing date Reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44643 2022-03-22View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44644 2022-03-22View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing Amendments 44642 2022-03-18View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing Amendments 44643 2022-03-18View all with same reporting date 4/A Statement of changes in beneficial ownership of securities - amendmentOpen document FilingOpen filing 44642 2022-03-18View all with same reporting date 4/A Statement of changes in beneficial ownership of securities - amendmentOpen document FilingOpen filing 44643 2022-03-18View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing Amendments 44641 2022-03-18View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing Amendments 44642 2022-03-18View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing Amendments 44641 2022-03-18View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing Amendments 44642 2022-03-18View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing Amendments 44641 2022-03-18View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing Amendments 44642 2022-03-18View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44638 2022-03-17View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44639 2022-03-17View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44638 2022-03-17View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44639 2022-03-17View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44638 2022-03-17View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44639 2022-03-17View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44637 2022-03-16View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44638 2022-03-16View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44637 2022-03-16View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44638 2022-03-16View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44637 2022-03-16View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44638 2022-03-16View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44637 2022-03-16View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44638 2022-03-16View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44631 2022-03-09View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44632 2022-03-09View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44631 2022-03-09View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44632 2022-03-09View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44631 2022-03-09View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44632 2022-03-09View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44631 2022-03-09View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44632 2022-03-09View all with same reporting date SC 13G/A Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing 44631 SC 13G/A Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing 44632 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44630 2022-03-08View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44631 2022-03-08View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44630 2022-03-08View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44631 2022-03-08View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44630 2022-03-08View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44631 2022-03-08View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44630 2022-03-08View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44631 2022-03-08View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44630 2022-03-09View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44631 2022-03-09View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44630 2022-03-09View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44631 2022-03-09View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44629 2022-03-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44630 2022-03-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44629 2022-03-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44630 2022-03-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44629 2022-03-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44630 2022-03-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44629 2022-03-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44630 2022-03-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44622 2022-03-01View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44623 2022-03-01View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44620 2022-02-25View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44621 2022-02-25View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44614 2022-02-22View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44615 2022-02-22View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44609 2022-02-16View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44610 2022-02-16View all with same reporting date 5 Annual statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44606 2021-12-31View all with same reporting date 6 Annual statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44607 2021-12-31View all with same reporting date SC 13G/A Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing 44606 SC 13G/A Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing 44607 5 Annual statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44603 2021-12-31View all with same reporting date 6 Annual statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44604 2021-12-31View all with same reporting date 5 Annual statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44603 2021-12-31View all with same reporting date 6 Annual statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44604 2021-12-31View all with same reporting date 5 Annual statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44603 2021-12-31View all with same reporting date 6 Annual statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44604 2021-12-31View all with same reporting date 5 Annual statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44603 2021-12-31View all with same reporting date 6 Annual statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44604 2021-12-31View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44603 2022-02-09View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44604 2022-02-09View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44603 2022-02-09View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44604 2022-02-09View all with same reporting date SC 13G/A Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing 44603 SC 13G/A Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing 44604 SC 13G/A Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing 44603 SC 13G/A Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing 44604 5 Annual statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44603 2021-12-31View all with same reporting date 6 Annual statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44604 2021-12-31View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44603 2022-02-09View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44604 2022-02-09View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44603 2022-02-09View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44604 2022-02-09View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44602 2022-02-08View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44603 2022-02-08View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44602 2022-02-08View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44603 2022-02-08View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44602 2022-02-08View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44603 2022-02-08View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44602 2021-11-26View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44603 2021-11-26View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44602 2021-11-24View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44603 2021-11-24View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44602 2021-11-23View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44603 2021-11-23View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44602 2021-11-19View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44603 2021-11-19View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44602 2021-11-17View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44603 2021-11-17View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44602 2021-11-16View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44603 2021-11-16View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44602 2021-11-04View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44603 2021-11-04View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44601 2022-02-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44602 2022-02-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44601 2022-02-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44602 2022-02-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44601 2022-02-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44602 2022-02-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44601 2022-02-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44602 2022-02-07View all with same reporting date SC 13G/A Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing 44601 SC 13G/A Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing 44602 SC 13G/A Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing 44601 SC 13G/A Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing 44602 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44600 2022-02-08View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44601 2022-02-08View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44600 2022-02-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44601 2022-02-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44600 2022-02-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44601 2022-02-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44600 2022-02-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44601 2022-02-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44600 2022-02-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44601 2022-02-07View all with same reporting date SC 13G Statement of acquisition of beneficial ownership by individualsOpen document FilingOpen filing 44600 SC 13G Statement of acquisition of beneficial ownership by individualsOpen document FilingOpen filing 44601 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44600 2022-02-04View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44601 2022-02-04View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44599 2022-02-04View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44600 2022-02-04View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44599 2022-02-04View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44600 2022-02-04View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44599 2022-02-04View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44600 2022-02-04View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44599 2022-02-04View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44600 2022-02-04View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44596 2022-02-03View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44597 2022-02-03View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44596 2022-02-03View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44597 2022-02-03View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44596 2022-02-03View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44597 2022-02-03View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44596 2022-02-03View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44597 2022-02-03View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44596 2022-02-03View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44597 2022-02-03View all with same reporting date SC 13G/A Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing 44595 SC 13G/A Statement of acquisition of beneficial ownership by individuals - amendmentOpen document FilingOpen filing 44596 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44594 2022-02-02View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44595 2022-02-02View all with same reporting date S-3ASR Automatic shelf registration statement of securities of well-known seasoned issuersOpen document FilingOpen filing 44594 S-3ASR Automatic shelf registration statement of securities of well-known seasoned issuersOpen document FilingOpen filing 44595 10-K Annual report [Section 13 and 15(d), not S-K Item 405]Open document FilingOpen filing 44594 2021-12-31View all with same reporting date 10-K Annual report [Section 13 and 15(d), not S-K Item 405]Open document FilingOpen filing 44595 2021-12-31View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44593 2022-02-01View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44594 2022-02-01View all with same reporting date 8-K Current reportOpen document FilingOpen filing 44593 2022-02-01View all with same reporting date 8-K Current reportOpen document FilingOpen filing 44594 2022-02-01View all with same reporting date 2.02 - Results of Operations and Financial Condition 2.02 - Results of Operations and Financial Condition 8.01 - Other Events (The registrant can use this Item to report events that are not specifically called for by Form 8-K, that the registrant considers to be of importance to security holders.) 8.01 - Other Events (The registrant can use this Item to report events that are not specifically called for by Form 8-K, that the registrant considers to be of importance to security holders.) 9.01 - Financial Statements and Exhibits 9.01 - Financial Statements and Exhibits4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44588 2022-01-25View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44589 2022-01-25View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44582 2022-01-20View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44583 2022-01-20View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44582 2022-01-20View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44583 2022-01-20View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44582 2022-01-20View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44583 2022-01-20View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44582 2022-01-20View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44583 2022-01-20View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44581 2022-01-19View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44582 2022-01-19View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44581 2022-01-19View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44582 2022-01-19View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44581 2022-01-19View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44582 2022-01-19View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44581 2022-01-19View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44582 2022-01-19View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44580 2022-01-18View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44581 2022-01-18View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44580 2022-01-18View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44581 2022-01-18View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44575 2022-01-12View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44576 2022-01-12View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44574 2022-01-12View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44575 2022-01-12View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44574 2022-01-12View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44575 2022-01-12View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44574 2022-01-11View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44575 2022-01-11View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44574 2022-01-11View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44575 2022-01-11View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44574 2022-01-11View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44575 2022-01-11View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44572 2022-01-10View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44573 2022-01-10View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44572 2022-01-10View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44573 2022-01-10View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44572 2022-01-10View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44573 2022-01-10View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44572 2022-01-10View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44573 2022-01-10View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44572 2022-01-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44573 2022-01-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44568 2022-01-05View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44569 2022-01-05View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44568 2022-01-05View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44569 2022-01-05View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44568 2022-01-05View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44569 2022-01-05View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44568 2022-01-05View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44569 2022-01-05View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44567 2022-01-05View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44568 2022-01-05View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44566 2022-01-05View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44567 2022-01-05View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44566 2022-01-05View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44567 2022-01-05View all with same reporting date 8-K Current reportOpen document FilingOpen filing 44565 2021-12-28View all with same reporting date 8-K Current reportOpen document FilingOpen filing 44566 2021-12-28View all with same reporting date 5.02 - Departure of Directors or Certain Officers; Election of Directors; Appointment of Certain Officers; Compensatory Arrangements of Certain Officers 5.02 - Departure of Directors or Certain Officers; Election of Directors; Appointment of Certain Officers; Compensatory Arrangements of Certain Officers4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44564 2022-01-03View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44565 2022-01-03View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44564 2022-01-03View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44565 2022-01-03View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44559 2021-12-27View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44560 2021-12-27View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44559 2021-12-27View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44560 2021-12-27View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44559 2021-12-27View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44560 2021-12-27View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44559 2021-12-27View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44560 2021-12-27View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44559 2021-12-27View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44560 2021-12-27View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44559 2021-12-27View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44560 2021-12-27View all with same reporting date 3 Initial statement of beneficial ownership of securitiesOpen document FilingOpen filing 44547 2021-12-07View all with same reporting date 4 Initial statement of beneficial ownership of securitiesOpen document FilingOpen filing 44548 2021-12-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44545 2021-12-15View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44546 2021-12-15View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44540 2021-12-09View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44541 2021-12-09View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44540 2021-12-09View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44541 2021-12-09View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44539 2021-12-08View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44540 2021-12-08View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44539 2021-12-08View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44540 2021-12-08View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44539 2021-12-08View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44540 2021-12-08View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44539 2021-12-08View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44540 2021-12-08View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44538 2021-12-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44539 2021-12-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44538 2021-12-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44539 2021-12-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44538 2021-12-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44539 2021-12-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44538 2021-12-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44539 2021-12-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44538 2021-12-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44539 2021-12-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44538 2021-12-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44539 2021-12-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44537 2021-12-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44538 2021-12-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44537 2021-12-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44538 2021-12-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44537 2021-12-06View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44538 2021-12-06View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44537 2021-12-06View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44538 2021-12-06View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44537 2021-12-06View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44538 2021-12-06View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44531 2021-12-01View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44532 2021-12-01View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44531 2021-12-01View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44532 2021-12-01View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44531 2021-12-01View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44532 2021-12-01View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44529 2021-11-25View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44530 2021-11-25View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44523 2021-11-19View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44524 2021-11-19View all with same reporting date 4/A Statement of changes in beneficial ownership of securities - amendmentOpen document FilingOpen filing 44523 2021-11-11View all with same reporting date 4/A Statement of changes in beneficial ownership of securities - amendmentOpen document FilingOpen filing 44524 2021-11-11View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44523 2021-11-21View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44524 2021-11-21View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44518 2021-11-16View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44519 2021-11-16View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44517 2021-11-17View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44518 2021-11-17View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44517 2021-11-16View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44518 2021-11-16View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44517 2021-11-16View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44518 2021-11-16View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44516 2021-11-15View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44517 2021-11-15View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44516 2021-11-15View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44517 2021-11-15View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44515 2021-11-12View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44516 2021-11-12View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44515 2021-11-12View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44516 2021-11-12View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44515 2021-11-12View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44516 2021-11-12View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44512 2021-11-10View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44513 2021-11-10View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44512 2021-11-10View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44513 2021-11-10View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44512 2021-11-10View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44513 2021-11-10View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44512 2021-11-09View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44513 2021-11-09View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44510 2021-11-09View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44511 2021-11-09View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44509 2021-11-08View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44510 2021-11-08View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44509 2021-11-08View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44510 2021-11-08View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44509 2021-11-08View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44510 2021-11-08View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44508 2021-11-05View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44509 2021-11-05View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44508 2021-11-05View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44509 2021-11-05View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44508 2021-11-05View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44509 2021-11-05View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44503 2021-11-03View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44504 2021-11-03View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44502 2021-11-02View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44503 2021-11-02View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44501 2021-11-01View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44502 2021-11-01View all with same reporting date 10-Q Quarterly report [Sections 13 or 15(d)]Open document FilingOpen filing 44496 2021-09-30View all with same reporting date 10-Q Quarterly report [Sections 13 or 15(d)]Open document FilingOpen filing 44497 2021-09-30View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44495 2021-10-25View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44496 2021-10-25View all with same reporting date 8-K Current reportOpen document FilingOpen filing 44495 2021-10-26View all with same reporting date 8-K Current reportOpen document FilingOpen filing 44496 2021-10-26View all with same reporting date 2.02 - Results of Operations and Financial Condition 2.02 - Results of Operations and Financial Condition 9.01 - Financial Statements and Exhibits 9.01 - Financial Statements and Exhibits4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44490 2021-10-20View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44491 2021-10-20View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44490 2021-10-20View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44491 2021-10-20View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44490 2021-10-20View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44491 2021-10-20View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44489 2021-10-19View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44490 2021-10-19View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44489 2021-10-19View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44490 2021-10-19View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44487 2021-10-18View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44488 2021-10-18View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44487 2021-10-18View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44488 2021-10-18View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44484 2021-10-13View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44485 2021-10-13View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44484 2021-10-13View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44485 2021-10-13View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44483 2021-10-12View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44484 2021-10-12View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44483 2021-10-12View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44484 2021-10-12View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44481 2021-10-11View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44482 2021-10-11View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44481 2021-10-11View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44482 2021-10-11View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44477 2021-10-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44478 2021-10-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44475 2021-10-06View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44476 2021-10-06View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44475 2021-10-04View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44476 2021-10-04View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44470 2021-10-01View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44471 2021-10-01View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44470 2021-09-29View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44471 2021-09-29View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44467 2021-09-25View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44468 2021-09-25View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44467 2021-09-25View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44468 2021-09-25View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44467 2021-09-25View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44468 2021-09-25View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44467 2021-09-25View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44468 2021-09-25View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44467 2021-09-25View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44468 2021-09-25View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44467 2021-09-25View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44468 2021-09-25View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44466 2021-09-23View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44467 2021-09-23View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44466 2021-09-23View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44467 2021-09-23View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44463 2021-09-24View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44464 2021-09-24View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44463 2021-09-22View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44464 2021-09-22View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44463 2021-09-22View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44464 2021-09-22View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44463 2021-09-22View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44464 2021-09-22View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44461 2021-09-21View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44462 2021-09-21View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44461 2021-09-21View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44462 2021-09-21View all with same reporting date 3 Initial statement of beneficial ownership of securitiesOpen document FilingOpen filing 44460 2021-09-21View all with same reporting date 4 Initial statement of beneficial ownership of securitiesOpen document FilingOpen filing 44461 2021-09-21View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44454 2021-09-15View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44455 2021-09-15View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44452 2021-09-09View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44453 2021-09-09View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44452 2021-09-09View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44453 2021-09-09View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44449 2021-09-08View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44450 2021-09-08View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44449 2021-09-08View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44450 2021-09-08View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44447 2021-09-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44448 2021-09-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44447 2021-09-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44448 2021-09-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44447 2021-09-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44448 2021-09-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44441 2021-09-01View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44442 2021-09-01View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44441 2021-09-01View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44442 2021-09-01View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44441 2021-09-02View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44442 2021-09-02View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44438 2021-08-29View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44439 2021-08-29View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44435 2021-08-25View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44436 2021-08-25View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44431 2021-08-20View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44432 2021-08-20View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44431 2021-08-20View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44432 2021-08-20View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44431 2021-08-19View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44432 2021-08-19View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44431 2021-08-19View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44432 2021-08-19View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44427 2021-08-18View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44428 2021-08-18View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44427 2021-08-18View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44428 2021-08-18View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44427 2021-08-18View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44428 2021-08-18View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44419 2021-08-11View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44420 2021-08-11View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44419 2021-08-11View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44420 2021-08-11View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44419 2021-08-10View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44420 2021-08-10View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44419 2021-08-10View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44420 2021-08-10View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44418 2021-08-09View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44419 2021-08-09View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44418 2021-08-09View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44419 2021-08-09View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44418 2021-08-09View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44419 2021-08-09View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44412 2021-08-04View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44413 2021-08-04View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44411 2021-08-03View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44412 2021-08-03View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44410 2021-07-30View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44411 2021-07-30View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44410 2021-08-02View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44411 2021-08-02View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44410 2021-07-29View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44411 2021-07-29View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44410 2021-07-29View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44411 2021-07-29View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44407 2021-07-28View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44408 2021-07-28View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44407 2021-07-28View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44408 2021-07-28View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44407 2021-07-28View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44408 2021-07-28View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44406 2021-07-27View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44407 2021-07-27View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44406 2021-07-27View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44407 2021-07-27View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44406 2021-07-27View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44407 2021-07-27View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44406 2021-07-27View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44407 2021-07-27View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44405 2021-07-26View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44406 2021-07-26View all with same reporting date 10-Q Quarterly report [Sections 13 or 15(d)]Open document FilingOpen filing 44405 2021-06-30View all with same reporting date 10-Q Quarterly report [Sections 13 or 15(d)]Open document FilingOpen filing 44406 2021-06-30View all with same reporting date 3 Initial statement of beneficial ownership of securitiesOpen document FilingOpen filing 44404 2021-07-27View all with same reporting date 4 Initial statement of beneficial ownership of securitiesOpen document FilingOpen filing 44405 2021-07-27View all with same reporting date 8-K Current reportOpen document FilingOpen filing 44404 2021-07-27View all with same reporting date 8-K Current reportOpen document FilingOpen filing 44405 2021-07-27View all with same reporting date 2.02 - Results of Operations and Financial Condition 2.02 - Results of Operations and Financial Condition 9.01 - Financial Statements and Exhibits 9.01 - Financial Statements and Exhibits4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44398 2021-07-21View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44399 2021-07-21View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44389 2021-07-08View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44390 2021-07-08View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44389 2021-07-08View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44390 2021-07-08View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44386 2021-07-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44387 2021-07-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44386 2021-07-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44387 2021-07-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44386 2021-07-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44387 2021-07-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44386 2021-07-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44387 2021-07-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44386 2021-07-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44387 2021-07-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44386 2021-07-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44387 2021-07-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44386 2021-07-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44387 2021-07-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44386 2021-07-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44387 2021-07-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44386 2021-07-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44387 2021-07-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44386 2021-07-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44387 2021-07-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44385 2021-07-06View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44386 2021-07-06View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44385 2021-07-06View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44386 2021-07-06View all with same reporting date 8-K Current reportOpen document FilingOpen filing 44385 2021-07-07View all with same reporting date 8-K Current reportOpen document FilingOpen filing 44386 2021-07-07View all with same reporting date 8.01 - Other Events (The registrant can use this Item to report events that are not specifically called for by Form 8-K, that the registrant considers to be of importance to security holders.) 8.01 - Other Events (The registrant can use this Item to report events that are not specifically called for by Form 8-K, that the registrant considers to be of importance to security holders.)4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44385 2021-07-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44386 2021-07-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44385 2021-07-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44386 2021-07-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44383 2021-07-02View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44384 2021-07-02View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44378 2021-07-01View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44379 2021-07-01View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44378 2021-07-01View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44379 2021-07-01View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44378 2021-06-30View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44379 2021-06-30View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44378 2021-06-29View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44379 2021-06-29View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44376 2021-06-25View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44377 2021-06-25View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44375 2021-06-25View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44376 2021-06-25View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44375 2021-06-25View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44376 2021-06-25View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44375 2021-06-25View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44376 2021-06-25View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44375 2021-06-25View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44376 2021-06-25View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44375 2021-06-25View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44376 2021-06-25View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44364 2021-06-16View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44365 2021-06-16View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44358 2021-06-09View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44359 2021-06-09View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44358 2021-06-09View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44359 2021-06-09View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44357 2021-06-08View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44358 2021-06-08View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44357 2021-06-08View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44358 2021-06-08View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44356 2021-06-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44357 2021-06-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44356 2021-06-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44357 2021-06-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44356 2021-06-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44357 2021-06-07View all with same reporting date 4 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44356 2021-06-07View all with same reporting date 5 Statement of changes in beneficial ownership of securitiesOpen document FilingOpen filing 44357 2021-06-07View all with same reporting date Showing 1 to 32 of 1,000 entries Showing 1 to 32 of 1,000 entries Data source: CIK0001652044.json Data source: CIK0001652044.json Investor Resources Investor Resources How to Use EDGAR How to Use EDGAR Learn how to use EDGAR to research public filings by public companies, mutual funds, ETFs, some annuities, and more. Learn how to use EDGAR to research public filings by public companies, mutual funds, ETFs, some annuities, and more. Before you Invest, Investor.gov Before you Invest, Investor.gov Get answers to your investing questions from the SEC's website dedicated to retail investors Get answers to your investing questions from the SEC's website dedicated to retail investors

0 comments on commit f1081d5

 Lock conversation

￼

Write Preview

Add heading textAdd bold text, <Ctrl+b>Add italic text, <Ctrl+i>

Add a quote, <Ctrl+Shift+.>Add code, <Ctrl+e>Add a link, <Ctrl+k>

Add a bulleted list, <Ctrl+Shift+8>Add a numbered list, <Ctrl+Shift+7>Add a task list, <Ctrl+Shift+l>

Directly mention a user or teamReference an issue, pull request, or discussionAdd saved reply

Attach files by dragging & dropping, selecting or pasting them.Styling with Markdown is supported

Comment on this commit

Unsubscribe 

You’re receiving notifications because you’re watching this repository.

Footer

© 2022 GitHub, Inc.

Footer navigation

Terms

Privacy

Security

Status

Docs

Contact GitHub

Pricing

API

Training

Blog

About

instructions · zakwarlord7/zakwarlord7@f1081d5

Web search

Copy

Copyright 2005-09-17,17:00:00:00 :;-17:00:00:00CSMT](All rights reserved. MIT license).
use serde::Deserialize;
table {mso-displayed-decimal-separator:"."; mso-displayed-thousand-separator:",";} tr {mso-height-source:auto;} col {mso-width-source:auto;} td {padding-top:1px; padding-right:1px; padding-left:1px; mso-ignore:padding; color:black; font-size:11.0pt; font-weight:400; font-style:normal; text-decoration:none; font-family:Calibri, sans-serif; mso-font-charset:0; text-align:general; vertical-align:bottom; border:none; white-space:nowrap; mso-rotate:0;} .xl48 {font-size:13.5pt; font-weight:700; font-family:"Courier New"; mso-generic-font-family:auto; mso-font-charset:0;} .xl49 {font-size:13.5pt;} .xl50 {font-size:13.5pt; font-weight:700; font-family:"Courier New"; mso-generic-font-family:auto; mso-font-charset:0; text-align:left;} .xl51 {font-size:13.5pt; font-weight:700; font-family:"Courier New"; mso-generic-font-family:auto; mso-font-charset:0; text-align:right;} .xl52 {font-family:Arial; mso-generic-font-family:auto; mso-font-charset:1; border-top:.5pt solid #CCCCCC; border-right:.5pt solid #CCCCCC; border-bottom:.5pt solid #CCCCCC; border-left:.5pt solid black;} .xl53 {font-family:Arial; mso-generic-font-family:auto; mso-font-charset:1; border:.5pt solid #CCCCCC;} .xl54 {font-size:9.0pt; font-family:Arial; mso-generic-font-family:auto; mso-font-charset:1; border-top:.5pt solid #CCCCCC; border-right:.5pt solid #CCCCCC; border-bottom:.5pt solid #CCCCCC; border-left:.5pt solid black;} .xl55 {font-family:Arial; mso-generic-font-family:auto; mso-font-charset:1; border-top:.5pt solid #CCCCCC; border-right:.5pt solid #CCCCCC; border-bottom:.5pt solid black; border-left:.5pt solid black;} .xl56 {font-family:Arial; mso-generic-font-family:auto; mso-font-charset:1; border-top:.5pt solid #CCCCCC; border-right:.5pt solid #CCCCCC; border-bottom:.5pt solid black; border-left:.5pt solid #CCCCCC;} .xl58 {font-family:Arial; mso-generic-font-family:auto; mso-font-charset:1; border-top:.5pt solid #CCCCCC; border-right:.5pt solid #CCCCCC; border-bottom:2.0pt double black; border-left:.5pt solid black;} .xl59 {font-family:Arial; mso-generic-font-family:auto; mso-font-charset:1; border-top:.5pt solid #CCCCCC; border-right:.5pt solid #CCCCCC; border-bottom:2.0pt double black; border-left:.5pt solid #CCCCCC;} .xl60 {font-size:9.0pt; font-weight:700; font-family:Arial; mso-generic-font-family:auto; mso-font-charset:1; border-top:.5pt solid #CCCCCC; border-right:.5pt solid #CCCCCC; border-bottom:.5pt solid #CCCCCC; border-left:.5pt solid black;} .xl66 {font-size:13.5pt; font-weight:700; font-family:"Courier New"; mso-generic-font-family:auto; mso-font-charset:0; white-space:normal;} .xl67 {font-family:Arial; mso-generic-font-family:auto; mso-font-charset:1; text-align:right; border-top:.5pt solid #CCCCCC; border-right:.5pt solid black; border-bottom:.5pt solid #CCCCCC; border-left:.5pt solid #CCCCCC;} .xl68 {font-family:Arial; mso-generic-font-family:auto; mso-font-charset:1; text-align:right; border-top:.5pt solid #CCCCCC; border-right:.5pt solid black; border-bottom:.5pt solid black; border-left:.5pt solid #CCCCCC;} .xl69 {font-family:Arial; mso-generic-font-family:auto; mso-font-charset:1; text-align:right; border-top:.5pt solid #CCCCCC; border-right:.5pt solid black; border-bottom:2.0pt double black; border-left:.5pt solid #CCCCCC;} .xl79 {color:#0563C1; text-decoration:underline; text-underline-style:single; white-space:normal;} .xl80 {color:#24292F; font-family:-Apple-System; mso-generic-font-family:auto; mso-font-charset:1;} .xl88 {font-family:Arial; mso-generic-font-family:auto; mso-font-charset:1; text-align:left; border-top:.5pt solid #CCCCCC; border-right:.5pt solid black; border-bottom:2.0pt double black; border-left:.5pt solid #CCCCCC;} .xl91 {font-family:Arial; mso-generic-font-family:auto; mso-font-charset:1; text-align:right; vertical-align:middle; border-top:2.0pt double black; border-right:.5pt solid #CCCCCC; border-bottom:none; border-left:none; white-space:normal;} .xl92 {font-family:Arial; mso-generic-font-family:auto; mso-font-charset:1; text-align:right; vertical-align:middle; border-top:none; border-right:.5pt solid #CCCCCC; border-bottom:none; border-left:none; white-space:normal;} .xl93 {font-family:Arial; mso-generic-font-family:auto; mso-font-charset:1; text-align:right; vertical-align:middle; border-top:none; border-right:.5pt solid #CCCCCC; border-bottom:.5pt solid #CCCCCC; border-left:none; white-space:normal;} .xl94 {font-family:Arial; mso-generic-font-family:auto; mso-font-charset:1; text-align:right; vertical-align:middle; border-top:2.0pt double black; border-right:none; border-bottom:.5pt solid #CCCCCC; border-left:.5pt solid black; white-space:normal;} .xl95 {font-family:Arial; mso-generic-font-family:auto; mso-font-charset:1; text-align:right; vertical-align:middle; border-top:2.0pt double black; border-right:none; border-bottom:.5pt solid #CCCCCC; border-left:none; white-space:normal;} .xl96 {font-family:Arial; mso-generic-font-family:auto; mso-font-charset:1; text-align:right; vertical-align:middle; border-top:2.0pt double black; border-right:.5pt solid #CCCCCC; border-bottom:.5pt solid #CCCCCC; border-left:none; white-space:normal;} .xl97 {font-family:Arial; mso-generic-font-family:auto; mso-font-charset:1; text-align:left; vertical-align:top; border-top:2.0pt double black; border-right:none; border-bottom:.5pt solid #CCCCCC; border-left:.5pt solid black; white-space:normal;} .xl98 {font-family:Arial; mso-generic-font-family:auto; mso-font-charset:1; text-align:left; vertical-align:top; border-top:2.0pt double black; border-right:none; border-bottom:.5pt solid #CCCCCC; border-left:none; white-space:normal;} $70,842,743,866.00 Taxable Marital Status:
Exemptions/AllowancesFederal:TX:Gross PayStatutoryFederal Income TaxSocial Security TaxMedicare TaxNet PayCHECKINGNet CheckYour federal taxable wages this period are $ALPHABET INCOME1600 AMPIHTHEATRE PARKWAY MOUNTAIN VIEW CA 94043Deposited to the account OfPLEASE READ THE IMPORTANT DISCLOSURES BELOWBased on facts as set forth in.The U.S. Internal Revenue Code of 1986, as amended, the Treasury Regulations promulgated thereunder, published pronouncements of the Internal Revenue Service, which may be cited or used as precedents, and case law, any of which may be changed at any time with retroactive effect. No opinion is expressed on any matters other than those specifically referred to above.EMPLOYER IDENTIFICATION NUMBER: 61-1767919[DRAFT FORM OF TAX OPINION]ORIGINAL REPORTIncome, Rents, & RoyaltyINCOME STATEMENTGOOGL_income-statement_Quarterly_As_Originally_ReportedGross ProfitTotal Revenue as Reported, SupplementalOther RevenueCost of RevenueCost of Goods and ServicesOperating Income/ExpensesSelling, General and Administrative ExpensesGeneral and Administrative ExpensesSelling and Marketing ExpensesResearch and Development ExpensesTotal Operating Profit/LossNon-Operating Income/Expenses, TotalTotal Net Finance Income/ExpenseNet Interest Income/ExpenseInterest Expense Net of Capitalized InterestInterest IncomeNet Investment IncomeGain/Loss on Investments and Other Financial InstrumentsIncome from Associates, Joint Ventures and Other Participating InterestsGain/Loss on Foreign ExchangeIrregular Income/ExpensesOther Irregular Income/ExpensesOther Income/Expense, Non-OperatingPretax IncomeProvision for Income TaxNet Income from Continuing OperationsNet Income after Extraordinary Items and Discontinued OperationsNet Income after Non-Controlling/Minority InterestsNet Income Available to Common StockholdersDiluted Net Income Available to Common StockholdersIncome Statement Supplemental SectionReported Normalized and Operating Income/Expense Supplemental SectionTotal Revenue as Reported, SupplementalTotal Operating Profit/Loss as Reported, SupplementalReported Effective Tax RateReported Normalized IncomeReported Normalized Operating ProfitOther Adjustments to Net Income Available to Common StockholdersDiscontinued OperationsBasic EPSBasic EPS from Continuing OperationsBasic EPS from Discontinued OperationsDiluted EPSDiluted EPS from Continuing OperationsDiluted EPS from Discontinued OperationsBasic Weighted Average Shares OutstandingDiluted Weighted Average Shares OutstandingReported Normalized Diluted EPSBasic EPSDiluted EPSBasic WASODiluted WASOFiscal year end September 28th., 2022. | USD31622,6:39 PMMorningstar.com Intraday Fundamental Portfolio View Print Report3/6/2022 at 6:37 PMGOOGL_income-statement_Quarterly_As_Originally_ReportedCash Flow from Operating Activities, IndirectNet Cash Flow from Continuing Operating Activities, IndirectCash Generated from Operating ActivitiesIncome/Loss before Non-Cash AdjustmentTotal Adjustments for Non-Cash ItemsDepreciation, Amortization and Depletion, Non-Cash AdjustmentDepreciation and Amortization, Non-Cash AdjustmentDepreciation, Non-Cash AdjustmentAmortization, Non-Cash AdjustmentStock-Based Compensation, Non-Cash AdjustmentTaxes, Non-Cash AdjustmentInvestment Income/Loss, Non-Cash AdjustmentGain/Loss on Financial Instruments, Non-Cash AdjustmentOther Non-Cash ItemsChanges in Operating CapitalChange in Trade and Other ReceivablesChange in Trade/Accounts ReceivableChange in Other Current AssetsChange in Payables and Accrued ExpensesChange in Trade and Other PayablesChange in Trade/Accounts PayableChange in Accrued ExpensesChange in Deferred Assets/LiabilitiesChange in Other Operating CapitalChange in Prepayments and DepositsCash Flow from Investing ActivitiesCash Flow from Continuing Investing ActivitiesPurchase/Sale and Disposal of Property, Plant and Equipment, NetPurchase of Property, Plant and EquipmentSale and Disposal of Property, Plant and EquipmentPurchase/Sale of Business, NetPurchase/Acquisition of BusinessPurchase/Sale of Investments, NetPurchase of InvestmentsSale of InvestmentsOther Investing Cash FlowPurchase/Sale of Other Non-Current Assets, NetSales of Other Non-Current AssetsCash Flow from Financing ActivitiesCash Flow from Continuing Financing ActivitiesIssuance of/Payments for Common Stock, NetPayments for Common StockProceeds from Issuance of Common StockIssuance of/Repayments for Debt, NetIssuance of/Repayments for Long Term Debt, NetProceeds from Issuance of Long Term DebtRepayments for Long Term DebtProceeds from Issuance/Exercising of Stock Options/WarrantsOther Financing Cash FlowCash and Cash Equivalents, End of PeriodChange in CashEffect of Exchange Rate ChangesCash and Cash Equivalents, Beginning of PeriodCash Flow Supplemental SectionChange in Cash as Reported, SupplementalIncome Tax Paid, SupplementalCash and Cash Equivalents, Beginning of Period12 Months Ended_________________________________________________________Income StatementUSD in "000'"sRepayments for Long Term DebtCosts and expenses:Cost of revenuesResearch and developmentSales and marketingGeneral and administrativeEuropean Commission finesTotal costs and expensesIncome from operationsOther income (expense), netIncome before income taxesProvision for income taxesNet income*include interest paid, capital obligation, and underweightingBasic net income per share of Class A and B common stock and Class C capital stock (in dollars par share)Diluted net income per share of Class A and Class B common stock and Class C capital stock (in dollars par share)For Paperwork Reduction Act Notice, see the seperate Instructions.rate112.27569887160061-176791988-1303491TTM$146,698,000,000.00 $257,637,000,000.00 $257,637,000,000.00 -1.10939E+11-1.10939E+11-67984000000-36422000000-13510000000-22912000000-31562000000787140000001202000000011530000001153000000-34600000014990000001236400000012270000000334000000-24000000000-149700000090734000000-1470100000076033000000760330000007603300000076033000000760330000002.57637E+11787140000000.162113.88113.88112.2112.2667650000677674000113.88112.2667650000677674000Advice number:NO State Incorne Taxunits67467800070842743866$70,842,743,866.00 Q4 2021$42,337,000,000.00 $75,325,000,000.00 $75,325,000,000.00 -32988000000-32988000000-20452000000-11744000000-4140000000-7604000000-8708000000218850000002517000000261000000261000000-1170000003780000002364000000247800000049000000-16300000000-10800000024402000000-37600000002064200000020642000000206420000002064200000020642000000753250000002188500000031.1531.1230.6930.6766266400067249300031.1530.69662664000672493000Q4 202124934000000249340000002493400000020642000000651700000034390000003439000000321500000022400000039540000001616000000-2478000000-2478000000-14000000-2225000000-5819000000-5819000000-3990000006994000000115700000011570000005837000000368000000-3369000000-11016000000-11016000000-6383000000-6383000000-385000000-385000000-4348000000-4086000000036512000000100000000-16511000000-16511000000-134730000001347300000011500000011500000062500000006365000000292300000002094500000025930000000181000000000)2.3719E+13277400000013412000000Pay date:_70842743866Q2 2021$35,653,000,000.00 $61,880,000,000.00 $61,880,000,000.00 -26227000000-26227000000-16292000000-8617000000-3341000000-5276000000-7675000000193610000002624000000313000000313000000-760000003890000002924000000288300000092000000-51000000-61300000021985000000-3460000000185250000001852500000018525000000185250000001852500000061880000000193610000000.15727.6927.6927.2627.2666895800067961200027.6927.26668958000679612000Q2 20213749700000021890000000218900000001852500000042360000002945000000294500000027300000002150000003803000000379000000-2883000000-2883000000-8000000-871000000-3661000000-3661000000-1990000004074000000-130000000-1300000004204000000-3000000-1082000000-9074000000-9074000000-5496000000-5496000000-308000000-308000000-3293000000-249490000002165600000023000000-15991000000-15991000000-12796000000-12796000000-1042000000-10420000006699000000-7741000000-245300000030000000023630000000-31750000001830000002.6622E+13-2992000000PLEASE READ THE IMPORTANT DISCLOSURES BELOW

FEDERAL RESERVE MASTER SUPPLIER ACCOUNT 31000053-052101023 COD
633-44-1725 Zachryiixixiiiwood@gmail.com 47-2041-6547 111000614 31000053
PNC Bank PNC Bank Business Tax I.D. Number: 633441725
CIF Department (Online Banking) Checking Account: 47-2041-6547
P7-PFSC-04-F Business Type: Sole Proprietorship/Partnership Corporation
500 First Avenue ALPHABET
Pittsburgh, PA 15219-3128 5323 BRADFORD DR
NON-NEGOTIABLE DALLAS TX 75235 8313
ZACHRY, TYLER, WOOD
4/18/2022 650-2530-000 469-697-4300
SIGNATURE Time Zone: Eastern Central Mountain Pacific
Investment Products  • Not FDIC Insured  • No Bank Guarantee  • May Lose ValueQ1 2021$31,211,000,000.00 $55,314,000,000.00 $55,314,000,000.00 ($24,103,000,000.00)-24103000000($14,774,000,000.00)-7289000000-2773000000-4516000000-7485000000164370000004846000000269000000269000000-76000000345000000486900000047510000005000000113000000-29200000021283000000-3353000000179300000001793000000017930000000179300000001793000000055314000000164370000000.15826.6326.6326.2926.2967322000068207100026.6326.29673220000682071000Q1 202131211000000192890000001928900000017930000000259200000027530000002753000000252500000022800000037450000001100000000-4751000000-4751000000-255000000-1233000000279400000027940000007000000-4956000000-982000000-982000000-3974000000137000000785000000-5383000000-5383000000-5942000000-5942000000-1666000000-16660000002195000000-370720000003926700000030000000-13606000000-13606000000-11395000000-11395000000-37000000-37000000900000000-937000000-21840000001000000026622000000300000000-1430000002.6465E+13xxxxxxxx6547Q4 2020308180000005689800000056898000000-26080000000-26080000000($15,167,000,000.00)-8145000000-2831000000-5314000000-7022000000156510000003038000000333000000333000000-5300000038600000035300000003262000000355000000-8700000000-82500000018689000000-34620000001522700000015227000000152270000001522700000015227000000568980000001565100000022.5422.4622.322.2367558100068296900022.5422.3675581000682969000Q4 202030818000000226770000002267700000015227000000574800000037250000003725000000353900000018600000032230000001670000000-3262000000-32620000003920000001702000000-5445000000-5445000000-73800000069380000009630000009630000005975000000207000000740000000-7281000000-7281000000-5479000000-5479000000-370000000-370000000-1375000000-3695500000035580000000-57000000-9270000000-9270000000-7904000000-7904000000-57000000-570000000-57000000-1647000000338000000000)2646500000061260000002100000002.0129E+136336000000-4990000000Q4 2019Dec. 31, 201916185771896260181846495511697127626342315394192890000001928900000019289000000PLEASE READ THE IMPORTANT DISCLOSURES BELOW

FEDERAL RESERVE MASTER SUPPLIER ACCOUNT 31000053-052101023 COD
633-44-1725 Zachryiixixiiiwood@gmail.com 47-2041-6547 111000614 31000053
PNC Bank PNC Bank Business Tax I.D. Number: 633441725
CIF Department (Online Banking) Checking Account: 47-2041-6547
P7-PFSC-04-F Business Type: Sole Proprietorship/Partnership Corporation
500 First Avenue ALPHABET
Pittsburgh, PA 15219-3128 5323 BRADFORD DR
NON-NEGOTIABLE DALLAS TX 75235 8313
ZACHRY, TYLER, WOOD
4/18/2022 650-2530-000 469-697-4300
SIGNATURE Time Zone: Eastern Central Mountain Pacific
Investment Products  • Not FDIC Insured  • No Bank Guarantee  • May Lose Valueyear to date7569887160000.00%Q3 2020$25,056,000,000.00 $46,173,000,000.00 $46,173,000,000.00 ($21,117,000,000.00)-21117000000-1384300000000.00%-6987000000-2756000000-4231000000-6856000000112130000002146000000412000000412000000-480000004600000001957000000201500000026000000-8400000000-22300000013359000000-2112000000112470000001124700000011247000000112470000001124700000046173000000112130000000.15816.5516.5516.416.467944900068585100016.5516.4679449000685851000NON-NEGOTIABLEZACHRY T.5323DALLASOther Benefits andInformationPto BalanceTotal Work HrsImportant NotesCOMPANY PH Y: 650-253-0000BASIS OF PAY: BASIC/DILUTED EPSYOUR BASIC/DILUTED EPS RATE HAS BEEN CHANGED FROM 0.001 TO 112.20 PAR SHARE VALUEAdvice number:Pay date:_xxxxxxxx6547NON-NEGOTIABLEQ2 20201974400000000.00%3829700000000.00%3829700000000.00%-1855300000000.00%-18553000000($13,361,000,000.00)-6486000000-2585000000-3901000000-687500000063830000001894000000420000000420000000-1300000043300000016960000001842000000-54000000-9200000000-2220000008277000000-1318000000695900000069590000006959000000695900000069590000003829700000063830000000.15910.2110.2110.1310.1368176800068702400010.2110.13681768000687024000Print|______________________________________________________________________________________________________________________DOLLARS [OBJ]FeaturesTaxable Marital Status:
Exemptions/AllowancesZACHRY T.|ESTATE OFDetaile on5323|BackFederal:|FOR_____________________________________DALLASTX:NO State Incorne Tax|PLEASE READ THE IMPORTANT DISCLOSURES BELOWrateunitsyear to dateOther Benefits and||AUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATURE.EXECUTOR/112.26746780007569887160000.00%Information|FEDERAL RESERVE MASTER SUPPLIER ACCOUNT 31000053-052101023 COD|{}.ADMINISTRATORPto Balance||AUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATURE.PERSONAL/Total Work Hrs|633-44-1725 Zachryiixixiiiwood@gmail.com 47-2041-6547 111000614 31000053|{}.REPRESENTATIVEGross Pay75698871600Important Notes|PNC Bank PNC Bank Business Tax I.D. Number: 633441725|AUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATURE.TRUSTEE||COMPANY PH Y: 650-253-0000|CIF Department (Online Banking) Checking Account: 47-2041-6547|Deposited to the account Of xxxxxxxx6547StatutoryBASIS OF PAY: BASIC/DILUTED EPS|P7-PFSC-04-F Business Type: Sole Proprietorship/Partnership CorporationFederal Income Tax|500 First Avenue ALPHABETSocial Security Tax|Pittsburgh, PA 15219-3128 5323 BRADFORD DRYOUR BASIC/DILUTED EPS RATE HAS BEEN CHANGED FROM 0.001 TO 112.20 PAR SHARE VALUE|Medicare Tax|NON-NEGOTIABLENet Pay7084274386670842743866CHECKINGNet Check$70,842,743,866.00 Your federal taxable wages this period are $Skip to contentALPHABET INCOMEAdvice number:Search or jump to…1600 AMPIHTHEATRE PARKWAY MOUNTAIN VIEW CA 94043Pay date:_Pull requestsIssuesDeposited to the account Ofxxxxxxxx6547MarketplacePLEASE READ THE IMPORTANT DISCLOSURES BELOW

FEDERAL RESERVE MASTER SUPPLIER ACCOUNT 31000053-052101023 COD
633-44-1725 Zachryiixixiiiwood@gmail.com 47-2041-6547 111000614 31000053
PNC Bank PNC Bank Business Tax I.D. Number: 633441725
CIF Department (Online Banking) Checking Account: 47-2041-6547
P7-PFSC-04-F Business Type: Sole Proprietorship/Partnership Corporation
500 First Avenue ALPHABET
Pittsburgh, PA 15219-3128 5323 BRADFORD DR
NON-NEGOTIABLE DALLAS TX 75235 8313
ZACHRY, TYLER, WOOD
4/18/2022 650-2530-000 469-697-4300
SIGNATURE Time Zone: Eastern Central Mountain Pacific
Investment Products  • Not FDIC Insured  • No Bank Guarantee  • May Lose ValueExploreNON-NEGOTIABLE PLEASE READ THE IMPORTANT DISCLOSURES BELOW#NAME?Your account has been flagged.Because of that, your profile is hidden from the public. If you believe this is a mistake, contact support to have your account status reviewed.zakwarlord7/Supremer-GalaxyPublicCodeIssuesPull requestsActionsProjectsWikiSecurityInsightsSettingsSupremer-Galaxy/Build and Deploy#NAME?zakwarlord7 Update Build and DeployLatest commit 761ec08 now History 1 contributor215 lines (205 sloc)  14.4 KBBased on facts as set forth in.The U.S. Internal Revenue Code of 1986, as amended, the Treasury Regulations promulgated thereunder, published pronouncements of the Internal Revenue Service, which may be cited or used as precedents, and case law, any of which may be changed at any time with retroactive effect. No opinion is expressed on any matters other than those specifically referred to above.Get answers to your investing questions from the SEC's website dedicated to retail investors :941EMPLOYER IDENTIFICATION NUMBER: 61-1767919ALPHABET1600 AMPITHEATRE PARKWAYPeriod Ending:MOUNTAIN VIEW, C.A., 94043Pay Date:[DRAFT FORM OF TAX OPINION]Taxable Marital Status:
Exemptions/AllowancesZACHRY T.5323Federal:DALLASTX:NO State Income Taxrateunitsyear to dateOther Benefits and112.26746780007569887160000.00%InformationPto BalanceTotal Work HrsGross Pay75698871600Important NotesCOMPANY PH Y: 650-253-0000StatutoryBASIS OF PAY: BASIC/DILUTED EPSFederal Income TaxSocial Security TaxYOUR BASIC/DILUTED EPS RATE HAS BEEN CHANGED FROM 0.001 TO 112.20 PAR SHARE VALUEORIGINAL REPORTMedicare TaxIncome, Rents, & RoyaltyNet Pay7084274386670842743866INCOME STATEMENT61-1767919CHECKING88-1303491Net Check$70,842,743,866.00 GOOGL_income-statement_Quarterly_As_Originally_ReportedTTMQ4 2021Q2 2021Q1 2021Q4 2020Q3 2020Q2 2020Your federal taxable wages this period are $ALPHABET INCOMEAdvice number:Gross Profit$146,698,000,000.00 $42,337,000,000.00 $35,653,000,000.00 $31,211,000,000.00 30818000000$25,056,000,000.00 1974400000000.00%1600 AMPIHTHEATRE PARKWAY MOUNTAIN VIEW CA 94043Pay date:Total Revenue as Reported, Supplemental$257,637,000,000.00 $75,325,000,000.00 $61,880,000,000.00 $55,314,000,000.00 56898000000$46,173,000,000.00 3829700000000.00%Deposited to the account Ofxxxxxxxx6547$257,637,000,000.00 $75,325,000,000.00 $61,880,000,000.00 $55,314,000,000.00 56898000000$46,173,000,000.00 3829700000000.00%PLEASE READ THE IMPORTANT DISCLOSURES BELOWOther RevenueFEDERAL RESERVE MASTER SUPPLIER ACCOUNT 31000053-052101023 CODCost of Revenue-1.10939E+11-32988000000-26227000000($24,103,000,000.00)-26080000000($21,117,000,000.00)-1855300000000.00%633-44-1725 Zachryiixixiiiwood@gmail.com 47-2041-6547 111000614 31000053Cost of Goods and Services-1.10939E+11-32988000000-26227000000-24103000000-26080000000-21117000000-18553000000PNC Bank PNC Bank Business Tax I.D. Number: 633441725Operating Income/Expenses-67984000000-20452000000-16292000000($14,774,000,000.00)($15,167,000,000.00)-1384300000000.00%($13,361,000,000.00)CIF Department (Online Banking) Checking Account: 47-2041-6547Selling, General and Administrative Expenses-36422000000-11744000000-8617000000-7289000000-8145000000-6987000000-6486000000P7-PFSC-04-F Business Type: Sole Proprietorship/Partnership CorporationGeneral and Administrative Expenses-13510000000-4140000000-3341000000-2773000000-2831000000-2756000000-2585000000500 First Avenue ALPHABETSelling and Marketing Expenses-22912000000-7604000000-5276000000-4516000000-5314000000-4231000000-3901000000Pittsburgh, PA 15219-3128 5323 BRADFORD DRResearch and Development Expenses-31562000000-8708000000-7675000000-7485000000-7022000000-6856000000-6875000000NON-NEGOTIABLE DALLAS TX 75235 8313Total Operating Profit/Loss7871400000021885000000193610000001643700000015651000000112130000006383000000ZACHRY, TYLER, WOODNon-Operating Income/Expenses, Total120200000002517000000262400000048460000003038000000214600000018940000004/18/2022 650-2530-000 469-697-4300Total Net Finance Income/Expense1153000000261000000313000000269000000333000000412000000420000000SIGNATURE Time Zone: Eastern Central Mountain PacificNet Interest Income/Expense1153000000261000000313000000269000000333000000412000000420000000Investment Products  • Not FDIC Insured  • No Bank Guarantee  • May Lose Value"NON-NEGOTIABLEPLEASE READ THE IMPORTANT DISCLOSURES BELOWInterest Expense Net of Capitalized Interest-346000000-117000000-76000000-76000000-53000000-48000000-13000000|Security enhanced document.  See back for detailsNO.Interest Income1499000000378000000389000000345000000386000000460000000433000000|[OBJ][OBJ]PNCBANKNet Investment Income12364000000236400000029240000004869000000353000000019570000001696000000|PNC Bank N.A.7170-2188/719Gain/Loss on Investments and Other Financial Instruments12270000000247800000028830000004751000000326200000020150000001842000000|    DATE____________________________________7364Income from Associates, Joint Ventures and Other Participating Interests3340000004900000092000000500000035500000026000000-54000000|Gain/Loss on Foreign Exchange-240000000-163000000-51000000113000000-87000000-84000000-92000000|PAY TO THEIrregular Income/Expenses00000|ORDER OF______________________________________________________________________________________________________________|$**22677000000000&00/100cents||Other Irregular Income/Expenses00000|    Security||Other Income/Expense, Non-Operating-1497000000-108000000-613000000-292000000-825000000-223000000-222000000|______________________________________________________________________________________________________________________DOLLARS [OBJ] Features Pretax Income9073400000024402000000219850000002128300000018689000000133590000008277000000|ESTATE OF                                                                                             DetaileProvision for Income Tax-14701000000-3760000000-3460000000-3353000000-3462000000-2112000000-1318000000|                                                                                                     on Back.Net Income from Continuing Operations7603300000020642000000185250000001793000000015227000000112470000006959000000|FOR_____________________________________Net Income after Extraordinary Items and Discontinued Operations7603300000020642000000185250000001793000000015227000000112470000006959000000|AUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATURE.EXECUTOR/Net Income after Non-Controlling/Minority Interests7603300000020642000000185250000001793000000015227000000112470000006959000000|{}.ADMINISTRATORNet Income Available to Common Stockholders7603300000020642000000185250000001793000000015227000000112470000006959000000|AUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATURE.PERSONAL/Diluted Net Income Available to Common Stockholders7603300000020642000000185250000001793000000015227000000112470000006959000000|{}.REPRESENTATIVEIncome Statement Supplemental Section|AUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATURE.TRUSTEE||Reported Normalized and Operating Income/Expense Supplemental Section|Deposited to the account Of xxxxxxxx6547Total Revenue as Reported, Supplemental2.57637E+11753250000006188000000055314000000568980000004617300000038297000000|PLEASE READ THE IMPORTANT DISCLOSURES BELOWTotal Operating Profit/Loss as Reported, Supplemental7871400000021885000000193610000001643700000015651000000112130000006383000000|Reported Effective Tax Rate0.1620.1570.1580.1580.159|FEDERAL RESERVE MASTER SUPPLIER ACCOUNT 31000053-052101023 CODReported Normalized Income|Reported Normalized Operating Profit|633-44-1725 Zachryiixixiiiwood@gmail.com 47-2041-6547 111000614 31000053Other Adjustments to Net Income Available to Common Stockholders|PNC Bank PNC Bank Business Tax I.D. Number: 633441725Discontinued Operations|CIF Department (Online Banking) Checking Account: 47-2041-6547Basic EPS113.8831.1527.6926.6322.5416.5510.21|P7-PFSC-04-F Business Type: Sole Proprietorship/Partnership CorporationBasic EPS from Continuing Operations113.8831.1227.6926.6322.4616.5510.21|500 First Avenue ALPHABETBasic EPS from Discontinued Operations|Pittsburgh, PA 15219-3128 5323 BRADFORD DRDiluted EPS112.230.6927.2626.2922.316.410.13GOOGL_income-statement_Quarterly_As_Originally_ReportedTTMQ4 2021Q2 2021Q1 2021Q4 2020Q3 2020Q2 2020Diluted EPS from Continuing Operations112.230.6727.2626.2922.2316.410.13Gross Profit$146,698,000,000.00 $42,337,000,000.00 $35,653,000,000.00 $31,211,000,000.00 30818000000$25,056,000,000.00 1974400000000.00%Diluted EPS from Discontinued OperationsTotal Revenue as Reported, Supplemental$257,637,000,000.00 $75,325,000,000.00 $61,880,000,000.00 $55,314,000,000.00 56898000000$46,173,000,000.00 3829700000000.00%Basic Weighted Average Shares Outstanding667650000662664000668958000673220000675581000679449000681768000$257,637,000,000.00 $75,325,000,000.00 $61,880,000,000.00 $55,314,000,000.00 56898000000$46,173,000,000.00 3829700000000.00%Diluted Weighted Average Shares Outstanding677674000672493000679612000682071000682969000685851000687024000Other RevenueReported Normalized Diluted EPSCost of Revenue-1.11E+11-32988000000-26227000000($24,103,000,000.00)-26080000000($21,117,000,000.00)-1855300000000.00%Basic EPS113.8831.1527.6926.6322.5416.5510.21Cost of Goods and Services-1.11E+11-32988000000-26227000000-24103000000-26080000000-21117000000-18553000000Diluted EPS112.230.6927.2626.2922.316.410.13Operating Income/Expenses-67984000000-20452000000-16292000000($14,774,000,000.00)($15,167,000,000.00)-1384300000000.00%($13,361,000,000.00)Basic WASO667650000662664000668958000673220000675581000679449000681768000Selling, General and Administrative Expenses-36422000000-11744000000-8617000000-7289000000-8145000000-6987000000-6486000000Diluted WASO677674000672493000679612000682071000682969000685851000687024000General and Administrative Expenses-13510000000-4140000000-3341000000-2773000000-2831000000-2756000000-2585000000Fiscal year end September 28th., 2022. | USDSelling and Marketing Expenses-22912000000-7604000000-5276000000-4516000000-5314000000-4231000000-3901000000Research and Development Expenses-31562000000-8708000000-7675000000-7485000000-7022000000-6856000000-687500000031622,6:39 PMTotal Operating Profit/Loss7871400000021885000000193610000001643700000015651000000112130000006383000000Morningstar.com Intraday Fundamental Portfolio View Print ReportPrintNon-Operating Income/Expenses, Total12020000000251700000026240000004846000000303800000021460000001894000000Total Net Finance Income/Expense11530000002610000003130000002690000003330000004120000004200000003/6/2022 at 6:37 PMNet Interest Income/Expense1153000000261000000313000000269000000333000000412000000420000000Interest Expense Net of Capitalized Interest-346000000-117000000-76000000-76000000-53000000-48000000-13000000Interest Income1499000000378000000389000000345000000386000000460000000433000000GOOGL_income-statement_Quarterly_As_Originally_ReportedQ4 2021Net Investment Income12364000000236400000029240000004869000000353000000019570000001696000000Cash Flow from Operating Activities, Indirect24934000000Q2 2021Q1 2021Q4 2020Gain/Loss on Investments and Other Financial Instruments12270000000247800000028830000004751000000326200000020150000001842000000Net Cash Flow from Continuing Operating Activities, Indirect24934000000374970000003121100000030818000000Income from Associates, Joint Ventures and Other Participating Interests3340000004900000092000000500000035500000026000000-54000000Cash Generated from Operating Activities24934000000218900000001928900000022677000000Gain/Loss on Foreign Exchange-240000000-163000000-51000000113000000-87000000-84000000-92000000Income/Loss before Non-Cash Adjustment20642000000218900000001928900000022677000000Irregular Income/Expenses00000Total Adjustments for Non-Cash Items6517000000185250000001793000000015227000000Other Irregular Income/Expenses00000Depreciation, Amortization and Depletion, Non-Cash Adjustment3439000000423600000025920000005748000000Other Income/Expense, Non-Operating-1497000000-108000000-613000000-292000000-825000000-223000000-222000000Depreciation and Amortization, Non-Cash Adjustment3439000000294500000027530000003725000000Pretax Income9073400000024402000000219850000002128300000018689000000133590000008277000000Depreciation, Non-Cash Adjustment3215000000294500000027530000003725000000Provision for Income Tax-14701000000-3760000000-3460000000-3353000000-3462000000-2112000000-1318000000Amortization, Non-Cash Adjustment224000000273000000025250000003539000000Net Income from Continuing Operations7603300000020642000000185250000001793000000015227000000112470000006959000000Stock-Based Compensation, Non-Cash Adjustment3954000000215000000228000000186000000Net Income after Extraordinary Items and Discontinued Operations7603300000020642000000185250000001793000000015227000000112470000006959000000Taxes, Non-Cash Adjustment1616000000380300000037450000003223000000Net Income after Non-Controlling/Minority Interests7603300000020642000000185250000001793000000015227000000112470000006959000000Investment Income/Loss, Non-Cash Adjustment-247800000037900000011000000001670000000Net Income Available to Common Stockholders7603300000020642000000185250000001793000000015227000000112470000006959000000Gain/Loss on Financial Instruments, Non-Cash Adjustment-2478000000-2883000000-4751000000-3262000000Diluted Net Income Available to Common Stockholders7603300000020642000000185250000001793000000015227000000112470000006959000000Other Non-Cash Items-14000000-2883000000-4751000000-3262000000Income Statement Supplemental SectionChanges in Operating Capital-2225000000-8000000-255000000392000000Reported Normalized and Operating Income/Expense Supplemental SectionChange in Trade and Other Receivables-5819000000-871000000-12330000001702000000Total Revenue as Reported, Supplemental2.58E+11753250000006188000000055314000000568980000004617300000038297000000Change in Trade/Accounts Receivable-5819000000-36610000002794000000-5445000000Total Operating Profit/Loss as Reported, Supplemental7871400000021885000000193610000001643700000015651000000112130000006383000000Change in Other Current Assets-399000000-36610000002794000000-5445000000Reported Effective Tax Rate0.1620.1570.1580.1580.159Change in Payables and Accrued Expenses6994000000-1990000007000000-738000000Reported Normalized IncomeChange in Trade and Other Payables11570000004074000000-49560000006938000000Reported Normalized Operating ProfitChange in Trade/Accounts Payable1157000000-130000000-982000000963000000Other Adjustments to Net Income Available to Common StockholdersChange in Accrued Expenses5837000000-130000000-982000000963000000Discontinued OperationsChange in Deferred Assets/Liabilities3680000004204000000-39740000005975000000Basic EPS113.8831.1527.6926.6322.5416.5510.21Change in Other Operating Capital-3369000000-3000000137000000207000000Basic EPS from Continuing Operations113.8831.1227.6926.6322.4616.5510.21Change in Prepayments and Deposits-1082000000785000000740000000Basic EPS from Discontinued OperationsCash Flow from Investing Activities-11016000000Diluted EPS112.230.6927.2626.2922.316.410.13Cash Flow from Continuing Investing Activities-11016000000-9074000000-5383000000-7281000000Diluted EPS from Continuing Operations112.230.6727.2626.2922.2316.410.13Purchase/Sale and Disposal of Property, Plant and Equipment, Net-6383000000-9074000000-5383000000-7281000000Diluted EPS from Discontinued OperationsPurchase of Property, Plant and Equipment-6383000000-5496000000-5942000000-5479000000Basic Weighted Average Shares Outstanding667650000662664000668958000673220000675581000679449000681768000Sale and Disposal of Property, Plant and Equipment-5496000000-5942000000-5479000000Diluted Weighted Average Shares Outstanding677674000672493000679612000682071000682969000685851000687024000Purchase/Sale of Business, Net-385000000Reported Normalized Diluted EPSPurchase/Acquisition of Business-385000000-308000000-1666000000-370000000Basic EPS113.8831.1527.6926.6322.5416.5510.21Purchase/Sale of Investments, Net-4348000000-308000000-1666000000-370000000Diluted EPS112.230.6927.2626.2922.316.410.13Purchase of Investments-40860000000-32930000002195000000-1375000000Basic WASO667650000662664000668958000673220000675581000679449000681768000Sale of Investments36512000000-24949000000-37072000000-36955000000Diluted WASO677674000672493000679612000682071000682969000685851000687024000Other Investing Cash Flow100000000216560000003926700000035580000000Fiscal year end September 28th., 2022. | USDPurchase/Sale of Other Non-Current Assets, Net2300000030000000-57000000Sales of Other Non-Current Assets31622,6:39 PMCash Flow from Financing Activities-16511000000Morningstar.com Intraday Fundamental Portfolio View Print ReportPrintCash Flow from Continuing Financing Activities-16511000000-15991000000-13606000000-9270000000Issuance of/Payments for Common Stock, Net-13473000000-15991000000-13606000000-92700000003/6/2022 at 6:37 PMPayments for Common Stock13473000000-12796000000-11395000000-7904000000Proceeds from Issuance of Common Stock-12796000000-11395000000-7904000000Issuance of/Repayments for Debt, Net115000000GOOGL_income-statement_Quarterly_As_Originally_ReportedIssuance of/Repayments for Long Term Debt, Net115000000-1042000000-37000000-57000000Cash Flow from Operating Activities, IndirectQ4 2021Q2 2021Q1 2021Q4 2020Proceeds from Issuance of Long Term Debt6250000000-1042000000-37000000-57000000Net Cash Flow from Continuing Operating Activities, Indirect24934000000374970000003121100000030818000000Repayments for Long Term Debt636500000066990000009000000000Cash Generated from Operating Activities24934000000218900000001928900000022677000000Proceeds from Issuance/Exercising of Stock Options/Warrants2923000000-7741000000-937000000-57000000Income/Loss before Non-Cash Adjustment24934000000218900000001928900000022677000000-2453000000-2184000000-1647000000Total Adjustments for Non-Cash Items20642000000185250000001793000000015227000000Depreciation, Amortization and Depletion, Non-Cash Adjustment6517000000423600000025920000005748000000Other Financing Cash FlowDepreciation and Amortization, Non-Cash Adjustment3439000000294500000027530000003725000000Cash and Cash Equivalents, End of PeriodDepreciation, Non-Cash Adjustment3439000000294500000027530000003725000000Change in Cash030000000010000000338000000000)Amortization, Non-Cash Adjustment3215000000273000000025250000003539000000Effect of Exchange Rate Changes20945000000236300000002662200000026465000000Stock-Based Compensation, Non-Cash Adjustment224000000215000000228000000186000000Cash and Cash Equivalents, Beginning of Period25930000000-31750000003000000006126000000Taxes, Non-Cash Adjustment3954000000380300000037450000003223000000Cash Flow Supplemental Section181000000000)183000000-143000000210000000Investment Income/Loss, Non-Cash Adjustment161600000037900000011000000001670000000Change in Cash as Reported, Supplemental2.3719E+132.6622E+132.6465E+132.0129E+13Gain/Loss on Financial Instruments, Non-Cash Adjustment-2478000000-2883000000-4751000000-3262000000Income Tax Paid, Supplemental2774000000-29920000006336000000Other Non-Cash Items-2478000000-2883000000-4751000000-3262000000Cash and Cash Equivalents, Beginning of Period13412000000-4990000000Changes in Operating Capital-14000000-8000000-255000000392000000Change in Trade and Other Receivables-2225000000-871000000-1233000000170200000012 Months EndedChange in Trade/Accounts Receivable-5819000000-36610000002794000000-5445000000_________________________________________________________Change in Other Current Assets-5819000000-36610000002794000000-5445000000Q4 2019Change in Payables and Accrued Expenses-399000000-1990000007000000-738000000Income StatementChange in Trade and Other Payables69940000004074000000-49560000006938000000USD in "000'"sChange in Trade/Accounts Payable1157000000-130000000-982000000963000000Repayments for Long Term DebtDec. 31, 2019Change in Accrued Expenses1157000000-130000000-982000000963000000Costs and expenses:Change in Deferred Assets/Liabilities58370000004204000000-39740000005975000000Cost of revenues161857Change in Other Operating Capital368000000-3000000137000000207000000Research and developmentChange in Prepayments and Deposits-3369000000-1082000000785000000740000000Sales and marketing71896Cash Flow from Investing ActivitiesGeneral and administrative26018Cash Flow from Continuing Investing Activities-11016000000-9074000000-5383000000-7281000000European Commission fines18464Purchase/Sale and Disposal of Property, Plant and Equipment, Net-11016000000-9074000000-5383000000-7281000000Total costs and expenses9551Purchase of Property, Plant and Equipment-6383000000-5496000000-5942000000-5479000000Income from operations1697Sale and Disposal of Property, Plant and Equipment-6383000000-5496000000-5942000000-5479000000Other income (expense), net127626Purchase/Sale of Business, NetIncome before income taxes34231Purchase/Acquisition of Business-385000000-308000000-1666000000-370000000Provision for income taxes5394Purchase/Sale of Investments, Net-385000000-308000000-1666000000-370000000Net income19289000000Purchase of Investments-4348000000-32930000002195000000-1375000000include interest paid, capital obligation, and underweighting19289000000Sale of Investments-40860000000-24949000000-37072000000-3695500000019289000000Other Investing Cash Flow36512000000216560000003926700000035580000000Basic net income per share of Class A and B common stock and Class C capital stock (in dollars par share)Purchase/Sale of Other Non-Current Assets, Net1000000002300000030000000-57000000Diluted net income per share of Class A and Class B common stock and Class C capital stock (in dollars par share)Sales of Other Non-Current AssetsCash Flow from Financing ActivitiesCash Flow from Continuing Financing Activities-16511000000-15991000000-13606000000-9270000000For Paperwork Reduction Act Notice, see the seperate Instructions.Issuance of/Payments for Common Stock, Net-16511000000-15991000000-13606000000-9270000000Payments for Common Stock-13473000000-12796000000-11395000000-7904000000Proceeds from Issuance of Common Stock13473000000-12796000000-11395000000-7904000000Issuance of/Repayments for Debt, NetIssuance of/Repayments for Long Term Debt, Net115000000-1042000000-37000000-57000000Proceeds from Issuance of Long Term Debt115000000-1042000000-37000000-57000000Repayments for Long Term Debt625000000066990000009000000000Proceeds from Issuance/Exercising of Stock Options/Warrants6365000000-7741000000-937000000-570000002923000000-2453000000-2184000000-1647000000Other Financing Cash FlowCash and Cash Equivalents, End of PeriodChange in Cash030000000010000000338000000000)Effect of Exchange Rate Changes20945000000236300000002662200000026465000000Cash and Cash Equivalents, Beginning of Period25930000000-31750000003000000006126000000Cash Flow Supplemental Section181000000000)183000000-143000000210000000Change in Cash as Reported, Supplemental2.37E+132.66E+132.65E+132.01E+13Income Tax Paid, Supplemental2774000000-29920000006336000000Cash and Cash Equivalents, Beginning of Period13412000000-499000000012 Months Ended_________________________________________________________Q4 2019Income StatementUSD in "000'"sRepayments for Long Term DebtDec. 31, 2019Costs and expenses:Cost of revenues161857Research and developmentSales and marketing71896General and administrative26018European Commission fines18464Total costs and expenses9551Income from operations1697Other income (expense), net127626Income before income taxes34231Provision for income taxes5394Net income19289000000include interest paid, capital obligation, and underweighting1928900000019289000000Basic net income per share of Class A and B common stock and Class C capital stock (in dollars par share)Diluted net income per share of Class A and Class B common stock and Class C capital stock (in dollars par share)For Paperwork Reduction Act Notice, see the seperate Instructions.
table {mso-displayed-decimal-separator:"."; mso-displayed-thousand-separator:",";} tr {mso-height-source:auto;} col {mso-width-source:auto;} td {padding-top:1px; padding-right:1px; padding-left:1px; mso-ignore:padding; color:black; font-size:11.0pt; font-weight:400; font-style:normal; text-decoration:none; font-family:Calibri, sans-serif; mso-font-charset:0; text-align:general; vertical-align:bottom; border:none; white-space:nowrap; mso-rotate:0;} .xl18 {color:#3A3838; font-size:9.0pt; font-family:"Courier New"; mso-generic-font-family:auto; mso-font-charset:0; background:white; mso-pattern:black none;} .xl19 {color:#3A3838; font-size:9.0pt; font-family:"Courier New"; mso-generic-font-family:auto; mso-font-charset:0; text-align:right; background:white; mso-pattern:black none;} .xl20 {color:#3A3838; font-size:9.0pt; font-family:"Courier New"; mso-generic-font-family:auto; mso-font-charset:0; background:white; mso-pattern:black none; white-space:normal;} .xl21 {color:#3A3838; font-size:9.0pt; font-family:"Courier New"; mso-generic-font-family:auto; mso-font-charset:0; text-align:right; background:white; mso-pattern:black none; white-space:normal;} .xl24 {color:#3A3838; font-size:9.0pt; font-family:"Courier New"; mso-generic-font-family:auto; mso-font-charset:0; text-align:left; vertical-align:top; background:white; mso-pattern:black none; white-space:normal;} .xl27 {color:#3A3838; font-size:9.0pt; font-family:"Courier New"; mso-generic-font-family:auto; mso-font-charset:0; text-align:center; background:white; mso-pattern:black none;} .xl34 {color:#3A3838; font-size:9.0pt; font-family:"Courier New"; mso-generic-font-family:auto; mso-font-charset:0; vertical-align:top; background:white; mso-pattern:black none; white-space:normal;} Federal 941 Deposit Report
ADP
Report Range5/4/2022 - 6/4/2022Local ID:EIN:63-3441725State ID: 633441725Employee Number: 3
DescriptionAmount5/4/2022 - 6/4/2022Payment Amount (Total)9.24675E+12Display All1. Social Security (Employee + Employer)26661.82. Medicare (Employee + Employer)8.61193E+11Hourly3. Federal Income Tax8.38556E+122.2663E+15Note: This report is generated based on the payroll data for your reference only. Please contact IRS office for special cases such as late payment, previous overpayment, penalty and others.
Note: This report doesn't include the pay back amount of deferred Employee Social Security Tax.CommissionEmployer Customized Report
ADP
Report Range5/4/2022 - 6/4/202288-1656496state ID: 633441725State: AllLocal ID: 000373055812267700EIN:Customized ReportAmountEmployee Payment Report
ADPEmployee Number: 3
DescriptionWages, Tips and Other Compensation2.2663E+13Report Range:TipsTaxable SS Wages215014.49Name:
SSN:0Taxable SS Tips0Payment SummaryTaxable Medicare Wages2.2663E+13SalaryVacation hourlyOTAdvanced EIC Payment03361013.7Federal Income Tax Withheld8.38556E+12Bonus00Employee SS Tax Withheld13330.90Other Wages 1Other Wages 2Employee Medicare Tax Withheld5.3258E+11Total00State Income Tax Withheld02.2663E+13Local Income Tax Withheld
Customized Employer Tax Report0Deduction SummaryDescriptionAmountHealth InsuranceEmployer SS Tax
Employer Medicare Tax13330.90Federal Unemployment Tax3.28613E+11Tax SummaryState Unemployment Tax441.7Federal Tax7Total TaxCustomized Deduction Report840$8,385,561,229,657@3,330.90Local TaxHealth Insurance0401K0Advanced EIC Payment8.91814E+1200Total401K00Social Security Tax Medicare TaxState Tax$532,580,113,050)SHAREHOLDERS ARE URGED TO READ THE DEFINITIVE PROXY STATEMENT AND ANY OTHER RELEVANT MATERIALS THAT THE COMPANY WILL FILE WITH THE SEC CAREFULLY IN THEIR ENTIRETY WHEN THEY BECOME AVAILABLE. SUCH DOCUMENTS WILL CONTAIN IMPORTANT INFORMATION ABOUT THE COMPANY AND ITS DIRECTORS, OFFICERS AND AFFILIATES. INFORMATION REGARDING THE INTERESTS OF CERTAIN OF THE COMPANY’S DIRECTORS, OFFICERS AND AFFILIATES WILL BE AVAILABLE IN THE DEFINITIVE PROXY STATEMENT.The Definitive Proxy Statement and any other relevant materials that will be filed with the SEC will be available free of charge at the SEC’s website at www.sec.gov. In addition, the Definitive Proxy Statement (when available) and other relevant documents will also be available, without charge, by directing a request by mail to Attn: Investor Relations, Alphabet Inc., 1600 Amphitheatre Parkway, Mountain View, California, 94043 or by contacting investor-relations@abc.xyz. The Definitive Proxy Statement and other relevant documents will also be available on the Company’s Investor Relations website at https://abc.xyz/investor/other/annual-meeting/.The Company and its directors and certain of its executive officers may be consideredno participants in the solicitation of proxies with respect to the proposals under the Definitive Proxy Statement under the rules of the SEC. Additional information regarding the participants in the proxy solicitations and a description of their direct and indirect interests, by security holdings or otherwise, also will be included in the Definitive Proxy Statement and other relevant materials to be filed with the SEC when they become available.9.24675E+123/6/2022 at 6:37 PMQ4 2021Q3 2021Q2 2021Q1 2021Q4 2020GOOGL_income-statement_Quarterly_As_Originally_Reported24934000000255390000003749700000031211000000308180000002493400000025539000000218900000001928900000022677000000Cash Flow from Operating Activities, Indirect2493400000025539000000218900000001928900000022677000000Net Cash Flow from Continuing Operating Activities, Indirect2064200000018936000000185250000001793000000015227000000Cash Generated from Operating Activities65170000003797000000423600000025920000005748000000Income/Loss before Non-Cash Adjustment34390000003304000000294500000027530000003725000000Total Adjustments for Non-Cash Items34390000003304000000294500000027530000003725000000Depreciation, Amortization and Depletion, Non-Cash Adjustment32150000003085000000273000000025250000003539000000Depreciation and Amortization, Non-Cash Adjustment224000000219000000215000000228000000186000000Depreciation, Non-Cash Adjustment39540000003874000000380300000037450000003223000000Amortization, Non-Cash Adjustment1616000000-128700000037900000011000000001670000000Stock-Based Compensation, Non-Cash Adjustment-2478000000-2158000000-2883000000-4751000000-3262000000Taxes, Non-Cash Adjustment-2478000000-2158000000-2883000000-4751000000-3262000000Investment Income/Loss, Non-Cash Adjustment-1400000064000000-8000000-255000000392000000Gain/Loss on Financial Instruments, Non-Cash Adjustment-22250000002806000000-871000000-12330000001702000000Other Non-Cash Items-5819000000-2409000000-36610000002794000000-5445000000Changes in Operating Capital-5819000000-2409000000-36610000002794000000-5445000000Change in Trade and Other Receivables-399000000-1255000000-1990000007000000-738000000Change in Trade/Accounts Receivable699400000031570000004074000000-49560000006938000000Change in Other Current Assets1157000000238000000-130000000-982000000963000000Change in Payables and Accrued Expenses1157000000238000000-130000000-982000000963000000Change in Trade and Other Payables583700000029190000004204000000-39740000005975000000Change in Trade/Accounts Payable368000000272000000-3000000137000000207000000Change in Accrued Expenses-33690000003041000000-1082000000785000000740000000Change in Deferred Assets/LiabilitiesChange in Other Operating Capital-11016000000-10050000000-9074000000-5383000000-7281000000Change in Prepayments and Deposits-11016000000-10050000000-9074000000-5383000000-7281000000Cash Flow from Investing ActivitiesCash Flow from Continuing Investing Activities-6383000000-6819000000-5496000000-5942000000-5479000000-6383000000-6819000000-5496000000-5942000000-5479000000Purchase/Sale and Disposal of Property, Plant and Equipment, NetPurchase of Property, Plant and Equipment-385000000-259000000-308000000-1666000000-370000000Sale and Disposal of Property, Plant and Equipment-385000000-259000000-308000000-1666000000-3700000000Purchase/Sale of Business, Net-4348000000-3360000000-32930000002195000000-1375000000Purchase/Acquisition of Business-40860000000-35153000000-24949000000-37072000000-36955000000Purchase/Sale of Investments, NetPurchase of Investments36512000000317930000002165600000039267000000355800000001000000003880000002300000030000000-57000000Sale of InvestmentsOther Investing Cash Flow-15254000000Purchase/Sale of Other Non-Current Assets, Net-16511000000-15254000000-15991000000-13606000000-9270000000Sales of Other Non-Current Assets-16511000000-12610000000-15991000000-13606000000-9270000000Cash Flow from Financing Activities-13473000000-12610000000-12796000000-11395000000-7904000000Cash Flow from Continuing Financing Activities13473000000-12796000000-11395000000-7904000000Issuance of/Payments for Common 343 sec cvxvxvcclpddf wearsStock, Net-42000000Payments for Common Stock115000000-42000000-1042000000-37000000-57000000Proceeds from Issuance of Common Stock1150000006350000000-1042000000-37000000-57000000Issuance of/Repayments for Debt, Net6250000000-639200000066990000009000000000Issuance of/Repayments for Long Term Debt, Net6365000000-2602000000-7741000000-937000000-57000000Proceeds from Issuance of Long Term DebtRepayments for Long Term Debt2923000000-2453000000-2184000000-1647000000Proceeds from Issuance/Exercising of Stock Options/Warrants0300000000100000003.38E+11Other Financing Cash FlowCash and Cash Equivalents, End of PeriodChange in Cash2094500000023719000000236300000002662200000026465000000Effect of Exchange Rate Changes25930000000)235000000000)-31750000003000000006126000000Cash and Cash Equivalents, Beginning of PeriodPAGE="$USD(181000000000)".XLSBRIN="$USD(146000000000)".XLS183000000-143000000210000000Cash Flow Supplemental Section2.3719E+132.6622E+132.6465E+132.0129E+13Change in Cash as Reported, Supplemental277400000089000000-29920000006336000000Income Tax Paid, Supplemental13412000000157000000ZACHRY T WOOD-4990000000Cash and Cash Equivalents, Beginning of PeriodDepartment of the TreasuryInternal Revenue ServiceQ4 2020Q4  2019Calendar YearDue: 04/18/2022Dec. 31, 2020Dec. 31, 2019USD in "000'"sRepayments for Long Term Debt182527161857Costs and expenses:Cost of revenues8473271896Research and development2757326018Sales and marketing1794618464General and administrative110529551European Commission fines01697Total costs and expenses141303127626Income from operations4122434231Other income (expense), net68580000005394Income before income taxes2267700000019289000000Provision for income taxes2267700000019289000000Net income2267700000019289000000include interest paid, capital obligation, and underweightingBasic net income per share of Class A and B common stock and Class C capital stock (in dollars par share)Diluted net income per share of Class A and Class B common stock and Class C capital stock (in dollars par share)include interest paid, capital obligation, and underweightingBasic net income per share of Class A and B common stock and Class C capital stock (in dollars par share)Diluted net income per share of Class A and Class B common stock and Class C capital stock (in dollars par share)20210418RateUnitsTotalYTDTaxes / DeductionsCurrentYTD--7084274500070842745000Federal Withholding00FICA - Social Security08853.6FICA - Medicare00Employer TaxesFUTA00SUTA00EIN: 61-1767919ID : 00037305581 SSN: 633441725Gross70842745000Earnings StatementTaxes / DeductionsStub Number: 10Net PaySSNPay SchedulePay PeriodSep 28, 2022 to Sep 29, 2023Pay Date4/18/202270842745000XXX-XX-1725AnnuallyCHECK NUMBERINTERNAL REVENUE SERVICE,PO BOX 1214,CHARLOTTE, NC 28201-1214ZACHRY WOOD157603300000020642000000189360000001852500000017930000000152270000001124700000069590000006836000000106710000007068000000For Disclosure, Privacy Act, and Paperwork Reduction Act Notice, see separate instructions.7603300000020642000000189360000001852500000017930000000152270000001124700000069590000006836000000106710000007068000000Cat. No. 11320B7603300000020642000000189360000001852500000017930000000152270000001124700000069590000006836000000106710000007068000000Form 1040 (2021)760330000002064200000018936000000Reported Normalized and Operating Income/Expense Supplemental SectionTotal Revenue as Reported, Supplemental2.57637E+1175325000000651180000006188000000055314000000568980000004617300000038297000000411590000004607500000040499000000Total Operating Profit/Loss as Reported, Supplemental787140000002188500000021031000000193610000001643700000015651000000112130000006383000000797700000092660000009177000000Reported Effective Tax Rate0.160.1790.1570.1580.1580.1590.1190.181Reported Normalized Income6836000000Reported Normalized Operating Profit7977000000Other Adjustments to Net Income Available to Common StockholdersDiscontinued OperationsBasic EPS113.8831.1528.4427.6926.6322.5416.5510.219.9615.4910.2Basic EPS from Continuing Operations113.8831.1228.4427.6926.6322.4616.5510.219.9615.4710.2Basic EPS from Discontinued OperationsDiluted EPS112.230.6927.9927.2626.2922.316.410.139.8715.3510.12Diluted EPS from Continuing Operations112.230.6727.9927.2626.2922.2316.410.139.8715.3310.12Diluted EPS from Discontinued OperationsBasic Weighted Average Shares Outstanding667650000662664000665758000668958000673220000675581000679449000681768000686465000688804000692741000Diluted Weighted Average Shares Outstanding677674000672493000676519000679612000682071000682969000685851000687024000692267000695193000698199000Reported Normalized Diluted EPS9.87Basic EPS113.8831.1528.4427.6926.6322.5416.5510.219.9615.4910.21Diluted EPS112.230.6927.9927.2626.2922.316.410.139.8715.3510.12Basic WASO667650000662664000665758000668958000673220000675581000679449000681768000686465000688804000692741000Diluted WASO677674000672493000676519000679612000682071000682969000685851000687024000692267000695193000698199000Fiscal year end September 28th., 2022. | USDFor Paperwork Reduction Act Notice, see the seperate Instructions.important informationDescriptionRestated Certificate of Incorporation of PayPal Holdings, Inc.(incorporated by reference to Exhibit  3.01 to PayPal Holdings, Inc.'sQuarterly Report on Form 10-Q, as filed with the Commission onJuly 27, 2017).Amended and Restated Bylaws of PayPal Holdings, Inc. (incorporatedby reference to Exhibit  3.1 to PayPal Holdings, Inc.'s Current Reporton Form 8-K, as filed with the Commission on January 18, 2019).Opinion of Faegre Drinker Biddle & Reath LLP.Consent of PricewaterhouseCoopers LLP, Independent Registered PublicAccounting Firm.Consent of Faegre Drinker Biddle & Reath LLP (included inExhibit 5.1 to this Registration Statement).Power of Attorney (included on the signature page of thisRegistration Statement).All of Us Financial Inc. 2021 Equity Incentive Plan.Filing Fee Table.Business Checking
For 24-hour account information, sign on topnc.com/mybusiness/
Business Checking Account number: 47-2041-6547 - continuedActivity DetailDeposits and Other AdditionsACH AdditionsDate postedAmount Transaction descriptionFor the period 04/13/2022 to 04/29/2022
ZACHRY TYLER WOOD
Primary account number: 47-2041-6547 Page 2 of 34467862.5Reverse Corporate ACH Debit
Effective 04-26-22Reference numberChecks and Other Deductions2.21169E+13DeductionsReference numberDate postedAmount Transaction description2.21169E+134467762.5Corporate ACH Quickbooks 180041ntuit 1940868Reference numberService Charges and Fees2.21169E+13Date postedAmount Transaction descriptionon your next statement as a single line item entitled Service
Waived - New Customer Period4467836Returned Item Fee (nsf)Detail of Services Used During Current PeriodNote: The total charge for the following services will be posted to your account on 05/02/2022 and will appear on your next statement a Charge Period Ending 04/29/2022,DescriptionVolumeAmountAccount Maintenance Charge708467438660        Total For Services Used This Peiiod00Total Service (harge00
0Reviewing Your Statement('PNCBANKPlease review this statement carefully and reconcile it with your records. Call the telephone number on the upper right side of the first page of this statement if:
you have any questions regarding your account(s); your name or address is incorrect;
• you have any questions regarding interest paid to an interest-bearing account.ÉBalancing Your Account
Update Your Account RegisterCertified Copy of Resolutionsl
Authorizations For Accounts And Loans@PNCBANK(Corporations, Partnerships, Unincorporated Associations, Sole Proprietorships & Other Organizations)step 2: Add together checks and other deductions listed in your account register but not on your statement.PNC Bank, National Association ("Bank")Taxpayer I.D. Number (TIN)C'eck
Deduction Descretio•Anount(iv)
(v)account or benefit, or in payment of the individual obligations of, any individual obligations of any such persons to the Bank without regard to the disposition or purpose of same as allowed by applicable law.D pNCBANKIn addition but not by way of limitation, the Bank may take checks, drafts or other items payable to "cash", the Bank or the Customer, and pay the sums represented by such Items in cash to any person presenting such items or credit such Items to the account or obligations of any person presenting such items or any other person or entity as directed by any such person.Products and Services. Resolved that any of the persons listed in Section 3 above are authorized to enter into contracts and agreements, written or verbal, for any products or services now or in the future offered by the Bank, including but not limited to (i) cash management services, (ii) purchases or sales of foreign exchange, securities or other financial products, (iii) computer/internet-based products and services, (iv) wire transfer of funds from or to the accounts of the Customer at the Bank, and (v) ACH transactions, and the Bank may charge any accounts of the Customer at the Bank for such products or services.5Taxpayer I.D. Number (TIN)OWNER("Customer")633-44-1725are hereby authorized (i) to effect loans, advances and renewals at any time for the Customer from the Bank; (ii) to sign and deliver any notes (with or without warrant of attorney to confess judgment) and evidences of indebtedness of the Customer; (iii) to request the Bank to issue letters of credit and to sign and deliver to the bank any agreements on behalf of the Customer to reimburse the Bank for all payments made and expenses incurred by it under such letters of credit and drafts drawn pursuant thereto; (iv) to sign and deliver any instruments or documents on behalf of the Customer guaranteeing, endorsing or securing the payment of any debts or obligations of any person, form or corporation to the Bank; (v) to pledge, assign, transfer, mortgage, grant a security interest in or otherwise hypothecate to the Bank any stock, securities, commercial paper, warehouse receipts and other documents of title, bills, accounts receivable, contract rights, inventory, equipment, real property, and any other investments or property of the Customer, real or personal, tangible or intangible as security for the payment of any and all loans, advances, indebtedness and other liabilities of the Customer to the Bank of every kind and description, direct or indirect, absolute and contingent, joint or several, whether as drawer, maker, endorsee, guarantor, surety or otherwise, and to execute on behalf of the Customer mortgages, pledges, security agreements, financing statements and other instruments or documents in connection therewith; and (vi) to sell or discount with the Bank any commercial paper, bills and other instruments and evidence of indebtedness, warehouse receipts and other documents of title, accounts, accounts receivable, contract rights, and other assets, tangible and intangible, at any time held by the Customer and for such purpose to endorse, assign, transfer and deliver the same to the Bank.6Revolving Credits. Resolved that in connection with any extension of credit obtained by any of the persons authorized in Section 5 above, that permit the Customer to effect multiple advances or draws under such credit, any of the persons listed in Sections 5 (Loans and Extensions of Credit) and 3 (Withdrawals and Endorsements)Resolution for ALPHABET7Telephonic and Facsimile Requests. Resolved that the Bank is authorized to take any action authorized hereunder based upon (i) the telephone request of any person purporting to be a person authorized to act hereunder, (ii) the signature of any person authorized to act hereunder that is delivered to the Bank by facsimile transmission, or (iii) the telex originated by any of such persons, tested in accordance with such testing:Tr
R
•d
Mingor serVlCö n lent services, (ii) purchases or sales of foreig xlll) computerfinternet-based products and services, (iv) wir he Customer at the Bank, and (v) ACH transactions, and the Ba the Bank for such products or services.
It. Resolved that any one of the following:procedures as may be established between the Customer and the Bank from time to time.
General. Resolved that a certified copy of these resolutions be delivered to the Bank; that the persons specified herein are vested with authority to act and may designate successor persons to act on behalf of Customer8without further authority from the Customer or governing body; and that Bank may rely on the authority given by this resolution until actual receipt by the Bank of a certified copy of a new resolution modifying or revoking the/Customer Copy, page 2 of 49Withdrawals and Transfers. Resolved that the Bank is authorized to make payments from the account(s) ofCustomer according to any check, draft, bill of exchange, acceptance or other written instrument or direction signed by any one of the following individuals, officers or designated agents, and that such designated individuals may also otherwise transfer, or enter into agreements with Bank concerning the transfer, of funds from Customer's account(s), whether by telephone, telegraph, computer or any other manner:Column1Column2Loans and Extensions of Credit. Resolved that any one of the following:45999-0023Date of this notice: 44658Employer Identification Number: 88-1656496Form: SS-4Number of this notice: CP 575 AFor assistance you may call us at:1-800-829-493375235IF YOU WRITE, ATTACH THE
STUB AT THE BD OF THIS NOTICE.We assigned youThis EIN will identify you, your business accounts, tax returns, andWE ASSIGNED YOU AN EMPLOYER IDENTIFICATION NUMBER
Thank you for applying for an Employer Identification Number (EIN) . EIN 88-1656496. If the information isPleaseb6.35-for the tax period(s) in question, please file the return (s) showing you have no liabilities .
If you have questions about at the the forms address or the shown due at dates the top shown, of you this can notice. call us If atyou the phone number or write to us Publication 538,
need help in determining your annual accounting period (tax year) , see Accounting Periods and Methods.8Total Year to Date3,Total for this PeriodOverdraft and Returned Item Fee Summary363618Total Returned Item Fees (NSF)t ly ofItemsAmountChecks and Other Deductions
DescriptionItemsAmount162.5ACH Deductions162.5heDeposits and Other Additions
DescriptionService Charges and Fees136ACH Additions162.5Total298.5DateLedger balanceDateLedger balanceTotalDaily Balance(27962.50-4467836DateLedger balanceYou'202Alphabet Inc Class C GOOGotm corresti2814TM 27.8414.76%6350053.:202Fair Value Estimate2160gro550ovrConsider Buying PriceConsider Selling PriceFair Value Uncertainty
Economic Moat
Stewardship Grade02-01-2022 1 by Ali MogharabiBusiness Strategy & Outlook 02-01-2022Analyst Digest 1 633-44-1725 10-15-94 Portfolio April 04,2022 - April 03,2022Berkshire Hathaway Inc Class A BRK.A525000527760$0.001 0.00%367500Fair Value EstimateConsider Buying Price$708,750.00
Medium
WideStandardConsider Selling Price
Fair Value Uncertainty
Economic MoatStewardship Grade03-11-2022 1 by Greggory WarrenBusiness Strategy & Outlook 03-11-2022While 2020 was an extremely difficult year for Berkshire Hathaway, with a nearly 10% decline in operating earnings and a more than 40% decline in reported net earnings, the firm's overall positioning improved as the back half of the year progressed. The firm saw an even more marked improvement in its insurance investment portfolio, as well as the operating results of its various subsidiaries, last year. As such, we expect 2022 and 2023 to be a return to more normalized levels of revenue growth and profitability (albeit with inflation impacting results in the first half of this year).We continue to view Berkshire's decentralized business model, broad business diversification, high cash-generation capabilities, and unmatched balance sheet strength as true differentiators. While these advantages have been overshadowed by an ever-expanding cash balance-ANhich is earning next to nothing in a near-zero interest-rate environment--we believe the company has finally hit a nexus where it is far more focused on reducing its cash hoard through stock and bond investments and share repurchases. During the past eight calendar quarters, theWhen filing tax documents,ING  payments, or replying to any related correspondence,it is very important that you use your EIN and complete name and address exactly as shown above. Any variation may cause a delay in processing, result in incorrect information inyour account, or even cause you to be assigned more than one EIN. If the information isnot correct as shown above, please make the correction using the attached tear-off stub and return it to us .
Based on the information received from you or your representative, you must file the following forms by the dates shown.We assigned you44658Form 94044658Form 94344658If the information isForm 106544658Form 72044658Your Form 2290 becomes due the month after your vehicle is put into use .
Your Form 1 IC and/or 730 becomes due the month after your wagering starts .
After our review of your information, we have determined that you have not filedtax returns for the above-mentioned tax period (s) dating as far back as 2007.Plea Sfile your return(s) by 04/22/2022.If there is a balance due on the return (s)penalties and interest will continue to accumulate from the due date of the return (s)until it is filed and paid. If you were not in business or did not hire any employeesfor the tax period(s) in question, please file the return (s) showing you have no liabilities .
If you have questions about the forms or the due dates shown, you can call us atPIthe phone number or write to us at the address shown at the top of this notice. If youneed help in determining your annual accounting period (tax year) , see Publication 538, Accounting Periods and Methods.Business Checking
PNCBANK@PNCBANKFor the period 04/13/2022Primary account number: 47-2041-6547 Page 1 of 35/19/23021022462Q 304Number of enclosures: 0ZACHRY TYLER WOOD ALPHABET
5323 BRADFORD DR
DALLAS TX 75235-8314For 24-hour banking sign on to
PNC Bank Online Banking on pnc.com
FREE Online Bill Pay
For customer service call 1-877-BUS-BNKG
PNC accepts Telecommunications Relay Service (TRS) calls.91.11E+62Para servicio en espalol, 1877.BUS-BNKC,
Moving? Please contact your local branch.
@ Write to: Customer Service PO Box 609
Pittsburgh , PA 15230-9738
Visit us at PNC.com/smaIIbusinessIMPORTANT INFORMATION FOR BUSINESS DEPOSIT CUSTOMERSDate of this notice: Effective February 18,2022, PNC will be temporarily waiving fees for statement, check image, deposit ticket and deposited item copy requests until further notice. Statement, check image, deposit ticket and deposited Item requests will continue to be displayed in the Details of Services Used section of your monthly statement. We will notify you via statement message prior to reinstating these fees.
If vou have any questions, you may reach out to your business banker branch or call us at 1-877-BUS-BNKG (1-877-287-2654).44658Business Checking Summary
Account number; 47-2041-6547
Overdraft Protection has not been established for this account. Please contact us if you would like to set up this service.Zachry Tyler Wood AlphabetEmployer Identification Number: 88-1656496Balance SummaryChecks and other deductionsEnding balanceForm: SS-4Beginning balanceDeposits and other additionsNumber of this notice: CP 575 A0=98.50 Average ledger balance36.00-
Average collected balanceFor assistance you may call ug at:6.35-6.35-1-800-829-4933Overdraft and Returned Item Fee SummaryTotal Year to DateTotal for this PeriodTotal Returned Item Fees (NSF)3636IF YOU WRITE, ATTATCHA TYE
STUB AT OYE END OF THIS NOTICE.Deposits and Other Additions
DescriptionItemsAmountChecks and Other Deductions
DescriptionItemsAmountACH Additions162.5ACH Deductions162.5We assigned youService Charges and Fees136Total162.5Total298.5Daily BalanceDateDateLedger balanceIf the information isDateLedger balanceLedger balance4466404467762.50-4467836Form 94044658Berkshire Hatha,a,n..Business CheckingFor the period 04/13/2022  to 04/29/202244680For 24-hour account information, sign on to pnc.com/mybusiness/ZACHRY TYLER WOODPrimary account number: 47-2041-6547 Page 2 of 3PleaseBusiness Checking Account number: 47-2041-6547 - continuedPage 2 of 3Acüvity DetailDeposits and Other Additionsdid not hire any employeeACH AdditionsReferenc numbDate posted 04/27Transaction
Amount description
62.50  Reverse Corporate ACH Debit
Effective 04-26-22the due dates shown, you can call us at2.21169E+13If youChecks and Other DeductionsACH DeductionsReferencDate postedTransaction
Amount descriptionnumber4/26/202270842743866Corporate ACH Quickbooks 180041ntuit 19408682.21169E+13ervice Charges and FeesReferencDate postedTransaction
Amount descripton27-Apr2.21169E+13numbDetail of Services Used During Current Period2.21169E+13 ::NOTE:: The total charge for the following services will be posted to your account on 05/02/2022 and will appear on your next statement as a single line item entitled Service Charge Period Ending 04/29/2022.e: The total charge for the following Penod Ending 04/29/2022.Service Charge descriptionAmountAccount Maintenance Charge$62.50Total For Services Used This Period$36.00Total Service Charge$98.50Waived - Waived - New Customer PeriodReviewing Your Statement
of this statement if:
you have any questions regarding your account(s); your name or address is incorrect; you have any questions regarding interest paid to an interest-bearing account.PNCBANKBalancing Your Account
Update Your Account RegisterVolumeCompare:The activity detail section of your statement to your account register.Check Off:
Add to Your Account Register: Balance:
Subtract From Your Account Register  Balance:All items in your account register that also appear on your statement. Remember to begin with the ending date of your last statement. (An asterisk { * } will appear in the Checks section if there is a gap in the listing of consecutive check numbers.)
Any deposits or additions including interest payments and ATM or electronic deposits listed on the statement that are not already entered in your register.
Any account deductions including fees and ATM or electronic deductions listed on the statement that are not already entered in your register.Your Statement Information : step 2: Add together checks and other deductions listed in your account register but not on your statement.AmountCheck
Deduction DescrptionAmountBalancing Your Account
Update Your Account Register-on :deposit=$B=+A: 22934637118600.00](usd)'"'4720416547Reviewing Your Statement
of this statement if:
you have any questions regarding your account(s); your name or address is incorrect; you have any questions regarding interest paid to an interest-bearing account.Total A=$22934637118600Step 3:$22,934,637,118,600 Enter the ending balance recorded on your statementAdd deposits and other additions not recordedTotal A + $22934637118600Subtotal=$22934637118600Subtract checks and other deductions not recorded Total B$2.29346E+13The result should equal your account register balance$2.29346E+13Total B22934637118600Verification of Direct DepositsTo verify whether a direct deposit or other transfer to your account has occurred, call us Monday - Friday: 7 AM - 10 PM ET and Saturday & Sunday: 8 AM - 5 PM ET at the customer service number listed on the upper right side of the first page of this statement.In Case of Errors or Questions About Your Electronic Transfers
Telephone us at the customer service number listed on the upper right side of the first page of this statement or write us at PNC Bank Debit Card Services, 500 First Avenue, 4th Floor, Mailstop P7-PFSC-04-M, Pittsburgh, PA 15219 as soon as you can, if you think your statement or receipt is wrong or if you need more information about a transfer on the statement or receipt. We must hear from you no later than 60 days after we sent you the FIRST statement on which the error or problem appeared.
Tell us your name and account number (if any).
Describe the error or the transfer you are unsure about, and explain as clearly as you can why you believe it is an error or why you need more information.
Tell us the dollar amount of the suspected error.
We will investigate your complaint and will correct any error promptly. If we take longer than 10 business days, we will provisionally credit your account for the amount you think is in error, so that you will have use of the money during the time it Cakes us to complete our investigation.
EquaLHousing LenderMember FDIC

Security enhanced document. See back for details				NO.																					Interest Income	1499000000	378000000	389000000	345000000	386000000	460000000	433000000	#NAME?	1499000000	378000000	389000000	345000000	386000000	460000000	433000000																																																																																																																																																																																										|	[OBJ][OBJ]PNCBANK																									Net Investment Income	12364000000	2364000000	2924000000	4869000000	3530000000	1957000000	1696000000	#NAME?	12364000000	2364000000	2924000000	4869000000	3530000000	1957000000	1696000000																																																																																																																																																																																										|		PNC Bank N.A.	71													70-2188/719										Gain/Loss on Investments and Other Financial Instruments	12270000000	2478000000	2883000000	4751000000	3262000000	2015000000	1842000000	#NAME?	12270000000	2478000000	2883000000	4751000000	3262000000	2015000000	1842000000																																																																																																																																																																																										|										 			DATE____________________________________7364													Income from Associates, Joint Ventures and Other Participating Interests	334000000	49000000	92000000	5000000	355000000	26000000	-54000000	#NAME?	334000000	49000000	92000000	5000000	355000000	26000000	-54000000																																																																																																																																																																																										|																										Gain/Loss on Foreign Exchange	-240000000	-163000000	-51000000	113000000	-87000000	-84000000	-92000000	#NAME?	-240000000	-163000000	-51000000	113000000	-87000000	-84000000	-92000000																																																																																																																																																																																										|PAY TO THE																										Irregular Income/Expenses	0	0			0	0	0	#NAME?	0	0			0	0	0																																																																																																																																																																																										|ORDER OF_______________________________________________________________________________________________________________|***$**22677000000000&00/100cents||																										Other Irregular Income/Expenses	0	0			0	0	0	#NAME?	0	0			0	0	0																																																																																																																																																																																										|																 Security||										Other Income/Expense, Non-Operating	-1497000000	-108000000	-613000000	-292000000	-825000000	-223000000	-222000000	#NAME?	-1497000000	-108000000	-613000000	-292000000	-825000000	-223000000	-222000000																																																																																																																																																																																										|______________________________________________________________________________________________________________________DOLLARS [OBJ] Features 																										Pretax Income	90734000000	24402000000	21985000000	21283000000	18689000000	13359000000	8277000000	#NAME?	90734000000	24402000000	21985000000	21283000000	18689000000	13359000000	8277000000																																																																																																																																																																																										|ESTATE OF															 Detaile											Provision for Income Tax	-14701000000	-3760000000	-3460000000	-3353000000	-3462000000	-2112000000	-1318000000	#NAME?	-14701000000	-3760000000	-3460000000	-3353000000	-3462000000	-2112000000	-1318000000																																																																																																																																																																																										|																 on Back.										Net Income from Continuing Operations	76033000000	20642000000	18525000000	17930000000	15227000000	11247000000	6959000000	#NAME?	76033000000	20642000000	18525000000	17930000000	15227000000	11247000000	6959000000																																																																																																																																																																																										|FOR_____________________________________																										Net Income after Extraordinary Items and Discontinued Operations	76033000000	20642000000	18525000000	17930000000	15227000000	11247000000	6959000000	#NAME?	76033000000	20642000000	18525000000	17930000000	15227000000	11247000000	6959000000																																																																																																																																																																																										|AUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATURE.EXECUTOR/																										Net Income after Non-Controlling/Minority Interests	76033000000	20642000000	18525000000	17930000000	15227000000	11247000000	6959000000	#NAME?	76033000000	20642000000	18525000000	17930000000	15227000000	11247000000	6959000000																																																																																																																																																																																										|{														}.ADMINISTRATOR												Net Income Available to Common Stockholders	76033000000	20642000000	18525000000	17930000000	15227000000	11247000000	6959000000	#NAME?	76033000000	20642000000	18525000000	17930000000	15227000000	11247000000	6959000000																																																																																																																																																																																										|AUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATURE.PERSONAL/																										Diluted Net Income Available to Common Stockholders	76033000000	20642000000	18525000000	17930000000	15227000000	11247000000	6959000000	#NAME?	76033000000	20642000000	18525000000	17930000000	15227000000	11247000000	6959000000																																																																																																																																																																																										|{														}.REPRESENTATIVE												Income Statement Supplemental Section								#NAME?																																																																																																																																																																																																	|AUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATUREAUTHORIZEDSIGNATURE.TRUSTEE||																										Reported Normalized and Operating Income/Expense Supplemental Section								#NAME?																																																																																																																																																																																																	|Deposited to the account Of xxxxxxxx6547																										Total Revenue as Reported, Supplemental	2.57637E+11	75325000000	61880000000	55314000000	56898000000	46173000000	38297000000	#NAME?	2.58E+11	75325000000	61880000000	55314000000	56898000000	46173000000	38297000000																																																																																																																																																																																										|PLEASE READ THE IMPORTANT DISCLOSURES BELOW																										Total Operating Profit/Loss as Reported, Supplemental	78714000000	21885000000	19361000000	16437000000	15651000000	11213000000	6383000000	#NAME?	78714000000	21885000000	19361000000	16437000000	15651000000	11213000000	6383000000																																																																																																																																																																																										|																										Reported Effective Tax Rate	0.162		0.157	0.158		0.158	0.159	#NAME?	0.162		0.157	0.158		0.158	0.159																																																																																																																																																																																										|FEDERAL RESERVE MASTER SUPPLIER ACCOUNT 31000053-052101023 COD																										Reported Normalized Income								#NAME?																																																																																																																																																																																																	|																										Reported Normalized Operating Profit								#NAME?																																																																																																																																																																																																	|633-44-1725 Zachryiixixiiiwood@gmail.com 47-2041-6547 111000614 31000053																										Other Adjustments to Net Income Available to Common Stockholders								#NAME?																																																																																																																																																																																																	|PNC Bank PNC Bank Business Tax I.D. Number: 633441725																										Discontinued Operations								#NAME?																																																																																																																																																																																																	|CIF Department (Online Banking) Checking Account: 47-2041-6547																										Basic EPS	113.88	31.15	27.69	26.63	22.54	16.55	10.21	WOOD.,	113.88	31.15	27.69	26.63	22.54	16.55	10.21																																																																																																																																																																																										|P7-PFSC-04-F Business Type: Sole Proprietorship/Partnership Corporation																										Basic EPS from Continuing Operations	113.88	31.12	27.69	26.63	22.46	16.55	10.21	S.R.	113.88	31.12	27.69	26.63	22.46	16.55	10.21																																																																																																																																																																																										|500 First Avenue ALPHABET																										Basic EPS from Discontinued Operations								ZACHRY																																																																																																																																																																																																	|Pittsburgh, PA 15219-3128 5323 BRADFORD DR																										Diluted EPS	112.2	30.69	27.26	26.29	22.3	16.4	10.13  112.2	30.69	27.26	26.29	22.3	16.4	10.13																																																																																																																																																																																										GOOGL_income-statement_Quarterly_As_Originally_Reported	TTM	Q4 2021	Q2 2021	Q1 2021	Q4 2020	Q3 2020	Q2 2020																			Diluted EPS from Continuing Operations	112.2	30.67	27.26	26.29	22.23	16.4	10.13	#NAME?	112.2	30.67	27.26	26.29	22.23	16.4	10.13																																																																																																																																																																																										Gross Profit	$146,698,000,000.00 	$42,337,000,000.00 	$35,653,000,000.00 	$31,211,000,000.00 	30818000000	$25,056,000,000.0
@zakwarlord7

Add heading textAdd bold text, <Ctrl+b>Add italic text, <Ctrl+i>
Add a quote, <Ctrl+Shift+.>Add code, <Ctrl+e>Add a link, <Ctrl+k>
Add a bulleted list, <Ctrl+Shift+8>Add a numbered list, <Ctrl+Shift+7>Add a task list, <Ctrl+Shift+l>
Directly mention a user or team
Reference an issue or pull request
Leave a comment
No file chosen
Attach files by dragging & dropping, selecting or pasting them.
Styling with Markdown is supported
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
{ env.SELECTOR }}'\""
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
0 results found.
Web searchCopyfrom ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages
import sys, os

import anki

setup(name='anki',
      version=anki.version,
      description='An intelligent spaced-repetition memory training library',
      long_description="",
      # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Education',
    'Topic :: Software Development :: Libraries :: Python Modules',
        ],
      keywords='',
      author='Damien Elmes',
      author_email='anki@ichi2.net',
      url='http://ichi2.net/anki/index.html',
      license='GPLv3',
      packages=["anki", "anki.importing"],
      package_data={'anki': ['locale/*/*/*'],},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        ],
      )
