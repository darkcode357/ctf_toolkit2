import cmd


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class ctf_shell(cmd.Cmd):
    """ctf_shell"""

    prompt = bcolors.OKGREEN + 'ctf_shell[$]: '
    intro = "ctf_prompt_beta1"

    doc_header = bcolors.OKGREEN + 'doc_header'
    misc_header = bcolors.OKBLUE + 'misc_header'
    undoc_header = bcolors.ENDC + 'undoc_header'

    ruler = '-'

    def do_prompt(self, line):
        "customizar o promt"
        self.prompt = line + ': '

    def do_comandos(self, line):
        comandos = ['dsa', 'dsadsa']
        for i in comandos:
            print(i)

    def do_EOF(self, line):
        return True


if __name__ == '__main__':
    ctf_shell().cmdloop()
