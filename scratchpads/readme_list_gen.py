from os import listdir, getcwd
from os.path import isfile, join, exists
from pathlib import Path

try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

mypath = getcwd()

class Leetcode_readme:
    
    def urls_gen(self):
        results = []
        for f in listdir(mypath):
            if not isfile(join(mypath, f)):
                hypen_idx = f.find('-')
                
                if hypen_idx > -1:
                    leet_id, leet_problem = f[:hypen_idx], f[hypen_idx+1:]
                    
                    readme_path= join(mypath, f, 'README.md')
                    if leet_id.isnumeric() and exists(readme_path):
                        html = Path(readme_path).read_text()
                        
                        
                        parsed_html = BeautifulSoup(html)
                        leet_header = parsed_html.body.find('a')
                        leet_name = leet_header.text
                        leet_link = leet_header['href']
                        leet_difficulty = parsed_html.body.find('h3').text
                        
                        results.append((int(leet_id), leet_problem, leet_link, f, leet_difficulty))
                        
        
        sorted_results = self.sortTuples(results)
        for s in sorted_results:
            result = self.stringBuilder(*s)
            print(result)
                    
                   
    def sortTuples(self, problems_solved):
        
        problems_solved.sort(key = lambda x: x[0]) 
        return problems_solved
                    
    def stringBuilder(self, l_id, l_title, l_url, f_name, l_diff ):
        beautify_title = self.convert_case(l_title)
        str_row = f'|**{l_id}**| [{beautify_title}]({l_url}) | [python3]({f_name}/{f_name}.py) | {l_diff} |'
        return str_row
    
    def convert_case(self, my_string):
        my_string = my_string[0].upper() + my_string[1:]
        return my_string.replace("-","%s" % " ")

l = Leetcode_readme()
l.urls_gen()