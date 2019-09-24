#!/bin/bash
touch bar.sh
chmod 755 bar.sh
echo "#!/bin/bash" >> bar.sh
echo "source ./resources/defineColors.sh" >> bar.sh
echo "cat "$1" |" >> bar.sh
#awk -v on="$fg$bg" -v off="$(tput sgr0)" '/tag/{$0=on $0 off}1' |
awk 'BEGIN{FS=",";RS="\n"}{
	if(NR!=1){
		print "awk -v  f1=\x22$"$4"_BACKGROUND$"$3"_FONT\x22 -v f2=\x22$(tput sgr0)\x22 \x27/"$1"/{$0=f1 $0 f2}1\x27 |"
	}
}' $2 >> bar.sh
echo "cat > outputB" >> bar.sh
echo "cat outputB" >> bar.sh
echo "rm outputB" >> bar.sh
./bar.sh
rm bar.sh
