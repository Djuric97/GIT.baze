import sqlite3
from sqlite3 import Error
from tkinter import *



#KLASE
class Radnik:
    def __init__(self, id, ime, prezime, plata):
        self.id = id
        self.ime = ime
        self.prezime = prezime
        self.plata = plata

    def __str__(self):
        return f'{self.ime} {self.prezime} ima platu od {self.plata} maraka.'

class Posjetilac:
    def __init__(self, id, ime, prezime, br_posjeta):
        self.id = id
        self.ime = ime
        self.prezime = prezime
        self.br_posjeta = br_posjeta

    def __str__(self):
        return f'{self.ime} {self.prezime} je posjetio ZOO {self.br_posjeta} puta.'

class Zivotinja:
    def __init__(self,id, vrsta, starost, krilo):
        self.id = id
        self.vrsta = vrsta
        self.starost = starost
        self.krilo = krilo

    def __str__(self):
        return f'{self.vrsta} je star {self.starost} godina i nalazi se u krilu {self.krilo}'

class Vozilo:
    def __init__(self, br_sasije, vrsta, godiste, boja):
        self.br_sasije = br_sasije
        self.vrsta = vrsta
        self.godiste = godiste
        self.boja = boja

    def __str__(self):
        return f'{self.br_sasije} je {self.vrsta} i {self.godiste}. je godiste.'


#############################################################################################
#############################################################################################
#TABELE
kon = sqlite3.connect('BazaGUI.db')
tabela_radnici = '''CREATE TABLE IF NOT EXISTS radnici (id_radnika INTEGER PRIMARY KEY, ime VARCHAR(20), prezime VARCHAR(20), plata INTEGER);'''
tabela_posjetioci = '''CREATE TABLE IF NOT EXISTS posjetioci (id_posjetioca INTEGER PRIMARY KEY, ime_posjetioca VARCHAR (20), prezime_posjetioca VARCHAR(20), broj_posjeta INTEGER);'''
tabela_zivotinje = '''CREATE TABLE IF NOT EXISTS zivotinje (id_zivotinje INTEGER PRIMARY KEY, vrsta_zivotinje VARCHAR (20), starost_zivotinje INTEGER, krilo VARCHAR(10));'''
tabela_vozila = '''CREATE TABLE IF NOT EXISTS vozila (broj_sasije INTEGER PRIMARY KEY, vrsta VARCHAR(20), godiste INTEGER, boja VARCHAR(20));'''

kurzor = kon.cursor()
kurzor.execute(tabela_radnici)
kurzor.execute(tabela_posjetioci)
kurzor.execute(tabela_zivotinje)
kurzor.execute(tabela_vozila)
#############################################################################################
#############################################################################################




