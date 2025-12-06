from pytm.pytm import TM, Server, Datastore, Dataflow

tm = TM("Beispielmodell")
tm.description = "Ein sehr einfaches Webserver–Datenbank-Modell"

web = Server("Webserver")
web.isHardened = False   # absichtlich unsicher, damit Findings entstehen

db = Datastore("Datenbank")
db.isHardened = False    # ebenfalls unsicher

flow = Dataflow(web, db, "Save Data")

tm.process()

# start with:
# python main_insecure.py --json tm_insecure.json