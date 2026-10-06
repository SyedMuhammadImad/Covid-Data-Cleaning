"""Correct stock-vs-flow aggregation for an OWID-style COVID sample."""
import argparse,json
from pathlib import Path
import pandas as pd

def analyze(frame):
    required={'iso_code','location','date','total_cases','total_deaths','total_vaccinations'}
    if not required<=set(frame.columns):raise ValueError('Missing required COVID columns')
    frame=frame.copy();frame['date']=pd.to_datetime(frame.date,errors='coerce')
    frame=frame.dropna(subset=['iso_code','date']).drop_duplicates(['iso_code','date'],keep='last')
    frame=frame[~frame.iso_code.astype(str).str.startswith('OWID_')].sort_values(['iso_code','date'])
    for col in ('total_cases','total_deaths','total_vaccinations'):frame[col]=pd.to_numeric(frame[col],errors='coerce')
    frame['daily_vaccinations']=frame.groupby('iso_code').total_vaccinations.diff()
    # Negative differences can be reporting revisions; retain and label them.
    frame['vaccination_revision']=frame.daily_vaccinations<0
    frame['vaccination_trend']=frame.groupby('iso_code').daily_vaccinations.transform(lambda s:s.rolling(5,min_periods=1).mean())
    # Stocks are cumulative. Summing them over dates double counts history.
    latest={}
    for code,rows in frame.groupby('iso_code'):
        values={}
        for col in ('total_cases','total_deaths','total_vaccinations'):
            valid=rows.dropna(subset=[col])
            values[col]={'value':None if valid.empty else float(valid.iloc[-1][col]),'as_of':None if valid.empty else valid.iloc[-1].date.strftime('%Y-%m-%d')}
        latest[str(code)]={'location':str(rows.iloc[-1].location),'latest_reported':values}
    return frame,{'source':'Supplied sample OWID-style CSV; historical data, not current public-health advice','rows':len(frame),'countries':latest,
                  'revision_rows':int(frame.vaccination_revision.sum()),'aggregation':'latest nonmissing cumulative value per country, with metric-specific date'}

def main():
    p=argparse.ArgumentParser();p.add_argument('--data',type=Path,default=Path(__file__).parent/'sample_owid_covid_data.csv');p.add_argument('--output',type=Path,default=Path('analysis.json'))
    a=p.parse_args();_,r=analyze(pd.read_csv(a.data));a.output.write_text(json.dumps(r,indent=2,allow_nan=False),encoding='utf-8');print(r['rows'],len(r['countries']))
if __name__=='__main__':main()
