input="out.txt"
output1="packet_eth.txt"
output2="packet_ip.txt"
output3="packet_tcp.txt"

i=0
j=0
var=''
while IFS= read -r first;
do
  i=$((i+1))
  if [ "$first" = "Source Address :$1" ];
  then
	var=$(sed -n "$((i+1)) p" $input)
	#echo $var
	if [ "$var" = "Destination Address :$2" ];
	then
		#echo "YES"
		sed -n $((i-13)),$((i-11))p $input > $output1	
		sed -n $((i-8)),$((i+1))p $input > $output2
		sed -n $((i+4)),$((i+12))p $input > $output3 
	fi
  elif [ "$first" = "Source Address :$2" ]
  then
        var=$(sed -n "$((i+1)) p" $input)
	#echo $var
	if [ "$var" = "Destination Address :$1" ]
	then
		#echo $argv[1]
		sed -n $((i-13)),$((i-11))p $input > $output1	
		sed -n $((i-8)),$((i+1))p $input > $output2
		sed -n $((i+4)),$((i+12))p $input > $output3 
	fi
  fi
done < "$input"
