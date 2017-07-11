// g++ -std=c++11 -o diofantica.exe diofantica.cpp

#include<bits/stdc++.h>
using namespace std;

const int MAX_LEN=20;
const int MAX_SUM=10000;
const int MAX_QTY_SOL=1000;

FILE *F;

void print(vector<int>&items){
	for(auto item:items)
		fprintf(F, "\n%d",item);
}

int n;
vector<vector<int>>memory;
vector<vector<int>>used;
vector<int>values;

bool dp(int pos, int sum){
	if(pos==n){
		return sum==0;
	}
	if(used[pos][sum])
		return memory[pos][sum];
	used[pos][sum]=1;
	int &ans=memory[pos][sum]=0;
	for(int i=0; i*values[pos]<=sum; i++){
		if(dp(pos+1,sum-i*values[pos])){
			ans=1;
		}
	}
	return ans;
}

vector<int>currentSolution;
int currentCapacity;

void rec(int pos, int sum){
	if(currentCapacity==0)
		return;
	if(pos==n){
		print(currentSolution);
		currentCapacity--;
		return;
	}
	for(int i=0;i*values[pos]<=sum;i++){
		if(currentCapacity==0)return;
		if(dp(pos+1, sum-i*values[pos])){
			currentSolution.push_back(i);
			rec(pos+1, sum-i*values[pos]);
			currentSolution.pop_back();
		}
	}
}

void solve(int target,vector<int> coeff){
	n=(int)coeff.size();
	memory=used=vector<vector<int>>(n,vector<int>(target+1));
	values=coeff;
	currentCapacity=MAX_QTY_SOL;
	rec(0,target);
	if(currentCapacity==0)
		printf("Number of solutions exceed %d\n",MAX_QTY_SOL);
}

int main(int argc, char *argv[]){
	F = fopen("soluciones.txt", "w");
	vector<int> v = vector<int>(atoi(argv[0]-1));
	for (int i = 2; i < argc; ++i){
		v.push_back(atoi(argv[i]));
	}
	solve(atoi(argv[1]), v);
	fclose(F);
}
