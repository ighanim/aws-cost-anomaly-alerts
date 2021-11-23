class AnomalyEvent:
    def __init__(self, anomalyStartDate, anomalyEndDate,anomalyTotalImpact, anomalyDetailsLink, anomalyRootCauses):
        self.anomalyStartDate = anomalyStartDate
        self.anomalyEndDate = anomalyEndDate
        self.anomalyTotalImpact = anomalyTotalImpact
        self.anomalyDetailsLink = anomalyDetailsLink
        self.anomalyRootCauses = anomalyRootCauses
        