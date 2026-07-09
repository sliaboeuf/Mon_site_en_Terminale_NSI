import os
import hashlib
from math import log10
import random
import re
    
MAX_EMPTY_IDE = 10**8

# print(env.variables.config['theme']['palette']) # access palette color. Automatic toggle of color ?

def define_env(env):
    "Hook function"

    @env.macro
    def script(lang: str, nom: str) -> str:
        "Renvoie le script dans une balise bloc avec langage spécifié"
        return f"""```{lang}
--8<---  "docs/""" + os.path.dirname(env.variables.page.url.rstrip('/')) + f"""/{nom}"
```"""
    # f"docs/{os.path.dirname(env.variables.page.url.rstrip('/'))}/scripts/{nom}.py"

    @env.macro
    def py(nom: str) -> str:
        "macro python rapide"
        return script('python', "scripts/" + nom + ".py")

    @env.macro
    def html_fig(num: int) -> str:
        "Renvoie le code HTML de la figure n° `num`"
        return f'--8<-- "docs/' + os.path.dirname(env.variables.page.url.rstrip('/')) + f'/figures/fig_{num}.html"'

    env.variables['compteur_exo'] = 0
    
    @env.macro
    def exercice(var=True, niveau=None, prem=None, text =""):
        # si var == False, alors l'exercice est placé dans une superfence.
        star = '⭐'
        if niveau is not None:
            star *= niveau
        if prem is not None : env.variables['compteur_exo'] = prem
        env.variables['compteur_exo'] += 1
        root = f"Exercice { env.variables['compteur_exo']} {star} {text}"
        return f"""exo \"{root}\"""" if var else '\"'+root+'\"'

    @env.macro
    def correction(booleen, texte):
        if booleen == False:
            return ""
        else:
            return texte
            
    @env.macro
    def cours():
        return f'done "Cours"'

    @env.macro
    def ext():
        return f'ext "Pour aller plus loin"'

    @env.macro
    def tit(ch = "", text = ""):
        # Tasklist In Table
        checked = 'checked=""' if ch == 'x' else ''
        return f"""<ul class="task-list"><li class="task-list-item">\
            <label class="task-list-control"><input type="checkbox" {checked}>\
            <span class="task-list-indicator"></span>\
            </label>{text}</li></ul>"""

    env.variables['term_counter'] = 0
    env.variables['IDE_counter'] = 0
    INFTY_SYMBOL = '\u221e'
    from urllib.parse import unquote

    @env.macro
    def terminal() -> str:
        """   
        Purpose : Create a Python Terminal.
        Methods : Two layers to avoid focusing on the Terminal. 1) Fake Terminal using CSS 2) A click hides the fake 
        terminal and triggers the actual Terminal.
        """        
        tc = env.variables['term_counter']
        env.variables['term_counter'] += 1
        return f"""<div onclick='start_term("id{tc}")' id="fake_id{tc}" class="terminal_f"><label class="terminal"><span>>>> </span></label></div><div id="id{tc}" class="hide"></div>"""

    def read_ext_file(nom_script : str, path : str, filetype : str = 'py') -> str:
        """
        Purpose : Read a Python file that is uploaded on the server.
        Methods : The content of the file is hidden in the webpage. Replacing \n by a string makes it possible
        to integrate the content in mkdocs admonitions.
        """
        docs_path = f"""docs/"""

        try: 
            if path == "":
                f = open(f"""{docs_path}/scripts/{nom_script}.{filetype}""", encoding="utf8")
            else:
                f = open(f"""{docs_path}/{path}/{nom_script}.{filetype}""", encoding="utf8")
            content = ''.join(f.readlines())
            f.close()
            content = content + "\n"
            # Hack to integrate code lines in admonitions in mkdocs
            # change backslash_newline by backslash-newline
            return content.replace('\n','bksl-nl').replace('_','py-und').replace('*','py-str')
        except :
            return ""
        
    def generate_content(nom_script : str, path : str, filetype : str = 'py') -> str:
        """
        Purpose : Return content and current number IDE {tc}.
        """
        content = read_ext_file(nom_script, path, filetype)

        if content not in [None, ""]:
            tc = hashlib.sha1(content.encode('utf-8')).hexdigest()
        else : # non-existent file, empty file
            tc = env.variables['IDE_counter']
            env.variables['IDE_counter'] += 1

        return content, str(tc).zfill(int(log10(MAX_EMPTY_IDE)))


    def create_upload_button(tc : str) -> str:
        """
        Purpose : Create upload button for a IDE number {tc}.
        Methods : Use an HTML input to upload a file from user. The user clicks on the button to fire a JS event
        that triggers the hidden input.
        """
        #path_img = env.variables.page.abs_url.split('/')[1]
        path_img = f""""""
        return f"""<button class="tooltip" onclick="document.getElementById('input_editor_{tc}').click()"><img src="{path_img}images/buttons/icons8-upload-64.png"><span class="tooltiptext">Téléverser</span></button>\
                <input type="file" id="input_editor_{tc}" name="file" enctype="multipart/form-data" class="hide"/>"""

    def create_unittest_button(tc: str, nom_script: str, path : str, mode: str, MAX : int = 5) -> str:
        """
        Purpose : Generate the button for IDE {tc} to perform the unit tests if a valid test_script.py is present.
        Methods : Hide the content in a div that is called in the Javascript
        """
        stripped_nom_script = nom_script.split('/')[-1]
        relative_path = '/'.join(nom_script.split('/')[:-1])
        nom_script = f"{relative_path}/{stripped_nom_script}_test"
        content = read_ext_file(nom_script, path)
        # print(nom_script, path, content, content == "")
        if content != "":
            #path_img = env.variables.page.abs_url.split('/')[1]
            path_img = f""""""
            return f"""<span id="test_term_editor_{tc}" class="hide">{content}</span>\
                <button class="tooltip" onclick=\'executeTest("{tc}","{mode}")\'>\
                <img src="{path_img}images/buttons/icons8-check-64.png">\
                <span class="tooltiptext">Valider</span></button><span class="compteur">\
                {MAX}/{MAX}\
                </span>"""
        else: 
            return ''

    def blank_space(s=0.3) -> str:
        """ 
        Purpose : Return 5em blank spaces. Use to spread the buttons evenly
        """
        return f"""<span style="display: inline-block; width:{s}em"></span>"""

    def get_max_from_file(content : str) -> tuple:#[str, int]: # compatibilité Python antérieur 3.8
        split_content = content.split('bksl-nl')
        max_var = split_content[0]
        if max_var[:4] != "#MAX":
            MAX = 5 
        else:
            value = max_var.split('=')[1].strip()
            MAX = int(value) if value not in ['+', 1000] else INFTY_SYMBOL
            i = 1
            while split_content[i] == '':
                i += 1
            content = 'bksl-nl'.join(split_content[i:])
        return content, MAX

    def test_style(nom_script : str, element : str) -> bool:
        guillemets = ["'", '"']
        ide_style = ["", "v"]
        styles = [f"""IDE{istyle}({i}{nom_script}{i}""" for i in guillemets for istyle in ide_style]
        return any([style for style in styles if style in element])

    def convert_url_to_utf8(nom : str) -> str:
        return unquote(nom, encoding='utf-8')
        

    @env.macro
    def IDEv(nom_script : str = '', MAX : int = 5, SANS : str = "") -> str:
        """
        Purpose : Easy macro to generate vertical IDE in Markdown mkdocs.
        Methods : Fire the IDE function with 'v' mode.
        """
        return IDE(nom_script, mode = 'v', MAX = MAX, SANS = SANS)

    def generate_key(path_file: str):
        try:
            f = open(f"docs/{path_file}/clef.txt", "r", encoding="utf8")
            clef = f.read()            
        except: 
            clef = "" # base case -> no clef.txt file
        return clef

    def tooltip_button(onclick_action : str, button_style : str):
        return f"""<button class="tooltip" onclick={onclick_action}>{button_style}</button>"""

    @env.macro
    def IDE(nom_script : str = '', mode : str = 'h', MAX : int = 5, SANS : str = "") -> str:
        """
        Purpose : Create an IDE (Editor+Terminal) on a Mkdocs document. {nom_script}.py is loaded on the editor if present. 
        Methods : Two modes are available : vertical or horizontal. Buttons are added through functional calls.
        Last span hides the code content of the IDE if loaded.
        """
        #print("docs_dirs", env.conf['docs_dir'])
        #print(env.variables.page.abs_url)
        #path_img = convert_url_to_utf8(env.variables.page.abs_url).split('/')[1]
        path_img = f""""""
        #print("coucou", path_img)
        path_file = '/'.join(filter(lambda folder: folder != "", convert_url_to_utf8(env.variables.page.abs_url).split('/')[2:-2]))
        #print('P1','/'.join(filter(lambda folder: folder != "", convert_url_to_utf8(env.variables.page.url).split('/')[:-2])))
        #print('P2','/'.join(filter(lambda folder: folder != "", convert_url_to_utf8(env.variables.page.abs_url).split('/')[2:-2])))

        clef = generate_key(path_file)

        content, tc = generate_content(nom_script, path_file)
        corr_content, _ = generate_content(f"""{'/'.join(nom_script.split('/')[:-1])}/{nom_script.split('/')[-1]}_corr""", path_file)

        content, max_from_file = get_max_from_file(content)
        MAX = max_from_file if MAX == 5 else MAX
        MAX = MAX if MAX not in ['+', 1000] else INFTY_SYMBOL

        SANS_formatted = ","+"".join(SANS.split(" ")) if len(SANS)>0 else ""
        div_edit = f'<div class="ide_classe" data-max={MAX} data-exclude={"eval,exec" + SANS_formatted} >'

        if mode == 'v':
            div_edit += f'<div class="wrapper"><span id="comment_editor_{tc}" class="comment">###</span><div class="interior_wrapper"><div id="editor_{tc}"></div></div><div id="term_editor_{tc}" class="term_editor"></div></div>'
        else:
            div_edit += f'<div class="wrapper_h"><span id="comment_editor_{tc}" class="comment">###</span><div class="line" id="editor_{tc}"></div><div id="term_editor_{tc}" class="term_editor_h terminal_f_h"></div></div>'

        div_edit += tooltip_button(f"""'interpretACE("editor_{tc}","{mode}")'""", f"""<img src="{path_img}images/buttons/icons8-play-64.png"><span class="tooltiptext">Lancer</span>""")
        div_edit += create_unittest_button(tc, nom_script, path_file, mode, MAX) + blank_space(1)
        div_edit += tooltip_button(f"""\'downloadFile("editor_{tc}","{nom_script}")\'""", f"""<img src="{path_img}images/buttons/icons8-download-64.png"><span class="tooltiptext">Télécharger</span>""")+ blank_space()
        div_edit += create_upload_button(tc) + blank_space(1)
        div_edit += tooltip_button(f"""\'reload("{tc}")\'""", f"""<img src="{path_img}images/buttons/icons8-restart-64.png"><span class="tooltiptext">Recharger</span>""") + blank_space()
        div_edit += tooltip_button(f"""\'saveEditor("{tc}")\'""", f"""<img src="{path_img}images/buttons/icons8-save-64.png"><span class="tooltiptext">Sauvegarder</span>""")
        div_edit += '</div>'

        div_edit += f"""<span id="content_editor_{tc}" class="hide">{content}</span>"""
        div_edit += f"""<span id="corr_content_editor_{tc}" class="hide" data-strudel="{str(clef)}">{corr_content}</span>"""
        
        elt_insertion = [elt for elt in env.page.markdown.split("\n") if test_style(nom_script, elt)]
        elt_insertion = elt_insertion[0] if len(elt_insertion) >=1 else ""
        indent = " "*(len(elt_insertion) - len(elt_insertion.lstrip()))
        if nom_script == '' : indent = " "  # to avoid conflict with empty IDEs
        if indent == "":
            div_edit += f'''
{indent}--8<--- "docs/xtra/start_REM.md"
'''
        div_edit += f'''
{indent}--8<--- "docs/{path_file if path_file != "" else 'scripts'}/{nom_script}_REM.md"''' if clef == "" else f""
        if indent == "":
            div_edit += f'''
{indent}--8<--- "docs/xtra/end_REM.md"
'''
        return div_edit
        
    @env.macro
    def mult_col(*text):
        cmd = """<table style="border-color:transparent;background-color:transparent"><tr>"""
        for column in text:
            cmd += f"""<td><b style="font-size:1.2em">{column}</td>"""
        cmd += f"""</tr></table>"""
        return cmd

    def generate_id():
        alphabet = [chr(ord('a') + i) for i in range(26)]
        return "".join(random.choices(alphabet, k = 6))

    @env.macro
    def qcm(list_answers, list_correct, opts = None, shuffle = True, single = True):
        # single -> une seule question de QCM
        print('opts', opts)
        if type(list_correct) == int : list_correct = [list_correct]
        list_correct = list(map(lambda x : x - 1, list_correct))  # back to 0 to n-1 indexing
        def spanify(html_tag):
            return f"""<span>{html_tag}</span>"""
        
        def buttonify(answer, id, correct):
            reveal = "reveal" if single else ""
            return f"""<input type="checkbox" id="{id}" class="qcm-checkbox {correct} {reveal}"><span class="check-toggle"></span><label for="{id}" class="qcm-item arithmatex">{answer}</label>"""

        def latexify(answer):
            """$ might not be the first character :
            blabla $1+1$
            """

            if answer.count('$') - answer.count('\$') >= 2: #regex begin ___$ and end $____ and $ not preceded by \
                string = ''
                start_dollar = True
                for i in range(len(answer)):
                    lettre = answer[i]
                    if lettre == '$':
                        if i == 0 or (i >= 1 and answer[i-1] != '\\'): # case escaping dollar \$ 
                            string += '\(' if start_dollar else '\)'
                            start_dollar = not start_dollar
                        else:
                            string += '$'
                    else :
                        string += lettre
                return string
            return answer
        
        def codeblockify(answer):
            if answer[0:3] == "`#!":
                sep = answer.index(" ")
                language = answer[3:sep]
                return f"""<pre style="display: inline;"><code style="display: inline;" class="language-{language} qcm">{answer[sep:-1]}</code></pre>"""
            return answer

        indices = [i for i in range(len(list_answers))]
        # if shuffle: random.shuffle(indices)

        dict_correspondance = {indices[i] : i for i in range(len(list_answers))}
        inv_dict_correspondance = {i : indices[i] for i in range(len(list_answers))}
        
        id = generate_id()

        prefix = "data-var-"
        variable_part = ""
        if opts != None:
            for clé in opts : 
                variable_part += f"{prefix}{clé} = '{opts[clé]}' "
        html_element = f"""<div class="wrapper_qcm" id = "qcm_{id}" data-n-correct = {len(list_correct)} data-shuffle = {1 if shuffle else 0} {variable_part}>"""

        for i in range(len(list_answers)):
            answer = list_answers[inv_dict_correspondance[i]]
            if type(answer) != str : 
                try: 
                    answer = str(answer)
                except:
                    answer = "Erreur de format"
            answer = codeblockify(latexify(answer))
            id_answer = f"""{id}-{i}""" 
            correct_answer = "correct" if inv_dict_correspondance[i] in list_correct else "incorrect"
            html_element += f"""{spanify(buttonify(answer, id_answer, correct_answer))}"""
        html_element += "</div>"

        return html_element

    def extract_csv_file(input_file):
        # extract info from external file
        docs_path = f"""docs/"""
        path = '/'.join(filter(lambda folder: folder != "", convert_url_to_utf8(env.variables.page.abs_url).split('/')[2:-2]))

        try: 
            if path == "":
                f = open(f"""{docs_path}/scripts/{input_file}""", encoding="utf8")
            else:
                f = open(f"""{docs_path}/{path}/{input_file}""", encoding="utf8")
            content = ''.join(f.readlines())
            f.close()
            content = content + "\n"
            # Hack to integrate code lines in admonitions in mkdocs
            # change backslash_newline by backslash-newline
        except :
            return ""        

    def get_variables_state(string, sep = '{}'):
        var_pos = {}
        for inter in re.finditer(fr"{sep[0]}\w+{sep[1]}", string):
            # print(inter.start(), inter.end(), inter.group(0)[1:-1])
            var_name = inter.group(0)[1:-1]
            if var_name not in var_pos:
                var_pos[var_name] = [inter.span()]
            else:
                var_pos[var_name].append(inter.span())
        return var_pos


    @env.macro
    def multi_qcm(*input, shuffle = True):
        liste_QCM = []
        if type(input) == str: 
            question, liste_bonne_reponse, liste_reponse = extract_csv_file(input)
            liste_QCM.append({"question" : question, "reponse": [rep for rep in liste_reponse], "bonne_reponse": [bonne_rep for bonne_rep in liste_bonne_reponse]})
        else:
            for i in range(len(input)):
                question = input[i][0]
                list_answers = input[i][1]
                list_correct = input[i][2]
                dictionnaire_var = input[i][3] if len(input[i]) == 4 else None
                    # dictionnaire_var = get_variables_state(input[i][4])
                liste_QCM.append({"question" : question, "reponse": list_answers, "bonne_reponse": list_correct})

        id_qcm = generate_id()
        html_element = "<div></div>"#f"""<span id = "setQCM_{id_qcm}">"""
        # print(html_element)
        for i in range(len(input)):
            question = input[i][0]
            list_answers = input[i][1]
            list_correct = input[i][2]
            dictionnaire_var = input[i][3] if len(input[i]) == 4 else None
                  # {'x' : [2,3,4], 'n' : [3,1,2]}
                # dictionnaire_var = {'x' : [2,3,4], 'n' : [3,1,2]}
            html_element += f"<span class = 'questionQCM arithmatex'>Question {i+1} : {question}</span>"
            print('dic', dictionnaire_var)
            html_element += qcm(list_answers, list_correct, opts = dictionnaire_var, shuffle = shuffle, single = False)
        html_element += f"""<div class="buttonWrapper"><span class = "validationButton" id = "valider_{id_qcm}">Valider</span><span class = "validationButton" id = "recharger_{id_qcm}">Recharger</span></div><div class = "showScore" id="score_{id_qcm}"></div>"""
        print(html_element)
        return html_element



