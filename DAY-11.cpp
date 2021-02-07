
#include <iostream>
#include <stdio.h>
#include<bits/stdc++.h>
using namespace std;
int main()
{
    int i;
    int upper=0,lower=0;
    char ch[100];
    gets(ch);
    for(i=0; ch[i]!=0; i++)
    {
        if(ch[i]>='A' && ch[i]<='Z')
        {
            upper++;
        }
        else if(ch[i]>='a' && ch[i]<='z')
        {
            lower++;
        }
    }
cout<<upper<<endl<<lower;
return 0;
}