#FUNKCIJA ZA UNOS U BAZU
def prozor_unosa_klasa():
    gl_prozor.destroy()
    kon = sqlite3.connect('BazaGUI.db')
    kla_prozor = Tk()

    center(kla_prozor, 300, 200)

    kla_naslov = Label(kla_prozor, text='ODABERI KLASU').pack()
    kla_prozor.title('GUI APLIKACIJA')

    def submit_radnik():
        kla_prozor.destroy()
        un_rad = Tk()

        center(un_rad, 350, 200)

        un_rad.title('UNOS RADNIKA')
        un_rad.title('GUI APLIKACIJA')

        #LABEL
        oz1 = Label(un_rad, text='ID RADNIKA')
        oz1.grid(row=1, column=0)
        oz2 = Label(un_rad, text='IME RADNIKA')
        oz2.grid(row=2, column=0)
        oz3 = Label(un_rad, text='PREZIME RADNIKA')
        oz3.grid(row=3, column=0)
        oz4 = Label(un_rad, text='PLATA RADNIKA')
        oz4.grid(row=4, column=0)

        #UNOSI/ENTRY
        unos_id = Entry(un_rad)
        unos_id.grid(row=1, column=1)
        unos_ime = Entry(un_rad)
        unos_ime.grid(row=2, column=1)
        unos_prezime = Entry(un_rad)
        unos_prezime.grid(row=3, column=1)
        unos_plata = Entry(un_rad)
        unos_plata.grid(row=4, column=1)


        def get_radnik():
            try:
                global id_radnika, plata
                if unos_id.get().isdigit() != True:
                    print('Unesite broj za ID!')
                else:
                    id_radnika = int(unos_id.get())
                ime = unos_ime.get()
                prezime = unos_prezime.get()
                if unos_plata.get().isdigit() != True:
                    print('Unesite broj za platu!!')
                else:
                    plata = int(unos_plata.get())
                radnik = Radnik(id_radnika, ime, prezime, plata)
                return (radnik.id, radnik.ime, radnik.prezime, radnik.plata)
            except NameError as ne:
                print(ne)

        def insert():
            try:
                komanda = '''INSERT INTO radnici VALUES (?,?,?,?);'''
                kurzor = kon.cursor()
                kurzor.execute(komanda, get_radnik())
                kon.commit()
                print('Uspjesno ste dodali objekat.')
            except Error as e:
                print(e)

        def back():
            un_rad.destroy()
            pocetak()

        dugme7 = Button(un_rad, text='MENI', width=8, fg='red', command=back)
        dugme7.grid(row=6, column=1)

        podnesi = Button(un_rad, text='PODNESI', width=8, command=insert)
        podnesi.grid(row=5, column=1)
        un_rad.mainloop()

    def submit_posjetilac():
        kla_prozor.destroy()
        un_pos = Tk()

        center(un_pos, 350, 200)

        un_pos.title('UNOS POSJETIOCA')
        un_pos.title('GUI APLIKACIJA')

        oz1 = Label(un_pos, text='ID POSJETIOCA')
        oz1.grid(row=1, column=0)
        oz2 = Label(un_pos, text='IME POSJETIOCA')
        oz2.grid(row=2, column=0)
        oz3 = Label(un_pos, text='PREZIME POSJETIOCA')
        oz3.grid(row=3, column=0)
        oz4 = Label(un_pos, text='BROJ POSJETA')
        oz4.grid(row=4, column=0)


        #UNOSI/ENTRY
        unos_id = Entry(un_pos)
        unos_id.grid(row=1, column=1)
        unos_ime = Entry(un_pos)
        unos_ime.grid(row=2, column=1)
        unos_prezime = Entry(un_pos)
        unos_prezime.grid(row=3, column=1)
        unos_br_pos = Entry(un_pos)
        unos_br_pos.grid(row=4, column=1)

        def get_posjetilac():
            try:
                global id_posj, br_pos
                if unos_id.get().isdigit() != True:
                    print('Unesite broj za ID')
                else:
                    id_posj = int(unos_id.get())
                ime = unos_ime.get()
                prezime = unos_prezime.get()
                if unos_br_pos.get().isdigit() != True:
                    print('Unesi broj za broj posjeta!')
                else:
                    br_pos = int(unos_br_pos.get())
                p = Posjetilac(id_posj, ime, prezime, br_pos)
                return (p.id, p.ime, p.prezime, p.br_posjeta)
            except NameError as ne:
                print(ne)

        def insert():
            try:
                komanda = '''INSERT INTO posjetioci VALUES (?,?,?,?);'''
                kurzor = kon.cursor()
                kurzor.execute(komanda, get_posjetilac())
                kon.commit()
                print('Uspjesno ste dodali objekat.')
            except Error as e:
                print(e)

        def back():
            un_pos.destroy()
            pocetak()

        dugme7 = Button(un_pos, text='MENI', width=8, fg='red', command=back)
        dugme7.grid(row=6, column=1)

        podnesi = Button(un_pos, text='PODNESI', width=8, command=insert)
        podnesi.grid(row=5, column=1)
        un_pos.mainloop()

    def submit_zivotinju():
        kla_prozor.destroy()
        un_ziv = Tk()

        center(un_ziv, 350, 200)

        un_ziv.title('UNOS ZIVOTINJE')
        un_ziv.title('GUI APLIKACIJA')

        #LABEL
        oz1 = Label(un_ziv, text='ID ZIVOTINJE')
        oz1.grid(row=1, column=0)
        oz2 = Label(un_ziv, text='VRSTA ZIVOTINJE')
        oz2.grid(row=2, column=0)
        oz3 = Label(un_ziv, text='STAROST ZIVOTINJE')
        oz3.grid(row=3, column=0)
        oz4 = Label(un_ziv, text='U KOM SE KRILU NALAZI')
        oz4.grid(row=4, column=0)


        #UNOSI/ENTRY
        unos_id = Entry(un_ziv)
        unos_id.grid(row=1, column=1)
        unos_vrsta = Entry(un_ziv)
        unos_vrsta.grid(row=2, column=1)
        unos_starost = Entry(un_ziv)
        unos_starost.grid(row=3, column=1)
        unos_krilo = Entry(un_ziv)
        unos_krilo.grid(row=4, column=1)

        def get_zivotinja():
            try:
                global id_ziv, starost
                if unos_id.get().isdigit() != True:
                    print('Unesi broj za ID!')
                else:
                    id_ziv = int(unos_id.get())
                vrsta = unos_vrsta.get()
                if unos_starost.get().isdigit() != True:
                    print('Unesi broj za starost!')
                else:
                    starost = int(unos_starost.get())
                krilo = unos_krilo.get()
                z = Zivotinja(id_ziv, vrsta, starost, krilo)
                return (z.id, z.vrsta, z.starost, z.krilo)
            except NameError as ne:
                print(ne)

        def insert():
            try:
                komanda = '''INSERT INTO zivotinje VALUES (?,?,?,?);'''
                kurzor = kon.cursor()
                kurzor.execute(komanda, get_zivotinja())
                kon.commit()
                print('Uspjesno ste dodali objekat.')
            except Error as e:
                print(e)


        def back():
            un_ziv.destroy()
            pocetak()

        dugme7 = Button(un_ziv, text='MENI', width=8, fg='red', command=back)
        dugme7.grid(row=6, column=1)

        podnesi = Button(un_ziv, text='PODNESI', width=8, command=insert)
        podnesi.grid(row=5, column=1)
        un_ziv.mainloop()

    def submit_vozilo():
        kla_prozor.destroy()
        un_voz = Tk()

        center(un_voz, 350, 200)

        un_voz.title('UNOS VOZILA')
        un_voz.title('GUI APLIKACIJA')

        #LABEL
        oz1 = Label(un_voz, text='BROJ SASIJE')
        oz1.grid(row=5, column=0)
        oz2 = Label(un_voz, text='VRSTA VOZILA')
        oz2.grid(row=6, column=0)
        oz3 = Label(un_voz, text='GODISTE VOZILA')
        oz3.grid(row=7, column=0)
        oz4 = Label(un_voz, text='BOJA VOZILA')
        oz4.grid(row=8, column=0)

        #UNOSI/ENTRY
        unos_br_sas = Entry(un_voz)
        unos_br_sas.grid(row=5, column=1)
        unos_vrsta = Entry(un_voz)
        unos_vrsta.grid(row=6, column=1)
        unos_god = Entry(un_voz)
        unos_god.grid(row=7, column=1)
        unos_boja = Entry(un_voz)
        unos_boja.grid(row=8, column=1)

        def get_vozilo():
            try:
                global br_sas, god
                if unos_br_sas.get().isdigit() != True:
                    print('Unesi broj za broj sasije!')
                else:
                    br_sas = int(unos_br_sas.get())
                vrsta = unos_vrsta.get()
                if unos_god.get().isdigit() != True:
                    print('Unesi broj za godiste vozila!')
                else:
                    god = int(unos_god.get())
                boja = unos_boja.get()
                v = Vozilo(br_sas, vrsta, god, boja)
                return (v.br_sasije, v.vrsta, v.godiste, v.boja)
            except NameError as ne:
                print(ne)

        def insert():
            try:
                komanda = '''INSERT INTO vozila VALUES (?,?,?,?);'''
                kurzor = kon.cursor()
                kurzor.execute(komanda, get_vozilo())
                kon.commit()
                print('Uspjesno ste dodali objekat.')
            except Error as e:
                print(e)

        def back():
            un_voz.destroy()
            pocetak()

        dugme7 = Button(un_voz, text='MENI', width=8, fg='red', command=back)
        dugme7.grid(row=10, column=1)


        podnesi = Button(un_voz, text='PODNESI',width=8, command=insert)
        podnesi.grid(row=9, column=1)
        un_voz.mainloop()

    def back():
        kla_prozor.destroy()
        pocetak()


    bt1 = Button(kla_prozor, text='RADNIK', width=20, command=submit_radnik).pack()
    bt2 = Button(kla_prozor, text='POSJETILAC', width=20, command=submit_posjetilac).pack()
    bt3 = Button(kla_prozor, text='ZIVOTINJA', width=20, command=submit_zivotinju).pack()
    bt4 = Button(kla_prozor, text='VOZILO', width=20, command=submit_vozilo).pack()

    dugme7 = Button(kla_prozor, text='MENI', width=20, fg='red', command=back)
    dugme7.pack()
    kla_prozor.mainloop()


