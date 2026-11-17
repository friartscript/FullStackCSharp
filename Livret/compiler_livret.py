import os
import glob
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ETAPES_DIR = os.path.join(SCRIPT_DIR, "etapes")
OUTPUT_TEX = os.path.join(SCRIPT_DIR, "LIVRET.tex")

PREAMBLE = r"""\documentclass[a4paper,11pt]{report}

\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[french]{babel}
\usepackage{lmodern}
\usepackage{amssymb}
\usepackage{geometry}
\geometry{a4paper, margin=1.8cm, top=2.2cm, bottom=2.2cm}
\usepackage{parskip}
\raggedbottom

\usepackage{xcolor}
\usepackage{colortbl}
\usepackage{tcolorbox}
\tcbuselibrary{skins,breakable}
\usepackage{hyperref}
\usepackage{microtype}
\usepackage{fancyhdr}
\usepackage{tabularx}
\usepackage{booktabs}
\usepackage{array}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,positioning,shapes.geometric,fit,backgrounds,calc}

% Palette Professionnelle Moderne
\definecolor{primary}{RGB}{15, 23, 42}         % Slate 900 (Titres majeurs, élégance)
\definecolor{secondary}{RGB}{37, 99, 235}      % Royal Blue (Architecture, liens)
\definecolor{accent}{RGB}{217, 119, 6}         % Amber 600 (Points d'attention)
\definecolor{emerald}{RGB}{16, 185, 129}       % Emerald 500 (Bonnes pratiques)
\definecolor{indigo}{RGB}{99, 102, 241}        % Indigo 500 (Composants UI / Front)
\definecolor{cyanproj}{RGB}{14, 165, 233}      % Sky 500 (Contrats & DTOs)
\definecolor{schemaframe}{RGB}{79, 70, 229}    % Violet/Indigo pour cadres schémas
\definecolor{tableheader}{RGB}{30, 41, 59}     % Slate 800 (Entêtes de tableaux)
\definecolor{cardbg}{RGB}{248, 250, 252}       % Slate 50 (Fonds alternés)
\definecolor{borderlight}{RGB}{226, 232, 240}  % Slate 200 (Bordures douces)

% Boîtes d'Enseignement Didactiques Sécables (Breakable)
\newtcolorbox{conceptbox}[1]{
    enhanced,
    breakable,
    colback=blue!3!white,
    colframe=secondary,
    fonttitle=\bfseries\color{white},
    title=$\blacktriangleright$~Concept Clé d'Architecture : #1,
    arc=2mm,
    boxrule=0.9pt,
    left=3.5mm,right=3.5mm,top=2.5mm,bottom=2.5mm
}

\newtcolorbox{schemabox}[1]{
    enhanced,
    colback=purple!2!white,
    colframe=schemaframe,
    fonttitle=\bfseries\color{white},
    title=$\blacktriangleright$~Schéma Conceptuel \& Flux : #1,
    arc=2mm,
    boxrule=0.9pt,
    left=3.5mm,right=3.5mm,top=2.5mm,bottom=2.5mm
}

\newtcolorbox{bestpracticebox}[1]{
    enhanced,
    breakable,
    colback=green!3!white,
    colframe=emerald!80!black,
    fonttitle=\bfseries\color{white},
    title=$\blacktriangleright$~Règle d'Ingénierie \& Bonne Pratique : #1,
    arc=2mm,
    boxrule=0.9pt,
    left=3.5mm,right=3.5mm,top=2.5mm,bottom=2.5mm
}

\newtcolorbox{faqbox}[1]{
    enhanced,
    breakable,
    colback=teal!3!white,
    colframe=teal!80!black,
    fonttitle=\bfseries\color{white},
    title=$\blacktriangleright$~Questions Fréquentes du Débutant : #1,
    arc=2mm,
    boxrule=0.9pt,
    left=3.5mm,right=3.5mm,top=2.5mm,bottom=2.5mm
}

\newtcolorbox{notebox}{
    enhanced,
    breakable,
    colback=accent!4!white,
    colframe=accent,
    fonttitle=\bfseries\color{white},
    title=$\blacktriangleright$~Directive Didactique du Livret,
    arc=2mm,
    boxrule=0.9pt,
    left=3.5mm,right=3.5mm,top=2.5mm,bottom=2.5mm
}

% Commandes d'Agencement Pédagogique Fluide (Sans Blocs Monolithiques)
\newcommand{\faqitem}[2]{%
    \par\vspace{0.25cm}%
    \noindent{\bfseries\color{secondary!90!black}\large $\blacktriangleright$~Q : #1}\par\nopagebreak[4]%
    \vspace{0.1cm}%
    \noindent\textbf{Réponse :} #2\par%
}

% En-têtes et Absence de Pied de Page (Marge de sécurité propre)
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\textbf{\color{secondary}FullStackCSharp} \textit{— Guide d'Architecture}}
\fancyhead[R]{\small\color{gray}\thepage}
\fancyfoot{}
\renewcommand{\headrulewidth}{0.6pt}
\renewcommand{\footrulewidth}{0pt}
\setlength{\headheight}{15pt}

\hypersetup{
    colorlinks=true,
    linkcolor=secondary,
    filecolor=secondary,
    urlcolor=accent,
    pdftitle={FullStackCSharp — Guide Conceptuel d'Architecture Fullstack - Kevin Friart},
    pdfauthor={Kevin Friart},
    pdfpagemode=FullScreen,
}

\begin{document}

% Page de Titre Haute Qualité Professionnelle & Équilibrée
\begin{titlepage}
\begin{center}
    \vspace*{1.2cm}
    
    {\scshape\large\bfseries\color{secondary} Guide de Référence \& Architecture Systèmes}\\[0.3cm]
    {\footnotesize\color{gray!80!black} Conception d'Applications d'Entreprise C\# Modernes}
    
    \vfill
    
    {\fontsize{40}{48}\selectfont\bfseries\color{primary} FullStackCSharp}\\[0.4cm]
    {\color{secondary}\rule{9cm}{1.5pt}}\\[0.6cm]
    {\LARGE\bfseries\color{secondary} Guide de Conception \& d'Ingénierie Fullstack}\\[0.3cm]
    {\large\color{gray!85!black} C\# 12 $\bullet$ .NET MAUI $\bullet$ ASP.NET Core Minimal APIs (.NET 8 LTS)}
    
    \vfill
    
    \begin{tcolorbox}[enhanced,colback=secondary!4!white,colframe=secondary!35!white,arc=3mm,boxrule=0.9pt,width=0.88\textwidth,top=5mm,bottom=5mm,left=6mm,right=6mm]
        \centering\normalsize\itshape\color{primary}
        Comprendre, concevoir et bâtir un écosystème logiciel d'entreprise complet :\\
        de l'autorité centrale des contrats jusqu'au client multiplateforme natif,\\
        à travers des diagrammes de flux et des micro-fiches ultra-granulaires.
    \end{tcolorbox}
    
    \vfill
    
    \begin{tcolorbox}[enhanced,colback=white,colframe=borderlight,arc=3.5mm,boxrule=1.1pt,width=0.75\textwidth,drop fuzzy shadow=black!10,top=6mm,bottom=6mm]
        \centering
        {\footnotesize\scshape\bfseries\color{secondary} Auteur \& Concepteur du Projet}\\[0.3cm]
        {\huge\bfseries\color{primary} Kevin Friart}\\[0.25cm]
        {\normalsize\color{gray!85!black} Ingénierie Logicielle \& Architecture Systèmes .NET}
    \end{tcolorbox}
    
    \vfill
    
    {\small\color{gray} .NET 8 LTS $\bullet$ Architecture 3 Tiers $\bullet$ \today}
    
    \vspace*{0.8cm}
\end{center}
\end{titlepage}

\tableofcontents
\newpage
"""

