"""
File:    particles.py
Author:  Mohiuddin Syed
Date:    2/14/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
    Tells you what type of particle the user inputs.
"""
particle_question = input("What particle are you looking for? ").lower()

if particle_question == "lepton":
        charge = int(input("What is the charge on the lepton? (-1 or 0) "))
            if charge == -1:
                        lepton_particle_specfic = input("Are they either light, medium or heavy? ").lower()
                                if lepton_particle_specfic == "light":
                                                print("This lepton is an electron")
                                elif lepton_particle_specfic == "medium":
                                                print("This lepton is an muon")
                                elif lepton_particle_specfic == "heavy":
                                                print("This lepton is a tau")
                                else:
                                                print("cant tell what this lepton is ")
            elif charge == 0:
                        print("you are a neutrino")
            elif particle_question == "quark":
                    charge = input("What type of charge is on the quark? ").lower()
                        if charge == "positive":
                                    family = int(input("What family is the lepton in? "))
                                            if 0 > family > 4:
                                                            print("only 3 known family currently")
                                            elif family == 1:
                                                            print("its an up quark")
                                            elif family == 2:
                                                            print("its a charm quark")
                                            elif family == 3:
                                                            print("its a top quark")
                                            elif charge == "negative":
                                                        negative_family = int(input("What family is the lepton in? "))
                                                                if negative_family == 1:
                                                                                print("its a down quark")
                                                                elif negative_family == 2:
                                                                                print("its a strange quark")
                                                                elif negative_family == 3:
                                                                                print("its a bottom quark")
                                                                elif 0 > negative_family > 4:
                                                                                print("only 3 known family currently")
                                                                else:
                                                                            print("all quarks have a charge positive or negative")
                                            else:
                                                    print("you're most likely talking about a boson particle")
                                                    
