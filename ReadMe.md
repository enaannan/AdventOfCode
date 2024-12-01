To download the input for every year:
1. set the session token in the .env file 
2. activate the virtual environment
3. run


    python download_input.py --day <day as num eg ; 1> --year <year eg; 2020>

In the Tests directory;
1. Add the sample input and expected output in the format (<sample input>,<expected output>)
2. Run the tests with


    python -m pytest

Run specifc tests with 

    python -m pytest y2024\test_day1.py