#FUNKCIJA ZA BRISANJE IZ BAZE
def prozor_brisanja_klasa():
    gl_prozor.destroy()
    kon = sqlite3.connect('BazaGUI.db')
    prozor_brisanja = Tk()

    center(prozor_brisanja, 400, 250)

    naslov = Label(prozor_brisanja, text='OBRISI KLASU')
    naslov.grid(row=0, column=1)
    prozor_brisanja.title('GUI APLIKACIJA')

    oznaka1 = Label(prozor_brisanja, text='UPISI TABELU',)
    oznaka1.grid(row=1, column=0)
    oznaka2 = Label(prozor_brisanja, text='ATRIBUT PO KOM BRISES')
    oznaka2.grid(row=2, column=0)
    oznaka3 = Label(prozor_brisanja, text='VRIJEDNOST ATRIBUTA')
    oznaka3.grid(row=3, column=0)

    unos1 = Entry(prozor_brisanja)
    unos1.grid(row=1, column=1)
    unos2 = Entry(prozor_brisanja)
    unos2.grid(row=2, column=1)
    unos3 = Entry(prozor_brisanja)
    unos3.grid(row=3, column=1)

    def brisanje():
        try:
            crsr = kon.cursor()
            komanda = f'''DELETE FROM {unos1.get().strip()} WHERE {unos2.get().replace(' ', '_')} = '{unos3.get()}' '''
            crsr.execute(komanda)
            kon.commit()
            print('Objekat je obrisan!')
        except Error as e:
            print(e)

    dgme = Button(prozor_brisanja, text='OBRISI', width=10, command=brisanje)
    dgme.grid(row=5, column=1)

    def back():
        prozor_brisanja.destroy()
        pocetak()

    dugme7 = Button(prozor_brisanja, text='MENI', width=10, fg='red', command=back)
    dugme7.grid(row=6, column=1)

    prozor_brisanja.mainloop()


