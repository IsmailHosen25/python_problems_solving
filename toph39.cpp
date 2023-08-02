#include<iostream>
#include <cmath>
#include<bits/stdc++.h>
using namespace std;

const int N = 1e7;

int main(void) {
    bitset< N > s;
    s.reset();

    for(int i=2 ; i<N ; i++) {
        if(s[i]) continue;


        for(int u = 2*i ; u<=N ; u += i) {
            s[u] = 1;
        }
    }

    int n;
    cin >> n;

    int count = 0;
    for(int i = 2 ; i < N ; i++) {
        if(!s[i]) count++;


        if(count == n) {
            cout << i << '\n';
            break;
        }
    }
    return 0;
}

// bool isprime(int x){
//         int i=2;
//         while ( i!=(ceil(x/2)+1))
//         {
//             if(x%i==0){
//                 return false;
//             }
//             i+=1;
//         }
//         return true;   
// }

// int main(){

// int takeinginput;
// cin>>takeinginput;
// int x=0;
// int i=2;
// int nprime=0;
// while (x!=takeinginput)
// {
//     if(isprime(i)==true){
//         x+=1;
//         nprime=i;
//     }
//     i+=1;
   
// }
// cout<<nprime;

// }

// def isPrime(x):
//     for i in range(2,math.ceil(x/2)+1):
//         if(x%i==0):
//             return False
//     return True
// takainginput=int(input())
// x=0
// i=2
// c=0
// while x!=takainginput:
//     if(isPrime(i)==True):
//        x+=1
//        c=i
//     i+=1
// print(c)

