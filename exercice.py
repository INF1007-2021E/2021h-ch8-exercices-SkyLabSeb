#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici


# TODO: Définissez vos fonction ici

def exo1(file1, file2):
    est_different = True
    with open(file1, encoding="utf-8") as f1, open(file2, encoding="utf-8") as f2:
        for line1 in f1:
            line2 = f2.readline()
            if line1 != line2:
                print("Les fichiers ne sont pas identiques")
                print(line1.strip())
                print("Est différent de:")
                print(line2)
                est_different = False
                break

        if est_different:
            print("Les fichiers sont identiques")


def ajout_espace(fichier, fichiercopie):

    with open(fichier, "r", encoding="utf-8") as f, open(fichiercopie, "x") as copie:
        for ligne in f:
            ligne_copie = ligne.replace(" ", "   ")
            copie.write(ligne_copie)


def ajout_grade(fichier, fichier_grade):

    with open(fichier, "r", encoding="utf-8") as f, open(fichier_grade, "w", encoding="utf-8") as f_grade:
        for note in f:
            for grade, pourcentage in PERCENTAGE_TO_LETTER.items():
                if pourcentage[0] <= int(note) < pourcentage[1]:
                    f_grade.write(note.strip() + " " + grade + "\n")
                    break



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    # exo1("notes.txt", "notes2.txt")
    # ajout_espace("exemple.txt", "exemplecopie.txt")
    ajout_grade("./notes.txt", "./notesgrades.txt")

