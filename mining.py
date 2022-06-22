from ethermine import Ethermine

ethermine = Ethermine()

address = "0x5cA67DAd35930dBF385C8B46408951C06e1639E1"



workers = ethermine.miner_workers(address)
dashboard = ethermine.miner_dashboard(address)

print(dashboard)
