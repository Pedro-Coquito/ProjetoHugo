#include <locale>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

//CARREGAMENTO
void Load(vector<int>& numeros, const string&arquivo){
    ifstream InFile(arquivo);
    if(!InFile.is_open()){
        cout << "N�o foi possivel carregar o arquivo!" << arquivo << "\n";
        return;
    }
    int num; 
    while(InFile >> num){
        numeros.push_back(num);
    }
    InFile.close();
}

//SALVVAMENTO
void Save(const vector<int>& numeros, const string& arquivo){
    ofstream OutFile(arquivo, ios::trunc);

    if(!OutFile.is_open()){
        cout << "Erro: Nenhum arquivo encontrado!\n" << arquivo;
        return;
    }
    for(int num : numeros){
        OutFile << num << " ";
    }
    OutFile << endl;
    OutFile.close();
}

//EXIBI��O DE NUMEROS
void ExibirNumero(const vector<int>& numeros){
    if(numeros.empty()){
        cout << "A lista est� vazia\n";
    }
    else{
        cout<< "Lista de numeros\n";
        for (size_t i = 0; i < numeros.size(); ++i){
            cout << i + 1 << ". " << numeros[i] << endl;
        }
    }
}

//ADICIONA NUMEROS
void AdicionarNumero(vector<int>& numeros, string& arquivo){
    int numero;
    cout << "digite um numero para adicionar a lista:\n";
    cin>> numero;

    numeros.push_back(numero);
    Save(numeros, arquivo);
    cout << "Numero adicionado com sucesso!!\n";
}

//REMOVE OS NUMEROS
void RemoverNumero(vector<int>& numeros, string& arquivo){
    if(numeros.empty()){
        cout << "A lista est� vazia, n�o h� numeros para serem removidos.\n";
    }
    
    int numero;
    cout << "Digite o numero que deseja remover!\n";
    cin >> numero;

    auto it = find(numeros.begin(), numeros.end(), numero);
    if(it != numeros.end()){
        numeros.erase(it);
        Save(numeros, arquivo);
        cout << "Numero removido com sucesso!!\n";
    } 
    else{
        cout << "Numero n�o encontrado na lista!!\n";
    }
}
//Ordena numeros  em ordem crescente
void ordenarNumero(vector<int>&numeros, string& arquivo){
    if(numeros.empty()){ 
        cout<< "A lista est� vazia, Nenhum numero para ordenar!!\n";
    return;
    }
    if(is_sorted(numeros.begin(), numeros.end())) {
        cout << "A lista j� est� ordenada!!\n";
    return;
    }

    sort(numeros.begin(), numeros.end());
    cout<< "Lista Ordenada em ordem crescente";
    Save(numeros, arquivo);
}

void Find(vector<int>& numeros, string& arquivo){
    if(numeros.empty()){
        cout<< "A lista est� vazia, nenhum numero para encontrar!\n";
        return;
    }

    int numero;
    cout<<"Digite o numero que quer encontrar:\n";
    cin >> numero;

    vector<int> indices;
    for (size_t i = 0; i < numeros.size(); i++){
        if(numeros[i] == numero) {
            indices.push_back(i +1);
        }

    }

    if(!indices.empty()){
        cout << "Numero encontrado nas posi��es: ";
        for(int pos : indices){
            cout << pos << " ";
        }
        cout << endl;
    }  
    else{
        cout << "Numero n�o encontrado na lista!!\n";
    }

    Save(numeros, arquivo);
}


int main(){
    system("cls");
    setlocale(LC_ALL, "Portuguese_Brazil");

    vector<int> numeros;
    string arquivo = "Lista Numeros.txt";

    Load(numeros, arquivo);
    


    int opcao;

    do {
         cout << "\n===== GERENCIADOR DE N�MEROS =====\n";
        cout << "1. Adicionar n�mero\n";
        cout << "2. Remover n�mero\n";
        cout << "3. Exibir n�meros\n";
        cout << "4. Ordenar n�meros\n";
        cout << "5. Buscar n�mero\n";
        cout << "6. Sair\n";
        cout << "Escolha uma op��o: ";
        cin >> opcao;

    switch(opcao) {

    case 1:
        AdicionarNumero(numeros, arquivo);
        break;
    case 2:
        RemoverNumero(numeros, arquivo);
        break;
    case 3:
        ExibirNumero(numeros);
        break;
    case  4: 
        ordenarNumero(numeros, arquivo);
        break;
    case 5:
        Find(numeros, arquivo);
        break;
    case 6:
        cout << "Saindo do Programa...\n";
      break;

    default:
        cout << "Op��o invalida! Tente novamente.\n"; 
        break;
    }
    } 
    while (opcao != 6);

    return 0;

}