# FUNKCIJA ZA AZURIRANJE
def prozor_azuriranja():
    gl_prozor.destroy()
    kon = sqlite3.connect('BazaGUI.db')
    prozor_azuriranje = Tk()

    center(prozor_azuriranje, 400, 250)

    naslov = Label(prozor_azuriranje, text='AZURIRAJ KLASU')
    naslov.grid(row=0, column=1)
    prozor_azuriranje.title('GUI APLIKACIJA')

    oznaka1 = Label(prozor_azuriranje, text='UPISI TABELU')
    oznaka1.grid(row=1, column=0)
    oznaka2 = Label(prozor_azuriranje, text='KOJI ATRIBUT BISTE AZURIRALI')
    oznaka2.grid(row=2, column=0)
    oznaka3 = Label(prozor_azuriranje, text='NOVA VERZIJA TOG ATRIBUTA')
    oznaka3.grid(row=3, column=0)
    oznaka4 = Label(prozor_azuriranje, text='ATRIBUT ZA PRETRAGU')
    oznaka4.grid(row=4, column=0)
    oznaka5 = Label(prozor_azuriranje, text='VRIJEDNOST ODABRANOG ATRIBUTA')
    oznaka5.grid(row=5, column=0)

    unos1 = Entry(prozor_azuriranje)
    unos1.grid(row=1, column=1)
    unos2 = Entry(prozor_azuriranje)
    unos2.grid(row=2, column=1)
    unos3 = Entry(prozor_azuriranje)
    unos3.grid(row=3, column=1)
    unos4 = Entry(prozor_azuriranje)
    unos4.grid(row=4, column=1)
    unos5 = Entry(prozor_azuriranje)
    unos5.grid(row=5, column=1)

    def azuriranje():
        try:
            crsr = kon.cursor()
            komanda = f'''UPDATE {unos1.get()} SET {unos2.get().replace(' ', '_')} = "{unos3.get()}" WHERE {unos4.get().replace(' ', '_')} = "{unos5.get()}"'''
            crsr.execute(komanda)
            kon.commit()
            print('Azuriranje uspjesno!')
        except Error as e:
            print(e)

    dugme = Button(prozor_azuriranje, text='AZURIRAJ', width=10, command=azuriranje)
    dugme.grid(row=7, column=1)

    def back():
        prozor_azuriranje.destroy()
        pocetak()

    dugme7 = Button(prozor_azuriranje, text='MENI', width=10, fg='red', command=back)
    dugme7.grid(row=8, column=1)


    prozor_azuriranje.mainloop()


