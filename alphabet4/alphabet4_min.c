main(i){char a[105];strcpy(&a[26],"qwertyuiopasdfghjklzxcvbnmpyfgcrlaoeuidhtnsqjkxbmwvz");for(i=0;i<26;)a[i]=a[103-i]=i+++65;puts(a);}
