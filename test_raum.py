import encoder
import cla

region_groesse = 20
datei_pfad = "/home/martin/Dokumente/htm/daten/test.csv"

if __name__ == "__main__":
    region = cla.region(region_groesse, 258)
    opened_file = encoder.open_file(datei_pfad)
    row = encoder.convert_row(opened_file[0])
    ls = encoder.show_only_actives(encoder.name_to_list(",")[0])

    for name in row:
        for wert in name:
            b = encoder.show_only_actives(wert)
            region.raeumliche_wahrnehmung(b)