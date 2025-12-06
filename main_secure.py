from pytm.pytm import TM, Server, Datastore, Dataflow

if __name__ == '__main__':
    tm = TM("Beispielmodell")
    web = Server("Webserver")
    db  = Datastore("Datenbank")
    Dataflow(web, db, "Save Data")    # Datenfluss vom Webserver zur Datenbank
    print(tm.process())                            # Erzeugt DFD und Threat-Bericht
    tm.sqlDump("dump.sql")

# start with:
# python main_secure.py --json tm_secure.json