from class1 import estimator 


AverageAge=0
AverageDailyIncomeInUSD=0
AverageDailyIncomeofPopulation=0
TimetoElapse=0
ReportedCases=0
Population=0
TotalHospitalBeds=0
DaysitDoubles=0

'Inputs Come Here'


Region=input("Enter Region:")
AverageAge=float(input("Enter Average Age: "))
AverageDailyIncomeInUSD=float(input("Enter Average Daily Income In USD: "))
AverageDailyIncomeofPopulation=float(input("Enter Average Daily Income of Population: "))
PeriodType=input("Enter Period Type: ")
TimetoElapse=int(input("Enter time for it to Elapse: "))
ReportedCases=int(input("Enter Reported Cases: "))
Population=int(input("Enter Population number: "))
TotalHospitalBeds=int(input("Enter Total Number of Hospital Beds: "))
DaysitDoubles=int(input("Enters the Interval of which the Virus doubles in days..Eg: Doubles every two days: "))

regionName=estimator(Region)
regionName.regionInputData(AverageAge,AverageDailyIncomeInUSD,AverageDailyIncomeofPopulation)
regionName.inputData2(PeriodType,TimetoElapse,ReportedCases,Population,TotalHospitalBeds)
Power=(TimetoElapse/(DaysitDoubles))
IncreaseinDays=((ReportedCases)/(2**Power))



'Processing Estimations'
currentlyInfectedOut=regionName.currentlyInfected()
infectionsByRequestedTimeOut=regionName.infectionsByRequestedTime(IncreaseinDays)
severeCasesByRequestedTimeOut=regionName.severeCasesByRequestedTime()
hospitalBedsByRequestedTImeOut=regionName.hospitalBedsByRequestedTime()
casesForICUByRequestedTimeOut=regionName.casesForICUByRequestedTime()
casesForVentilatorsOut=regionName.casesForVentilatorsByRequestedTime()
dollarsInFlightOut=regionName.dollarsInFlight()




'Outputing The Estimations'
print(Region)
print(AverageAge)
print(AverageDailyIncomeInUSD)
print(AverageDailyIncomeofPopulation)
print(PeriodType)
print(TimetoElapse)
print(ReportedCases)
print(Population)
print(TotalHospitalBeds)
print(DaysitDoubles)
print(currentlyInfectedOut)
print(infectionsByRequestedTimeOut)
print(severeCasesByRequestedTimeOut)
print(hospitalBedsByRequestedTImeOut)
print(casesForICUByRequestedTimeOut)
print(casesForVentilatorsOut)
print(dollarsInFlightOut)