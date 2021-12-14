#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

int read_data(string filename, vector<int>& data){
    ifstream input_file(filename);
    if (!input_file.is_open()) {
        cerr << "Could not open the file - '"
             << filename << "'" << endl;
        return EXIT_FAILURE;
    }

    string line, word;
    int age;
    vector<int> ages;
    while (getline(input_file, line, ',')){
        stringstream lineStream(line);
        lineStream >> age;
        cout << age << endl;
        ages.push_back(age);
    }

    input_file.close();
    data = ages;
    return EXIT_SUCCESS;
}

void print_pop(vector<long int>& pop){
        for (long int age:pop){
        cout << age << ',';
    }
    cout << endl;
}

int main(int argc, char *argv[]) {
    string filename(argv[1]);
    int days = atoi(argv[2]);
    vector<int> data; 
    read_data(filename, data);
    vector<long int> pop(9, 0);
    for (int age:data){
        pop[age] += 1;
    }
    print_pop(pop);
    for (int day = 0; day < days; day++){
        vector<long int> new_pop(9, 0);
        new_pop[8] = pop[0];
        new_pop[7] = pop[8];
        new_pop[6] = pop[7] + pop[0];
        new_pop[5] = pop[6];
        new_pop[4] = pop[5];
        new_pop[3] = pop[4];
        new_pop[2] = pop[3];
        new_pop[1] = pop[2];
        new_pop[0] = pop[1];
        pop = new_pop;
        print_pop(pop);
    }
    long int sum = 0;
    for (long int p:pop){
        sum += p;
    }
    cout << sum << endl;
}