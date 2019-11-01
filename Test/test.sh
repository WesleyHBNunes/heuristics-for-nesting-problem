#!/bin/bash
sort_function[0]=area_polygon
sort_function[1]=area_no_used_of_polygon
sort_function[2]=percent_area_no_used_of_polygon
sort_function[3]=ray_polygon
sort_function[4]=rectangle_polygon_area

rotate_function[0]=heuristic_highest_axis
rotate_function[1]=heuristic_highest_side

txt_files[0]=blaz
txt_files[1]=shapes
txt_files[2]=shirts
txt_files[3]=swim
txt_files[4]=trousers

xls_files[0]=albano
xls_files[1]=mao
xls_files[2]=dighe
xls_files[3]=marques
xls_files[4]=han

sheets[0]=Albano
sheets[1]=Mao
sheets[2]=Dighe2
sheets[3]=Marques
sheets[4]=Han

heuristic[0]=Bottom-Left
heuristic[1]=Bottom-Left-Slide
heuristic[2]=Greedy
heuristic[3]=New-Heuristic
heuristic[4]=New-Heuristic-Modified

for h in {0..3}
do
    echo "${heuristic[h]}"
    echo
    echo "TXT FILES"
    echo
    for i in {0..4}
    do
        for j in {0..4}
        do
            for k in {0..1}
            do
                echo "File ${txt_files[i]}, sort_function: ${sort_function[j]}, rotate_function: ${rotate_function[k]}"
                python3 ../Tests.py ${txt_files[i]} $j $k $h
                echo
            done
        done
    done
    echo "XLS FILES"
    echo
    for i in {0..4}
    do
        for j in {0..4}
        do
            for k in {0..1}
            do
                echo "File ${xls_files[i]}, sort_function: ${sort_function[j]}, rotate_function: ${rotate_function[k]}"
                python3 ../Tests.py ${xls_files[i]} ${sheets[i]} $j $k $h
                echo
            done
        done
    done
    echo
    echo
done




for h in {4..4}
do
    echo "${heuristic[h]}"
    echo
    echo "TXT FILES"
    echo
    for i in {0..4}
    do
        for j in {0..4}
        do
            echo "File ${txt_files[i]}, sort_function: ${sort_function[j]}"
            python3 ../Tests.py ${txt_files[i]} $j 2 $h 2>/dev/null
            echo
        done
    done

    echo "XLS FILES"
    echo
    for i in {0..4}
    do
        for j in {0..4}
        do
            echo "File ${xls_files[i]}, sort_function: ${sort_function[j]}"
            python3 ../Tests.py ${xls_files[i]} ${sheets[i]} $j 2 $h 2>/dev/null
            echo
        done
    done
    echo
    echo
done
