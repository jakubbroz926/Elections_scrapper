import Input_gathering as Indat
import Link_request as linkr
import Main_soup as ms
import csv_creation as csvr


def main():
    link_of_main_page, name_of_file, name_of_directory = Indat.data_inputs()
    html_text = linkr.requesting(link_of_main_page)
    hrefs, codes = ms.souping(html_text, link_of_main_page)
    test = input("Pokud chcete vytvořit soubor a uložit svá data, napište ano:\n")
    if test == "ano":
        for i, (href, code) in enumerate(zip(hrefs[:], codes)):
            local_soup = ms.souping_local(href)
            local_info_soup = ms.gettting_city_name(local_soup)
            local_numbers = ms.local_numbers(local_soup)
            row = [code, local_info_soup]
            row.extend(local_numbers)
            if i == 0:
                local_parties = ms.local_parties(local_soup)
                local_labels = ms.local_labels(local_soup)
                field = ["Kód obce", "Lokalita"]
                field.extend(local_labels + local_parties)
                csvr.creation(name_of_file, field)
            csvr.row_add(name_of_file, field, row)
        csvr.directory_creation(name_of_directory)
        csvr.file_transfer(name_of_file, fr"{name_of_directory}")


if __name__ == "__main__":
    main()
