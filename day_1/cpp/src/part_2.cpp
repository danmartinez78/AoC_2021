#include <iostream>
#include <fstream>
#include <vector>
#include <numeric>

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
    for(int i = 3; i < data.size(); i++){
        vector<int> a = vector<int>(data.begin() + i - 3, data.begin() + i);
        int sum_a = accumulate(a.begin(), a.end(), 0);
        vector<int> b = vector<int>(data.begin() + i - 2, data.begin() + i + 1);
        int sum_b = accumulate(b.begin(), b.end(), 0);
        cout << "i: " << i << ", a: ";
        for (auto c : a){cout << c << ',';}
        cout << " and b: ";
        for (auto c : b){cout << c << ',';}
        cout << " , " << sum_a << "," << sum_b << endl;
        if (sum_b > sum_a){
            count++;
        }
    }
    cout << count << endl;
}