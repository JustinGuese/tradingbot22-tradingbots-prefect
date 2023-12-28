import alphavantageUpdate
import comp_bigtechmom
import comp_bondtqqq
import comp_buydips_adapted
import comp_buydips_explored
import comp_buydips_orig
import comp_buydips_shorting
import comp_notboring
import databaseBackup
import finnhub_recommendations
import headShoulderPrefect
import msftDecisionTree
import pairtrade_glri_vstm
import pairtrade_uboh_glri
import portoflioworthUpdate
from prefect.client.schemas.schedules import CronSchedule
from prefect.deployments import Deployment
from tqdm import tqdm

# all flows
FLOWS = [
    # main update functions
    (portoflioworthUpdate.portfolioWorthFlow, "0_portfolioworthupdate", "10 22 * * *"),
    (alphavantageUpdate.alphavantageUpdateFlow, "0_alphavantageupdate", "0 18 * * *"),
    # composer
    (comp_bigtechmom.bigTechMomFlow, "composer-bigtechmomentum-v1", "42 3 * * *"),
    (comp_bondtqqq.compBondTQQQ, "composer-bondtqqq-v1", "15 22 * * *"),
    (comp_buydips_orig.buydipsOriginal, "composer-buydipsqqq-original", "40 1 * * *"),
    (
        comp_buydips_shorting.buydipsShorting,
        "composer-buydipsqqq-shorting",
        "55 1 * * *",
    ),
    (
        comp_buydips_adapted.compBuydipsAdapted,
        "composer-buydipsqqq-shorting-adapted",
        "35 1 * * *",
    ),
    (
        comp_buydips_explored.buydipsExplored,
        "composer-buydipsqqq-shorting-explored",
        "30 1 * * *",
    ),
    (comp_notboring.compNotBoring, "composer-notboring-v1", "20 1 * * *"),
    # others
    (headShoulderPrefect.headAndShoulderFlow, "head-and-shoulders-qqq", "5 16 * * *"),
    (finnhub_recommendations.finnhubRecomm, "finnhub-recommendations", "0 16 * * 3"),
    (msftDecisionTree.msftDecisionTree, "msft-decisiontree", "5 4 * * 3"),
    # (pairtrade_glri_vstm.pairTradeGLRIVSTM, "pairtrade-glri-vstm", "0 17 * * *"), # deactivated, shorting not implemented
    # (pairtrade_uboh_glri.pairTradeUBOHGLRI, "pairtrade-uboh-glri", "5 17 * * *"), # deactivated, shorting not implemented
    # database backup
    (databaseBackup.backupAllDatabases, "0_database-backup", "0 3 * * *"),
]

for flow, name, cron in tqdm(FLOWS):
    print("building flow: ", name)
    deployment = Deployment.build_from_flow(
        flow, name=name, schedule=CronSchedule(cron=cron)
    )
    deployment.apply()
