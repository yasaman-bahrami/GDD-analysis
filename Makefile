#------------------------------Information Of Directories------------
s = ./src/
r = ./reports/
d = ./CSVData/
p = ./plots/
t = ./src/testSuite/

#--------------------------------INPUTS-------------------------------
startYear = 2016
endYear = 2016
baseTemp = 10
stationId = -st 50089 51442 51459
cityName = -ct 'St_Johns' 'Vancouver' 'Toronto'
percentage = -pr '5' '25'
gColor = -gc 'crimson' 'lime' 'tomato'
dmmColor = -dmm '01153E'
taskColor1 = -tc1 'ADD8E6' 'D2B48C'
taskColor3 = -tc3 '6E096A' 'D52B93' 'C995C7' '740029' '91A3CC'
taskColor4 = -tc4 'B9E294' '6CC4A8' '8E9AC8'
tempList = -tl '10' '12' '14' '16' '18'

all : report.pdf

$(d)St_JohnsGDDData.csv : $(s)downloadData.py $(s)computeGDD.py
	python $(s)downloadData.py $(startYear) $(endYear) $(stationId) $(cityName)
	python $(s)computeGDD.py $(baseTemp) $(stationId) $(cityName)
	
$(d)MontrealGDDData.csv : $(s)downloadData.py $(s)computeGDD.py
	python $(s)downloadData.py $(startYear) $(endYear) $(stationId) $(cityName)
	python $(s)computeGDD.py $(baseTemp) $(stationId) $(cityName)

$(d)CalgaryGDDData.csv : $(s)downloadData.py $(s)computeGDD.py
	python $(s)downloadData.py $(startYear) $(endYear) $(stationId) $(cityName)
	python $(s)computeGDD.py $(baseTemp) $(stationId) $(cityName)
	
$(p)GDDPlotIMG.png : $(s)getCSVData.py $(s)drawGDDPlot.py $(d)St_JohnsGDDData.csv $(d)MontrealGDDData.csv $(d)CalgaryGDDData.csv
	mkdir -p plots
	python $(s)drawGDDPlot.py $(stationId) $(cityName) $(gColor)
	
$(p)minMaxPlotSt_Johns.png : $(s)getCSVData.py $(s)drawMinMaxPlot.py $(d)St_JohnsGDDData.csv
	mkdir -p plots
	python $(s)drawMinMaxPlot.py $(stationId) $(cityName) $(dmmColor)
	
$(p)minMaxPlotMontreal.png : $(s)getCSVData.py $(s)drawMinMaxPlot.py $(d)MontrealGDDData.csv
	mkdir -p plots
	python $(s)drawMinMaxPlot.py $(stationId) $(cityName) $(dmmColor)

$(p)minMaxPlotCalgary.png : $(s)getCSVData.py $(s)drawMinMaxPlot.py $(d)CalgaryGDDData.csv
	mkdir -p plots
	python $(s)drawMinMaxPlot.py $(stationId) $(cityName) $(dmmColor)

$(p)secTask-1St_Johns.html : $(s)getCSVData.py $(s)secTask-1.py $(d)St_JohnsGDDData.csv
	mkdir -p plots
	python $(s)secTask-1.py $(stationId) $(cityName) $(percentage) $(taskColor1)
	
$(p)secTask-1Montreal.html : $(s)getCSVData.py $(s)secTask-1.py $(d)MontrealGDDData.csv
	mkdir -p plots
	python $(s)secTask-1.py $(stationId) $(cityName) $(percentage) $(taskColor1)
	
$(p)secTask-1Calgary.html : $(s)getCSVData.py $(s)secTask-1.py $(d)CalgaryGDDData.csv
	mkdir -p plots
	python $(s)secTask-1.py $(stationId) $(cityName) $(percentage) $(taskColor1)

$(p)secTask-3.png : $(s)getCSVData.py $(s)secTask-3.py $(d)CalgaryGDDData.csv $(d)MontrealGDDData.csv $(d)St_JohnsGDDData.csv
	mkdir -p plots
	python $(s)secTask-3.py $(tempList)

$(p)secTask-4.html : $(s)getCSVData.py $(s)secTask-4.py $(d)CalgaryGDDData.csv $(d)MontrealGDDData.csv $(d)St_JohnsGDDData.csv
	mkdir -p plots
	python $(s)secTask-4.py $(stationId) $(cityName)

$(p)secTask-5.html : $(s)getCSVData.py $(s)secTask-5.py $(d)CalgaryGDDData.csv $(d)MontrealGDDData.csv $(d)St_JohnsGDDData.csv
	mkdir -p plots
	#bokeh serve $(s)secTask-5.py
	python $(s)secTask-5.py $(stationId) $(cityName)
	
$(p)finalTaskSt_Johns.png : $(s)finalTask.py
	mkdir -p plots
	python $(s)finalTask.py $(stationId) $(cityName)

$(p)finalTaskMontreal.png : $(s)finalTask.py
	mkdir -p plots
	python $(s)finalTask.py $(stationId) $(cityName)
	
$(p)finalTaskCalgary.png : $(s)finalTask.py
	mkdir -p plots
	python $(s)finalTask.py $(stationId) $(cityName)

testSuite : $(t)*.py
	python $(t)testComputeGDD.py
	python $(t)testDownloadData.py
	python $(t)testGetCSVData.py
	
report.pdf : $(r)report.tex $(p)GDDPlotIMG.png $(p)minMaxPlotSt_Johns.png $(p)minMaxPlotMontreal.png $(p)minMaxPlotCalgary.png $(p)secTask-1St_Johns.html $(p)secTask-1Montreal.html $(p)secTask-1Calgary.html $(p)secTask-3.png $(p)secTask-4.html $(p)secTask-5.html $(p)finalTaskSt_Johns.png $(p)finalTaskMontreal.png $(p)finalTaskCalgary.png
	pdflatex $(r)report.tex
	pdflatex $(r)report.tex
	rm -f report.log report.aux report.toc report.out
	
clean : 
	rm -rf *.csv $(s)__pycache__ CSVData plots
	rm -f report.log report.aux report.pdf report.toc


help:
	@echo "Please make sure you have installed pdflatex program.
	@echo "# Calling the Makefile"
	@echo "$ make"
	@echo "# Clean the complied and data files"
	@echo "#$ make clean"
	@echo "# Calling by file name"
	@echo "#$ make report.pdf"
