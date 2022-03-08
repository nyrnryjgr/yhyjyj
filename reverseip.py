import requests, sys, subprocess

try:
    import blessed
except:
    print("Module Error, Installing Blessed Module")
    subprocess.run("pip3 install blessed", shell=True, stderr=subprocess.DEVNULL)
   


term = blessed.Terminal()
d1 = term.color_rgb(200, 20, 245)

reset = term.reset()
underline = term.underline()
def run():
    
    try:
        print(f'{d1}')
        print(r'''
░█████╗░██╗░░░██╗██████╗░░█████╗░██████╗░░█████╗░
██╔══██╗██║░░░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗
███████║██║░░░██║██████╔╝██║░░██║██████╔╝███████║
██╔══██║██║░░░██║██╔══██╗██║░░██║██╔══██╗██╔══██║
██║░░██║╚██████╔╝██║░░██║╚█████╔╝██║░░██║██║░░██║
╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝
''')
        d2 = term.color_rgb(207, 68, 242)
        d3 = term.color_rgb(215, 84, 247)
        d4 = term.color_rgb(220, 100, 250)
        d5 = term.color_rgb(227, 124, 252)
        d6 = term.color_rgb(230, 139, 252)
        print(f'{reset}{underline}{d2}Rev{d3}ers{d4}e {d5}I{d6}P{reset}\n\033[31m───\033[32m﹥ Aurora-Corp')

        url = sys.argv[1]
        
        
       

        api = requests.get(f"https://api.hackertarget.com/reverseiplookup/?q={url}", headers={'Cache-Control': 'no-cache'})
        raw = api.text
        

        subprocess.run('sudo rm -r iplist.txt', shell=True)
        with open('iplist.txt', '+a')as f:
            f.write(raw)
            f.close()
        b = term.color_rgb(255, 105, 197)
        print(f'\n{b}[{d2}S{d3}ucc{d4}es{d5}..{d8}.{b}]:\n\033[31m───\033[32m﹥ {d8}Sav{d7}e{d6}d {d5}i{d4}n {d3}ip{d2}list.{d1}txt')
        sys.exit()
        
    except:
        print('\033[31m───\033[32m﹥ \033[0mUsage: python3 reverseip.py (url)\n')

if __name__ == "__main__":
    run()
