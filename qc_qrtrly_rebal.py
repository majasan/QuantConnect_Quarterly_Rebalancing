#region imports
from AlgorithmImports import *
#endregion
class VerticalTachyonRegulators(QCAlgorithm):
 
   def Initialize(self):
       self.SetStartDate(2010, 8, 15)
       self.SetEndDate(2023, 1, 14)
       self.SetCash(10000)
       self.first = self.AddEquity("SPXL",Resolution.Daily)
       self.second = self.AddEquity("TMF",Resolution.Daily)
       # Universe selection
       tickers = ["TMF", "TQQQ"]
       symbols = [ Symbol.Create(ticker, SecurityType.Equity, Market.USA) for ticker in tickers]
       self.AddUniverseSelection(ManualUniverseSelectionModel(symbols))
       self.SetUniverseSelection(ManualUniverseSelectionModel(symbols))
       self.UniverseSettings.Resolution = Resolution.Daily     
       self.next = self.Time
      
   def OnData(self, data):
       insights = []
       if self.next >= self.Time:
           return
      
       for security in self.ActiveSecurities.Values:
           insights.append(Insight.Price(security.Symbol, Expiry.EndOfQuarter, InsightDirection.Up))
      
       self.EmitInsights(insights)
 
       self.SetHoldings(self.first.Symbol,.55)
       self.SetHoldings(self.second.Symbol,.45)
       self.next = Expiry.EndOfQuarter(self.Time)
      
