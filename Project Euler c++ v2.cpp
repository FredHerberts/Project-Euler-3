#include <iostream>
#include <vector>
#include <cmath>
#include<ctime>
using namespace std;
int y = 1;
int count = 26;
bool factor = true;
long long number = 600851475143;
std::vector<int> primelist = {};
std::vector<int> primelist2 = {};
int start_s=clock() ;
int main()
{
    std::vector<int> primelist2 = {2, 3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101 };
    for (int x = 0; x < count; x++){
        factor = true;
        int z = primelist2[x];
        while (factor == true){
            if (number % z != 0){
                factor = false;
                break;
            }
            cout << z << endl;
            number /= z;
            if (z > number){return(0);}
        }
    }
    std::vector<int> primelist = { 3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101 };
    for (int y = 103; y <= number; y += 2) {
        bool prime = true;
        for (int x = 0; x < number; x++) {
            int z = primelist[x];
            if (y % z == 0) { prime = false; break; };
            if (z > sqrt(y)) { break; };
        }
        if (prime == true) { primelist.push_back(y);
            factor = true;
            while (factor == true){
                if (number % y != 0){
                    factor = false;
                    break;
                }
                cout << y << endl;
                number /= y;
            }
        };
    }
    int stop_s=clock();
    cout<<(stop_s-start_s)/double(CLOCKS_PER_SEC);
}
