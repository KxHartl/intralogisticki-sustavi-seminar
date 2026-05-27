import os
import re

tex_file = "d:/truenas_kresimir_share_cp/FSB/semestar_10/ais_v2/docs/seminar.tex"
out_dir = "d:/truenas_kresimir_share_cp/FSB/semestar_10/ais_v2/docs"

with open(tex_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix biblatex preamble
preamble_match = re.search(r'(.*?\\begin\{document\})', content, re.DOTALL)
preamble = preamble_match.group(1)
preamble = preamble.replace(r'\usepackage{mathptmx}', r'\usepackage{mathptmx}' + '\n' + r'\usepackage[style=ieee,backend=biber]{biblatex}' + '\n' + r'\addbibresource{../sources.bib}')

# Title page and TOC
title_page_match = re.search(r'(\\begin\{titlepage\}.*?\\end\{titlepage\})', content, re.DOTALL)
title_page = title_page_match.group(1)

toc_part_match = re.search(r'(\\pagenumbering\{Roman\}.*?\\pagenumbering\{arabic\})', content, re.DOTALL)
toc_part = toc_part_match.group(1)

# Sections
sections = re.findall(r'(\\section\{.*?\}.*?)(?=\\section|\\begin\{thebibliography\})', content, re.DOTALL)

file_names = [
    "01_uvod.tex",
    "02_klasicni_vs_autonomni.tex",
    "03_sigurnosni_sustavi.tex",
    "04_navigacijske_tehnologije.tex",
    "05_primjeri.tex",
    "06_prednosti.tex",
    "07_zakljucak.tex"
]

main_tex = preamble + "\n\n" + title_page + "\n\n" + toc_part + "\n\n"

for i, sec_content in enumerate(sections):
    if i < len(file_names):
        filename = file_names[i]
        
        # Inject some citations since they are missing
        if i == 0: # UVOD
            sec_content = sec_content.replace('Arthur Mac Barrett predstavio prvo', 'Arthur Mac Barrett predstavio prvo \\cite{barrett}')
        elif i == 2: # SIGURNOSNI
            sec_content = sec_content.replace('ISO 3691-4', 'ISO 3691-4 \\cite{iso3691}')
            sec_content = sec_content.replace('ISO 13849-1', 'ISO 13849-1 \\cite{iso13849}')
        elif i == 3: # NAVIGACIJA
            sec_content = sec_content.replace('EKF-SLAM-u', 'EKF-SLAM-u \\cite{slam}')
            sec_content = sec_content.replace('YOLO modela', 'YOLO modela \\cite{yolo}')
            sec_content = sec_content.replace('Prošireni Kalmanov filtar', 'Prošireni Kalmanov filtar \\cite{sensorfusion}')
        elif i == 5: # PREDNOSTI
            sec_content = sec_content.replace('standard DIN 18202', 'standard DIN 18202 \\cite{din18202}')
        elif i == 6: # ZAKLJUCAK
            sec_content = sec_content.replace('Industrije 4.0', 'Industrije 4.0 \\cite{kion}')
            sec_content = sec_content.replace('VDA 5050', 'VDA 5050 \\cite{vda5050}')
            
        filepath = os.path.join(out_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(sec_content.strip() + "\n")
        
        main_tex += f"\\input{{{filename}}}\n\\clearpage\n"

main_tex += "\n\\printbibliography[heading=bibintoc, title={LITERATURA}]\n"

# Prilozi
prilozi_match = re.search(r'(\\newpage\s*\\section\*\{PRILOZI\}.*?\\end\{document\})', content, re.DOTALL)
if prilozi_match:
    main_tex += "\n" + prilozi_match.group(1)

with open(os.path.join(out_dir, "main.tex"), 'w', encoding='utf-8') as f:
    f.write(main_tex)
    
print("LaTeX split successfully.")
