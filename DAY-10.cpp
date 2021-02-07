/* Read input from STDIN. Print your output to STDOUT*/
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>
#include<bits/stdc++.h>
#include<iostream>
using namespace std;
int main()
{
    int n;cin>>n;
    int a[n];
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }
    int d= sizeof(a)/sizeof(a[0]);
    sort(a,a+d);
    cout<<a[n-2];


}
