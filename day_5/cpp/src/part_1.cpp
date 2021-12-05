#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

struct command{
    string direction;
    int magnitude;
};

struct position{
    int horizontal = 0;
    int depth = 0;
};

int read_data(string filename, vector<command>& data){
    ifstream input_file(filename);
    if (!input_file.is_open()) {
        cerr << "Could not open the file - '"
             << filename << "'" << endl;
        return EXIT_FAILURE;
    }

    string line, word;
    string dir;
    int mag;
    vector<command> commands;
    while (getline(input_file, line)){
        stringstream lineStream(line);
        lineStream >> dir >> mag;
        cout << dir << "," << mag << endl;;
        command cmd;
        cmd.direction = dir;
        cmd.magnitude = mag;
        commands.push_back(cmd);
    }

    input_file.close();
    data = commands;
    return EXIT_SUCCESS;
}

int main(int argc, char *argv[]) {
    string filename(argv[1]);
    vector<command> data; 
    read_data(filename, data);
    position pos;
    for (auto cmd : data){
        if (cmd.direction == "forward"){pos.horizontal += cmd.magnitude;}
        else if (cmd.direction == "up"){pos.depth -= cmd.magnitude;}
        else if (cmd.direction == "down"){pos.depth += cmd.magnitude;}
        }
    cout << pos.horizontal << ", " << pos.depth << ", " << pos.horizontal * pos.depth << endl;
}