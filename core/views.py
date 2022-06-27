from django.shortcuts import redirect, render
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from core.models import Region, Parameter, YearTemperature, MonthTemperature
# Create your views here.


def extractData(request):
    if request.method == "POST":
        regions = ["UK", "England", "Wales", "Scotland", "Northern_Ireland",
                   "England_and_Wales", "England_N", "England_S", "Scotland_N",
                   "Scotland_E", "Scotland_W", "England_E_and_NE", "England_NW_and_N_Wales",
                   "Midlands", "East_Anglia", "England_SW_and_S_Wales", "England_SE_and_Central_S"]
        parameters = ["Tmax", "Tmin", "Tmean", "Sunshine",
                      "Rainfall", "Raindays1mm", "AirFrost"]
        months = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"]

        for region in regions:
            regionobj = Region(regionName=region)
            regionobj.save()
            for parameter in parameters:
                parameterobj = Parameter(
                    parameter_name=parameter, region=regionobj)
                parameterobj.save()
                req = Request(
                    "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/{}/date/{}.txt".format(parameter, region), headers={'User-Agent': 'Mozilla/5.0'})
                soup = BeautifulSoup(urlopen(req), 'html.parser')
                for script in soup(["script", "style"]):
                    script.extract()    # rip it out
                text = soup.get_text()
                for line in text.splitlines()[-11:][:-1]:
                    countMonth = 0
                    year = line.split()[0]
                    yearobj = YearTemperature()
                    (win, spr, sum, aut, ann) = tuple(line.split()[13:])
                    yearobj = YearTemperature()
                    yearobj.parameter = parameterobj
                    yearobj.year = year
                    if win != "---":
                        yearobj.win = float(win)
                    if spr != "---":
                        yearobj.spr = float(spr)
                    if sum != "---":
                        yearobj.sum = float(sum)
                    if aut != "---":
                        yearobj.aut = float(aut)
                    if ann != "---":
                        yearobj.ann = float(ann)
                    yearobj.save()
                    for monthData in tuple(line.split()[1:13]):
                        monthobj = MonthTemperature()
                        monthobj.year = yearobj
                        monthobj.month = months[countMonth]
                        monthobj.temperature = float(monthData)
                        countMonth += 1
                        monthobj.save()
                print(region, parameter)
        return redirect('core:extract')
    return render(request, 'core/main.html')
