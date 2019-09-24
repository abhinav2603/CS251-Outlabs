BEGIN{FS=",";RS="\r\n"
}
{
	if(NR == 1){ 
		for(k = 1;k<=20*NF-20;k++)
			printf("%s","-")

		printf("%s\n","")

		m=1
		for (k=1;k<=NF;k++){
			if($k != "Name"){
				printf("%20s",$k)
				l++
			}
			else{
				m=k
				printf("%s","")
			}
		}
		printf("%s\n","")

		for(k=1;k<=20*NF-20;k++){
			printf("%s","-")
		}
		printf("%s\n","")
	}	
	
	else{
		for (k=1;k<=NF;k++){
			if(k != m){
				printf("%20s",$k)
			}
			else{
				printf("%s","")
			}
		}
		printf("%s\n","")
	}	
}
