# DS5111_FALL2023_SW2_Lab
DS5111_FALL2023_SW2_Lab 

Neil McPherson -- nhm5as

Here is the last section of Part 2 of the SW Skills II Reading and Lab:

1 point each for a reply in your README to each of the following questions:
What did you have to do to get make to work?

To get the pytest and tests target to work, I had to create the decorated function snooze5111() as described, and when this was defined correctly to return a string equal to the input, the assert statement passes in the pytest run.   


Similarly for python3 -m venv env, what did you have to do? (How likely are you to have guessed that without their clear error message?)
I had to install the venv first or the option to create the virutal environ wouldn't work -- would not have guessed that myself!


Both the pip install on the requirements.txt, and the call to run bin/clockdeco_param.py should be activating the virtual environment first. In other words, there are two bash commands separated by a ;, the first of which activates. Why can't we just do that on a separate line? In other words, why do we have to do that in one line and separate the commands with a ;

The reason here is that you need these commands to be run all in one subshell not in two separate shells. 


As it is, both the env and tests jobs run differently in that only one runs if the directory exists. This is as intended and all is well. What do you think about the job run? What would happen if you accidentaly had a file called run in your directory? What can we do to fix this?

Generally, to avoid conflict with a file called run, you can make the run task not dependent on any target and/or you can make run one of the .PHONY targets.  I also made my run target dependent on the env target here to ensure it it was created and activated.

The code provided to you for the test file starts with two lines, seemingly to append something to sys.path. What is the purpose of these lines?

This makes sure the PATH variable which the operating system searches for executables finds the current working directory first for any executables (which will be the tests directory, which is what you want to be tested!)  and this makes sure you are testing the right code.

Extra credit (Add these to your README at the bottom):
NB: Also add these to your README for the extra credit, just add an extra credit section at the bottom

1 point: Execute sudo apt install tree, and use that application to print out the file and directory structure, just as it is shown in this document at the top. You will have to look up in the reading, or google it in stackoverflow, what flag you need to exclude the 'env' directory. No need to cut and paste the structure, just include the full line you used to get it working.
Extra credit (Add these to your README at the bottom):
NB: Also add these to your README for the extra credit, just add an extra credit section at the bottom

1 point: Execute sudo apt install tree, and use that application to print out the file and directory structure, just as it is shown in this document at the top. You will have to look up in the reading, or google it in stackoverflow, what flag you need to exclude the 'env' directory. No need to cut and paste the structure, just include the full line you used to get it working.



1 point: Your .gitignore has 'env/', and also a callout to ignore the compiled python files, the ones in __pycache__ folders. What is the meaning of the **/* ?


1 point: do a pip list or pip freeze and call out versions of the pytest and pylint packages in your requirements.txt. Include them in your requirements.txt, and for the extra credit, just add a note reminding me you included them.


1 points: In the sample code from the book, why does the line if __name__=="__main__": allow the script to run if called directly, but not otherwise? What's going on there?


1 point: If you add two print statements, (or any statements for that matter), one above and one below the if __name__... line, what would happen when I do an import of the file? What happens when I call the file directly with python <filename>. Most importantly, why?.

1 point: Your .gitignore has 'env/', and also a callout to ignore the compiled python files, the ones in __pycache__ folders. What is the meaning of the **/* ?

The "**/*" means that *all* subdirectories below the current directory ('**' SPANS directories/subdirecties while a single '*' would only go one level deeper).   This is a way to ignore "all testing artifacts" so they arent uploaded to git.   


1 point: do a pip list or pip freeze and call out versions of the pytest and pylint packages in your requirements.txt. Include them in your requirements.txt, and for the extra credit, just add a note reminding me you included them.

Note to prof:   I included the versions here in my requirements.txt file!   Thanks this is good to know!  


1 points: In the sample code from the book, why does the line if __name__=="__main__": allow the script to run if called directly, but not otherwise? What's going on there?

Here this is a nice way to write some code all in one file so that it can be imported into other code or it can be tested in the same module -- in this way the code can be imported into other python code and only the functions not defined __main__ are imported, and if you are running (testing) this module alone you can just run the code directly by executing the python file, in which case the main function is running. 



1 point: If you add two print statements, (or any statements for that matter), one above and one below the if __name__... line, what would happen when I do an import of the file? What happens when I call the file directly with python <filename>. Most importantly, why?.

If you added a print statement above the "if __name__..." line, then when you import the file into another file, the line woould always be executed -- which is probably not what you want !   But the second print statement would only come into play when you are testing the isolated code and wouldn't run if you were importing it elsewhere.   This is because when you import the code here somewhere else, the code that is testing whether it the __name__ is __main__ or not doesn't get executed.   I tested this out and I made sure I was right by passing the -s option to pytest, after I inserted print statements into the code to see what happens (which was what I expected!) and I had to learn the -s option to make sure my "make tests" target showed this.   I left the code in and commented it out -- all in all this was an excellent learning experience!  -- Neil 