#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int read_data(string filename, vector<int>& data){
    ifstream input_file(filename);
    if (!input_file.is_open()) {
        cerr << "Could not open the file - '"
             << filename << "'" << endl;
        return EXIT_FAILURE;
    }

    int number;
    while (input_file >> number) {
        data.push_back(number);
    }

    input_file.close();
    return EXIT_SUCCESS;;
}

int main(int argc, char *argv[]) {
    string filename(argv[1]);
    vector<int> data; 
    read_data(filename, data);

    int count = 0;
    for(int i = 1; i < data.size(); i++){
        if (data[i] > data[i-1]){
            count++;
        }
    }
    cout << count << endl;
}