POSTAMBLE = r"""
\end{document}
"""

def assemble_livret():
    etape_files = sorted(glob.glob(os.path.join(ETAPES_DIR, "*.tex")))
    
    if not etape_files:
        print("[INFO] Aucun fichier d'étape trouvé dans Livret/etapes/.")
        return False
        
    print(f"[INFO] Assemblage de {len(etape_files)} livrets d'étape(s) :")
    content_parts = [PREAMBLE]
    
    for f in etape_files:
        basename = os.path.basename(f)
        print(f"  -> {basename}")
        with open(f, "r", encoding="utf-8") as fp:
            content_parts.append(fp.read())
        content_parts.append("\n\\newpage\n")
        
    content_parts.append(POSTAMBLE)
    
    with open(OUTPUT_TEX, "w", encoding="utf-8") as out:
        out.write("\n".join(content_parts))
        
    print(f"[OK] Fichier consolidé généré : {OUTPUT_TEX}")
    return True

def compile_pdf():
    if not assemble_livret():
        return
    print("[INFO] Compilation avec pdflatex...")
    try:
        subprocess.run(["pdflatex", "-interaction=nonstopmode", "LIVRET.tex"], cwd=SCRIPT_DIR, check=True)
        subprocess.run(["pdflatex", "-interaction=nonstopmode", "LIVRET.tex"], cwd=SCRIPT_DIR, check=True)
        print("[OK] Compilation réussie : Livret/LIVRET.pdf")
    except Exception as e:
        print(f"[ERREUR] Échec de la compilation : {e}")

if __name__ == "__main__":
    compile_pdf()

