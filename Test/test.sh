#!/bin/bash
sort_function[0]=area_polygon
sort_function[1]=area_no_used_of_polygon
sort_function[2]=percent_area_no_used_of_polygon
sort_function[3]=ray_polygon
sort_function[4]=rectangle_polygon_area

rotate_function[0]=heuristic_highest_axis
rotate_function[1]=heuristic_highest_side

txt_files[0]=blaz.txt
txt_files[1]=shapes.txt
txt_files[2]=shirts.txt
txt_files[3]=swim.txt
txt_files[4]=trousers.txt

xls_files[0]=albano.xls
xls_files[1]=mao.xls
xls_files[2]=dighe.xls
xls_files[3]=marques.xls
xls_files[4]=han.xls

sheets[0]=Albano
sheets[1]=Mao
sheets[2]=Dighe2
sheets[3]=Marques
sheets[4]=Han

echo "TXT FILES"
echo 
for i in {0..4}
do
	for j in {0..4}
	do   
    	for k in {0..1}
    	do
    		echo "File ${txt_files[i]}, sort_function: ${sort_function[j]}, rotate_function: ${rotate_function[k]}"
      		python3 ../Tests.py ${txt_files[i]} $j $k
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
      		python3 ../Tests.py ${xls_files[i]} ${sheets[i]} $j $k
      		echo 
   		done
	done
done