class inputData:
    def __init__(self,name):
        self.name=name

    def regionInputData(self,avgAge,avgDailyIncomeInUSD,avgDailyIncomePopulation):
            self.avgAge=avgAge
            self.avgDailyIncomeInUSD=avgDailyIncomeInUSD
            self.avgDailyIncomePopulation=avgDailyIncomePopulation
    
    def getRegionInputData(self):
            return self.name,self.avgAge,self.avgDailyIncomeInUSD,self.avgDailyIncomePopulation
    
    def inputData2(self,periodType,timeToElapse,reportedCases,population,totalHospitalBeds):
            self.periodType=periodType
            self.timeToElapse=timeToElapse
            self.reportedCases=reportedCases
            self.popultion=population
            self.totalHospitalBeds=totalHospitalBeds
            
    def getInputData2(self):
        return self.periodType,self.timeToElapse,self.reportedCases,self.popultion,self.totalHospitalBeds
    
    def mainInputData(self):
        return self.name,self.avgAge,self.avgDailyIncomeInUSD,self.avgDailyIncomePopulation,self.periodType,self.timeToElapse,self.reportedCases,self.popultion,self.totalHospitalBeds




'Inheriting From Input Data'
class estimator(inputData):
    def currentlyInfected(self):
        impactA=self.reportedCases*10
        severeImpactA=self.reportedCases*50
        return int(impactA),int(severeImpactA)
    
    def infectionsByRequestedTime(self,increaseDays):
        self.increaseDays=increaseDays
        impactB=self.reportedCases*10*(increaseDays)
        severeImpactB=self.reportedCases*50*(increaseDays)
        return int(impactB),int(severeImpactB)

    def severeCasesByRequestedTime(self):
        severeImpactB=int(self.reportedCases*50*(self.increaseDays))
        severeCasesBRT=severeImpactB*(0.15)
        return int(severeCasesBRT)

    def hospitalBedsByRequestedTime(self):
        severeCasesBRT=int(self.reportedCases*50*(self.increaseDays))*(15/100)
        bedsforSeverePatients=int(self.totalHospitalBeds)*(35/100)
        bedsAvailable=bedsforSeverePatients-severeCasesBRT
        return int(bedsAvailable)

    def casesForICUByRequestedTime(self):
        severeImpactB=int(self.reportedCases*50*(self.increaseDays))
        ICUcare=severeImpactB*(5/100)
        return int(ICUcare)

    def casesForVentilatorsByRequestedTime(self):
        severeImpactB=int(self.reportedCases*50*(self.increaseDays))
        requireVentilators=severeImpactB*(2/100)
        return int(requireVentilators)

    def dollarsInFlight(self):
        severeImpactB=int(self.reportedCases*50*(self.increaseDays))
        loss=(severeImpactB * 0.65 * 1.5)/30
        return int(loss)