#include <string>
#include <vector>
#include <sstream>
#include <ctype.h>

using namespace std;

vector<string> flag_rules;

bool isNumber(const string& str)
{
    for (char const &c : str) {
        if (isdigit(c) == 0) return false;
    }
    return true;
}

bool isAlpha(const string& str)
{
    for (char const &c : str) {
        if (isalpha(c) == 0) return false;
    }
    return true;
}


vector<string> split(string input, char delimiter) {
    vector<string> ret;
    stringstream ss(input);
    string temp;
 
    while (getline(ss, temp, delimiter)) {
        ret.push_back(temp);
    }
 
    return ret;
}

bool checkValidFlag(string flag, string &arg_type)
{
    if(flag[0] != '-')
        return false;
    
    for(int i=0; i<flag_rules.size(); i++)
    {
        if(flag == split(flag_rules[i],' ')[0])
            arg_type = split(flag_rules[i],' ')[1];
    }
    
    string flag_name = flag.substr(1,10);
    return isAlpha(flag_name);
}

bool checkValidFlagArgType(string flag_arg, string &arg_type)
{
    if(arg_type == "STRING" || arg_type == "STRINGS")
        return isAlpha(flag_arg);
    else if(arg_type == "NUMBER" || arg_type == "NUMBERS")
        return isNumber(flag_arg);
    else
        return false;
}

bool checkArgsPart(vector<string> args)
{    
    string arg_type;
    bool need_flag = true;
    string need_type;
    for(int i=0; i<args.size();i++)
    {
        if(need_flag)
        {
            if(args[i][0] != '-') return false;

            if(!checkValidFlag(args[i], arg_type))
            return false;
            if(arg_type == "NULL")
            {
                need_flag = true;
            }
            else
            {
                need_flag = false;
                if(arg_type == "NUMBERS")
                {

                }
                if(arg_type == "")
                if(!checkValidFlagArgType(args[i+1], arg_type))
                    return false;
                need_type = arg_type;
            }
        }        
        else
        {
            if(need_type == "STRINGS" || need_type == "NUMBERS")
            {
                if(args[i][0] != '-')
                {
                    need_flag = true;
                    i--;
                    continue;
                }
                if(!checkValidFlagArgType(args[i], need_type))
                    return false;
            }
            else
            {
                return false;
            }
        }
    }
    return true;
}

void parseCommand(string _command, string &program, vector<string> &args)
{
    vector<string> command = split(_command, ' ');
    program = command[0];
    command.erase(command.begin());
    args = command;
}

bool checkCommand(string command, string program_name)
{
    vector<string> args;
    string program;
        
    parseCommand(command, program, args);
    
    if(program_name != program)
        return false;
    return checkArgsPart(args);
}

vector<bool> solution(string program, vector<string> _flag_rules, vector<string> commands) {
    vector<bool> answer;
    flag_rules = _flag_rules;

    for(int i=0; i<commands.size(); i++)
    {
        bool bResult;
        bResult = checkCommand(commands[i],program);
        answer.push_back(bResult);
    }
    
    return answer;
}