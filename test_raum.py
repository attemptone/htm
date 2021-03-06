import encoder
import cla

region_groesse = 20
datei_pfad = "/home/martin/Dokumente/htm/daten/test.csv"

if __name__ == "__main__":
    input_region = encoder.InputRegion(258)
    region = cla.Region(region_groesse)
    region.initialize_dendrites(input_region)

    opened_file = encoder.open_file(datei_pfad)
    row = encoder.convert_row(opened_file[0])

    for name in row:
        for wert in name:
            b = encoder.show_only_actives(wert)
            input_region.new_input(b)
            region.raeumliche_wahrnehmung()