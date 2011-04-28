int main(){int i,k=103;char a[104]; for(i=0;i<26;++i,--k)a[i]=a[k]=i+65;strcpy(&a[26],"qwertyuiopasdfghjklzxcvbnmpyfgcrlaoeuidhtnsqjkxbmwvz");for(i=0;i<104; ++i)printf("%c",a[i]);}