#FUNKCIJA ZA SELECT
def prozor_prikaza():
    gl_prozor.destroy()
    kon = sqlite3.connect('BazaGUI.db')
    prozor_selekt = Tk()

    center(prozor_selekt, 350, 200)

    naslov = Label(prozor_selekt, text='PRIKAZ ODABRANE TABELE')
    naslov.grid(row=0, column=1)
    prozor_selekt.title('GUI APLIKACIJA')

    oznaka1 = Label(prozor_selekt, text='UPISITE TABELU ZA PRIKAZ')
    oznaka1.grid(row=1, column=0)

    unos_tab = Entry(prozor_selekt)
    unos_tab.grid(row=1, column=1)

    def prikaz():
        try:
            komanda = f'''SELECT * FROM {unos_tab.get()}'''
            crsr = kon.cursor()
            crsr.execute(komanda)
            rez = crsr.fetchall()
            for i in rez:
                print(i)
        except Error as e:
            print(e)
    dugme = Button(prozor_selekt, text='PRIKAZI', width=10, command=prikaz)
    dugme.grid(row=3, column=1)

    def back():
        prozor_selekt.destroy()
        pocetak()


    dugme7 = Button(prozor_selekt, text='MENI', width=10, fg='red', command=back)
    dugme7.grid(row=4, column=1)

    prozor_selekt.mainloop()



# GLAVNI PROZOR KOMANDI
def pocetak():
    global gl_prozor
    gl_prozor = Tk()

    #Centriranje prozora
    center(gl_prozor, 350, 200)

    naslov = Label(gl_prozor, text='ODABERI KOMANDU')
    naslov.pack()
    gl_prozor.title('GUI APLIKACIJA')

    # IZBORNI MENI
    but_unos = Button(gl_prozor, text='UNOS', width=20, command=prozor_unosa_klasa).pack()
    but_brisanje = Button(gl_prozor, text='BRISANJE',width=20, command=prozor_brisanja_klasa).pack()
    but_update = Button(gl_prozor, text='AZURIRAJ',width=20, command=prozor_azuriranja).pack()
    but_prikaz = Button(gl_prozor, text='PRIKAZ',width=20, command=prozor_prikaza).pack()

    gl_prozor.mainloop()


#FUNKCIJA ZA CENTRIRANJE PROZORA NA EKRANU
def center(prozor, sirina, visina):
    sirina_prozora = sirina
    visina_prozora = visina

    sirina_ekrana = prozor.winfo_screenwidth()
    visina_ekrana = prozor.winfo_screenheight()

    poz_top = int(visina_ekrana/2 - visina_prozora/2)
    poz_str = int(sirina_ekrana/2 - sirina_prozora/2)
    prozor.geometry(f'{sirina_prozora}x{visina_prozora}+{poz_str}+{poz_top}')



