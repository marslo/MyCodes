### How to run my program
- Check the Help information
    <pre><code>┌─ (marslo@MJ ~/FizzBuzzWhizz/V1.0) ->
    └─ $ python mainFizzBuzzWhizz.py  --help
    NAME
            mainFizzBuzzWhizz.py - Print the Fizz, Buzz and Whizz password
    USAGE
            mainFizzBuzzWhizz.py < [--help] | [ --fizz=n ] | [ --buzz=n ] | [ --whizz=n ] | [ --scope=n ] >
    SYNOPSIS
            pythonmainFizzBuzzWhizz.py [Options]
    OPTIONS
            --fizz=TheFirstNumber
                    Default: 3, it will replaced by Fizz.
            --buzz=TheSecondNumber
                    Default: 5. It will replaced by Buzz.
            --whizz=TheThirdNumber
                    Default: 7. It will replaced by Whizz.
            --scope=TheScopeNumber
                    The Scope. Default: 100.
    EXAMPLE
            pythonmainFizzBuzzWhizz.py
            pythonmainFizzBuzzWhizz.py 3 5 7
            pythonmainFizzBuzzWhizz.py --whizz=8
            pythonmainFizzBuzzWhizz.py --fizz=3 --buzz=5 --whizz=7
            pythonmainFizzBuzzWhizz.py 3 5 7 --scope=100
    AUTHOR
            This program made by Marslo Jiao (marslo.jiao@gmail.com)
    </code></pre>

- Input the argus (<kbd>Enter</kbd>: default value):
    <pre><code>┌─ (marslo@MJ ~/FizzBuzzWhizz/V1.0) ->
    └─ $ python mainFizzBuzzWhizz.py
    Please input three Positive Integers divided by comma (default is 3,5,7). [Enter. UnitTest press <Enter>]:
    </code></pre>

- Run program with argus
    - Argus with opts
        <pre><code>┌─ (marslo@MJ ~/FizzBuzzWhizz/V1.0) ->
        └─ $ python mainFizzBuzzWhizz.py --fizz=3 --buzz=5 --whizz=7
        </code></pre>

    - Some of argus with opts
        <pre><code>┌─ (marslo@MJ ~/FizzBuzzWhizz/V1.0) ->
        └─ $ python mainFizzBuzzWhizz.py --fizz=3 --buzz=4
        </code></pre>

    - Arugs without opt:
        <pre><code>┌─ (marslo@MJ ~/FizzBuzzWhizz/V1.0) ->
        └─ $ python mainFizzBuzzWhizz.py 3 6 9
        </code></pre>

### How to run the Unit Test
    <pre><code>┌─ (marslo@MJ ~/FizzBuzzWhizz/V1.0) ->
    └─ $ python testFizzBuzzWhizz.py 
    testargusValidity_fail (__main__.testdictProcess) ... Error:
            The value can ONLY be Positive Integer
    Check the valid options by inputing: $ python testFizzBuzzWhizz.py --help
    ok
    testargusValidity_ok (__main__.testdictProcess) ... ok
    testcalcPwd_13 (__main__.testdictProcess) ... ok
    testcalcPwd_15 (__main__.testdictProcess) ... ok
    testcalcPwd_3 (__main__.testdictProcess) ... ok
    testcalcPwd_5 (__main__.testdictProcess) ... ok
    testcalcPwd_7 (__main__.testdictProcess) ... ok
    testcreateRelDict (__main__.testdictProcess) ... Please input three Positive Integers divided by comma (default is 3,5,7). [Enter. UnitTest press <Enter>]:
    ok
    testoptValidity_fail (__main__.testdictProcess) ... Error:
            The options is invalid.
    Check the valid options by inputing: $ python testFizzBuzzWhizz.py --help
    ok
    testoptValidity_ok (__main__.testdictProcess) ... ok

    ----------------------------------------------------------------------
    Ran 10 tests in 0.002s

    OK
    </code></pre>

### Truth (No picture no truth)