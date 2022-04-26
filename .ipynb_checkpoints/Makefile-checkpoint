help:
	@echo 'How to use our repository                                                 '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make clean                           clearing all figures/output folders        '
	@echo '   make all                              re-run all analysis folders       '
	@echo '   make env                              runs the code to download the correct packages given the notebook environment'
	@echo '                                                                          '
    
    
clean:
	rm -rf figurs
	rm -rf audio
	@echo ' Clearing Figures folder                                                                        '
	mkdir figurs
	mkdir audio
	touch figurs/.gitkeep
	touch figurs/.gitkeep
    
html:
	jupyterbook build .
    
html-hub:
	jupyter execute analysis.ipynb
    
env:
	conda install -c conda-forge palettable
	conda install -c conda-forge python-docx