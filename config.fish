# CommandLine Debug during contests:- Compile, Debug && Timed: C++
    function deb # ABHIJAY_DEBUG FILE_NAME.cpp
        echo "[ABHIJAY_DEBUG MODE] Compiling" $argv".cpp with G++17..."
        echo "Input: "
        g++ -std=c++17 -DABHIJAY_DEBUG $argv.cpp -o a.out && ./a.out
    end

    function runsamples # runnig and testing sample testcases

        #navigating to problem dir:
        cd ..
        cd $argv
        # Compiling file
        g++ -std=c++17 $argv.cpp -o $argv.out
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Running testcases:
        if test -f sample_input_1.txt;
            ./$argv.out <sample_input_1.txt> my_output_1.txt
            if cmp -s sample_output_1.txt my_output_1.txt;
                echo Running Testcase 1:(set_color --bold green) 'Passed!' (set_color normal)
            else
                echo Running Testcase 1:(set_color --bold red) 'Failed' (set_color normal)
                echo " Correct Output                         My Output"
                echo "```````````````                        ````````````"
                diff -y -W 70 sample_output_1.txt my_output_1.txt
                echo ""
            end
        end
        if test -f sample_input_2.txt;
            ./$argv.out <sample_input_2.txt> my_output_2.txt
            if cmp -s sample_output_2.txt my_output_2.txt;
                echo Running Testcase 2:(set_color --bold green) 'Passed!' (set_color normal)
            else
                echo Running Testcase 2:(set_color --bold red) 'Failed' (set_color normal)
                echo " Correct Output                         My Output"
                echo "```````````````                        ````````````"
                diff -y -W 70 sample_output_2.txt my_output_2.txt
                echo ""
            end
        end
        if test -f sample_input_3.txt;
            ./$argv.out <sample_input_3.txt> my_output_3.txt
            if cmp -s sample_output_3.txt my_output_3.txt;
                echo Running Testcase 3:(set_color --bold green) 'Passed!' (set_color normal)
            else
                echo Running Testcase 3:(set_color --bold red) 'Failed' (set_color normal)
                echo " Correct Output                         My Output"
                echo "```````````````                        ````````````"
                diff -y -W 70 sample_output_3.txt my_output_3.txt
                echo ""
            end
        end
    end

    function checkfile 
        if test -f $argv;
            echo (set_color --bold green)"File Exist."
        else
            echo (set_color --bold red)"File Doesn't Exist."
        end
    end
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    function crun # ABHIJAY_DEBUG FILE_NAME
        echo "Compiling" $argv.cpp "with G++17..."
        #echo "Input: "
        g++ -std=c++17 $argv.cpp -o a.out && ./a.out
    end
    function deb-timed # ABHIJAY_DEBUG FILE_NAME + gtimeout 5 sec
        echo "[ABHIJAY_DEBUG MODE] Compiling" $argv.cpp "with G++17..."
        echo "Input: "
        g++ -std=c++17 -DABHIJAY_DEBUG $argv.cpp -o a.out && gtimeout 3s ./a.out
    end
    function dbrun # runnig and testing sample testcases
        echo "Compiling main.cpp with G++17..." \n
        cd upsolve
        # # [Clearing Directories...]
        # rm -r upsolve
        # mkdir upsolve
        # cd upsolve 
        # codeforces .. upsolve
        # Compiling file
        g++ -std=c++17 $argv.cpp -o $argv.out
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Running testcases:
        if test -f sample_input_1.txt;
            ./$argv.out <sample_input_1.txt> my_output_1.txt
            if cmp -s sample_output_1.txt my_output_1.txt;
                echo Running Testcase 1:(set_color --bold green) 'Passed!' (set_color normal)
            else
                echo Running Testcase 1:(set_color --bold red) 'Failed' (set_color normal)
                echo " Correct Output                         My Output"
                echo "```````````````                        ````````````"
                diff -y -W 70 sample_output_1.txt my_output_1.txt
                echo ""
            end
        end
        if test -f sample_input_2.txt;
            ./$argv.out <sample_input_2.txt> my_output_2.txt
            if cmp -s sample_output_2.txt my_output_2.txt;
                echo Running Testcase 2:(set_color --bold green) 'Passed!' (set_color normal)
            else
                echo Running Testcase 2:(set_color --bold red) 'Failed' (set_color normal)
                echo " Correct Output                         My Output"
                echo "```````````````                        ````````````"
                diff -y -W 70 sample_output_2.txt my_output_2.txt
                echo ""
            end
        end
        if test -f sample_input_3.txt;
            ./$argv.out <sample_input_3.txt> my_output_3.txt
            if cmp -s sample_output_3.txt my_output_3.txt;
                echo Running Testcase 3:(set_color --bold green) 'Passed!' (set_color normal)
            else
                echo Running Testcase 3:(set_color --bold red) 'Failed' (set_color normal)
                echo " Correct Output                         My Output"
                echo "```````````````                        ````````````"
                diff -y -W 70 sample_output_3.txt my_output_3.txt
                echo ""
            end
        end
        codeforces #codeforces local directory
    end
#