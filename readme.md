Zbudowałem dwutabelową relacyjną bazę danych, pracownicy i działy. Program utowrzy bazę, uzupełni ja danymi, wygeneruje raporty . wykresy.

1. Uruchamiamy plik database.py (Tworzenie struktury i relacji, powstaje plik company.db)
2. Uruchamimy plik seed_data.py (Uzupełniam obie tabele przykładowymi rekordami)
3. Uruchamiamy plik reports.py ( W terminalu otrzymujemy informację o liczbie pracowaniów w kazdym dziale oraz statystyki wynagrodzeń w działach : średnia, suma)
4. Uruchamiamy plik export_reports.py (Powstają trzy nowe pliki , dwa .csv i jeden .xlsx, eksportujemy to co otrzymaliśmy powyżej)
5. Uruchamiamy plik visualize.py (Otrzymujemy 2 pliki .png które wyświetlają liczbę pracowników na dział, oraz sumę wynagrodzeń na dział)


W tym projekcie udało się zrealizować:
    - kompletny projekt bazy + raportów + wizualizacji,
    - wszystkie pliki CSV i Excel spójne z bazą,
    - wykresy gotowe do prezentacji,
    - pełną wiedzę, jak Python łączy się z bazą i generuje raporty.