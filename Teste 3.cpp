#include <iostream>
#include <vector>
#include <locale>
#include <fstream>
#include<algorithm>

using namespace std;

//criar um app amarzene numeros, e ordenar esses numeros.

void Load(vector<int>& numeros, const string& arquivo){
    ifstream InFile(arquivo);

    int num;
    while(InFile >> num){
        numeros.push_back(num);
    }
    InFile.close();

}

void save(const vector<int>& numeros, const string& arquivo){
    ofstream OutFile(arquivo, ios::trunc);

for(int num : numeros){
    OutFile << num << " ";
}
OutFile << endl;
OutFile.close();

}

void exibirnumeros( vector<int>& numeros){
    for(size_t i = 0; i < numeros.size(); ++i) {
        cout << i + 1 << ". "<< numeros[i] << endl;
    }

}

void ordenar(vector<int>& numeros, string& arquivo){
    sort(numeros.begin(), numeros.end());
    cout << "numeros ordenados\n";
    save(numeros, arquivo);
}

int main(){
    system("cls");
    setlocale(LC_ALL, "Portuguese_Brazil");

vector<int> numeros;
string arquivo = "lista_Num.txt";

Load(numeros, arquivo);
exibirnumeros(numeros);
ordenar(numeros, arquivo);


}
