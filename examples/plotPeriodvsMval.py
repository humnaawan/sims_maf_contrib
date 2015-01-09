import os
import numpy as np
import matplotlib.pyplot as plt
import lsst.sims.maf.sliceMetrics as sliceMetrics

metricDir = 'testVar'
metricFile = 'ops2_1075_PeriodDeviationMetric_r_HEAL.npz'

sm = sliceMetrics.BaseSliceMetric(useResultsDb=False, outDir=metricDir)

iid = sm.readMetricData(os.path.join(metricDir, metricFile))

iid = iid[0]

nslices = sm.slicers[iid].nslice
nperiods = len(sm.metricValues[iid][-1:][0]['periods'])

periods = []
periodsdev = []

for mval in sm.metricValues[iid]:
    if isinstance(mval, dict):
        for p, pdev in zip(mval['periods'], mval['periodsdev']):
            periods.append(p)
            periodsdev.append(pdev)

periods = np.array(periods, 'float')
periodsdev = np.array(periodsdev, 'float')

plt.plot(periods, periodsdev*periods, 'k.')
plt.xlabel('Period (days)')
plt.ylabel(r'$\Delta$(P)/P')
plt.title(metricFile)

plt.show()
