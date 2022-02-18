#Codeforces Contest Bot
    function cf_contest_bot
        # Directory location of Codeforces Bot
        /Users/abhijayrajvansh/Desktop/development/projects/Codeforces-Contest-Bot && python main.py $argv
        # After running bot and downloading TC
        codeforces
        cd $argv && cd A
    end
    function cf-upsolver
        #directory of upsolver bot
        /Users/abhijayrajvansh/Desktop/development/projects/Codeforces-Contest-Bot && python cf-upsolver.py $argv
        #after running bot and downloading testcases
        /Users/abhijayrajvansh/desktop/codeforces/upsolve
    end

    
    # CommandLine Debug during contests:- Compile, Debug && Timed: C++
    function deb # ABHIJAY_DEBUG FILE_NAME.cpp
        echo "[ABHIJAY_DEBUG MODE] Compiling" $argv.cpp" with G++17..."
        echo
        echo "Input: "
        cat sample_input_1.txt
        echo "``````````````````````````````````````````````````````"
        g++ -std=c++17 -DABHIJAY_DEBUG $argv.cpp -o a.out
        sleep 1
        ./a.out
        
    end


    function run # ABHIJAY_DEBUG FILE_NAME.cpp
        echo "Compiling" $argv.cpp" with G++17..."
        echo
        g++ -std=c++17 $argv.cpp -o a.out
        sleep 1
        if test -f sample_input_1.txt;
            ./a.out <sample_input_1.txt> my_output_1.txt
            if cmp -s sample_output_1.txt my_output_1.txt;
                echo Running Testcase 1:(set_color --bold green) 'Passed!' 
                echo " Expected                                My Output"
                echo "```````````                             ````````````"
                diff -y -W 70 sample_output_1.txt my_output_1.txt
            else
                echo Running Testcase 1:(set_color --bold red) 'Failed' 
                echo " Expected                                My Output"
                echo "```````````                             ````````````"
                diff -y -W 70 sample_output_1.txt my_output_1.txt
            end
        end
    end

    function runsamples # runnig and testing sample testcases
        echo "[ABHIJAY_DEBUG MODE] Compiling main.cpp with G++17." \n
        sleep 1
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
                echo ""
            else
                echo Running Testcase 1:(set_color --bold red) 'Failed' (set_color normal)
                echo " Expected                              My Output"
                echo "```````````                           ````````````"
                diff -y -W 70 sample_output_1.txt my_output_1.txt
                echo ""
            end
        end
        if test -f sample_input_2.txt;
            ./$argv.out <sample_input_2.txt> my_output_2.txt
            if cmp -s sample_output_2.txt my_output_2.txt;
                echo Running Testcase 2:(set_color --bold green) 'Passed!' (set_color normal)
                echo ""
            else
                echo Running Testcase 2:(set_color --bold red) 'Failed' (set_color normal)
                echo " Expected                              My Output"
                echo "```````````                           ````````````"
                diff -y -W 70 sample_output_2.txt my_output_2.txt
                echo ""
            end
        end
        if test -f sample_input_3.txt;
            ./$argv.out <sample_input_3.txt> my_output_3.txt
            if cmp -s sample_output_3.txt my_output_3.txt;
                echo Running Testcase 3:(set_color --bold green) 'Passed!' (set_color normal)
                echo ""
            else
                echo Running Testcase 3:(set_color --bold red) 'Failed' (set_color normal)
                echo " Expected                              My Output"
                echo "```````````                           ````````````"
                diff -y -W 70 sample_output_3.txt my_output_3.txt
                echo ""
            end
        end
        if test -f sample_input_4.txt;
            ./$argv.out <sample_input_4.txt> my_output_4.txt
            if cmp -s sample_output_4.txt my_output_4.txt;
                echo Running Testcase 4:(set_color --bold green) 'Passed!' (set_color normal)
                echo ""
            else
                echo Running Testcase 4:(set_color --bold red) 'Failed' (set_color normal)
                echo " Expected                              My Output"
                echo "```````````                           ````````````"
                diff -y -W 70 sample_output_4.txt my_output_4.txt
                echo ""
            end
        end
    end
    function runtestcases # runnig  and testing sample testcases
        echo "[ABHIJAY_DEBUG MODE] Compiling main.cpp with G++17." \n
        sleep 1
        # Compiling file
        g++ -std=c++17 main.cpp -o main.out
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Running testcases:
        if test -f sample_input_1.txt;
            ./main.out <sample_input_1.txt> my_output_1.txt
            if cmp -s sample_output_1.txt my_output_1.txt;
                echo Running Testcase 1:(set_color --bold green) 'Passed!' (set_color normal)
            else
                echo Running Testcase 1:(set_color --bold red) 'Failed' (set_color normal)                
                echo "Expected                              My Output"
                echo "``````````                           ````````````"
                diff -y -W 70 sample_output_1.txt my_output_1.txt
                echo ""                
            end
        end
        if test -f sample_input_2.txt;
            ./main.out <sample_input_2.txt> my_output_2.txt
            if cmp -s sample_output_2.txt my_output_2.txt;
                echo Running Testcase 2:(set_color --bold green) 'Passed!' (set_color normal)
            else
                echo Running Testcase 2:(set_color --bold red) 'Failed' (set_color normal)                
                echo "Expected                               My Output"
                echo "``````````                            ````````````"
                diff -y -W 70 sample_output_2.txt my_output_2.txt
                echo ""                
            end
        end
        if test -f sample_input_3.txt;
            ./main.out <sample_input_3.txt> my_output_3.txt
            if cmp -s sample_output_3.txt my_output_3.txt;
                echo Running Testcase 3:(set_color --bold green) 'Passed!' (set_color normal)
            else
                echo Running Testcase 3:(set_color --bold red) 'Failed' (set_color normal)                
                echo "Expected                               My Output"
                echo "``````````                            ````````````"
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

    function compare
        if cmp -s sample_output_1.txt my_output_1.txt;
            printf 'The files are same'
        else
            printf 'The files are different'
            echo ""
            diff -y -W 70 sample_output_1.txt my_output_1.txt
        end
    end